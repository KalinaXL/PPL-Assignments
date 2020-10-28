# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_declaration.
    def visitVariable_declaration(self, ctx:BKITParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_name.
    def visitArray_name(self, ctx:BKITParser.Array_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_name.
    def visitVariable_name(self, ctx:BKITParser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_initializer.
    def visitVariable_initializer(self, ctx:BKITParser.Variable_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_value.
    def visitVariable_value(self, ctx:BKITParser.Variable_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_value.
    def visitArray_value(self, ctx:BKITParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_value_list.
    def visitArray_value_list(self, ctx:BKITParser.Array_value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declaration.
    def visitFunction_declaration(self, ctx:BKITParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameters.
    def visitParameters(self, ctx:BKITParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#post_statement.
    def visitPost_statement(self, ctx:BKITParser.Post_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment.
    def visitAssignment(self, ctx:BKITParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indices.
    def visitIndices(self, ctx:BKITParser.IndicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_start.
    def visitIf_start(self, ctx:BKITParser.If_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_statement.
    def visitElseif_statement(self, ctx:BKITParser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_statement.
    def visitElse_statement(self, ctx:BKITParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_condition.
    def visitFor_condition(self, ctx:BKITParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#in_parameters.
    def visitIn_parameters(self, ctx:BKITParser.In_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_function.
    def visitCall_function(self, ctx:BKITParser.Call_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)



del BKITParser