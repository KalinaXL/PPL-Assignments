'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from AST import *

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class Unknown(Type): pass
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.intype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self, dimen, eletype):
        self.dimen = dimen   #List[int]  
        self.eletype = eletype

class Access:
    def __init__(self, frame, sym, isLeft):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft

class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Function"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass

class Undeclared(StaticError):
    def __init__(self, k, n):
        self.k = k
        self.n = n
    
    def __str__(self):
        return  "str(Undeclared("+ str(self.k) + "(), '" + self.n + "'))"

class Redeclared(StaticError):
    def __init__(self, k, n):
        self.k = k
        self.n = n
    
    def __str__(self):
        return  "str(Redeclared("+ str(self.k) + "(), '" + self.n + "'))"

class TypeMismatchInExpression(StaticError):
    def __init__(self, exp):
        self.exp = exp
    def __str__(self):
        return  "str(TypeMismatchInExpression("+ str(self.exp) + '))'

class TypeMismatchInStatement(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt
    def __str__(self):
        return "str(TypeMismatchInStatement("+ str(self.stmt) + '))'

class TypeCannotBeInferred(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "str(TypeCannotBeInferred("+ str(self.stmt) + '))'

class NoEntryPoint(StaticError):
    def __str__(self):
        return "str(NoEntryPoint())"

class NotInLoop(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "str(NotInLoop(" + str(self.stmt) + "))"

class InvalidArrayLiteral(StaticError):
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return "str(InvalidArrayLiteral(" + str(self.arr) + '))'

class FunctionNotReturn(StaticError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "str(FunctionNotReturn('" + self.name + '\'))'

class UnreachableFunction(StaticError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "str(UnreachableFunction('" + self.name + "'))"

class UnreachableStatement(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "str(UnreachableStatement(" + str(self.stmt) + '))'

class IndexOutOfRange(StaticError):
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return "str(IndexOutOfRange(" + str(self.cell) + '))'

class NotAConstant(Exception):
    pass

def get_type(obj):
    if type(obj) is Symbol:
        if type(obj.mtype) is MType:
            return type(obj.mtype.rettype)
        return type(obj.mtype)
    return type(obj)
def check_and_assign(obj, tp, force_casttype = False, dims = None):
    if type(obj) is Symbol:
        if type(obj.mtype) is Unknown:
            obj.mtype = tp
        elif type(obj.mtype) is MType:
            if type(obj.mtype.rettype) is Unknown:
                if force_casttype and dims:
                    raise TypeCannotBeInferred(None)
                else:
                    obj.mtype.rettype = tp
            elif force_casttype and type(obj.mtype.rettype) is ArrayType and type(obj.mtype.rettype.eletype) is Unknown:
                obj.mtype.rettype.eletype = tp
        elif force_casttype and type(obj.mtype) is ArrayType and type(obj.mtype.eletype) is Unknown:
            obj.mtype.eletype = tp


class StaticChecker(BaseVisitor):
    BREAK = -3
    CONTINUE = -2
    RETURN = -1

    ALL_RETURN = -4
    ALL_BRKCNT = -5
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_to_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("print",MType([StringType()],VoidType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]

        self.current_fn = None
        self.fn_returntype = None
        self.fn_called = set()
        self.fn_decls = set()
        self.in_loop_counter = 0
        self.has_oor = False
        self.oor_counter = 0
        self.oor_flag = 0

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
        return func_envs
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
        self.fn_returntype = fns[0].mtype.rettype
        for stmt in ast.body[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v == StaticChecker.RETURN:
                counter += 1
                has_return = True
            elif v in [StaticChecker.BREAK, StaticChecker.CONTINUE]:
                counter += 1
            elif type(stmt) is If and v == StaticChecker.ALL_RETURN:
                counter += 1
                has_return = True
        # intypes = [x.mtype for x in fns[0].mtype.intype]
        # intypes = [eval(self.primetype2str(tp)) if type(tp) is not ArrayType else eval(self.arraytype2str(tp)) for tp in intypes]
        # fns[0].mtype.intype = intypes
        if type(fns[0].mtype.rettype) is Unknown:
            fns[0].mtype.rettype = VoidType()
        elif type(fns[0].mtype.rettype) is not VoidType and not has_return:
            raise FunctionNotReturn(ast.name.name)
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
        left_exp = ast.left.accept(self, param)
        check_and_assign(left_exp, in_type())
        if get_type(left_exp) is not in_type:
            raise TypeMismatchInExpression(ast)
        self.infer_type(ast.right, in_type(), param)
        right_exp = ast.right.accept(self, param)
        check_and_assign(right_exp, in_type())
        if get_type(right_exp) is not in_type:
            raise TypeMismatchInExpression(ast)
        return out_type()

    def visitUnaryOp(self, ast, param):
        if self.has_oor:
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
        if get_type(exp) is in_type:
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
            for i, (tp, pr) in enumerate(zip(fn.mtype.intype, ast.param)):
                par = pr.accept(self, param)
                if get_type(tp) is not Unknown and get_type(par) is not Unknown:
                    if get_type(tp) == get_type(par):
                        self.handle_assign_equal_type(ast, tp, par, False)
                    else:
                        raise TypeMismatchInExpression(ast)
                if get_type(tp) is Unknown:
                    if get_type(par) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif get_type(par) is not ArrayType:
                        if type(tp) is Unknown:
                            fn.mtype.intype[i] = get_type(par)()
                        check_and_assign(tp, get_type(par)())
                    else:
                        #
                        #   Think ?
                        #
                        raise TypeMismatchInExpression(ast)
                elif get_type(par) is Unknown and get_type(tp) is not Unknown:
                    if type(tp) is Symbol and type(tp.mtype) is ArrayType:
                        if type(tp.mtype.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                        if type(par.mtype) is MType:
                            par.mtype.rettype = tp.mtype
                        else:
                            raise TypeMismatchInExpression(ast)
                    if type(pr) is ArrayCell:
                        check_and_assign(pr.arr.accept(self, param), get_type(tp)(), True)
                    else:
                        if get_type(tp) is not ArrayType:
                            check_and_assign(par, get_type(tp)())
                if get_type(par) is VoidType:
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

        if type(fn.mtype.rettype) is Unknown:
            fn.mtype.rettype = VoidType()
        elif type(fn.mtype.rettype) is not VoidType:
            raise TypeMismatchInStatement(ast)

        if len(fn.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        else:
            for i, (tp, pr) in enumerate(zip(fn.mtype.intype, ast.param)):
                try:
                    par = pr.accept(self, param)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)
                if get_type(tp) is not Unknown and get_type(par) is not Unknown:
                    if get_type(tp) == get_type(par):
                        self.handle_assign_equal_type(ast, tp, par)
                    else:
                        raise TypeMismatchInStatement(ast)
                if get_type(tp) is Unknown:
                    if get_type(par) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif get_type(par) is not ArrayType:
                        if type(tp) is Unknown:
                            fn.mtype.intype[i] = get_type(par)()
                        check_and_assign(tp, get_type(par)())
                    else:
                        #
                        #   Think ?
                        #
                        raise TypeMismatchInStatement(ast)
                elif get_type(par) is Unknown and get_type(tp) is not Unknown:
                    if type(tp) is Symbol and type(tp.mtype) is ArrayType:
                        if type(tp.mtype.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                        if type(par.mtype) is MType:
                            par.mtype.rettype = tp.mtype
                        else:
                            raise TypeMismatchInStatement(ast)
                    if type(pr) is ArrayCell:
                        check_and_assign(pr.arr.accept(self, param), get_type(tp)(), True)
                    else:
                        if get_type(tp) is not ArrayType:
                            check_and_assign(par, get_type(tp)())
                if get_type(par) is VoidType:
                    raise TypeMismatchInStatement(ast)

    def visitId(self, ast, param):
        ids = list(filter(lambda x: ast.name == x.name and type(x.mtype) is not MType, param[0] + param[1]))
        if not ids:
            raise Undeclared(Identifier(), ast.name)
        return ids[0]

    def visitArrayCell(self, ast, param):
        arr = ast.arr.accept(self, param)
        if type(arr) is Symbol:
            if type(arr.mtype) is MType:
                if type(arr.mtype.rettype) is Unknown:
                    # arr.mtype.rettype = ArrayType([-1] * len(ast.idx), Unknown())
                    raise TypeCannotBeInferred(ast)
                elif type(arr.mtype.rettype) is not ArrayType:
                    raise TypeMismatchInExpression(ast)
            elif type(arr.mtype) is not ArrayType:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)
        if type(arr.mtype) is MType:
            dims = arr.mtype.rettype.dimen
        else:
            dims = arr.mtype.dimen
        if len(dims) != len(ast.idx):
            raise TypeMismatchInExpression(ast)
        self.oor_counter += 1
        self.has_oor = self.oor_counter == self.oor_flag
        for idx in ast.idx:
            self.infer_type(idx, IntType(), param)
            idx_type = idx.accept(self, param)
            if get_type(idx_type) is Unknown:
                check_and_assign(idx_type, IntType(), True)
            if get_type(idx_type) is not IntType:
                raise TypeMismatchInExpression(ast)
        self.oor_flag += 1
        self.has_oor = self.oor_counter == self.oor_flag
        if self.has_oor:
            for i, idx in enumerate(ast.idx):
                try:
                    idx_value = idx.accept(self, param)
                    if type(idx_value) is not int:
                        raise NotAConstant()
                    if idx_value < 0 or idx_value >= dims[i]:
                        raise IndexOutOfRange(ast)
                except Exception as e:
                    if type(e) is IndexOutOfRange:
                        raise e
        self.has_oor = False
        self.oor_flag -= 1
        self.oor_counter -= 1
        return arr.mtype.rettype.eletype if type(arr.mtype) is MType else arr.mtype.eletype

    def handle_assign_equal_type(self, ast, left, right, is_stmt = True):
        error = TypeMismatchInStatement if is_stmt else TypeMismatchInExpression
        if type(left) is ArrayType and type(right) is ArrayType:
            if left.dimen != right.dimen:
                raise error(ast)
            elif type(left.eletype) is Unknown:
                if type(right.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    pass
                    #
                    # Not Found a solution
                    #
            elif type(left.eletype) != type(right.eletype) and type(right.eletype) is not Unknown:
                raise error(ast)
        elif type(left) is Symbol and get_type(left) is ArrayType:
            if type(right) is Symbol:
                if type(right.mtype) is not MType:
                    if left.mtype.dimen != right.mtype.dimen:
                        raise error(ast)
                    elif type(left.mtype.eletype) is Unknown:
                        if type(right.mtype.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                        else:
                            left.mtype.eletype = right.mtype.eletype
                    elif type(right.mtype.eletype) is Unknown:
                        right.mtype.eletype = left.mtype.eletype
                    elif type(left.mtype.eletype) != type(right.mtype.eletype):
                        raise error(ast)
                else:
                    if left.mtype.dimen != right.mtype.rettype.dimen:
                        raise error(ast)
                    elif type(left.mtype.eletype) is Unknown:
                        if type(right.mtype.rettype.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                        else:
                            left.mtype.eletype = right.mtype.rettype.eletype
                    elif type(left.mtype.eletype) != type(right.mtype.rettype.eletype):
                        raise error(ast)
            else:
                if left.mtype.dimen != right.dimen:
                    raise error(ast)
                elif type(left.mtype.eletype) is Unknown:
                    if type(right.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        left.mtype.eletype = right.eletype
                elif type(left.mtype.eletype) != type(right.eletype) and type(right.eletype) is not Unknown:
                    raise error(ast)
        elif type(right) is Symbol and get_type(right) is ArrayType:
            if left.dimen != right.mtype.dimen:
                raise error(ast)
            elif type(left.eletype) is Unknown:
                if type(right.mtype.eletype) is Unknown:
                    raise error(ast)
                else:
                    pass
                    #
                    # Not Found a Solution
                    #
                pass
            elif type(left.eletype) != type(right.mtype.eletype):
                raise error(ast)

    def visitAssign(self, ast, param):
        try:
            left_type = ast.lhs.accept(self, param)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        try:
            right_type = ast.rhs.accept(self, param)
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
                left_tp = left_type.mtype
            else:
                left_tp = left_type
            if type(ast.rhs) is ArrayCell:
                # if get_type(left_type) is Unknown:
                #     if get_type(right_type) not in [Unknown, ArrayType]:
                #         pre_idx = ast.lhs.arr.accept(self, param)
                #         check_and_assign(pre_idx, get_type(right_type)(), True)
                #         return
                # elif get_type(right_type) is ArrayType:
                #     raise TypeMismatchInStatement(ast)
                check_and_assign(ast.rhs.arr.accept(self, param), left_tp, True)
            else:
                if type(left_tp) is ArrayType:
                    if type(left_tp.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                check_and_assign(right_type, left_tp)

    def visitIf(self, ast, param):
        return_counter = 0
        jump_counter = 0
        for cond_exp, var_decls, stmts in ast.ifthenStmt:
            try:
                self.infer_type(cond_exp, BoolType(), param)
                cond_type = cond_exp.accept(self, param)
                check_and_assign(cond_type, BoolType())
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            if get_type(cond_type) is not BoolType:
                raise TypeMismatchInStatement(ast)
            new_env = reduce(lambda env, ele: ele.accept(self, env), var_decls, ([], param[0] + param[1]))
            v, counter = None, 0
            for stmt in stmts:
                v = stmt.accept(self, new_env)
                if counter == 1:
                    raise UnreachableStatement(stmt)
                elif v in [StaticChecker.CONTINUE, StaticChecker.BREAK, StaticChecker.RETURN]:
                    counter += 1
                    jump_counter += 1
                    if v == StaticChecker.RETURN:
                        return_counter += 1
                elif type(stmt) is If:
                    if v in [StaticChecker.ALL_RETURN, StaticChecker.ALL_BRKCNT]:
                        counter += 1
                        jump_counter += 1
                        if v == StaticChecker.ALL_RETURN:
                            return_counter += 1
            # if type(self.fn_returntype) not in [Unknown, VoidType] and not has_return:
            #     raise FunctionNotReturn(self.current_fn)
        var_decls, stmts = ast.elseStmt
        new_env = reduce(lambda env, ele: ele.accept(self, env), var_decls, ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in stmts:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.CONTINUE, StaticChecker.BREAK, StaticChecker.RETURN]:
                counter += 1
                jump_counter += 1
                if v == StaticChecker.RETURN:
                    return_counter += 1
        if len(stmts):
            if return_counter == len(ast.ifthenStmt) + 1:
                return StaticChecker.ALL_RETURN
            elif self.in_loop_counter and jump_counter == len(ast.ifthenStmt) + 1:
                return StaticChecker.ALL_BRKCNT
        return
        # if type(self.fn_returntype) not in [Unknown, VoidType] and not has_return and (len(var_decls) + len(stmts)):
        #     raise FunctionNotReturn(self.current_fn)


    def visitFor(self, ast, param):
        self.in_loop_counter += 1
        idx = ast.idx1.accept(self, param)
        if get_type(idx.mtype) is Unknown:
            idx.mtype = IntType()
        elif get_type(idx.mtype) is not IntType:
            raise TypeMismatchInStatement(ast)

        try:
            self.infer_type(ast.expr1, IntType(), param)
            exp1_type = ast.expr1.accept(self, param)
            check_and_assign(exp1_type, IntType())
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if get_type(exp1_type) is not IntType:
            raise TypeMismatchInStatement(ast)

        try:
            self.infer_type(ast.expr2, BoolType(), param)
            exp2_type = ast.expr2.accept(self, param)
            check_and_assign(exp2_type, BoolType())
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if get_type(exp2_type) is not BoolType:
            raise TypeMismatchInStatement(ast)

        try:
            self.infer_type(ast.expr3, IntType(), param)
            exp3_type = ast.expr3.accept(self, param)
            check_and_assign(exp3_type, IntType())
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if get_type(exp3_type) is not IntType:
            raise TypeMismatchInStatement(ast)

        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.loop[0], ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in ast.loop[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.BREAK, StaticChecker.CONTINUE, StaticChecker.RETURN]:
                counter += 1
            elif type(stmt) is If and v in [StaticChecker.ALL_RETURN, StaticChecker.ALL_BRKCNT]:
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
            try:
                rettype = ast.expr.accept(self, param)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            if get_type(rettype) is Unknown:
                if get_type(fn_type) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    if type(rettype) is Symbol:
                        if type(rettype.mtype) is MType:
                            check_and_assign(rettype, fn_type.mtype.rettype)
                        elif type(rettype.mtype) is not ArrayType:
                            if type(fn_type.mtype.rettype) is not ArrayType:
                                check_and_assign(rettype, fn_type.mtype.rettype)
                            else:
                                raise TypeMismatchInStatement(ast)
                        else:
                            if type(rettype.mtype.eletype) is Unknown:
                                if type(fn_type.mtype.rettype) is ArrayType:
                                    if type(fn_type.mtype.rettype.eletype) is Unknown:
                                        raise TypeCannotBeInferred(ast)
                                    else:
                                        rettype.mtype.eletype = fn_type.mtype.rettype.eletype
                                    if fn_type.mtype.rettype.dimen != rettype.mtype.dimen or type(fn_type.mtype.rettype.eletype) != type(rettype.mtype.eletype):
                                        raise TypeMismatchInStatement(ast)
                                elif type(fn_type.mtype.rettype) is Unknown:
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    rettype.mtype.eletype = fn_type.mtype.rettype

                    elif get_type(fn_type) is ArrayType:
                        raise TypeMismatchInStatement(ast)
                    elif type(ast.expr) is ArrayCell:
                        arr = ast.expr.arr
                        if type(fn_type.mtype) is MType:
                            tp = fn_type.mtype.rettype
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
                        if type(rettype.mtype.rettype) is ArrayType and type(fn_type.mtype.rettype) is ArrayType:
                            if type(rettype.mtype.rettype.eletype) is Unknown:
                                if type(fn_type.mtype.rettype.eletype) is Unknown:
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    rettype.mtype.rettype.eletype = fn_type.mtype.rettype.eletype
                            else:
                                if type(fn_type.mtype.rettype.eletype) is Unknown:
                                    fn_type.mtype.rettype.eletype = rettype.mtype.rettype.eletype
                                elif type(rettype.mtype.rettype.eletype) != type(fn_type.mtype.rettype.eletype):
                                    raise TypeMismatchInStatement(ast)
                            if rettype.mtype.rettype.dimen != fn_type.mtype.rettype.dimen:
                                raise TypeMismatchInStatement(ast)
                        elif type(rettype.mtype.rettype) is not ArrayType and type(fn_type.mtype.rettype) is not ArrayType:
                            if type(rettype.mtype.rettype) is Unknown and type(fn_type.mtype.rettype) is Unknown:
                                raise TypeCannotBeInferred(ast)
                            elif type(rettype.mtype.rettype) is Unknown:
                                rettype.mtype.rettype = fn_type.mtype.rettype
                            elif type(fn_type.mtype.rettype) is Unknown:
                                fn_type.mtype.rettype = rettype.mtype.rettype
                            elif type(rettype.mtype.rettype) != type(fn_type.mtype.rettype):
                                raise TypeMismatchInStatement(ast)
                        else:
                            raise TypeMismatchInStatement(ast)
                    elif type(rettype.mtype) is ArrayType:
                        if type(fn_type.mtype.rettype) is ArrayType:
                            if type(rettype.mtype.eletype) is Unknown:
                                if type(fn_type.mtype.rettype.eletype) is Unknown:
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    rettype.mtype.eletype = fn_type.mtype.rettype.eletype
                            else:
                                if type(fn_type.mtype.rettype.eletype) is Unknown:
                                    fn_type.mtype.rettype.eletype = rettype.mtype.eletype
                                elif type(fn_type.mtype.rettype.eletype) != type(rettype.mtype.eletype):
                                    raise TypeMismatchInStatement(ast)
                            if rettype.mtype.dimen != fn_type.mtype.rettype.dimen:
                                raise TypeMismatchInStatement(ast)
                        elif type(fn_type.mtype.rettype) is Unknown:
                            if type(rettype.mtype.eletype) is Unknown:
                                raise TypeCannotBeInferred(ast)
                            else:
                                fn_type.mtype.rettype = rettype.mtype
                        else:
                            raise TypeMismatchInStatement(ast)
                    elif type(fn_type.mtype.rettype) is Unknown:
                        tp = rettype.mtype
                else:
                    tp = rettype
                if get_type(fn_type) is Unknown:
                    fn_type.mtype.rettype = tp
                elif get_type(fn_type) != get_type(rettype):
                    raise TypeMismatchInStatement(ast)
        else:
            if get_type(fn_type) is Unknown:
                check_and_assign(fn_type, VoidType())
            elif get_type(fn_type) is not VoidType:
                raise TypeMismatchInStatement(ast)
        self.fn_returntype = fn_type.mtype.rettype
        return StaticChecker.RETURN
    def visitDowhile(self, ast, param):
        self.in_loop_counter += 1
        new_env = reduce(lambda env, ele: ele.accept(self, env), ast.sl[0], ([], param[0] + param[1]))
        v, counter = None, 0
        for stmt in ast.sl[1]:
            v = stmt.accept(self, new_env)
            if counter == 1:
                raise UnreachableStatement(stmt)
            elif v in [StaticChecker.RETURN, StaticChecker.BREAK, StaticChecker.CONTINUE]:
                counter += 1
            elif type(stmt) is If and v in [StaticChecker.ALL_RETURN, StaticChecker.ALL_BRKCNT]:
                counter += 1
        try:
            self.infer_type(ast.exp, BoolType(), param)
            exp = ast.exp.accept(self, param)
            check_and_assign(exp, BoolType())
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if get_type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.in_loop_counter -= 1

    def visitWhile(self, ast, param):
        self.in_loop_counter += 1
        try:
            self.infer_type(ast.exp, BoolType(), param)
            exp = ast.exp.accept(self, param)
            check_and_assign(exp, BoolType())
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
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
            elif type(stmt) is If and v in [StaticChecker.ALL_RETURN, StaticChecker.ALL_BRKCNT]:
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
        elif type(tp) is StringType:
            prime = 'StringType()'
        elif type(tp) is Unknown:
            prime = 'Unknown()'
        else:
            prime = 'VoidType()'
        return prime

def getNDim(arr):
    if type(arr) is not ArrayLiteral: return 0
    return 1 + getNDim(arr.value[0])

def getTypeOfLiteral(literal):
    if type(literal) is IntLiteral:
        return IntType()
    elif type(literal) is FloatLiteral:
        return FloatType()
    elif type(literal) is StringLiteral:
        return StringType()
    elif type(literal) is BooleanLiteral:
        return BoolType()
    else:
        return getTypeOfLiteral(literal.value[0])

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("read", MType([], StringType()), CName(self.libName)),
                Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
		        Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName)),
                Symbol('string_of_bool', MType([BoolType()], StringType()), CName(self.libName)),
                Symbol('string_of_float', MType([FloatType()], StringType()), CName(self.libName)),
                Symbol('int_of_float', MType([FloatType()], IntType()), CName(self.libName)),
                Symbol('float_to_int', MType([IntType()], FloatType()), CName(self.libName)),
                Symbol('int_of_string', MType([StringType()], IntType()), CName(self.libName)),
                Symbol('float_of_string', MType([StringType()], FloatType()), CName(self.libName)),
                Symbol('bool_of_string', MType([StringType()], BoolType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

def get_tp(obj):
    if type(obj) is Symbol:
        if type(obj.mtype) is MType:
            return obj.mtype.rettype
        return obj.mtype
    return obj

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        self.static_check = StaticChecker(astTree)
        builtin_fns  = ['read', 'printLn', 'printStrLn', 'print', 'string_of_int', 'string_of_bool', 'string_of_float', 'int_of_float', 'float_to_int', 'int_of_string', 'float_of_string', 'bool_of_string']
        self.symbols_table = list(filter(lambda x: type(x.mtype) is MType and x.name not in builtin_fns, self.static_check.check()[0]))
        # self.symbols_table = list(filter(lambda x: type(x.mtype) is MType, self.symbols_table))
        self.astTree = astTree
        self.className = "MCClass"
        self.env = [Symbol(fn.name, MType([get_tp(in_) for in_ in fn.mtype.intype], get_tp(fn.mtype.rettype)), CName(self.className)) for fn in self.symbols_table] + env
        # for fn in self.env:
        #     print(fn.name, fn.mtype.intype, fn.mtype.rettype)
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.global_variables = []
        self.is_clinit = False
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = MethodEnv(None, self.env)
        # self.genMain(e)
        fn_decls = []
        for decl in ast.decl:
            if type(decl) is VarDecl:
                self.global_variables.append(decl)
            else:
                fn_decls.append(decl)
        g_env = reduce(lambda acc, ele: MethodEnv(None, [self.visit(ele, acc)] + acc.sym), self.global_variables, e)
        for decl in fn_decls:
            self.visit(decl, g_env)
        # map(lambda x: self.visit(x, e), ast.decl)
        # generate default constructor
        self.genInit()
        self.is_clinit = True
        self.genClinit()
        self.is_clinit = False
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
    def genClinit(self):
        methodname,methodtype = "<clinit>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        for decl in self.global_variables:
            self.visit(decl, MethodEnv(frame, []))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def genMethod(self, ast, param):
        func = list(filter(lambda x: x.name == ast.name.name, self.env))[0]
        if ast.name.name == 'main':
            func.mtype = MType([ArrayType([], StringType())], VoidType())
        frame = Frame(ast.name.name, func.mtype)
        self.emit.printout(self.emit.emitMETHOD(ast.name.name, func.mtype, True, frame))
        frame.enterScope(True)
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        syms = param.sym
        if ast.name.name == 'main':
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), startLabel, endLabel, frame))
        else:
            for pr, tp in zip(ast.param, func.mtype.intype):
                idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, pr.variable.name, tp, startLabel, endLabel, frame))
                syms = [Symbol(pr.variable.name, tp, Index(idx))] + syms
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        # map(lambda x: self.visit(x, param), ast.body[0] + ast.body[1])
        env = reduce(lambda acc, ele: MethodEnv(frame, [self.visit(ele, acc)] + acc.sym), ast.body[0], MethodEnv(frame, syms))

        has_return_global = False
        for stmt in ast.body[1]:
            self.visit(stmt, env)
            if not has_return_global:
                has_return_global = type(stmt) is Return
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        if not has_return_global:
            self.emit.printout(self.emit.emitRETURN(func.mtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitVarDecl(self, ast, param):
        var_tp = getTypeOfLiteral(ast.varInit)
        if ast.varDimen:
            var_tp = ArrayType(ast.varDimen, var_tp)
        if not param.frame:
            var_code = self.emit.emitATTRIBUTE(ast.variable.name, var_tp, False, '')
            val = CName(self.className)
            self.emit.printout(var_code)
            return Symbol(ast.variable.name, var_tp, val)
        if self.is_clinit:
            value_code, var_tp = self.visit(ast.varInit, param)
            self.emit.printout(value_code)
            self.emit.printout(self.emit.emitPUTSTATIC(f'{self.className}/{ast.variable.name}', var_tp, param.frame))
            return
               
        start_label = param.frame.getStartLabel()
        end_label = param.frame.getEndLabel()
        index = param.frame.getNewIndex()
        var_code = self.emit.emitVAR(index, ast.variable.name, var_tp, start_label, end_label, param.frame)
        val = Index(index)
        self.emit.printout(var_code)
        if ast.varInit:
            value_code, var_tp = self.visit(ast.varInit, param)
            self.emit.printout(value_code)
            self.emit.printout(self.emit.emitWRITEVAR(ast.variable.name, var_tp, index, param.frame))
        return Symbol(ast.variable.name, var_tp, val)
    
    def visitFuncDecl(self, ast, param):
        self.genMethod(ast, param)
    
    def visitBinaryOp(self, ast, param):
        left_code, left_tp = ast.left.accept(self, param)
        right_code, right_tp = ast.right.accept(self, param)
        if ast.op in ['+', '-', '+.', '-.']:
            op_code = self.emit.emitADDOP(ast.op[0], left_tp, param.frame)
        elif ast.op in ['*', '\\', '*.', '\.']:
            op_code = self.emit.emitMULOP(ast.op[0], left_tp, param.frame)
        elif ast.op == '%':
            op_code = self.emit.emitMOD(param.frame)
        elif ast.op in ['&&', '||']:
            if ast.op == '&&': op_code = self.emit.emitANDOP(param.frame)
            else: op_code = self.emit.emitOROP(param.frame)
        elif ast.op == '=/=':
            op_code = self.emit.emitREOP('!=', left_tp, param.frame)
        elif ast.op == '==':
            op_code = self.emit.emitREOP(ast.op, left_tp, param.frame)
        else:
            op_code = self.emit.emitREOP(ast.op.rstrip('.'), left_tp, param.frame)
        return left_code + right_code + op_code, left_tp

    def visitUnaryOp(self, ast, param):
        exp_code, tp = ast.body.accept(self, param)
        if ast.op == '!':
            op_code = self.emit.emitNOT(tp, param.frame)
        else:
            op_code = self.emit.emitNEGOP(tp, param.frame)
        return exp_code + op_code, tp
    
    def visitCallExpr(self, ast, param):
        sym = list(filter(lambda x: x.name == ast.method.name, param.sym))[0]
        param_code = reduce(lambda acc, ele: acc + self.visit(ele, Access(param.frame, param.sym, False))[0], ast.param, '')
        fn_call_code = self.emit.emitINVOKESTATIC(f'{sym.value.value}/{sym.name}', sym.mtype, param.frame)
        return param_code + fn_call_code, sym.mtype.rettype
    
    
    def visitId(self, ast, param):
        # list(map(lambda x: print(x.name, ast.name), param.sym))
        sym = list(filter(lambda x: x.name == ast.name, param.sym))[0]

        if type(sym.value) is Index:
            fn = self.emit.emitWRITEVAR if param.isLeft else self.emit.emitREADVAR
            id_code = fn(ast.name, sym.mtype, sym.value.value, param.frame)
        else:
            fn = self.emit.emitPUTSTATIC if param.isLeft else self.emit.emitGETSTATIC
            id_code = fn(f'{sym.value.value}/{ast.name}', sym.mtype, param.frame)
        return id_code, sym.mtype
    
    def visitArrayCell(self, ast, param):
        arr_code, arr_tp = self.visit(ast.arr, Access(param.frame, param.sym, False))
        idx_code = reduce(lambda acc, ele: acc + [self.visit(ele, Access(param.frame, param.sym, False))[0]] + [self.emit.emitAALOAD(param.frame)], ast.idx[:-1], [])
        idx_code += [self.visit(ast.idx[-1], Access(param.frame, param.sym, False))[0]]
        if param.isLeft:
            return (arr_code + ''.join(idx_code), arr_tp.eletype), arr_tp.eletype
        idx_code += [self.emit.emitALOAD(arr_tp.eletype, param.frame)]
        return arr_code + ''.join(idx_code), arr_tp.eletype
    
    def visitAssign(self, ast, param):
        if type(ast.lhs) is ArrayCell:
            left_code, left_tp = self.visit(ast.lhs, Access(param.frame, param.sym, True))
            right_code, right_tp = self.visit(ast.rhs, Access(param.frame, param.sym, False))
        else:
            right_code, right_tp = self.visit(ast.rhs, Access(param.frame, param.sym, False))
            left_code, left_tp = self.visit(ast.lhs, Access(param.frame, param.sym, True))

        if type(left_code) is tuple:
            store_code = self.emit.emitASTORE(left_code[1], param.frame)
            self.emit.printout(left_code[0] + right_code + store_code)
        else:
            self.emit.printout(right_code + left_code)
    
    def visitIf(self, ast, param):
        endLabel = param.frame.getNewLabel()
        labels = [param.frame.getNewLabel() for _ in range(len(ast.ifthenStmt))]
        for i, (exp, var_decls, stmts) in enumerate(ast.ifthenStmt):
            if i != 0:
                self.emit.printout(self.emit.emitLABEL(labels[i - 1], param.frame))
            exp_code, exp_tp = self.visit(exp, Access(param.frame, param.sym, False))
            self.emit.printout(exp_code)
            self.emit.printout(self.emit.emitIFFALSE(labels[i - 1], param.frame))
            param.frame.enterScope(False)
            start_label, end_label = param.frame.getStartLabel(), param.frame.getEndLabel()
            self.emit.printout(self.emit.emitLABEL(start_label, param.frame))
            sub_env = reduce(lambda acc, ele: MethodEnv(param.frame, [self.visit(ele, acc)] + acc.sym), var_decls, MethodEnv(param.frame, param.sym))
            for stmt in stmts:
                self.visit(stmt, sub_env)
            self.emit.printout(self.emit.emitLABEL(end_label, param.frame))
            param.frame.exitScope()
            self.emit.printout(self.emit.emitGOTO(endLabel, param.frame))
        self.emit.printout(self.emit.emitLABEL(labels[-1], param.frame))
        var_decls, stmts = ast.elseStmt
        if var_decls + stmts:
            param.frame.enterScope(False)
            start_label, end_label = param.frame.getStartLabel(), param.frame.getEndLabel()
            self.emit.printout(self.emit.emitLABEL(start_label, param.frame))
            sub_env = reduce(lambda acc, ele: MethodEnv(param.frame, [self.visit(ele, acc)] + acc.sym), var_decls, MethodEnv(param.frame, param.sym))
            for stmt in stmts:
                self.visit(stmt, sub_env)
            self.emit.printout(self.emit.emitLABEL(end_label, param.frame))
            param.frame.exitScope()
        self.emit.printout(self.emit.emitLABEL(endLabel, param.frame))

    
    def visitFor(self, ast, param):
        param.frame.enterLoop()
       
        continue_label = param.frame.getContinueLabel()
        break_label = param.frame.getBreakLabel()
        cond_label = param.frame.getNewLabel()

        self.visit(Assign(ast.idx1, ast.expr1), param)
        self.emit.printout(self.emit.emitLABEL(cond_label, param.frame))
        exp2_code, exp2_tp = self.visit(ast.expr2, Access(param.frame, param.sym, False))
        self.emit.printout(exp2_code)
        self.emit.printout(self.emit.emitIFFALSE(break_label, param.frame))
        
        param.frame.enterScope(False)
        start_label, end_label = param.frame.getStartLabel(), param.frame.getEndLabel()
        self.emit.printout(self.emit.emitLABEL(start_label, param.frame))
        local = reduce(lambda acc, ele: MethodEnv(param.frame, [self.visit(ele, acc)] + acc.sym), ast.loop[0], MethodEnv(param.frame, param.sym))
        list(map(lambda x: self.visit(x, local), ast.loop[1]))
        self.emit.printout(self.emit.emitLABEL(end_label, param.frame))
        param.frame.exitScope()

        self.emit.printout(self.emit.emitLABEL(continue_label, param.frame))
        idx1_code, idx1_tp = self.visit(ast.idx1, Access(param.frame, param.sym, False))
        exp3_code, exp3_tp = self.visit(ast.expr3, Access(param.frame, param.sym, False))
        self.emit.printout(idx1_code)
        self.emit.printout(exp3_code)
        self.emit.printout(self.emit.emitADDOP('+', idx1_tp, param.frame))
        idx1_code, idx1_tp = self.visit(ast.idx1, Access(param.frame, param.sym, True))
        self.emit.printout(idx1_code)
        self.emit.printout(self.emit.emitGOTO(cond_label, param.frame))
        self.emit.printout(self.emit.emitLABEL(break_label, param.frame))
        param.frame.exitLoop()
    
    def visitContinue(self, ast, param):
        self.emit.emitGOTO(param.frame.getContinueLabel(), param.frame)
    
    def visitBreak(self, ast, param):
        self.emit.emitGOTO(param.frame.getBreakLabel(), param.frame)
    
    def visitReturn(self, ast, param):
        if ast.expr:
            exp_code, exp_tp = self.visit(ast.expr, Access(param.frame, param.sym, False))
            self.emit.printout(exp_code)
        else:
            exp_tp = VoidType()
        self.emit.printout(self.emit.emitRETURN(exp_tp, param.frame))
    
    def visitDowhile(self, ast, param):
        param.frame.enterLoop()
        continue_label = param.frame.getContinueLabel()
        break_label = param.frame.getBreakLabel()
        start_label = param.frame.getNewLabel()

        self.emit.printout(self.emit.emitLABEL(start_label, param.frame))
        self.visitBlock(ast, param)
        self.emit.printout(self.emit.emitLABEL(continue_label, param.frame))
        exp_code, exp_tp = self.visit(ast.exp, Access(param.frame, param.sym, False))
        self.emit.printout(exp_code)
        self.emit.printout(self.emit.emitIFTRUE(start_label, param.frame))
        self.emit.printout(self.emit.emitLABEL(break_label, param.frame))
        param.frame.exitLoop()

    def visitWhile(self, ast, param):
        param.frame.enterLoop()
        continue_label = param.frame.getContinueLabel()
        break_label = param.frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(continue_label, param.frame))
        exp_code, exp_tp = self.visit(ast.exp, Access(param.frame, param.sym, False))
        self.emit.printout(exp_code)
        self.emit.printout(self.emit.emitIFFALSE(break_label, param.frame))
        
        self.visitBlock(ast, param)
        self.emit.printout(self.emit.emitGOTO(continue_label, param.frame))
        self.emit.printout(self.emit.emitLABEL(break_label, param.frame))
        param.frame.exitLoop()
    def visitBlock(self, ast, param):
        param.frame.enterScope(False)
        start_label, end_label = param.frame.getStartLabel(), param.frame.getEndLabel()
        self.emit.printout(self.emit.emitLABEL(start_label, param.frame))
        local = reduce(lambda acc, ele: MethodEnv(param.frame, [self.visit(ele, acc)] + acc.sym), ast.sl[0], MethodEnv(param.frame, param.sym))
        list(map(lambda x: self.visit(x, local), ast.sl[1]))
        self.emit.printout(self.emit.emitLABEL(end_label, param.frame))
        param.frame.exitScope()

    def visitCallStmt(self, ast, param):
        sym = list(filter(lambda x: x.name == ast.method.name, param.sym))[0]
        param_code = reduce(lambda acc, ele: acc + self.visit(ele, Access(param.frame, param.sym, False))[0], ast.param, '')
        fn_call_code = self.emit.emitINVOKESTATIC(f'{sym.value.value}/{sym.name}', sym.mtype, param.frame)
        self.emit.printout(param_code + fn_call_code)
    def visitIntLiteral(self, ast, param):
        return self.emit.emitPUSHICONST(ast.value, param.frame), IntType()
    
    def visitFloatLiteral(self, ast, param):
        return self.emit.emitPUSHFCONST(str(ast.value), param.frame), FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), param.frame), BoolType()
    
    def visitStringLiteral(self, ast, param):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), param.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        dim1_code, dim1_tp = self.visit(IntLiteral(len(ast.value)), param)
        tp = getTypeOfLiteral(ast.value[0])
        if type(ast.value[0]) is not ArrayLiteral:
            if type(ast.value[0]) is StringLiteral:
                arr1d_code = self.emit.emitANEWARRAY(None, StringType(), param.frame)
            else:
                arr1d_code = self.emit.emitNEWARRAY(tp, param.frame)
            code = ''
            for i, value in enumerate(ast.value):
                code += self.emit.emitDUP(param.frame)
                code += self.visit(IntLiteral(i), param)[0]
                code += self.visit(value, param)[0]
                code += self.emit.emitASTORE(tp, param.frame)
            return dim1_code + arr1d_code + code, ArrayType([len(ast.value)], tp)
        else:
            arrnd_code = self.emit.emitANEWARRAY(getNDim(ast) - 1, tp, param.frame)
            code = ''
            inner_type = None
            for i, value in enumerate(ast.value):
                code += self.emit.emitDUP(param.frame)
                code += self.visit(IntLiteral(i), param)[0]
                c, inner_type =  self.visit(value, param)
                code += c
                code += self.emit.emitASTORE(ArrayType(None, None), param.frame)
            return dim1_code + arrnd_code + code, ArrayType([len(ast.value)] + inner_type.dimen, tp)

