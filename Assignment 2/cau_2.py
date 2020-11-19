class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1 + ctx.vardecls().accept(self)

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 1 + ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0: return 1
        return 1 + ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return ctx.mptype().accept(self) + ctx.ids().accept(self) + 1;

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1: return 1
        return 1 + ctx.ids().accept(self)