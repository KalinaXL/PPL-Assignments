# Cau 6
from functools import reduce

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return ctx.exp().accept(self)
    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1: return ctx.term(0).accept(self)
        last_index = (ctx.getChildCount() - 1) // 2
        return reduce(lambda x, y: Binary(y[0].getText(), y[1].accept(self), x), zip(ctx.ASSIGN()[::-1], ctx.term()[:-1][::-1]), ctx.term(last_index).accept(self))
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 1: return ctx.factor(0).accept(self)
        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount() == 1: return ctx.operand(0).accept(self)
        return reduce(lambda x, y: Binary(y[0].getText(), x, y[1].accept(self)), zip(ctx.ANDOR(), ctx.operand()[1:]), ctx.operand(0).accept(self))
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT(): return BooleanLiteral(eval(ctx.BOOLIT().getText()))
        return ctx.exp().accept(self)