import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_vardecl_1(self):
        input = """Var: x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_vardecl_2(self):
        input = """Var: x,y;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_vardecl_3(self):
        input = """Var: x = 10;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_vardecl_4(self):
        input = """Var: x = 10, y = True;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_vardecl_5(self):
        input = """Var: n[10];"""
        expect = Program([VarDecl(Id("n"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_vardecl_6(self):
        input = """Var: n[10], y = "string";"""
        expect = Program([VarDecl(Id("n"),[10],None),VarDecl(Id("y"),[],StringLiteral("string"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_vardecl_7(self):
        input = """Var: n[10] = {1,2,3,4}, n = 10;"""
        expect = Program([VarDecl(Id("n"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),VarDecl(Id("n"),[],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_vardecl_8(self):
        input = r"""Var: n = True;
Var: t,x,z;"""
        expect = Program([VarDecl(Id("n"),[],BooleanLiteral(True)),VarDecl(Id("t"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("z"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_vardecl_9(self):
        input = """Var: n[2][1] = {{True},{"string"}};"""
        expect = Program([VarDecl(Id("n"),[2,1],ArrayLiteral([ArrayLiteral([BooleanLiteral(True)]),ArrayLiteral([StringLiteral("string")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_vardecl_10(self):
        input = r"""Var: n[10];
Var: t = "String";
Var: m = 10;"""
        expect = Program([VarDecl(Id("n"),[10],None),VarDecl(Id("t"),[],StringLiteral("String")),VarDecl(Id("m"),[],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_vardecl_11(self):
        input = """Var: n = 7, t = {1,2,3};"""
        expect = Program([VarDecl(Id("n"),[],IntLiteral(7)),VarDecl(Id("t"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_vardecl_12(self):
        input = """Var: t[1];
Var: m,y = 7,z;"""
        expect = Program([VarDecl(Id("t"),[1],None),VarDecl(Id("m"),[],None),VarDecl(Id("y"),[],IntLiteral(7)),VarDecl(Id("z"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_vardecl_13(self):
        input = """Var: n = 0x45;"""
        expect = Program([VarDecl(Id("n"),[],IntLiteral(69))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_vardecl_14(self):
        input = """Var: t = 0o12, n = 0O11;"""
        expect = Program([VarDecl(Id("t"),[],IntLiteral(10)),VarDecl(Id("n"),[],IntLiteral(9))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_vardecl_15(self):
        input = r"""Var: n[3] = {0x14,0O7,5.e-1};
Var: t = 0X7F;"""
        expect = Program([VarDecl(Id("n"),[3],ArrayLiteral([IntLiteral(20),IntLiteral(7),FloatLiteral(0.5)])),VarDecl(Id("t"),[],IntLiteral(127))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    
    def test_funcdecl_1(self):
        input = r"""Function: foo
Body:
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_funcdecl_2(self):
        input = r"""Function: hello
Body:
    Var: n = 7;
    n = n + 1;
EndBody."""
        expect = Program([FuncDecl(Id("hello"),[],([VarDecl(Id("n"),[],IntLiteral(7))],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_funcdecl_3(self):
        input = r"""Function: foo
Parameter: x
Body:
    t = 0;
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("t"),IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_funcdecl_4(self):
        input = r"""Function: ppl
Parameter: t[10], x
Body:
EndBody."""
        expect = Program([FuncDecl(Id("ppl"),[VarDecl(Id("t"),[10],None),VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_funcdecl_5(self):
        input = r"""Function: test
Body:
    t = 4*5;
EndBody."""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(Id("t"),BinaryOp("*",IntLiteral(4),IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_assign_stmt_1(self):
        input = r"""Function: foo
Body:
    t = 1 + {1,2,3};
    e = 7;
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("t"),BinaryOp("+",IntLiteral(1),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),Assign(Id("e"),IntLiteral(7))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_assign_stmt_2(self):
        input = r"""Function: test
Parameter: x
Body:
    Var: x = 7;
    x =  x + 1;
EndBody."""
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("x"),[],IntLiteral(7))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_assign_stmt_3(self):
        input = r"""Function: test
Body:
    m = 12 + call(x,y);
EndBody."""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(Id("m"),BinaryOp("+",IntLiteral(12),CallStmt(Id("call"),[Id("x"),Id("y")])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_assign_stmt_4(self):
        input = r"""Function: a
Body:
    t = 7.8 + 0X7 - 3.e-4;
    m = 0;
    t = "String" + "string";
EndBody."""
        expect = Program([FuncDecl(Id("a"),[],([],[Assign(Id("t"),BinaryOp("-",BinaryOp("+",FloatLiteral(7.8),IntLiteral(7)),FloatLiteral(0.0003))),Assign(Id("m"),IntLiteral(0)),Assign(Id("t"),BinaryOp("+",StringLiteral("String"),StringLiteral("string")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_if_stmt_1(self):
        input = r"""Function: test_if
Parameter: a
Body:
    If a > 0 Then
        a = a + 1;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id("test_if"),[VarDecl(Id("a"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(0)),[],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_if_stmt_2(self):
        input = r"""Function: test_if
Body:
    If a > 0 Then
        Return a;
    Else
        Return 0;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id("test_if"),[],([],[If([(BinaryOp(">",Id("a"),IntLiteral(0)),[],[Return(Id("a"))])],([],[Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_if_stmt_3(self):
        input = r"""Function: foo
Parameter: a,b
Body:
    If a > 0 Then
        Return 1;
    ElseIf b >= 0 Then
        Return 0;
    Else
        Return -1;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(0)),[],[Return(IntLiteral(1))]),(BinaryOp(">=",Id("b"),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[Return(UnaryOp("-",IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_if_stmt_4(self):
        input = r"""Function: f
Body:
    If (a>0) && (b>0) Then
        Return a;
    ElseIf b > 0 Then
        Return b;
    Else
        Return -1;
    EndIf.
    If 7 Then
        i = i + 1;
    Else
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id("f"),[],([],[If([(BinaryOp("&&",BinaryOp(">",Id("a"),IntLiteral(0)),BinaryOp(">",Id("b"),IntLiteral(0))),[],[Return(Id("a"))]),(BinaryOp(">",Id("b"),IntLiteral(0)),[],[Return(Id("b"))])],([],[Return(UnaryOp("-",IntLiteral(1)))])),If([(IntLiteral(7),[],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_if_stmt_5(self):
        input = r"""Function: t
Parameter: a,b
Body:
    If (a == 0) || (b < 0) Then
        b = b + 1;
        Return True;
    ElseIf b > 0 Then
        b = call();
        Return False;
    Else
        t = t + 1;
        Return False;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id("t"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(0)),BinaryOp("<",Id("b"),IntLiteral(0))),[],[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Return(BooleanLiteral(True))]),(BinaryOp(">",Id("b"),IntLiteral(0)),[],[Assign(Id("b"),CallStmt(Id("call"),[])),Return(BooleanLiteral(False))])],([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1))),Return(BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_if_stmt_6(self):
        input = r"""Function: y
Body:
    If i == 0 Then
        i = i + 1;
        Break;
        Return 1;
    ElseIf (i > 0) && (y == 6) Then
        y = y + 7;
    ElseIf y > 7 Then
    Else
        Return False;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id("y"),[],([],[If([(BinaryOp("==",Id("i"),IntLiteral(0)),[],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Break(),Return(IntLiteral(1))]),(BinaryOp("&&",BinaryOp(">",Id("i"),IntLiteral(0)),BinaryOp("==",Id("y"),IntLiteral(6))),[],[Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(7)))]),(BinaryOp(">",Id("y"),IntLiteral(7)),[],[])],([],[Return(BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_for_stmt_1(self):
        input = r"""Function: test_for1
Parameter: x,y
Body:
    For(x = 1, x < 5, 2) Do
        t = t + 1;
    EndFor.
    Return t;
EndBody."""
        expect = Program([FuncDecl(Id("test_for1"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[For(Id("x"),IntLiteral(1),BinaryOp("<",Id("x"),IntLiteral(5)),IntLiteral(2),([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1)))])),Return(Id("t"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_for_stmt_2(self):
        input = r"""Function: test_for2
Body:
    Var: t = 0, y = True;
    For(i = 0, i < n, call(update)) Do
        t = t + 1;
        y = False;
    EndFor.
    t = t + 1;
EndBody."""
        expect = Program([FuncDecl(Id("test_for2"),[],([VarDecl(Id("t"),[],IntLiteral(0)),VarDecl(Id("y"),[],BooleanLiteral(True))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),CallStmt(Id("call"),[Id("update")]),([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1))),Assign(Id("y"),BooleanLiteral(False))])),Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_for_stmt_3(self):
        input = r"""Function: test_for3
Parameter: x
Body:
    For(i = 0, i < 10, update) Do
        t = t + 1;
        For(j = 1, j < i,update1) Do
            t = t + 2;
        EndFor.
    EndFor.
EndBody."""
        expect = Program([FuncDecl(Id("test_for3"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),Id("update"),([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1))),For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),Id("i")),Id("update1"),([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(2)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_for_stmt_4(self):
        input = r"""Function: test_for4
Body:
    For(i = call(init),call(condition),call(update)) Do
    EndFor.
EndBody."""
        expect = Program([FuncDecl(Id("test_for4"),[],([],[For(Id("i"),CallStmt(Id("call"),[Id("init")]),CallStmt(Id("call"),[Id("condition")]),CallStmt(Id("call"),[Id("update")]),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_for_stmt_5(self):
        input = r"""Function: test
Body:
    For(a = 0,c,u) Do
        call();
        Return 1;
    EndFor.
EndBody."""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("a"),IntLiteral(0),Id("c"),Id("u"),([],[CallStmt(Id("call"),[]),Return(IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_for_stmt_6(self):
        input = r"""Function: sum
Parameter: t, sum
Body:
    For(a = 0, a < t, 1) Do
        sum = sum + a;
    EndFor.
    For(a = t, a > 0, -1) Do
    EndFor.
    Return;
EndBody."""
        expect = Program([FuncDecl(Id("sum"),[VarDecl(Id("t"),[],None),VarDecl(Id("sum"),[],None)],([],[For(Id("a"),IntLiteral(0),BinaryOp("<",Id("a"),Id("t")),IntLiteral(1),([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("a")))])),For(Id("a"),Id("t"),BinaryOp(">",Id("a"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_while_stmt_1(self):
        input = r"""Var: x = 1, y;
Function: foo
Body:
    While x < 10 Do
        println(x);
    EndWhile.
EndBody."""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],None),FuncDecl(Id("foo"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(10)),([],[CallStmt(Id("println"),[Id("x")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_while_stmt_2(self):
        input = r"""Function: test_while
Body:
    While n + 10 Do
        n = n + 1;
        n = 3;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("test_while"),[],([],[While(BinaryOp("+",Id("n"),IntLiteral(10)),([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Assign(Id("n"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    def test_while_stmt_3(self):
        input = r"""Function: test
Parameter: x
Body:
    While n == 10 Do
        Var: t = 0;
        x = x + 1;
        call("string");
        Return True;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("==",Id("n"),IntLiteral(10)),([VarDecl(Id("t"),[],IntLiteral(0))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),CallStmt(Id("call"),[StringLiteral("string")]),Return(BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_while_stmt_4(self):
        input = r"""Function: testw
Parameter: n
Body:
    While i < 10 Do
        Var: i = 0;
        While j > i Do
            Var: x = 7;
            y[10] = 7;
        EndWhile.
        x = x + 1;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("testw"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("<",Id("i"),IntLiteral(10)),([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp(">",Id("j"),Id("i")),([VarDecl(Id("x"),[],IntLiteral(7))],[Assign(ArrayCell(Id("y"),[IntLiteral(10)]),IntLiteral(7))])),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_while_stmt_5(self):
        input = r"""Function: t
Body:
    While t =/= 0 Do
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("t"),[],([],[While(BinaryOp("=/=",Id("t"),IntLiteral(0)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_while_stmt_6(self):
        input = r"""Function: a
Body:
    While x Do m = m + 1; EndWhile.
    While n Do x = x + 1; EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("a"),[],([],[While(Id("x"),([],[Assign(Id("m"),BinaryOp("+",Id("m"),IntLiteral(1)))])),While(Id("n"),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_do_stmt_1(self):
        input = r"""Function: foo
Body:
    Do
        t = t + 1;
    While t < 10 EndDo.
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1)))]),BinaryOp("<",Id("t"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_do_stmt_2(self):
        input = r"""Function: test
Body:
    Do
        x = 1 + y;
        y = call(i);
    While y > 0 EndDo.
EndBody."""
        expect = Program([FuncDecl(Id("test"),[],([],[Dowhile(([],[Assign(Id("x"),BinaryOp("+",IntLiteral(1),Id("y"))),Assign(Id("y"),CallStmt(Id("call"),[Id("i")]))]),BinaryOp(">",Id("y"),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_do_stmt_3(self):
        input = r"""Function: while
Parameter: x
Body:
    Var: x = 0;
    Do
        Do
            x = 0;
            t = x && r;
        While t EndDo.
    While False EndDo.
EndBody."""
        expect = Program([FuncDecl(Id("while"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("x"),[],IntLiteral(0))],[Dowhile(([],[Dowhile(([],[Assign(Id("x"),IntLiteral(0)),Assign(Id("t"),BinaryOp("&&",Id("x"),Id("r")))]),Id("t"))]),BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_do_stmt_4(self):
        input = r"""Function: foo
Body:
    Do
    While x > 0 EndDo.
    Return;
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[]),BinaryOp(">",Id("x"),IntLiteral(0))),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_do_stmt_5(self):
        input = r"""Function: a
Body:
    Do
        f = t + (call() + t[6]);
        y = t[6][7];
    While y < 0 EndDo.
    Do
        Break;
    While i EndDo. 
EndBody."""
        expect = Program([FuncDecl(Id("a"),[],([],[Dowhile(([],[Assign(Id("f"),BinaryOp("+",Id("t"),BinaryOp("+",CallStmt(Id("call"),[]),ArrayCell(Id("t"),[IntLiteral(6)])))),Assign(Id("y"),ArrayCell(Id("t"),[IntLiteral(6),IntLiteral(7)]))]),BinaryOp("<",Id("y"),IntLiteral(0))),Dowhile(([],[Break()]),Id("i"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_do_stmt_6(self):
        input = r"""Function: y_
Body:
    Do
        Var: x = 10;
        x = x + 1;
    While x < 10 EndDo.
EndBody."""
        expect = Program([FuncDecl(Id("y_"),[],([],[Dowhile(([VarDecl(Id("x"),[],IntLiteral(10))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),BinaryOp("<",Id("x"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_break_stmt_1(self):
        input = r"""Function: test
Body:
    Break;
EndBody."""
        expect = Program([FuncDecl(Id("test"),[],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_break_stmt_2(self):
        input = r"""Function: t
Body:
    For(x = 0, x < 10, 1) Do
        t = t + " ";
        Break;
    EndFor.
EndBody."""
        expect = Program([FuncDecl(Id("t"),[],([],[For(Id("x"),IntLiteral(0),BinaryOp("<",Id("x"),IntLiteral(10)),IntLiteral(1),([],[Assign(Id("t"),BinaryOp("+",Id("t"),StringLiteral(" "))),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_break_stmt_3(self):
        input = r"""Function: t
Body:
    While x < 10 Do
        While n > 4 Do
            a = 1 + func();
            Break;
            Break;
        EndWhile.
        Break;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("t"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(10)),([],[While(BinaryOp(">",Id("n"),IntLiteral(4)),([],[Assign(Id("a"),BinaryOp("+",IntLiteral(1),CallStmt(Id("func"),[]))),Break(),Break()])),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_continue_stmt_1(self):
        input = r"""Function: foo
Body:
    Continue;
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_continue_stmt_2(self):
        input = r"""Function: test
Parameter: x
Body:
    While x < 10 Do
        x = x + 1;
        Continue;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("<",Id("x"),IntLiteral(10)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_continue_stmt_3(self):
        input = r"""Function: sum
Parameter: m
Body:
    Var: sum = 0;
    For(i = 0, i < m, 1) Do
        If i == m\2 Then
            Continue;
        Else
            sum = sum + i;
        EndIf.
    EndFor.
EndBody."""
        ifstmt = If([(BinaryOp("==",Id("i"),BinaryOp("\\",Id("m"),IntLiteral(2))),[],[Continue()])],([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("i")))]))
        expect = Program([FuncDecl(Id("sum"),[VarDecl(Id("m"),[],None)],([VarDecl(Id("sum"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("m")),IntLiteral(1),([],[ifstmt]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    def test_call_stmt_1(self):
        input = r"""Function: my_func
Parameter: n, m
Body:
    x = callfunc(n);
    m = x + 1;
    Return;
EndBody."""
        expect = Program([FuncDecl(Id("my_func"),[VarDecl(Id("n"),[],None),VarDecl(Id("m"),[],None)],([],[Assign(Id("x"),CallStmt(Id("callfunc"),[Id("n")])),Assign(Id("m"),BinaryOp("+",Id("x"),IntLiteral(1))),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_call_stmt_2(self):
        input = r"""Function: func
Body:
    print("Hello World");
    x = x + call(a[5][6]);
EndBody."""
        expect = Program([FuncDecl(Id("func"),[],([],[CallStmt(Id("print"),[StringLiteral("Hello World")]),Assign(Id("x"),BinaryOp("+",Id("x"),CallStmt(Id("call"),[ArrayCell(Id("a"),[IntLiteral(5),IntLiteral(6)])])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    
    def test_call_stmt_3(self):
        input = r"""Var: m = 0;
Function: test
Body:
    If m =/= -1 Then
        x = call()[m];
    EndIf.
EndBody."""
        ifstmt = If([(BinaryOp("=/=",Id("m"),UnaryOp("-",IntLiteral(1))),[],[Assign(Id("x"),ArrayCell(CallStmt(Id("call"),[]),[Id("m")]))])],([],[]))
        expect = Program([VarDecl(Id("m"),[],IntLiteral(0)),FuncDecl(Id("test"),[],([],[ifstmt]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_call_stmt_4(self):
        input = r"""Function: ppl
Body:
    call("this is parameter1",para2);
EndBody."""
        expect = Program([FuncDecl(Id("ppl"),[],([],[CallStmt(Id("call"),[StringLiteral("this is parameter1"),Id("para2")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_call_stmt_5(self):
        input = r"""Function: test_call
Body:
    While t < call(x) Do
        m = m + t(7,8,9.e1);
        t = g("string","end") + "string1";
    EndWhile. 
EndBody."""
        expect = Program([FuncDecl(Id("test_call"),[],([],[While(BinaryOp("<",Id("t"),CallStmt(Id("call"),[Id("x")])),([],[Assign(Id("m"),BinaryOp("+",Id("m"),CallStmt(Id("t"),[IntLiteral(7),IntLiteral(8),FloatLiteral(90.0)]))),Assign(Id("t"),BinaryOp("+",CallStmt(Id("g"),[StringLiteral("string"),StringLiteral("end")]),StringLiteral("string1")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    
    def test_return_stmt_1(self):
        input = r"""Var: m = 0;
Function: foo
Body:
    Return;
EndBody."""
        expect = Program([VarDecl(Id("m"),[],IntLiteral(0)),FuncDecl(Id("foo"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_return_stmt_2(self):
        input = r"""Function: test_return
Body:
    If True Then
        Return True;
    ElseIf (x==False) && (x==True) Then
        Return "Stupid";
    Else
        Return False;
    EndIf.
EndBody."""
        ifstmt = If([(BooleanLiteral(True),[],[Return(BooleanLiteral(True))]),(BinaryOp("&&",BinaryOp("==",Id("x"),BooleanLiteral(False)),BinaryOp("==",Id("x"),BooleanLiteral(True))),[],[Return(StringLiteral("Stupid"))])],([],[Return(BooleanLiteral(False))]))
        expect = Program([FuncDecl(Id("test_return"),[],([],[ifstmt]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    def test_return_stmt_3(self):
        input = r"""Function: test_ret
Parameter: ret, m
Body:
    Var: x = 0;
    While x < m Do
        If x == m - 1 Then
            Return call(m*m);
        ElseIf x < m\2 Then
            Return call(m,ret);
        Else
            x = x + 1;
        EndIf.
    EndWhile.
EndBody."""
        ifstmt = If([(BinaryOp("==",Id("x"),BinaryOp("-",Id("m"),IntLiteral(1))),[],[Return(CallStmt(Id("call"),[BinaryOp("*",Id("m"),Id("m"))]))]),(BinaryOp("<",Id("x"),BinaryOp("\\",Id("m"),IntLiteral(2))),[],[Return(CallStmt(Id("call"),[Id("m"),Id("ret")]))])],([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))
        expect = Program([FuncDecl(Id("test_ret"),[VarDecl(Id("ret"),[],None),VarDecl(Id("m"),[],None)],([VarDecl(Id("x"),[],IntLiteral(0))],[While(BinaryOp("<",Id("x"),Id("m")),([],[ifstmt]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_exp_stmt_1(self):
        input = r"""Function: foo
Body:
    x = x + 1;
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_exp_stmt_2(self):
        input = r"""Function: func
Body:
    y = y * 2 \ 5 + t;
    m = foo() + ( 7 + 2 )*8;
    Return;
EndBody."""
        expect = Program([FuncDecl(Id("func"),[],([],[Assign(Id("y"),BinaryOp("+",BinaryOp("\\",BinaryOp("*",Id("y"),IntLiteral(2)),IntLiteral(5)),Id("t"))),Assign(Id("m"),BinaryOp("+",CallStmt(Id("foo"),[]),BinaryOp("*",BinaryOp("+",IntLiteral(7),IntLiteral(2)),IntLiteral(8)))),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_exp_stmt_3(self):
        input = r"""Function: ppl
Body:
    call(x+y,t*2+1);
    foo()[1+2][t()] = 7 + x;
EndBody."""
        expect = Program([FuncDecl(Id("ppl"),[],([],[CallStmt(Id("call"),[BinaryOp("+",Id("x"),Id("y")),BinaryOp("+",BinaryOp("*",Id("t"),IntLiteral(2)),IntLiteral(1))]),Assign(ArrayCell(CallStmt(Id("foo"),[]),[BinaryOp("+",IntLiteral(1),IntLiteral(2)),CallStmt(Id("t"),[])]),BinaryOp("+",IntLiteral(7),Id("x")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    def test_exp_stmt_4(self):
        input = r"""Function: test_Exp
Parameter: p, t[6]
Body:
    Var: t = 0, x[5] = {1,2,3,4,5};
    x[4] = t() + 6+7\2;
    y = x + 2 == 8;
EndBody."""
        expect = Program([FuncDecl(Id("test_Exp"),[VarDecl(Id("p"),[],None),VarDecl(Id("t"),[6],None)],([VarDecl(Id("t"),[],IntLiteral(0)),VarDecl(Id("x"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))],[Assign(ArrayCell(Id("x"),[IntLiteral(4)]),BinaryOp("+",BinaryOp("+",CallStmt(Id("t"),[]),IntLiteral(6)),BinaryOp("\\",IntLiteral(7),IntLiteral(2)))),Assign(Id("y"),BinaryOp("==",BinaryOp("+",Id("x"),IntLiteral(2)),IntLiteral(8)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_exp_stmt_5(self):
        input = r"""Function: t
Body:
    If x == 2 + foo()*1.5 Then
        t = foo({1,2,3});
    Else
        sum = sum + 1;
        n = y||8+2;
    EndIf.
EndBody."""
        ifstmt = If([(BinaryOp("==",Id("x"),BinaryOp("+",IntLiteral(2),BinaryOp("*",CallStmt(Id("foo"),[]),FloatLiteral(1.5)))),[],[Assign(Id("t"),CallStmt(Id("foo"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))])],([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),IntLiteral(1))),Assign(Id("n"),BinaryOp("||",Id("y"),BinaryOp("+",IntLiteral(8),IntLiteral(2))))]))
        expect = Program([FuncDecl(Id("t"),[],([],[ifstmt]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    def test_exp_stmt_6(self):
        input = r"""Function: love
Body:
    m = m <= 2 + 7 || foo()* call();
    Return m; 
EndBody."""
        expect = Program([FuncDecl(Id("love"),[],([],[Assign(Id("m"),BinaryOp("<=",Id("m"),BinaryOp("||",BinaryOp("+",IntLiteral(2),IntLiteral(7)),BinaryOp("*",CallStmt(Id("foo"),[]),CallStmt(Id("call"),[]))))),Return(Id("m"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    
    def test_exp_stmt_7(self):
        input = r"""Function: k
Body:
    i = 7.6e-1 \. 9 +. t();
    m = {1,2,3} * 6;
EndBody."""
        expect = Program([FuncDecl(Id("k"),[],([],[Assign(Id("i"),BinaryOp("+.",BinaryOp("\.",FloatLiteral(0.76),IntLiteral(9)),CallStmt(Id("t"),[]))),Assign(Id("m"),BinaryOp("*",ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),IntLiteral(6)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    
    def test_exp_stmt_8(self):
        input = r"""Function: hi
Body:
    Var: b[2][3]={{1,2,3},{4,5,6}};
    m = m *. 5 + t[7][foo() + 5];
    Return b;
EndBody."""
        expect = Program([FuncDecl(Id("hi"),[],([VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))],[Assign(Id("m"),BinaryOp("+",BinaryOp("*.",Id("m"),IntLiteral(5)),ArrayCell(Id("t"),[IntLiteral(7),BinaryOp("+",CallStmt(Id("foo"),[]),IntLiteral(5))]))),Return(Id("b"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    
    def test_exp_stmt_9(self):
        input = r"""Function: zero
Body:
    b = b + 1;
    b = b + 2 -. 6 +. 2.;
    While m == 0 || i && 7 Do
        Break;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("zero"),[],([],[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+.",BinaryOp("-.",BinaryOp("+",Id("b"),IntLiteral(2)),IntLiteral(6)),FloatLiteral(2.0))),While(BinaryOp("==",Id("m"),BinaryOp("&&",BinaryOp("||",IntLiteral(0),Id("i")),IntLiteral(7))),([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    
    def test_exp_stmt_10(self):
        input = r"""Function: m
Parameter: b[6]
Body:
    a[3 + foo(2)] = a[b[2][3]] + 4;
    o = n + 4*.foo(2,"string") - 8%(t);
EndBody."""
        expect = Program([FuncDecl(Id("m"),[VarDecl(Id("b"),[6],None)],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallStmt(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id("o"),BinaryOp("-",BinaryOp("+",Id("n"),BinaryOp("*.",IntLiteral(4),CallStmt(Id("foo"),[IntLiteral(2),StringLiteral("string")]))),BinaryOp("%",IntLiteral(8),Id("t"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    
    def test_free_1(self):
        input = r"""Function: foo
Parameter: a[5], b
Body:
    Var: i = 0;
    While (i < 5) Do
        a[i] = b +. 1.0;
        i = i + 1;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    
    def test_free_2(self):
        input = r"""Var: x;
Function: fact
Parameter: n
Body:
    If n == 0 Then
        Return 1;
    Else
        Return n * fact (n - 1);
    EndIf.
EndBody.
Function: main
Body:
    x = 10;
    fact (x);
EndBody."""
        ifstmt = If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallStmt(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[ifstmt])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    
    def test_free_3(self):
        input = r"""Var: x = 0, y, u[2] = {1,2};
Function: foo
Parameter: p
Body:
    Var: square = 1;
    If x==0 Then
        x = 1;
        While u =/= null Do
            square = square * 2;
        EndWhile.
        print(square);
    EndIf.
EndBody.
Function: main
Body:
    If u[0] == 1 Then
        foo(1);
        u[1] = 1;
    ElseIf u[1] == 1 Then
        foo(2); 
    EndIf.
EndBody."""
        if1 = If([(BinaryOp("==",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),IntLiteral(1)),While(BinaryOp("=/=",Id("u"),Id("null")),([],[Assign(Id("square"),BinaryOp("*",Id("square"),IntLiteral(2)))])),CallStmt(Id("print"),[Id("square")])])],([],[]))
        func1 = FuncDecl(Id("foo"),[VarDecl(Id("p"),[],None)],([VarDecl(Id("square"),[],IntLiteral(1))],[if1]))
        if2 = If([(BinaryOp("==",ArrayCell(Id("u"),[IntLiteral(0)]),IntLiteral(1)),[],[CallStmt(Id("foo"),[IntLiteral(1)]),Assign(ArrayCell(Id("u"),[IntLiteral(1)]),IntLiteral(1))]),(BinaryOp("==",ArrayCell(Id("u"),[IntLiteral(1)]),IntLiteral(1)),[],[CallStmt(Id("foo"),[IntLiteral(2)])])],([],[]))
        func2 = FuncDecl(Id("main"),[],([],[if2]))
        expect = Program([VarDecl(Id("x"),[],IntLiteral(0)),VarDecl(Id("y"),[],None),VarDecl(Id("u"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),func1,func2])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_free_4(self):
        input = r"""Var: x = True;
Function: fact
    Parameter: n
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * fact (n - 1);
        EndIf.
    EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody."""
        ifstmt = If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallStmt(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[ifstmt])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    
    def test_free_5(self):
        input = r"""**This is my
*program**
Var: x = "this is my string\\n";
Function: check
Parameter: y
Body:
    If x == y Then
        Return True;
    Else
        Return 0;
    EndIf.
EndBody."""
        ifstmt = If([(BinaryOp("==",Id("x"),Id("y")),[],[Return(BooleanLiteral(True))])],([],[Return(IntLiteral(0))]))
        expect = Program([VarDecl(Id("x"),[],StringLiteral("this is my string\\\\n")),FuncDecl(Id("check"),[VarDecl(Id("y"),[],None)],([],[ifstmt]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    
    def test_free_6(self):
        input = r"""Function: helloWorld
Parameter: x, e[2][2]
Body:
    a[3 + foo(2)] = a[b[2][3]] + 4;
    writeln("Hello World\\n");
    Return 0;
EndBody."""
        expect = Program([FuncDecl(Id("helloWorld"),[VarDecl(Id("x"),[],None),VarDecl(Id("e"),[2,2],None)],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallStmt(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),CallStmt(Id("writeln"),[StringLiteral("Hello World\\\\n")]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    def test_free_7(self):
        input = r"""Function: test_for
Body:
    For (i = 0, i < 10, 2) Do
        write(i);
        If i == 6 Then Continue;EndIf.
    EndFor.
EndBody."""
        expect = Program([FuncDecl(Id("test_for"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("write"),[Id("i")]),If([(BinaryOp("==",Id("i"),IntLiteral(6)),[],[Continue()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    
    def test_free_8(self):
        input = r"""Var: str = "escape@@string'"";
Function: length
Parameter: str
Body:
    If str =/= null Then
        Return len(str);
    EndIf.
EndBody."""
        expect = Program([VarDecl(Id("str"),[],StringLiteral("escape@@string'\"")),FuncDecl(Id("length"),[VarDecl(Id("str"),[],None)],([],[If([(BinaryOp("=/=",Id("str"),Id("null")),[],[Return(CallStmt(Id("len"),[Id("str")]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    
    def test_free_9(self):
        input = r"""Var: m = 0,t[2] = {1,2};
Var: f = 1.2e2;
Function: foo
Parameter: m
Body:
    Var: t[1] = {1};
    Var: m = 0X7;
    m = m + 1.e-1 + {1,2};
    Return 0;
EndBody."""
        expect = Program([VarDecl(Id("m"),[],IntLiteral(0)),VarDecl(Id("t"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("f"),[],FloatLiteral(120.0)),FuncDecl(Id("foo"),[VarDecl(Id("m"),[],None)],([VarDecl(Id("t"),[1],ArrayLiteral([IntLiteral(1)])),VarDecl(Id("m"),[],IntLiteral(7))],[Assign(Id("m"),BinaryOp("+",BinaryOp("+",Id("m"),FloatLiteral(0.1)),ArrayLiteral([IntLiteral(1),IntLiteral(2)]))),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    
    def test_free_10(self):
        input = r"""Function: main
Body:
    Var: u[4] = {"string",1.e-1,0O7,True};
    foo(a)[1] = u[2][1] + 0O45 + False;
    Return a;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("u"),[4],ArrayLiteral([StringLiteral("string"),FloatLiteral(0.1),IntLiteral(7),BooleanLiteral(True)]))],[Assign(ArrayCell(CallStmt(Id("foo"),[Id("a")]),[IntLiteral(1)]),BinaryOp("+",BinaryOp("+",ArrayCell(Id("u"),[IntLiteral(2),IntLiteral(1)]),IntLiteral(37)),BooleanLiteral(False))),Return(Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    
#     def test_free_11(self):
#         input = r"""Var: i;
# Function: main
# Body:
#     m = m + True;
#     t[1][2][a[7]] = {1,{"String",7.4}};
# EndBody."""
#         expect = """Program([VarDecl(Id(i)),FuncDecl(Id(main)[],([][Assign(Id(m),BinaryOp(+,Id(m),BooleanLiteral(true))),Assign(ArrayCell(Id(t),[IntLiteral(1),IntLiteral(2),ArrayCell(Id(a),[IntLiteral(7)])]),ArrayLiteral(IntLiteral(1),ArrayLiteral(StringLiteral(String),FloatLiteral(7.4))))]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,383))

#     def test_free_12(self):
#         input = r"""Var: m = "string";
# Var: f = 1.2;
# Var: m = {1,2};"""
#         expect = """Program([VarDecl(Id(m),StringLiteral(string)),VarDecl(Id(f),FloatLiteral(1.2)),VarDecl(Id(m),ArrayLiteral(IntLiteral(1),IntLiteral(2)))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,384))

#     def test_free_13(self):
#         input = r"""Function: foo
# Body:
# EndBody.
# Function: foo
# Body:
# EndBody.
# Function: foo
# Body:
# EndBody."""
#         expect = """Program([FuncDecl(Id(foo)[],([][])),FuncDecl(Id(foo)[],([][])),FuncDecl(Id(foo)[],([][]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,385))

#     def test_free_14(self):
#         input = r"""Var: x,x,x,x,x,x;
# Function: main
# Body:
#     Var: main,main,main;
#     Var: x,x,x,x,x;
# EndBody."""
#         expect = """Program([VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x)),FuncDecl(Id(main)[],([VarDecl(Id(main)),VarDecl(Id(main)),VarDecl(Id(main)),VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x)),VarDecl(Id(x))][]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,386))

#     def test_free_15(self):
#         input = r"""Function: test
# Body:
#     Var: a[5];
#     a[3 + foo(2)] = a[b[2][3]] + 4;
#     If bool_of_string ("True") Then
#         a = int_of_string (read ());
#         b = float_of_int (a) +. 2.0;
#     EndIf.
# EndBody."""
#         ifstmt = If([(CallStmt(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallStmt(Id("int_of_string"),[CallStmt(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallStmt(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],([],[]))
#         expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[5],None)],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallStmt(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),ifstmt]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,387))

#     def test_free_16(self):
#         input = r"""Var: m,n[2] = "string";
# Var: variablelist;
# Function: main
# Body:
#     Var: r = 10., v;
#     v = (4. \. 3.) *. 3.14 *. r *. r *. r;
# EndBody."""
#         expect = """Program([VarDecl(Id(m)),VarDecl(Id(n),[2],StringLiteral(string)),VarDecl(Id(variablelist)),FuncDecl(Id(main)[],([VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][Assign(Id(v),BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(\.,FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id(r)),Id(r)),Id(r)))]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,388))

#     def test_free_17(self):
#         input = r"""Function: main
# Body:
#     For (i = 0, i < 10, 2) Do
#         writeln(i);
#         While n < 10 Do
#             While m == True Do
#                 m = m + 1;
#                 Return m;
#             EndWhile.
#             Do
#                 foo (2 + x, 4. \. y);
#                 goo ();
#             While i + 1 EndDo.
#         EndWhile.
#         If m && 5 Then
#             call();
#             Break;
#         EndIf.
#     EndFor.
#     **This is a comment
#     a = a + 1;
#     **
#     Return True + " string ";
# EndBody."""
#         ifstmt = If([(BinaryOp("&&",Id("m"),IntLiteral(5)),[],[CallStmt(Id("call"),[]),Break()])],([],[]))
#         whilestmt = While(BinaryOp("<",Id("n"),IntLiteral(10)),([],[While(BinaryOp("==",Id("m"),BooleanLiteral(True)),([],[Assign(Id("m"),BinaryOp("+",Id("m"),IntLiteral(1))),Return(Id("m"))])),Dowhile(([],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\.",FloatLiteral(4.0),Id("y"))]),CallStmt(Id("goo"),[])]),BinaryOp("+",Id("i"),IntLiteral(1)))]))
#         forstmt = For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")]),whilestmt,ifstmt]))
#         expect = Program([FuncDecl(Id("main"),[],([],[forstmt,Return(BinaryOp("+",BooleanLiteral(True),StringLiteral(" string ")))]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,389))

#     def test_free_18(self):
#         input = r"""Function: m
# Parameter: x
# Body:
#     If x == 5 Then
#         x = 1;
#         Continue;
#     ElseIf x == 6 Then
#         x = 2;
#         Break;
#     ElseIf x == 4 Then
#         x = 3;
#         Return x;
#     Else
#         x = 0;
#     EndIf.
#     Return False;
# EndBody."""
#         expect = """Program([FuncDecl(Id(m)[VarDecl(Id(x))],([][If(BinaryOp(==,Id(x),IntLiteral(5)),[],[Assign(Id(x),IntLiteral(1)),Continue()])ElseIf(BinaryOp(==,Id(x),IntLiteral(6)),[],[Assign(Id(x),IntLiteral(2)),Break()])ElseIf(BinaryOp(==,Id(x),IntLiteral(4)),[],[Assign(Id(x),IntLiteral(3)),Return(Id(x))])Else([],[Assign(Id(x),IntLiteral(0))]),Return(BooleanLiteral(false))]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,390))

#     def test_free_19(self):
#         input = r"""Function
# :

# main
# Body:
#     Var:
#     **This is a comment
#     x, y = 10;**
#     n[5] = {1,2,3,4,"t"};
#     Var: m;
#     If **cmt**
#     t != 1
#     Then **cmt%!#)**
#     call(**this**n);
#     EndIf.
# EndBody."""
#         ifstmt = If([(BinaryOp("!=",Id("t"),IntLiteral(1)),[],[CallStmt(Id("call"),[Id("n")])])],([],[]))
#         expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("n"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),StringLiteral("t")])),VarDecl(Id("m"),[],None)],[ifstmt]))])
#         self.assertTrue(TestAST.checkASTGen(input,expect,391))

#     def test_free_20(self):
#         input = r"""**

# This
# is
# a
# cmt
#         **

# Function: max
# Parameter: a,**** b
# Body:
#     If a >=. b Then
#         Return a;
#         For(index = 0,index<.10.e1,1.e1) Do
#             x = call(a)[7][8];
#         EndFor.
#     Else
#         Return b;
#     EndIf.
# EndBody."""
#         expect = """Program([FuncDecl(Id(max)[VarDecl(Id(a)),VarDecl(Id(b))],([][If(BinaryOp(>=.,Id(a),Id(b)),[],[Return(Id(a)),For(Id(index),IntLiteral(0),BinaryOp(<.,Id(index),FloatLiteral(100.0)),FloatLiteral(10.0),[],[Assign(Id(x),ArrayCell(CallStmt(Id(call),[Id(a)]),[IntLiteral(7),IntLiteral(8)]))])])Else([],[Return(Id(b))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,392))

#     def test_free_21(self):
#         input = r"""Function: r
# Body:
#     While x > 1 Do
#         If r %2 == 0 Then
#             While x < 10 Do
#                 Break;
#             EndWhile.
#         ElseIf t Then
#         Else
#         EndIf.
#     EndWhile.
# EndBody."""
#         expect = """Program([FuncDecl(Id(r)[],([][While(BinaryOp(>,Id(x),IntLiteral(1)),[],[If(BinaryOp(==,BinaryOp(%,Id(r),IntLiteral(2)),IntLiteral(0)),[],[While(BinaryOp(<,Id(x),IntLiteral(10)),[],[Break()])])ElseIf(Id(t),[],[])Else([],[])])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,393))

    # def test_free_22(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,394))

    # def test_free_23(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,395))

    # def test_free_24(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,396))

    # def test_free_25(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,397))

    # def test_free_26(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))

    # def test_free_27(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))

    # def test_free_28(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,400))


    