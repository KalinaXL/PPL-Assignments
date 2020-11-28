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
def check_and_assign(obj, tp, force_casttype = False, dims = None):
    if type(obj) is Symbol:
        if type(obj.mtype) is Unknown:
            obj.mtype = tp
        elif type(obj.mtype) is MType:
            if type(obj.mtype.restype) is Unknown:
                if force_casttype and dims:
                    obj.mtype.restype = ArrayType(dims, tp)
                else:
                    obj.mtype.restype = tp
            elif force_casttype and type(obj.mtype.restype) is ArrayType and type(obj.mtype.restype.eletype) is Unknown:
                obj.mtype.restype.eletype = tp
        elif force_casttype and type(obj.mtype) is ArrayType and type(obj.mtype.eletype) is Unknown:
            obj.mtype.eletype = tp

class NotAConstant(Exception):
    pass

class StaticChecker(BaseVisitor):
    BREAK = -3
    CONTINUE = -2
    RETURN = -1
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

        self.current_fn = None
        self.fn_returntype = None
        self.fn_called = set()
        self.fn_decls = set()
        self.in_loop_counter = 0
        self.has_oor = False

    def check(self):
        return self.visit(self.ast,self.global_envi)
    
    def pre_visit_fn(self, fn_decls, env):
        for fn_decl in fn_decls:
            try:
                params = reduce(lambda env, ele: ele.accept(self, env), fn_decl.param, ([], []))[0]
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
            env[0].append(Symbol(fn_decl.name.name, MType(params, Unknown())))
        

    def visitProgram(self,ast, c):
        var_decls = list(filter(lambda decl: type(decl) is VarDecl, ast.decl))
        func_decls = list(filter(lambda decl: type(decl) is FuncDecl, ast.decl))
        var_envs = reduce(lambda env, ele: ele.accept(self, env), var_decls, (self.global_envi, []))
        self.pre_visit_fn(func_decls, var_envs)
        func_envs = reduce(lambda env, ele: ele.accept(self, env), func_decls, var_envs)
        if not any(x.name == 'main' for x in func_envs[0] if type(x.mtype) is MType):
            raise NoEntryPoint()
        residual_fns = self.fn_decls - self.fn_called - {'main'}
        if len(residual_fns) > 0:
            for fn_name in residual_fns:
                raise UnreachableFunction(fn_name)
        # self.first_iter = False
        # reduce(lambda env, ele: ele.accept(self, env), func_decls, func_envs)
        # # reduce(lambda env, ele: ele.accept(self, env), ast.decl + ast.decl, (self.global_envi, []))
        # if 'main' not in self.fn_decls:
        #     raise NoEntryPoint()

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
        fns = list(filter(lambda x: x.name == ast.name.name, param[0]))
        if len(fns) > 1:
            raise Redeclared(Function(), ast.name.name)
        var_decl_env = reduce(lambda env, ele: ele.accept(self, env), ast.body[0], (fns[0].mtype.intype, []))
        new_env = (var_decl_env[0], var_decl_env[1] + 
                                    param[0] + param[1])
        # reduce(lambda env, ele: ele.accept(self, env), ast.body[1], new_env)
        self.current_fn = ast.name.name
        self.fn_decls.add(ast.name.name)
        v, counter, has_return = None, 0, False
        self.fn_returntype = fns[0].mtype.restype
        for stmt in ast.body[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v == StaticChecker.RETURN: 
                counter += 1
                has_return = True
            elif v in [StaticChecker.BREAK, StaticChecker.CONTINUE]:
                counter += 1
        intypes = [x.mtype for x in fns[0].mtype.intype]
        intypes = [eval(self.primetype2str(tp)) if type(tp) is not ArrayType else eval(self.arraytype2str(tp)) for tp in intypes]
        fns[0].mtype.intype = intypes
        if type(fns[0].mtype.restype) is Unknown:
            fns[0].mtype.restype = VoidType()
        elif type(fns[0].mtype.restype) is not VoidType and not has_return:
            raise FunctionNotReturn(ast.name.name)
        # print(fns[0])
        return param

    def infer_type(self, ast, tp, param):
        if type(ast) is ArrayCell and type(tp) is not ArrayType:
            check_and_assign(ast.arr.accept(self, param), tp, True, [-1] * len(ast.idx))
    def eval_exp_value(self, op, left, right = None):
        if op == '\\':
            op = '//'
        return eval(f'{left} {op} {right}' if right else f'{op} {left}')
    def visitBinaryOp(self, ast, param):
        if self.has_oor:
            left_exp = ast.left.accept(self, param)
            right_exp = ast.right.accept(self, param)
            if type(left_exp) is not int or type(right_exp) is not int:
                raise NotAConstant()
            try:
                return self.eval_exp_value(ast.op, left_exp, right_exp)
            except:
                raise NotAConstant()
        if ast.op in ['&&', '||']:
            in_type = BoolType
            out_type = BoolType
        elif ast.op in ['+', '-', '*', '\\', '%']:
            in_type = IntType
            out_type = IntType
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            in_type = IntType
            out_type = BoolType
        elif ast.op in ['+.', '-.', '*.', '\.']:
            in_type = FloatType
            out_type = FloatType
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            in_type = FloatType
            out_type = BoolType
        else:
            raise TypeMismatchInExpression(ast)
        self.infer_type(ast.left, in_type(), param)
        self.infer_type(ast.right, in_type(), param)
        left_exp = ast.left.accept(self, param)
        right_exp = ast.right.accept(self, param)
        check_and_assign(left_exp, in_type())
        check_and_assign(right_exp, in_type())
        if get_type(left_exp) is in_type and get_type(right_exp) is in_type:
                return out_type()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, param):
        if has_oor:
            exp = ast.body.accept(self, param)
            if type(exp) is not int:
                raise NotAConstant()
            try:
                return self.eval_exp_value(ast.op, exp)
            except:
                raise NotAConstant()
        if ast.op == '!':
            in_type = BoolType
            out_type = BoolType
        elif ast.op == '-':
            in_type = IntType
            out_type = IntType
        elif ast.op == '-.':
            in_type = FloatType
            out_type = FloatType
        else:
            raise TypeMismatchInExpression(ast)
        self.infer_type(ast.body, in_type(), param)
        exp = ast.body.accept(self, param)
        check_and_assign(exp, in_type())
        if type(exp) is in_type:
            return out_type()
        raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, param):
        func = list(filter(lambda x: ast.method.name == x.name, param[0] + param[1]))
        if not func:
            raise Undeclared(Function(), ast.method.name)
        fn = func[0]
        if self.current_fn != fn.name:
            self.fn_called.add(fn.name)
        if type(fn.mtype) is not MType:
            raise TypeMismatchInExpression(ast)
        if len(fn.mtype.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        else:
            for tp, pr in zip(fn.mtype.intype, ast.param):
                par = pr.accept(self, param)
                if get_type(tp) is Unknown:
                    if get_type(par) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        par_tp = par.mtype if type(par) is Symbol else par
                        check_and_assign(tp, par_tp)
                        # fn.mtype.intype[i] = par_tp
                else:
                    if get_type(par) is Unknown:
                        if type(tp) is Symbol:
                            check_and_assign(par, tp.mtype)
                        else:
                            check_and_assign(par, tp)
                    elif get_type(tp) != get_type(par):
                        raise TypeMismatchInExpression(ast) 
        return fn
        
    def visitCallStmt(self, ast, param):
        func = list(filter(lambda x: ast.method.name == x.name, param[0] + param[1]))
        if not func:
            raise Undeclared(Function(), ast.method.name)
        fn = func[0]
        if self.current_fn != fn.name:
            self.fn_called.add(fn.name)
        if type(fn.mtype) is not MType:
            raise TypeMismatchInStatement(ast)

        if type(fn.mtype.restype) is Unknown:
            fn.mtype.restype = VoidType()
        elif type(fn.mtype.restype) is not VoidType:
            raise TypeMismatchInStatement(ast)

        if len(fn.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        else:
            for tp, pr in zip(fn.mtype.intype, ast.param):
                par = pr.accept(self, param)
                if get_type(tp) is Unknown:
                    if get_type(par) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        par_tp = par.mtype if type(par) is Symbol else par
                        check_and_assign(tp, par_tp)
                else:
                    if get_type(par) is Unknown:
                        if type(tp) is Symbol:
                            check_and_assign(par, tp.mtype)
                        else:
                            check_and_assign(par, tp)
                    elif get_type(tp) != get_type(par):
                        raise TypeMismatchInStatement(ast) 
    
    def visitId(self, ast, param):
        ids = list(filter(lambda x: ast.name == x.name, param[0] + param[1]))
        if not ids:
            raise Undeclared(Identifier(), ast.name)
        return ids[0]
    
    def visitArrayCell(self, ast, param):
        arr = ast.arr.accept(self, param)
        if type(arr) is Symbol:
            if type(arr.mtype) is MType:
                if type(arr.mtype.restype) is Unknown:
                    #
                    # Not Found A Solution
                    #
                    arr.mtype.restype = ArrayType([-1] * len(ast.idx), Unknown())
                elif type(arr.mtype.restype) is not ArrayType:
                    raise TypeMismatchInExpression(ast)
            elif type(arr.mtype) is not ArrayType:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)
        for idx in ast.idx:
            idx_type = idx.accept(self, param)
            if get_type(idx_type) is Unknown:
                check_and_assign(idx_type, IntType())
            if get_type(idx_type) is not IntType:
                raise TypeMismatchInExpression(ast)
        self.has_oor = True
        if self.has_oor:
            if type(arr.mtype) is MType:
                dims = arr.mtype.restype.dimen
            else:
                dims = arr.mtype.dimen
            for i, idx in enumerate(ast.idx):
                try:
                    idx_value = idx.accept(self, param)
                    if type(idx_value) is not int:
                        raise NotAConstant()
                    if idx_value < 0 or (idx_value >= dims[i] and dims[i] != -1):
                        raise IndexOutOfRange(ast)
                except NotAConstant:
                    pass
        self.has_oor = False
        if type(arr.mtype) is MType:
            dims = arr.mtype.restype.dimen
        else:
            dims = arr.mtype.dimen
        if len(dims) != len(ast.idx):
            raise TypeMismatchInExpression(ast)
        return arr.mtype.restype.eletype if type(arr.mtype) is MType else arr.mtype.eletype
    
    def handle_assign_equal_type(self, ast, left, right):
        if type(left) is ArrayType and type(right) is ArrayType:
            if left.dimen != right.dimen:
                raise TypeMismatchInStatement(ast)
            elif type(left.eletype) is Unknown:
                if type(right.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    pass
                    #
                    # Not Found a solution
                    #
            elif type(left.eletype) != type(right.eletype) and type(right.eletype) is not Unknown:
                raise TypeMismatchInStatement(ast)
        elif type(left) is Symbol and get_type(left) is ArrayType:
            if type(right) is Symbol:
                if left.mtype.dimen != right.mtype.dimen:
                    raise TypeMismatchInStatement(ast)
                elif type(left.mtype.eletype) is Unknown:
                    if type(right.mtype.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        left.mtype.eletype = right.mtype.eletype
                elif type(left.mtype.eletype) != type(right.mtype.eletype):
                    raise TypeMismatchInStatement(ast)
            else:
                if left.mtype.dimen != right.dimen:
                    raise TypeMismatchInStatement(ast)
                elif type(left.mtype.eletype) is Unknown:
                    if type(right.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        left.mtype.eletype = right.eletype
                elif type(left.mtype.eletype) != type(right.eletype) and type(right.eletype) is not Unknown:
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
        try:
            right_type = ast.rhs.accept(self, param)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        try:
            left_type = ast.lhs.accept(self, param)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if get_type(left_type) is VoidType or get_type(right_type) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(ast.lhs) is ArrayCell:
            if get_type(left_type) is Unknown:
                if get_type(right_type) not in [Unknown, ArrayType]:
                    pre_idx = ast.lhs.arr.accept(self, param)
                    check_and_assign(pre_idx, get_type(right_type)(), True)
                    return
            elif get_type(right_type) is ArrayType:
                raise TypeMismatchInStatement(ast)

        elif type(ast.lhs) is not Id:
            raise TypeMismatchInStatement(ast)
        if get_type(left_type) is not Unknown and get_type(right_type) is not Unknown:
            if get_type(left_type) == get_type(right_type):
                self.handle_assign_equal_type(ast, left_type, right_type)
            else:
                raise TypeMismatchInStatement(ast)
        elif get_type(left_type) is Unknown:
            if get_type(right_type) is Unknown:
                raise TypeCannotBeInferred(ast)
            elif get_type(right_type) is not ArrayType:
                check_and_assign(left_type, get_type(right_type)())
            else:
                raise TypeMismatchInStatement(ast)
        elif get_type(right_type) is Unknown and get_type(left_type) is not Unknown:
            if type(left_type) is Symbol:
                if type(left_type.mtype) is MType:
                    left_tp = left_type.mtype.restype
                else:
                    left_tp = left_type.mtype
            else:
                left_tp = left_type
            check_and_assign(right_type, left_tp)
    
    def visitIf(self, ast, param):
        for cond_exp, var_decls, stmts in ast.ifthenStmt:
            self.infer_type(cond_exp, BoolType(), param)
            cond_type = cond_exp.accept(self, param)
            check_and_assign(cond_type, BoolType())
            if get_type(cond_type) is not BoolType:
                raise TypeMismatchInStatement(ast)
            new_env = reduce(lambda env, ele: ele.accept(self, env), var_decls, ([], param[0] + param[1]))
            v, counter, has_return = None, 0, False
            for stmt in stmts:
                v = stmt.accept(self, new_env)
                if counter == 1:
                    raise UnreachableStatement(stmt)
                elif v in [StaticChecker.CONTINUE, StaticChecker.BREAK]:
                    counter += 1
                elif v == StaticChecker.RETURN:
                    counter += 1
                    has_return = True
            if type(self.fn_returntype) not in [Unknown, VoidType] and not has_return:
                raise FunctionNotReturn(self.current_fn)
        var_decls, stmts = ast.elseStmt
        new_env = reduce(lambda env, ele: ele.accept(self, env), var_decls, ([], param[0] + param[1]))
        v, counter, has_return = None, 0, False
        for stmt in stmts:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.CONTINUE, StaticChecker.BREAK]:
                    counter += 1
            elif v == StaticChecker.RETURN:
                counter += 1
                has_return = True
        if type(self.fn_returntype) not in [Unknown, VoidType] and not has_return and (len(var_decls) + len(stmts)):
            raise FunctionNotReturn(self.current_fn)
        
            
    def visitFor(self, ast, param):
        self.in_loop_counter += 1
        self.infer_type(ast.expr1, IntType(), param)
        exp1_type = ast.expr1.accept(self, param)
        check_and_assign(exp1_type, IntType())
        if get_type(exp1_type) is not IntType:
            raise TypeMismatchInStatement(ast)
        idx = ast.idx1.accept(self, param)
        if get_type(idx.mtype) is Unknown:
            idx.mtype = IntType()
        elif get_type(idx.mtype) is not IntType:
            raise TypeMismatchInStatement(ast)
        self.infer_type(ast.expr2, BoolType(), param)
        self.infer_type(ast.expr3, IntType(), param)
        exp2_type = ast.expr2.accept(self, param)
        exp3_type = ast.expr3.accept(self, param)
        check_and_assign(exp2_type, BoolType())
        check_and_assign(exp3_type, IntType())
        if get_type(exp2_type) is not BoolType or get_type(exp3_type) is not IntType:
            raise TypeMismatchInStatement(ast)
        
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.loop[0], ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in ast.loop[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
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
        fn_type = list(filter(lambda x: x.name == self.current_fn and type(x.mtype) is MType, param[0] + param[1]))[0]
        if ast.expr:
            rettype = ast.expr.accept(self, param)
            if get_type(rettype) is Unknown:
                if get_type(fn_type) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    if type(rettype) is Symbol:
                        if type(rettype.mtype) is MType:
                            check_and_assign(rettype, fn_type.mtype.restype)
                        elif type(rettype.mtype) is not ArrayType:
                            if type(fn_type.mtype.restype) is not ArrayType:
                                check_and_assign(rettype, fn_type.mtype.restype)
                            else:
                                raise TypeMismatchInStatement(ast)
                        else:
                            if type(rettype.mtype.eletype) is Unknown:
                                if type(fn_type.mtype.restype) is ArrayType:
                                    if fn_type.mtype.restype.dimen[-1] == -1:
                                        fn_type.mtype.restype.dimen = rettype.mtype.dimen
                                    if type(fn_type.mtype.restype.eletype) is Unknown:
                                        raise TypeCannotBeInferred(ast)
                                    else:
                                        rettype.mtype.eletype = fn_type.mtype.restype.eletype
                                    if fn_type.mtype.restype.dimen != rettype.mtype.dimen or type(fn_type.mtype.restype.eletype) != type(rettype.mtype.eletype):
                                        raise TypeMismatchInStatement(ast)
                                elif type(fn_type.mtype.restype) is Unknown:
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    rettype.mtype.eletype = fn_type.mtype.restype

                    elif get_type(fn_type) is ArrayType:
                        raise TypeMismatchInStatement(ast)
                    elif type(ast.expr) is ArrayCell:
                        arr = ast.expr.arr
                        if type(fn_type.mtype) is MType:
                            tp = fn_type.mtype.restype
                        else:
                            tp = fn_type.mtype
                        if type(tp) is ArrayType:
                            raise TypeMismatchInStatement(ast)
                        else:
                            check_and_assign(arr.accept(self, param), tp, True)
            else:
                if get_type(rettype) is VoidType:
                    raise TypeMismatchInStatement(ast)
                if type(rettype) is Symbol:
                    if type(rettype.mtype) is MType:
                        if type(rettype.mtype.restype) is ArrayType and type(fn_type.mtype.restype) is ArrayType:
                            if type(rettype.mtype.restype.eletype) is Unknown:
                                if type(fn_type.mtype.restype.eletype) is Unknown:
                                    raise TypeCannotBeInferred(ast)
                                elif rettype.mtype.restype.dimen and rettype.mtype.restype.dimen[-1] == -1:
                                    rettype.mtype.restype.dimen = fn_type.mtype.restype.dimen
                                elif fn_type.mtype.restype.dimen and fn_type.mtype.restype.dimen[-1] == -1:
                                    fn_type.mtype.restype.dimen = rettype.mtype.restype.dimen
                                else:
                                    rettype.mtype.restype.eletype = fn_type.mtype.restype.eletype
                            else:
                                if type(fn_type.mtype.restype.eletype) is Unknown:
                                    fn_type.mtype.restype.eletype = rettype.mtype.restype.eletype
                                elif type(rettype.mtype.restype.eletype) != type(fn_type.mtype.restype.eletype):
                                    raise TypeMismatchInStatement(ast)
                        elif type(rettype.mtype.restype) is not ArrayType and type(fn_type.mtype.restype) is not ArrayType:
                            if type(rettype.mtype.restype) is Unknown and type(fn_type.mtype.restype) is Unknown:
                                raise TypeCannotBeInferred(ast)
                            elif type(rettype.mtype.restype) is Unknown:
                                rettype.mtype.restype = fn_type.mtype.restype
                            elif type(fn_type.mtype.restype) is Unknown:
                                fn_type.mtype.restype = rettype.mtype.restype
                            elif type(rettype.mtype.restype) != type(fn_type.mtype.restype):
                                raise TypeMismatchInStatement(ast)
                        else:
                            raise TypeMismatchInStatement(ast)
                    elif type(rettype.mtype) is ArrayType:
                        if type(fn_type.mtype.restype) is ArrayType:
                            if type(rettype.mtype.eletype) is Unknown:
                                if type(fn_type.mtype.restype.eletype) is Unknown:
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    rettype.mtype.eletype = fn_type.mtype.restype.eletype
                                if fn_type.mtype.restype.dimen and fn_type.mtype.restype.dimen[-1] == -1:
                                    fn_type.mtype.restype.dimen = rettype.mtype.dimen
                                else:
                                    rettype.mtype.eletype = fn_type.mtype.restype.eletype
                            else:
                                if type(fn_type.mtype.restype.eletype) is Unknown:
                                    fn_type.mtype.restype.eletype = rettype.mtype.eletype
                                elif type(fn_type.mtype.restype.eletype) != type(rettype.mtype.eletype):
                                    raise TypeMismatchInStatement(ast)
                        elif type(fn_type.mtype.restype) is Unknown:
                            if type(rettype.mtype.eletype) is Unknown:
                                raise TypeCannotBeInferred(ast)
                            else:
                                fn_type.mtype.restype = rettype.mtype
                        else:
                            raise TypeMismatchInStatement(ast)
                    elif type(fn_type.mtype.restype) is Unknown:
                        tp = rettype.mtype
                else:
                    tp = rettype
                if get_type(fn_type) is Unknown:
                    fn_type.mtype.restype = tp
                elif get_type(fn_type) != get_type(rettype):
                    raise TypeMismatchInStatement(ast)
        else:
            if get_type(fn_type) is Unknown:
                check_and_assign(fn_type, VoidType())
            elif get_type(fn_type) is not VoidType:
                raise TypeMismatchInStatement(ast)
        self.fn_returntype = fn_type.mtype.restype
        return StaticChecker.RETURN
    def visitDowhile(self, ast, param):
        self.in_loop_counter += 1
        self.infer_type(ast.exp, BoolType(), param)
        exp = ast.exp.accept(self, param)
        check_and_assign(exp, BoolType())
        if get_type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.sl[0], ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in ast.sl[1]:
            v = stmt.accept(self, new_env)  
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.RETURN, StaticChecker.BREAK, StaticChecker.CONTINUE]:
                counter += 1
        self.in_loop_counter -= 1

    def visitWhile(self, ast, param):
        self.in_loop_counter += 1
        self.infer_type(ast.exp, BoolType(), param)
        exp = ast.exp.accept(self, param)
        check_and_assign(exp, BoolType())
        if get_type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.sl[0], ([], param[0] + param[1]))   
        v, counter = None, 0
        for stmt in ast.sl[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.BREAK, StaticChecker.RETURN, StaticChecker.CONTINUE]:
                counter += 1
        self.in_loop_counter -= 1
    
    def visitIntLiteral(self, ast, param):
        if self.has_oor:
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
    
        



        
