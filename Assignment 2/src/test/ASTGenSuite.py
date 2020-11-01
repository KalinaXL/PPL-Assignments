import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_case_1(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_case_2(self):
        input = """Var:x, y[2][3] = {2, 3};"""
        expect = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'),[2,3],ArrayLiteral([IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_case_3(self):
        input = """Var:x, y = 10, s ="ad\\fs", y[2][3] = {{2}, {3}};"""
        expect = Program([VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], IntLiteral(10)),VarDecl(Id('s'), [], StringLiteral("ad\\fs")),VarDecl(Id('y'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2)]),ArrayLiteral([IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_case_4(self):
        input = """Var:x, y = 10, s ="ad\\fs", y[2][3]; Var: xyasd = 123, flag = True;"""
        expect = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(10)),VarDecl(Id('s'), [],StringLiteral('ad\\fs')),VarDecl(Id('y'), [2, 3], None),VarDecl(Id('xyasd'),[],IntLiteral(123)),VarDecl(Id('flag'), [],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))
    def test_case_5(self):
        input = """
        Function: main
        Body:
            Return 0;
        EndBody.
        """
        expect =  Program([FuncDecl(Id('main'),[], ([], [Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
    def test_case_6(self):
        input = """
        Function: main
        Body:
            Return 1 + 2 + 3;
        EndBody.
        """
        expect =  Program([FuncDecl(Id('main'),[], ([], [Return(BinaryOp('+',BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
    def test_case_7(self):
        input = """
        Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.
        """
        i1 = (BinaryOp('==',Id('n'),IntLiteral(0)), [], [Return(IntLiteral(1))])
        i2 = ([], [Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])
        if_stmts = If([i1], i2)
        fn = FuncDecl(Id('fact'), [VarDecl(Id('n'), [], None)], ([], [if_stmts]))
        expect =  Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    def test_case_8(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.
        """
        w = While(BinaryOp('<',Id('i'),IntLiteral(5)), ([], [Assign(ArrayCell(Id('a'),[Id('i')]), BinaryOp('+.',Id('b'),FloatLiteral(1.0))), Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1)))]))
        fn = FuncDecl(Id('foo'), [VarDecl(Id('a'), [5], None), VarDecl(Id('b'), [], None)], ([VarDecl(Id('i'), [], IntLiteral(0))], [w]))
        expect =  Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    def test_case_9(self):
        input = """
        Function: main
        Body:
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """
        f = For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(2), ([], [CallStmt(Id('writeln'), [Id('i')])]))
        fn = FuncDecl(Id('main'), [], ([], [f]))
        expect =  Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))
    def test_case_10(self):
        input = """
        Function: main
        Body:
            Do
                a[3 + foo(2)] = a[b[2][3]] + 4;
            While i == False EndDo.

        EndBody.
        """
        f = Dowhile(([], [Assign(ArrayCell(Id('a'), [BinaryOp('+', IntLiteral(3), CallExpr(Id('foo'), [IntLiteral(2)]))]), BinaryOp('+', ArrayCell(Id('a'), [ArrayCell(Id('b'), [IntLiteral(2), IntLiteral(3)])]), IntLiteral(4)))]), BinaryOp('==', Id('i'), BooleanLiteral(False)))
        fn = FuncDecl(Id('main'), [], ([], [f]))
        expect =  Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    def test_case_11(self):
        input = """
        Function: main
        Parameter: a[10], b
        Body:
            Var: i = 0;
            While x > 0 Do
                If i == 0 Then
                    Var: k = 0.;
                    main(i);
                EndIf.
            EndWhile.

        EndBody.
        """
        f = While(BinaryOp('>', Id('x'), IntLiteral(0)), ([], [If([(BinaryOp('==', Id('i'), IntLiteral(0)), [VarDecl(Id('k'), [], FloatLiteral(0.))], [CallStmt(Id('main'), [Id('i')])])], ())]))
        fn = FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None), VarDecl(Id('b'), [], None)], ([VarDecl(Id('i'), [], IntLiteral(0))], [f]))
        expect =  Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    def test_case_12(self):
        input = """
        Var: a = 5, n[10], s = False;
        Var: bb[2][3] = {{2, 3, 4}, {4, 5, 6}};
        Function: main
        Body:
            flag = 2;
            a = !!!!True || dkd;
            Return fool() + uuuuu(2 + 3, f[2][4]) && dk;

        EndBody.
        """
        stmts = [Assign(Id('flag'), IntLiteral(2)), Assign(Id('a'), BinaryOp('||', UnaryOp('!', UnaryOp('!', UnaryOp('!', UnaryOp('!', BooleanLiteral(True))))),Id('dkd'))),\
                Return(BinaryOp('&&', BinaryOp('+', CallExpr(Id('fool'), []), CallExpr(Id('uuuuu'), [BinaryOp('+', IntLiteral(2), IntLiteral(3)), ArrayCell(Id('f'), [IntLiteral(2), IntLiteral(4)])])), Id('dk')))]
        fn = FuncDecl(Id('main'), [], ([], stmts))
        expect =  Program([VarDecl(Id('a'), [], IntLiteral(5)), VarDecl(Id('n'), [10], None), VarDecl(Id('s'), [], BooleanLiteral(False)), \
        VarDecl(Id('bb'), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), 
        fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

 
   