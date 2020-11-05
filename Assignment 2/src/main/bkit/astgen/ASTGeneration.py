from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.function_declaration():
            fn_decls = [fn_ctx.accept(self) for fn_ctx in ctx.function_declaration()]
        else:
            fn_decls = []
        return Program(var_decls + fn_decls)
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INTEGER(): return IntLiteral(eval(ctx.INTEGER().getText()))
        if ctx.FLOAT(): return FloatLiteral(eval(ctx.FLOAT().getText()))
        if ctx.BOOLEAN(): return BooleanLiteral(eval(ctx.BOOLEAN().getText()))
        if ctx.STRING(): return StringLiteral(ctx.STRING().getText())
        return ctx.array_value_list().accept(self)
    def visitArray_value_list(self, ctx: BKITParser.Array_value_listContext):
        if ctx.getChildCount() == 2: return ArrayLiteral([])
        return ArrayLiteral(ctx.array_value().accept(self))
    def visitVariable_value(self, ctx: BKITParser.Variable_valueContext):
        return ctx.literal().accept(self)

    def visitArray_value(self, ctx: BKITParser.Array_valueContext):
        return [vv_ctx.accept(self) for vv_ctx in ctx.variable_value()]
    def visitOperands(self, ctx: BKITParser.OperandsContext):
        if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
        return ctx.literal().accept(self)
    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() == 1: return ctx.exp1(0).accept(self)
        left = ctx.exp1(0).accept(self)
        right = ctx.exp1(1).accept(self)
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1: return ctx.exp2().accept(self)
        left = ctx.exp1().accept(self)
        right = ctx.exp2().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 1: return ctx.exp3().accept(self)
        left = ctx.exp2().accept(self)
        right = ctx.exp3().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1: return  ctx.exp4().accept(self)
        left = ctx.exp3().accept(self)
        right = ctx.exp4().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1: return ctx.exp5().accept(self)
        return UnaryOp(ctx.NOT().getText(), ctx.exp4().accept(self))
    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1: return ctx.exp6().accept(self)
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp5().accept(self))
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.getChildCount() == 1: return ctx.exp7().accept(self)
        if ctx.IDENTIFIER():
            lhs = Id(ctx.IDENTIFIER().getText())
        else:
            lhs = ctx.call_function().accept(self)
        indices = ctx.indices().accept(self)
        return ArrayCell(lhs, indices)
    def visitExp7(self, ctx: BKITParser.Exp7Context):
        if ctx.exp8(): return ctx.exp8().accept(self)
        return ctx.call_function().accept(self)
    def visitExp8(self, ctx: BKITParser.Exp8Context):
        if ctx.getChildCount() == 1: return ctx.operands().accept(self)
        return ctx.expression().accept(self)
    def visitIn_parameters(self, ctx: BKITParser.In_parametersContext):
        return [exp_ctx.accept(self) for exp_ctx in ctx.expression()]
    def visitCall_function(self, ctx: BKITParser.Call_functionContext):
        name = Id(ctx.IDENTIFIER().getText())
        params = ctx.in_parameters().accept(self) if ctx.in_parameters() else []
        return CallExpr(name, params)
    def visitArray_name(self, ctx: BKITParser.Array_nameContext):
        name = ctx.IDENTIFIER().getText()
        dims = [eval(int_ctx.getText()) for int_ctx in ctx.INTEGER()]
        return Id(name), dims
    def visitVariable_name(self, ctx: BKITParser.Variable_nameContext):
        if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText()), []
        return ctx.array_name().accept(self)
    def visitVariable_initializer(self, ctx: BKITParser.Variable_initializerContext):
        name, dims = ctx.variable_name().accept(self)
        value = ctx.variable_value().accept(self) if ctx.variable_value() else None
        return VarDecl(name, dims, value)
    def visitVariable_declaration(self, ctx: BKITParser.Variable_declarationContext):
        return [vi_ctx.accept(self) for vi_ctx in ctx.variable_initializer()]

    def visitParameter_list(self, ctx: BKITParser.Parameter_listContext):
        return [pr_ctx.accept(self) for pr_ctx in ctx.variable_name()]
    def visitParameters(self, ctx: BKITParser.ParametersContext):
        vrs =  ctx.parameter_list().accept(self)
        return [VarDecl(vr[0], vr[1], None) for vr in vrs]
    def visitFunction_declaration(self, ctx: BKITParser.Function_declarationContext):
        name = Id(ctx.IDENTIFIER().getText())
        params = ctx.parameters().accept(self) if ctx.parameters() else []
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [pt_ctx.accept(self) for pt_ctx in ctx.post_statement()]
        else:
            stmts = []
        return FuncDecl(name, params, (var_decls, stmts))

    def visitIndices(self, ctx: BKITParser.IndicesContext):
        return [exp_ctx.accept(self) for exp_ctx in ctx.expression()]
    def visitAssignment(self, ctx: BKITParser.AssignmentContext):
        if ctx.IDENTIFIER(): lhs = Id(ctx.IDENTIFIER().getText())
        elif ctx.call_function(): lhs = ctx.call_function().accept(self)
        if ctx.indices():
            indices = ctx.indices().accept(self)
            lhs = ArrayCell(lhs, indices)
        value = ctx.expression().accept(self)
        return Assign(lhs, value)

    def visitIf_start(self, ctx: BKITParser.If_startContext):
        exp = ctx.expression().accept(self)
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [st_ctx.accept(self) for st_ctx in ctx.post_statement()]
        else:
            stmts = []
        return exp, var_decls, stmts
    def visitElseif_statement(self, ctx: BKITParser.Elseif_statementContext):
        exp = ctx.expression().accept(self)
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [st_ctx.accept(self) for st_ctx in ctx.post_statement()]
        else:
            stmts = []
        return exp, var_decls, stmts
    def visitElse_statement(self, ctx: BKITParser.Else_statementContext):
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [st_ctx.accept(self) for st_ctx in ctx.post_statement()]
        else:
            stmts = []
        return var_decls, stmts
    def visitIf_statement(self, ctx: BKITParser.If_statementContext):
        if_tup = [ctx.if_start().accept(self)]
        if ctx.elseif_statement():
            for ef_ctx in ctx.elseif_statement():
                if_tup.append(ef_ctx.accept(self))
        else_tup = ctx.else_statement().accept(self) if ctx.else_statement() else []
        return If(if_tup, else_tup)
    
    def visitFor_condition(self, ctx: BKITParser.For_conditionContext):
        idx1 = Id(ctx.IDENTIFIER().getText())
        exp1 = ctx.expression(0).accept(self)
        exp2 = ctx.expression(1).accept(self)
        exp3 = ctx.expression(2).accept(self)
        return idx1, exp1, exp2, exp3
    def visitFor_statement(self, ctx: BKITParser.For_statementContext):
        idx1, exp1, exp2, exp3 = ctx.for_condition().accept(self)
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [st_ctx.accept(self) for st_ctx in ctx.post_statement()]
        else:
            stmts = []
        return For(idx1, exp1, exp2, exp3, (var_decls, stmts))
    def visitWhile_statement(self, ctx: BKITParser.While_statementContext):
        exp = ctx.expression().accept(self)
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [st_ctx.accept(self) for st_ctx in ctx.post_statement()]
        else:
            stmts = []
        return While(exp, (var_decls, stmts))
    def visitDo_while_statement(self, ctx: BKITParser.Do_while_statementContext):
        if ctx.variable_declaration():
            var_decls = [var_decl for vd_ctx in ctx.variable_declaration() for var_decl in vd_ctx.accept(self)]
        else:
            var_decls = []
        if ctx.post_statement():
            stmts = [st_ctx.accept(self) for st_ctx in ctx.post_statement()]
        else:
            stmts = []
        exp = ctx.expression().accept(self)
        return Dowhile((var_decls, stmts), exp)
    def visitCall_statement(self, ctx: BKITParser.Call_statementContext):
        fn = ctx.call_function().accept(self)
        return CallStmt(fn.method, fn.param)
    def visitPost_statement(self, ctx: BKITParser.Post_statementContext):
        return ctx.getChild(0).accept(self)


    def visitBreak_statement(self, ctx: BKITParser.Break_statementContext):
        return Break()
    def visitContinue_statement(self, ctx: BKITParser.Continue_statementContext):
        return Continue()
    def visitReturn_statement(self, ctx: BKITParser.Return_statementContext):
        expr = ctx.expression().accept(self) if ctx.expression() else None
        return Return(expr)