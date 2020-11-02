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
    def test_case_13(self):
        input = """
        Var: s = "daofjsdg";
        Function: main
        Body:
            Var: arr[26];
            f = fact(n) % 0O10;
            While (i < length(s)) Do
                arr[lower(s[i]) - 97] =  arr[lower(s[i]) - 97] +. 1.e0;
            EndWhile.
            max_length = max(arr);
        EndBody.
        Function: sum
        Parameter: n
        Body:
            p = 1.;
            For (i = 1, i < n, 1) Do
                p = p *. i;
            EndFor.
            Return i;
        EndBody.
        """
        f1 = FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [26], None)], [Assign(Id('f'), BinaryOp('%', CallExpr(Id('fact'), [Id('n')]), IntLiteral(0o10))), \
            While(BinaryOp('<', Id('i'), CallExpr(Id('length'), [Id('s')])), ([], [Assign(ArrayCell(Id('arr'), [BinaryOp('-', CallExpr(Id('lower'), [ArrayCell(Id('s'), [Id('i')])]), IntLiteral(97))]), BinaryOp('+.', ArrayCell(Id('arr'), [BinaryOp('-', CallExpr(Id('lower'), [ArrayCell(Id('s'), [Id('i')])]), IntLiteral(97))]), FloatLiteral(1.0)))])),\
                Assign(Id('max_length'), CallExpr(Id('max'), [Id('arr')]))]))
        f2 = FuncDecl(Id('sum'), [VarDecl(Id('n'), [], None)], ([], [Assign(Id('p'), FloatLiteral(1.)), For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), Id('n')), IntLiteral(1), ([], [Assign(Id('p'), BinaryOp('*.', Id('p'), Id('i')))])), Return(Id('i'))]))
        expect =  Program([VarDecl(Id('s'), [], StringLiteral("daofjsdg")), f1, f2])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    def test_case_14(self):
        input = """
        Var: s = "daofjsdg";
        Function: main
        Body:
            Var: arr[26];
            f = fact(n) % 0O10;
            While (i < length(s)) Do
                arr[lower(s[i]) - 97] =  arr[lower(s[i]) - 97] +. 1.e0;
            EndWhile.
            max_length = max(arr);
        EndBody.
        Function: sum
        Parameter: n
        Body:
            p = 1.;
            For (i = 1, i < n, 1) Do
                p = p *. i;
            EndFor.
            Return i;
        EndBody.
        """
        f1 = FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [26], None)], [Assign(Id('f'), BinaryOp('%', CallExpr(Id('fact'), [Id('n')]), IntLiteral(0o10))), \
            While(BinaryOp('<', Id('i'), CallExpr(Id('length'), [Id('s')])), ([], [Assign(ArrayCell(Id('arr'), [BinaryOp('-', CallExpr(Id('lower'), [ArrayCell(Id('s'), [Id('i')])]), IntLiteral(97))]), BinaryOp('+.', ArrayCell(Id('arr'), [BinaryOp('-', CallExpr(Id('lower'), [ArrayCell(Id('s'), [Id('i')])]), IntLiteral(97))]), FloatLiteral(1.0)))])),\
                Assign(Id('max_length'), CallExpr(Id('max'), [Id('arr')]))]))
        f2 = FuncDecl(Id('sum'), [VarDecl(Id('n'), [], None)], ([], [Assign(Id('p'), FloatLiteral(1.)), For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), Id('n')), IntLiteral(1), ([], [Assign(Id('p'), BinaryOp('*.', Id('p'), Id('i')))])), Return(Id('i'))]))
        expect =  Program([VarDecl(Id('s'), [], StringLiteral("daofjsdg")), f1, f2])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))
    def test_case_15(self):
        input = """
        Function: main
        Body:
            Var: x = 0x213ACF, s = 123e-3;
            v = 4 \. (3 *. 314e-2) * r * r * r;
            If x < 10 Then
                Break;
            Else
                x = x && d >. 1;
            EndIf.
        EndBody.
        """
        expect =  Program([FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], IntLiteral(0x213ACF)), VarDecl(Id('s'), [], FloatLiteral(123e-3))], \
            [Assign(Id('v'), BinaryOp('*', BinaryOp('*', BinaryOp('*', BinaryOp('\\.', IntLiteral(4), BinaryOp('*.', IntLiteral(3), FloatLiteral(314e-2))), Id('r')),Id('r')), Id('r'))), \
                If([(BinaryOp('<', Id('x'), IntLiteral(10)), [], [Break()])], ([], [Assign(Id('x'), BinaryOp('>.', BinaryOp('&&', Id('x'), Id('d')), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    def test_case_16(self):
        input = """
        Function: main
        Body:
            Do
                Var: k = 12;
                k = -.-k;
                a[2][3 + 3] = foo(2 + k, k, arr[0]);
                m = a[1][2 + f[2]];
            While x == 0 EndDo.
        EndBody.
        """
        expect =  Program([FuncDecl(Id('main'), [], ([], [Dowhile(([VarDecl(Id('k'), [], IntLiteral(12))], [Assign(Id('k'), UnaryOp('-.', UnaryOp('-', Id('k')))), \
            Assign(ArrayCell(Id('a'), [IntLiteral(2), BinaryOp('+', IntLiteral(3), IntLiteral(3))]), \
            CallExpr(Id('foo'), [BinaryOp('+', IntLiteral(2), Id('k')), Id('k'), ArrayCell(Id('arr'), [IntLiteral(0)])])), \
            Assign(Id('m'), ArrayCell(Id('a'), [IntLiteral(1), BinaryOp('+', IntLiteral(2), ArrayCell(Id('f'), [IntLiteral(2)]))]))]), BinaryOp('==', Id('x'), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    def test_case_17(self):
        input = """
        Var: m, n[10]; 
        Function: main 
        Parameter: n 
        Body: 
            x = {{{1,2}, {3,4}}, {5,6}};
            If n == 0 Then 
                Return 1; 
            Else
                Return n * face({1,2});
            EndIf.
        EndBody. 
        """
        expect =  Program([VarDecl(Id('m'), [], None), VarDecl(Id('n'), [10], None), FuncDecl(Id('main'), [VarDecl(Id('n'), [], None)], ([], [\
            Assign(Id('x'), ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])]), ArrayLiteral([IntLiteral(5), IntLiteral(6)])])),\
            If([(BinaryOp('==', Id('n'), IntLiteral(0)), [], [Return(IntLiteral(1))])], ([], [Return(BinaryOp('*', Id('n'), CallExpr(Id('face'), [ArrayLiteral([IntLiteral(1), IntLiteral(2)])])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    def test_case_18(self):
        input = """
        Var: a, b, c = 10e12;
        Function: main
        Body:
            Var: i = 0, arr[10];
            c = arr[0];
            For (i = 1, i < 10, 1) Do
                If (c < arr[i]) Then
                    c = arr[i];
                EndIf.
            EndFor.  
            f(1, 2, 3);
            Return;
        EndBody.
        """
        expect =  Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], FloatLiteral(10e12)), FuncDecl(Id('main'), [], ([VarDecl(Id('i'), [], IntLiteral(0)), VarDecl(Id('arr'), [10], None)], [\
                Assign(Id('c'), ArrayCell(Id('arr'), [IntLiteral(0)])),\
                For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [If([(BinaryOp('<', Id('c'), ArrayCell(Id('arr'), [Id('i')])), [], [Assign(Id('c'), ArrayCell(Id('arr'), [Id('i')]))])], ())])),\
                CallStmt(Id('f'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))
    def test_case_19(self):
        input = """
        Function: sort
        Parameter: arr[0o100], left, right
        Body:
            For(i = left + 1, i <= right, 1) Do
                Var: temp, j;
                temp = arr[i];
                j = i - 1;
                While (j >= left) && (arr[j] > temp) Do
                    arr[j + 1] = arr[j];
                    j = j - 1;
                EndWhile.
                arr[j + 1] = temp;
            EndFor.
        EndBody.
        """
        expect =  Program([FuncDecl(Id('sort'), [VarDecl(Id('arr'), [0o100], None), VarDecl(Id('left'), [], None), VarDecl(Id('right'), [], None)], ([], [\
                For(Id('i'), BinaryOp('+', Id('left'), IntLiteral(1)), BinaryOp('<=', Id('i'), Id('right')), IntLiteral(1), ([VarDecl(Id('temp'), [], None), VarDecl(Id('j'), [], None)], \
                [Assign(Id('temp'), ArrayCell(Id('arr'), [Id('i')])), Assign(Id('j'), BinaryOp('-', Id('i'), IntLiteral(1))),\
                While(BinaryOp('&&', BinaryOp('>=', Id('j'), Id('left')), BinaryOp('>', ArrayCell(Id('arr'), [Id('j')]), Id('temp'))),([], [Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), ArrayCell(Id('arr'), [Id('j')])), Assign(Id('j'), BinaryOp('-', Id('j'), IntLiteral(1)))])),\
                Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), Id('temp'))
                ]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    def test_case_20(self):
        input = """
        Function: convert
        Parameter: str
        Body:
            Var: arr[100];
            Var: length;
            length = length(str) - 1;
            Return length;
        EndBody.
        Function: main
        Body:
            convert();
        EndBody.
        """
        f1 = FuncDecl(Id('convert'), [VarDecl(Id('str'), [], None)], ([VarDecl(Id('arr'), [100], None), VarDecl(Id('length'), [], None)], [Assign(Id('length'), BinaryOp('-', CallExpr(Id('length'), [Id('str')]), IntLiteral(1))), Return(Id('length'))]))
        f2 = FuncDecl(Id('main'), [], ([], [CallStmt(Id('convert'), [])]))
        expect =  Program([f1, f2])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

   