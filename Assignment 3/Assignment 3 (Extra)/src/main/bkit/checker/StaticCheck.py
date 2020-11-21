"""
 * @author nhphung
 * @modified: Nguyen Huynh Minh
 * @stdid: 1813085
 * @time: 11/2020
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

def get_type(obj):
    if type(obj) is Symbol:
        if type(obj.mtype) is MType:
            return type(obj.mtype.restype)
        return type(obj.mtype)
    return type(obj)
def check_and_assign(obj, tp):
    if type(obj) is Symbol:
        if type(obj.mtype) is Unknown:
            obj.mtype = tp
        elif type(obj.mtype) is MType and type(obj.mtype.restype) is Unknown:
            obj.mtype.restype = tp
class NotIntegerNumber(Exception):
    pass

class StaticChecker(BaseVisitor):
    RETURN = -3
    BREAK = -2
    CONTINUE = -1
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]   

        self.in_loop_counter = 0
        self.func_rettypes = set()
        self.fn_called = set()
        self.current_fn = None
        self.fn_decls = set()
        self.first_iter = True
        self.eval_index = False
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        # [self.visit(x,c) for x in ast.decl]
        # ([], []) : 1st []: current scope, 2nd []: outer scope
        # decls, _ = reduce(lambda env, ele: ele.accept(self, env), ast.decl, (self.global_envi, []))
        var_decls = list(filter(lambda decl: type(decl) is VarDecl, ast.decl))
        func_decls = list(filter(lambda decl: type(decl) is FuncDecl, ast.decl))
        var_envs = reduce(lambda env, ele: ele.accept(self, env), var_decls, (self.global_envi, []))
        # try:
        #     func_envs = reduce(lambda env, ele: ele.accept(self, env), func_decls, var_envs)
        # except:
        #     func_envs = var_envs
        func_envs = reduce(lambda env, ele: ele.accept(self, env), func_decls, var_envs)
        self.first_iter = False
        reduce(lambda env, ele: ele.accept(self, env), func_decls, func_envs)
        # reduce(lambda env, ele: ele.accept(self, env), ast.decl + ast.decl, (self.global_envi, []))
        if 'main' not in self.fn_decls:
            raise NoEntryPoint()
        unreachable_fns = self.fn_decls - self.fn_called - {'main'}
        for fn_name in unreachable_fns:
            raise UnreachableFunction(fn_name)

    def visitVarDecl(self, ast, param):
        if any(ast.variable.name == i.name for i in param[0]):
            raise Redeclared(Variable(), ast.variable.name)
        var_type = ast.varInit.accept(self, param) if ast.varInit else Unknown()
        if type(var_type) is ArrayType:
            var_type = var_type.eletype
        if ast.varDimen:
            var_type = ArrayType(ast.varDimen, var_type)
        return param[0] + [Symbol(ast.variable.name, var_type)], param[1]
    
    def visitFuncDecl(self, ast, param):
        if any(ast.name.name == i.name for i in param[0]) and self.first_iter:
            raise Redeclared(Function(), ast.name.name)
        try:
            param_env = reduce(lambda env, ele: ele.accept(self, env), ast.param, ([], []))
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        var_decl_env = reduce(lambda env, ele: ele.accept(self, env), ast.body[0], param_env)
        param_types = [sym.mtype for sym in param_env[0]]
        new_env = (var_decl_env[0], var_decl_env[1] + 
                                    param[0] + param[1] +
                                    [Symbol(ast.name.name, MType(param_types, Unknown()))])
        # reduce(lambda env, ele: ele.accept(self, env), ast.body[1], new_env)
        self.current_fn = ast.name.name
        self.fn_decls.add(ast.name.name)
        v, counter = None, 0
        for stmt in ast.body[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            if v == StaticChecker.RETURN:
                counter += 1

        if len(self.func_rettypes) > 1:
            for rettype in self.func_rettypes:
                if type(rettype) is VoidType:
                    raise FunctionNotReturn(ast.name.name)
            raise TypeMismatchInExpression(ast)
        else:
            rettype = list(self.func_rettypes)
            if rettype:
                if type(rettype[0]) is str:
                    rettype = eval(rettype[0])
                else:
                    rettype = rettype[0]()
            else:
                rettype = VoidType()
        self.func_rettypes = set()
        param_types = [sym.mtype for sym in new_env[0] if any(p.name == sym.name for p in param_env[0])]
        return param[0] + [Symbol(ast.name.name, MType(param_types, rettype))], param[1]
    
    def eval_index_exp(self, op, left, right = None):
        if op == '\\':
            op = '//'
        exp = f'{left} {op} {right}' if right else f'{op} {left}'
        return eval(exp)

    def visitBinaryOp(self, ast, param):
        left_exp = ast.left.accept(self, param)
        right_exp = ast.right.accept(self, param)
        if self.eval_index:
            if type(left_exp) is not int or type(right_exp) is not int:
                raise NotIntegerNumber()
            return self.eval_index_exp(ast.op, left_exp, right_exp)
        if ast.op in ['&&', '||']:
            check_and_assign(left_exp, BoolType())
            check_and_assign(right_exp, BoolType())
            if self.first_iter:
                return BoolType()
            if get_type(left_exp) is BoolType and get_type(right_exp) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['+', '-', '*', '\\', '%']:
            check_and_assign(left_exp, IntType())
            check_and_assign(right_exp, IntType())
            if self.first_iter:
                return IntType()
            if get_type(left_exp) is IntType and get_type(right_exp) is IntType:
                return IntType()
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            check_and_assign(left_exp, IntType())
            check_and_assign(right_exp, IntType())
            if self.first_iter:
                return BoolType()
            if get_type(left_exp) is IntType and get_type(right_exp) is IntType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['+.', '-.', '*.', '\.']:
            check_and_assign(left_exp, FloatType())
            check_and_assign(right_exp, FloatType())
            if self.first_iter:
                return FloatType()
            if get_type(left_exp) is FloatType and get_type(right_exp) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            check_and_assign(left_exp, FloatType())
            check_and_assign(right_exp, FloatType())
            if self.first_iter:
                return BoolType()
            if get_type(left_exp) is FloatType and get_type(right_exp) is FloatType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast, param):
        exp = ast.body.accept(self, param)
        if self.eval_index:
            if type(exp) is not int:
                raise NotIntegerNumber()
            return self.eval_index_exp(ast.op, exp)
        if ast.op == '!':
            check_and_assign(exp, BoolType())
            if self.first_iter:
                return BoolType()
            if isinstance(exp, BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif ast.op == '-':
            check_and_assign(exp, IntType())
            if self.first_iter:
                return IntType()
            if isinstance(exp, IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)
        elif ast.op == '-.':
            check_and_assign(exp, FloatType())
            if self.first_iter:
                return FloatType()
            if isinstance(exp, FloatType):
                return FloatType()
            raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, param):
        func = list(filter(lambda x: ast.method.name == x.name and get_type(x.mtype) is MType, param[0] + param[1]))
        if not func:
            if self.first_iter:
                return
            raise Undeclared(Function(), ast.method.name)
        fn = func[0]
        if fn.name != self.current_fn:
            self.fn_called.add(fn.name)
        if get_type(fn.mtype.restype) is Unknown and not self.first_iter:
            raise TypeCannotBeInferred(ast)
        elif len(fn.mtype.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        else:
            for tp, pr in zip(fn.mtype.intype, ast.param):
                if get_type(tp) is Unknown:
                    raise TypeCannotBeInferred(ast)
                par = pr.accept(self, param)
                check_and_assign(par, get_type(tp)())
                if get_type(tp) != get_type(par):
                    raise TypeMismatchInExpression(ast)
        return fn.mtype.restype
        
    def visitCallStmt(self, ast, param):
        func = list(filter(lambda x: ast.method.name == x.name and type(x.mtype) is MType, param[0] + param[1]))
        if not func:
            if self.first_iter:
                return
            raise Undeclared(Function(), ast.method.name)
        fn = func[0]
        if fn.name != self.current_fn:
            self.fn_called.add(fn.name)
        if get_type(fn.mtype.restype) is not VoidType and not self.first_iter:
            raise TypeMismatchInStatement(ast)
        elif len(fn.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        else:
            if not self.first_iter:
                for tp, pr in zip(fn.mtype.intype, ast.param):
                    if get_type(tp) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    par = pr.accept(self, param)
                    check_and_assign(par, tp)
                    if get_type(tp) != get_type(par):
                        raise TypeMismatchInStatement(ast)
        return VoidType()
    
    def visitId(self, ast, param):
        ids = list(filter(lambda x: ast.name == x.name, param[0] + param[1]))
        if not ids:
            raise Undeclared(Identifier(), ast.name)
        return ids[0]
    
    def visitArrayCell(self, ast, param):
        arr = ast.arr.accept(self, param)
        if get_type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for idx in ast.idx:
            idx_type = idx.accept(self, param)
            if get_type(idx_type) is not IntType:
                raise TypeMismatchInExpression(ast)
        if type(arr) is Symbol:
            dims = arr.mtype.dimen
        else:
            dims = arr.dimen
        self.eval_index = not self.first_iter
        if self.eval_index:
            for i, idx in enumerate(ast.idx):
                try:
                    value = idx.accept(self, param)
                    if value < 0 or value >= dims[i]:
                        raise IndexOutOfRange(ast)
                except NotIntegerNumber:
                    pass
        remaining_dims = dims[len(ast.idx): ]
        if remaining_dims:
            return ArrayType(remaining_dims, arr.mtype.eletype)
        return arr.mtype.eletype if type(arr) is Symbol else arr.eletype
    
    def handle_assign_equal_type(self, ast, left, right):
        if type(left) is ArrayType and type(right) is ArrayType:
            if left.dimen != right.dimen:
                raise TypeMismatchInStatement(ast)
            elif type(left.eletype) is Unknown:
                if type(right.eletype) is Unknown:
                    raise TypeMismatchInStatement(ast)
                else:
                    pass
                    #
                    # Not Found a solution
                    #
            elif type(left.eletype) != type(right.eletype):
                raise TypeMismatchInStatement(ast)
        elif type(left) is Symbol and get_type(left) is ArrayType:
            if type(right) is Symbol:
                if left.mtype.dimen != right.mtype.dimen:
                    raise TypeMismatchInStatement(ast)
                elif type(left.mtype.eletype) is Unknown:
                    if type(right.mtype.eletype) is Unknown:
                        raise TypeMismatchInStatement(ast)
                    else:
                        left.mtype.eletype = right.mtype.eletype
                elif type(left.mtype.eletype) != type(right.mtype.eletype):
                    raise TypeMismatchInStatement(ast)
            else:
                if left.mtype.dimen != right.dimen:
                    raise TypeMismatchInStatement(ast)
                elif type(left.mtype.eletype) is Unknown:
                    if type(right.eletype) is Unknown:
                        raise TypeMismatchInStatement(ast)
                    else:
                        left.mtype.eletype = right.eletype
                elif type(left.mtype.eletype) != type(right.eletype):
                    raise TypeMismatchInStatement(ast)
        elif type(right) is Symbol and get_type(right) is ArrayType:
            if left.dimen != right.mtype.dimen:
                raise TypeMismatchInStatement(ast)
            elif type(left.eletype) is Unknown:
                if type(right.mtype.eletype) is Unknown:
                    raise TypeMismatchInStatement(ast)
                else:
                    pass
                    #
                    # Not Found a Solution
                    #
                pass 
            elif type(left.eletype) != type(right.mtype.eletype):
                raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        right_type = ast.rhs.accept(self, param)
        left_type = ast.lhs.accept(self, param)
        if self.first_iter and right_type is None:
            return
        if right_type is None:
            return
        if get_type(left_type) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif get_type(left_type) is not Unknown and get_type(right_type) is not Unknown:
            if get_type(left_type) == get_type(right_type):
                self.handle_assign_equal_type(ast, left_type, right_type)
            else:
                raise TypeMismatchInStatement(ast)
        elif get_type(left_type) is Unknown:
            if get_type(right_type) is Unknown:
                raise TypeCannotBeInferred(ast)
            else:
                check_and_assign(left_type, get_type(right_type)())
        elif get_type(right_type) is Unknown and get_type(left_type) is not Unknown:
            raise TypeMismatchInStatement(ast)
    
    def visitIf(self, ast, param):
        for cond_exp, var_decls, stmts in ast.ifthenStmt:
            cond_type = cond_exp.accept(self, param)
            if get_type(cond_type) is not BoolType:
                raise TypeMismatchInStatement(ast)
            new_env = reduce(lambda env, ele: ele.accept(self, env), var_decls, ([], param[0] + param[1]))
            v, counter = None, 0
            for stmt in stmts:
                v = stmt.accept(self, new_env)
                if counter == 1:
                    raise UnreachableStatement(stmt)
                if v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
                    counter += 1

        var_decls, stmts = ast.elseStmt
        new_env = reduce(lambda env, ele: ele.accept(self, env), var_decls, ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in stmts:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            if v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
                    counter += 1
            
    def visitFor(self, ast, param):
        exp1_type = ast.expr1.accept(self, param)
        if get_type(exp1_type) is not IntType:
            raise TypeMismatchInStatement(ast)
        idx = ast.idx1.accept(self, param)
        if get_type(idx.mtype) is Unknown:
            idx.mtype = IntType()
        elif get_type(idx.mtype) is not IntType:
            raise TypeMismatchInStatement(ast)
        exp2_type = ast.expr2.accept(self, param)
        exp3_type = ast.expr3.accept(self, param)
        if get_type(exp2_type) is not BoolType or get_type(exp3_type) is not IntType:
            raise TypeMismatchInStatement(ast)
        
        self.in_loop_counter += 1
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.loop[0], ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in ast.loop[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            if v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
                counter += 1
            
        self.in_loop_counter -= 1
    
    def visitContinue(self, ast, param):
        if self.in_loop_counter == 0:
            raise NotInLoop(ast)
        return StaticChecker.CONTINUE
    
    def visitBreak(self, ast, param):
        if self.in_loop_counter == 0:
            raise NotInLoop(ast)
        return StaticChecker.BREAK
    

    def visitReturn(self, ast, param):
        if ast.expr:
            rettype = ast.expr.accept(self, param)
            if get_type(rettype) is Unknown:
                raise TypeCannotBeInferred(ast)
            if type(rettype) is Symbol:
                if type(rettype.mtype) is ArrayType:
                    prime = self.primetype2str(rettype.mtype.eletype)
                    rettype = f'ArrayType(' + str(rettype.mtype.dimen) + ', ' + prime + ')'
                    self.func_rettypes.add(rettype)
                else:
                    self.func_rettypes.add(type(rettype.mtype))
            else:
                self.func_rettypes.add(type(rettype))
        else:
            self.func_rettypes.add(VoidType)
        return StaticChecker.RETURN
        
    def visitDowhile(self, ast, param):
        exp = ast.exp.accept(self, param)
        if get_type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.in_loop_counter += 1
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.sl[0], ([], param[0] + param[1]))
        # for stmt in ast.sl[1]:
        #     stmt.accept(self, new_env)
        v, counter = None, 0
        for stmt in ast.sl[1]:
            v = stmt.accept(self, new_env)  
            if counter == 1:
                raise UnreachableStatement(stmt)
            if v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
                counter += 1
            
        self.in_loop_counter -= 1

    def visitWhile(self, ast, param):
        exp = ast.exp.accept(self, param)
        if get_type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.in_loop_counter += 1
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.sl[0], ([], param[0] + param[1]))   
        v, counter = None, 0
        for stmt in ast.sl[1]:
            v = stmt.accept(self, new_env)  
            if counter == 1:
                raise UnreachableStatement(stmt)
            if v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
                counter += 1
            
        self.in_loop_counter -= 1
    
    def visitIntLiteral(self, ast, param):
        if self.eval_index:
            return ast.value
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        elements = [element.accept(self, param) for element in ast.value]
        ele_types = [type(element) for element in elements]
        if len(ele_types) == 0:
            return ArrayType([], Unknown())
        if ele_types[0] is not ArrayType:
            if len(set(ele_types)) > 1:
                raise InvalidArrayLiteral(ast)
            return ArrayType([len(ast.value)], ele_types[0]())
        else:
            ele_types = [self.arraytype2str(ele) for ele in elements]
            if len(set(ele_types)) > 1:
                raise InvalidArrayLiteral(ast)
            inner_type = eval(ele_types[0])
            return ArrayType([len(ast.value)] + inner_type.dimen, inner_type.eletype)
    def arraytype2str(self, ele):
        return 'ArrayType(' + str(ele.dimen) + ', ' + self.primetype2str(ele.eletype) + ')'
    def primetype2str(self, tp):
        if type(tp) is IntType:
            prime = 'IntType()'
        elif type(tp) is BoolType:
            prime = 'BoolType()'
        elif type(tp) is FloatType:
            prime = 'FloatType()'
        elif type(tp) is Unknown:
            prime = 'Unknown()'
        else:
            prime = 'VoidType()'
        return prime
    
        