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
    def test_case_21(self):
        input = """
        Function: main
        Body:
            a = f(2, 3 + 4)[1 + 2];
        EndBody.
        """
        f = FuncDecl(Id('main'), [], ([], [Assign(Id('a'), ArrayCell(CallExpr(Id('f'), [IntLiteral(2), BinaryOp('+', IntLiteral(3), IntLiteral(4))]), [BinaryOp('+', IntLiteral(1), IntLiteral(2))]))]))
        expect =  Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))
    def test_case_22(self):
        input = """
        Function: fact
        Parameter: x, a[2]
        Body:
            For (i = 0, i < 10, 2) Do
                If (x) Then Break; EndIf.
            EndFor.
            If (x) Then Break; EndIf.
        EndBody.
        """
        if_stmt = If([(Id('x'), [], [Break()])], ())
        f = FuncDecl(Id('fact'), [VarDecl(Id('x'), [], None), VarDecl(Id('a'), [2], None)], ([], [For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(2), ([], [if_stmt])), if_stmt]))
        expect =  Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
    def test_case_23(self):
        input = """
        Function: main
        Body:
            Var: x = 10;
            kk = 0o10 && 0x123 || 12.3 + True;
            f(1 + 2, a)[2 + a[2]] = a[0][2 + 2][f()]; 
            While x < cond() Do
                print("string, hala madrid");
            EndWhile.
        EndBody.
        """
        f = FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], IntLiteral(10))], [Assign(Id('kk'), BinaryOp('||', BinaryOp('&&', IntLiteral(0o10), IntLiteral(0x123)), BinaryOp('+', FloatLiteral(12.3), BooleanLiteral(True)))), \
                                        Assign(ArrayCell(CallExpr(Id('f'), [BinaryOp('+', IntLiteral(1), IntLiteral(2)), Id('a')]), [BinaryOp('+', IntLiteral(2), ArrayCell(Id('a'), [IntLiteral(2)]))]), ArrayCell(Id('a'), [IntLiteral(0), BinaryOp('+', IntLiteral(2), IntLiteral(2)), CallExpr(Id('f'), [])])),\
                                        While(BinaryOp('<', Id('x'), CallExpr(Id('cond'), [])), ([], [CallStmt(Id('print'), [StringLiteral("string, hala madrid")])]))
                                        ]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    def test_case_24(self):
        input = """
        Function: main
        Body:
            Do
                f_n_f(12);
                While x Do
                    Var: x;
                    If x == 1 Then
                        Var: x;
                    EndIf.
                EndWhile.
            While True EndDo.
        EndBody.
        """
        dowhile = Dowhile(([], [CallStmt(Id('f_n_f'), [IntLiteral(12)]), While(Id('x'), ([VarDecl(Id('x'), [], None)], [If([(BinaryOp('==', Id('x'), IntLiteral(1)), [VarDecl(Id('x'), [], None)], [])], ())]))]), BooleanLiteral(True))
        f = FuncDecl(Id('main'), [], ([], [dowhile]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))
    def test_case_25(self):
        input = """
        Function: main
        Body:
            For(i = init(), i < bound(), step()) Do
                a = in(f(in(2, f())))[f()];
            EndFor.
        EndBody.
        """
        f = FuncDecl(Id('main'), [], ([], [For(Id('i'), CallExpr(Id('init'), []), BinaryOp('<', Id('i'), CallExpr(Id('bound'), [])), CallExpr(Id('step'), []), ([],\
             [Assign(Id('a'), ArrayCell(CallExpr(Id('in'), [CallExpr(Id('f'), [CallExpr(Id('in'), [IntLiteral(2), CallExpr(Id('f'), [])])])]), [CallExpr(Id('f'), [])]))]))]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    def test_case_26(self):
        input = """
        Function: main
        Body:
            Var: x = 0., y = 2.;
            While (x =/= f()) Do
                x = x +. 1;
                y = y -. 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        f = FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], FloatLiteral(0.)), VarDecl(Id('y'), [], FloatLiteral(2.))], [While(BinaryOp('=/=', Id('x'), CallExpr(Id('f'), [])), ([], \
            [Assign(Id('x'), BinaryOp('+.', Id('x'), IntLiteral(1))), Assign(Id('y'), BinaryOp('-.', Id('y'), IntLiteral(1)))])), Return(IntLiteral(0))]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))
    def test_case_27(self):
        input = """
        Function: main
        Parameter: k
        Body:
            Var: i = 10, k[10][2] = {{}, {}};
            Do
                Continue;
            While i <= 10 EndDo.
            Return 0;
        EndBody.
        """
        f = FuncDecl(Id('main'), [VarDecl(Id('k'), [], None)], ([VarDecl(Id('i'), [], IntLiteral(10)), VarDecl(Id('k'), [10, 2], ArrayLiteral([ArrayLiteral([]), ArrayLiteral([])]))], [Dowhile(([], [Continue()]), BinaryOp('<=', Id('i'), IntLiteral(10))), Return(IntLiteral(0))]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))
    def test_case_28(self):
        input = """
        Function: main
        Body:
           x =  f("1", "194") + a[0][3] * "blu bla";
        EndBody.
        """
        f = FuncDecl(Id('main'), [], ([], [Assign(Id('x'), BinaryOp('+', CallExpr(Id('f'), [StringLiteral("1"), StringLiteral("194")]), BinaryOp('*', ArrayCell(Id('a'), [IntLiteral(0), IntLiteral(3)]), StringLiteral("blu bla"))))]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))
    def test_case_29(self):
        input = """
        Function: main
        Body:
            For(counter = 0., foo() * a[23] == 2, "asd") Do
                x = 213;
            EndFor.
        EndBody.
        """
        f = FuncDecl(Id('main'), [], ([], [For(Id('counter'), FloatLiteral(0.), BinaryOp('==', BinaryOp('*', CallExpr(Id('foo'), []), ArrayCell(Id('a'), [IntLiteral(23)])), IntLiteral(2)), StringLiteral("asd"), ([], [Assign(Id('x'), IntLiteral(213))]))]))
        expect = Program([f])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))
    def test_case_30(self):
        input = """
        Function: main
        Body:
            inp = 123 * daf[g132[423][2] * 132 + {13}];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [],([], [Assign(Id('inp'),BinaryOp('*',IntLiteral(123),ArrayCell(Id('daf'),[BinaryOp('+',BinaryOp('*',ArrayCell(Id('g132'),[IntLiteral(423),IntLiteral(2)]),IntLiteral(132)),ArrayLiteral([IntLiteral(13)]))])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
    def test_case_31(self):
        input = """
        Function: main
        Body:
            If "" Then
            in = 123 - 4234 +. 432 || !False;
            inp = {123, 435, 423} * in;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [],([], [If([(StringLiteral(''),[],[Assign(Id('in'),BinaryOp('||',BinaryOp('+.',BinaryOp('-',IntLiteral(123),IntLiteral(4234)),IntLiteral(432)),UnaryOp('!',BooleanLiteral(False)))),Assign(Id('inp'),BinaryOp('*',ArrayLiteral([IntLiteral(123),IntLiteral(435),IntLiteral(423)]),Id('in')))])], ())]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    def test_case_32(self):
        input = """
        Var: x, y =1, y = "abc'" hello \\t ", m[13425], n[1053245] = {1,2,{"a534n",5.54324},5.e-145232};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+2120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;
        
        object = 4123542 + 7 > 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(1)),VarDecl(Id('y'), [],StringLiteral("""abc'" hello \\t """)),VarDecl(Id('m'),[13425], None),VarDecl(Id('n'),[1053245],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([StringLiteral("""a534n"""),FloatLiteral(5.54324)]),FloatLiteral(0.0)])),VarDecl(Id('a_jacj933'), [],FloatLiteral(12.21)),FuncDecl(Id('fact'),[VarDecl(Id('n'), [], None),VarDecl(Id('aca_312aAX'),[3,44,12799], None),VarDecl(Id('cxa'),[18,1,8,0], None)],([VarDecl(Id('t'), [], None),VarDecl(Id('r'), [],FloatLiteral(10.0)),VarDecl(Id('thread'), [],FloatLiteral('inf')),VarDecl(Id('r'), [],FloatLiteral(10.0))],[Assign(Id('v'),BinaryOp('*',BinaryOp('*',BinaryOp('*.',BinaryOp('*.',BinaryOp('\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('a'))),Assign(Id('object'),BinaryOp('>',BinaryOp('+',IntLiteral(4123542),IntLiteral(7)),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    def test_case_33(self):
        input = """
        Function: main
        Body:
            If "" Then
                If 1 Then
                    inp = f23 + ads[2+10] --- 2 *f ** "87235jkfgshgsfg $&^# ** ;
                ElseIf 1 Then 
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [],([],[If([(StringLiteral(""""""),[],[If([(IntLiteral(1),[],[Assign(Id('inp'),BinaryOp('-',BinaryOp('+',Id('f23'),ArrayCell(Id('ads'),[BinaryOp('+',IntLiteral(2),IntLiteral(10))])),BinaryOp('*',UnaryOp('-',UnaryOp('-',IntLiteral(2))),Id('f'))))]),(IntLiteral(1),[],[])], ())])], ())]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    def test_case_34(self):
        input = """
		Var: x = 1,y= "abc",z[1];
		Var: temp = 0;
		Function: main
		Parameter: x,y,arr[10][12]
		Body:
			Var: x = 1;
			x = True && 1;
			Break;
			foo(1);
			Return x + 1;
		EndBody.
		"""
        expect = Program([VarDecl(Id('x'), [],IntLiteral(1)),VarDecl(Id('y'), [],StringLiteral("""abc""")),VarDecl(Id('z'), [1], None),VarDecl(Id('temp'), [],IntLiteral(0)),FuncDecl(Id('main'), [VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [10,12], None)],([VarDecl(Id('x'), [],IntLiteral(1))],[Assign(Id('x'),BinaryOp('&&',BooleanLiteral(True),IntLiteral(1))),Break(),CallStmt(Id('foo'),[IntLiteral(1)]),Return(BinaryOp('+',Id('x'),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))
    def test_case_35(self):
        input = """
        Var: max_length = 100;
        Function: countintSort
        Parameter: arr[100]
        Body:
            Var: output[100];
            Var: count[100], i;
            memset(count, 0, sizeof(count));
            For(i = 0, arr[i] > 0, 1) Do
                count[arr[i]] = count[arr[i]] + 1;
            EndFor.
            For(i = 1, i <= range(arr), 1) Do
                count[i] = count[i] + count[i - 1];
            EndFor.
            For(i = 0, arr[i] > 0, 1) Do
                output[count[arr[i]] - 1] = arr[i];
                count[arr[i]] = count[arr[i]] - 1;
            EndFor.
            For( i = 0, arr[i] != 0, 1) Do
                If i % 2 == 0 Then
                    arr[i] = i \\ 2;
                ElseIf i % 3 == 0 Then
                    arr[i] = 3 *. i;
                ElseIf i % 5 == 1 Then
                    arr[i] = i;
                Else
                    arr[i] = output[i];
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('max_length'), [],IntLiteral(100)),FuncDecl(Id('countintSort'), [VarDecl(Id('arr'), [100], None)],([VarDecl(Id('output'), [100], None),VarDecl(Id('count'), [100], None),VarDecl(Id('i'), [], None)],[CallStmt(Id('memset'),[Id('count'),IntLiteral(0),CallExpr(Id('sizeof'),[Id('count')])]),For(Id('i'),IntLiteral(0),BinaryOp('>',ArrayCell(Id('arr'),[Id('i')]),IntLiteral(0)),IntLiteral(1), ([],[Assign(ArrayCell(Id('count'),[ArrayCell(Id('arr'),[Id('i')])]),BinaryOp('+',ArrayCell(Id('count'),[ArrayCell(Id('arr'),[Id('i')])]),IntLiteral(1)))])),For(Id('i'),IntLiteral(1),BinaryOp('<=',Id('i'),CallExpr(Id('range'),[Id('arr')])),IntLiteral(1), ([],[Assign(ArrayCell(Id('count'),[Id('i')]),BinaryOp('+',ArrayCell(Id('count'),[Id('i')]),ArrayCell(Id('count'),[BinaryOp('-',Id('i'),IntLiteral(1))])))])),For(Id('i'),IntLiteral(0),BinaryOp('>',ArrayCell(Id('arr'),[Id('i')]),IntLiteral(0)),IntLiteral(1), ([],[Assign(ArrayCell(Id('output'),[BinaryOp('-',ArrayCell(Id('count'),[ArrayCell(Id('arr'),[Id('i')])]),IntLiteral(1))]),ArrayCell(Id('arr'),[Id('i')])),Assign(ArrayCell(Id('count'),[ArrayCell(Id('arr'),[Id('i')])]),BinaryOp('-',ArrayCell(Id('count'),[ArrayCell(Id('arr'),[Id('i')])]),IntLiteral(1)))])),For(Id('i'),IntLiteral(0),BinaryOp('!=',ArrayCell(Id('arr'),[Id('i')]),IntLiteral(0)),IntLiteral(1), ([],[If([(BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(2)),IntLiteral(0)),[],[Assign(ArrayCell(Id('arr'),[Id('i')]),BinaryOp('\\',Id('i'),IntLiteral(2)))]),(BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(3)),IntLiteral(0)),[],[Assign(ArrayCell(Id('arr'),[Id('i')]),BinaryOp('*.',IntLiteral(3),Id('i')))]),(BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(5)),IntLiteral(1)),[],[Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i'))])], ([],[Assign(ArrayCell(Id('arr'),[Id('i')]),ArrayCell(Id('output'),[Id('i')]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))
    def test_case_36(self):
        input = """
        Var:x ;
        Var: f = 1232324.e23432;
        Function: main
        Parameter: a[2], b
        Body:
            While i < 10 Do
                While i < 10 Do
                    For (i = init(), con(), up()) Do
                    EndFor.
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id('x'), [], None),VarDecl(Id('f'), [],FloatLiteral('inf')),FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None),VarDecl(Id('b'), [], None)],([],[While(BinaryOp('<',Id('i'),IntLiteral(10)),([],[While(BinaryOp('<',Id('i'),IntLiteral(10)),([],[For(Id('i'),CallExpr(Id('init'),[]),CallExpr(Id('con'),[]),CallExpr(Id('up'),[]), ([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_case_37(self):
        input = """Var:x;
        Function: test
        Body:
            f = -1234.;
            Do 
                Do
                    If k Then If k Then EndIf. EndIf.
                While False
                EndDo.
            While f < 10
            EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('x'), [], None),FuncDecl(Id('test'), [],([],[Assign(Id('f'),UnaryOp('-',FloatLiteral(1234.0))),Dowhile(([],[Dowhile(([],[If([(Id('k'),[],[If([(Id('k'),[],[])], ())])], ())]),BooleanLiteral(False))]),BinaryOp('<',Id('f'),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_case_38(self):
        input = """
        Var: s = "dad";
        Function: sum
        Body:
            Var: sum = 0.;
            For (i = init(i * init()), cond(c *. c() - c(c())), step(step - step(step \. step(step % step)))) Do
                sum = sum + random(randint(range(0, rand())));
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('s'), [],StringLiteral("""dad""")),FuncDecl(Id('sum'), [],([VarDecl(Id('sum'), [],FloatLiteral(0.0))],[For(Id('i'),CallExpr(Id('init'),[BinaryOp('*',Id('i'),CallExpr(Id('init'),[]))]),CallExpr(Id('cond'),[BinaryOp('-',BinaryOp('*.',Id('c'),CallExpr(Id('c'),[])),CallExpr(Id('c'),[CallExpr(Id('c'),[])]))]),CallExpr(Id('step'),[BinaryOp('-',Id('step'),CallExpr(Id('step'),[BinaryOp('\.',Id('step'),CallExpr(Id('step'),[BinaryOp('%',Id('step'),Id('step'))]))]))]), ([],[Assign(Id('sum'),BinaryOp('+',Id('sum'),CallExpr(Id('random'),[CallExpr(Id('randint'),[CallExpr(Id('range'),[IntLiteral(0),CallExpr(Id('rand'),[])])])])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_case_39(self):
        input = """
        Var: s;
        Function: reverse
        Parameter: str
        Body:
            For(i = 0, i < len(str) \ 2, s) Do
                str[i] = str[len(str) - i - 1];
            EndFor.
        EndBody."""
        expect = Program([VarDecl(Id('s'), [], None),FuncDecl(Id('reverse'), [VarDecl(Id('str'), [], None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),BinaryOp('\\',CallExpr(Id('len'),[Id('str')]),IntLiteral(2))),Id('s'), ([],[Assign(ArrayCell(Id('str'),[Id('i')]),ArrayCell(Id('str'),[BinaryOp('-',BinaryOp('-',CallExpr(Id('len'),[Id('str')]),Id('i')),IntLiteral(1))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_case_40(self):
        input = """
        Var: ar[0x13][0o2][23];
        Function: ppl
        Parameter: threshold
        Body:
            If score >= threshold Then
                Return "Pass";
            Else
                Return "Again";
            EndIf.
            Return ppl;
        EndBody."""
        expect = Program([VarDecl(Id('ar'), [19,2,23], None),FuncDecl(Id('ppl'), [VarDecl(Id('threshold'), [], None)],([],[If([(BinaryOp('>=',Id('score'),Id('threshold')),[],[Return(StringLiteral("""Pass"""))])], ([],[Return(StringLiteral("""Again"""))])),Return(Id('ppl'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_case_41(self):
        input = """
        Function: dfff
        Body:
            Var: s[100];
            While !empty(s) Do
                print(pop(s));
            EndWhile.
            While !full(s) Do
                s = push(s, vr());
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('dfff'), [],([VarDecl(Id('s'), [100], None)],[While(UnaryOp('!',CallExpr(Id('empty'),[Id('s')])),([],[CallStmt(Id('print'),[CallExpr(Id('pop'),[Id('s')])])])),While(UnaryOp('!',CallExpr(Id('full'),[Id('s')])),([],[Assign(Id('s'),CallExpr(Id('push'),[Id('s'),CallExpr(Id('vr'),[])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_case_42(self):
        input = """
        Function: main
        Parameter: arr
        Body:
            print(1 + 2, 0x22)[f()[2][3+arr[3]]] = arr[2 * f()[f()]];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [VarDecl(Id('arr'), [], None)],([],[Assign(ArrayCell(CallExpr(Id('print'),[BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(34)]),[ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(2),BinaryOp('+',IntLiteral(3),ArrayCell(Id('arr'),[IntLiteral(3)]))])]),ArrayCell(Id('arr'),[BinaryOp('*',IntLiteral(2),ArrayCell(CallExpr(Id('f'),[]),[CallExpr(Id('f'),[])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_case_43(self):
        input = """
        Function: fn
        Body:
            f(f(2 + 2));
            If i == 0 Then
                If True Then
                    If t Then ElseIf con Then ElseIf con Then Else EndIf.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('fn'), [],([],[CallStmt(Id('f'),[CallExpr(Id('f'),[BinaryOp('+',IntLiteral(2),IntLiteral(2))])]),If([(BinaryOp('==',Id('i'),IntLiteral(0)),[],[If([(BooleanLiteral(True),[],[If([(Id('t'),[],[]),(Id('con'),[],[]),(Id('con'),[],[])], ([],[]))])], ())])], ())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_case_44(self):
        input = """Var: x;
        Function: symmetry
        Body:
            Var: str = "";
            str = str(input());
            For(i = 0, i < len(str) \. 2, 1) Do
                If str[i] != str[len(str) - i - 1] Then
                    Return False;
                EndIf.
            EndFor.
            Return True;
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None),FuncDecl(Id('symmetry'), [],([VarDecl(Id('str'), [],StringLiteral(""""""))],[Assign(Id('str'),CallExpr(Id('str'),[CallExpr(Id('input'),[])])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),BinaryOp('\.',CallExpr(Id('len'),[Id('str')]),IntLiteral(2))),IntLiteral(1), ([],[If([(BinaryOp('!=',ArrayCell(Id('str'),[Id('i')]),ArrayCell(Id('str'),[BinaryOp('-',BinaryOp('-',CallExpr(Id('len'),[Id('str')]),Id('i')),IntLiteral(1))])),[],[Return(BooleanLiteral(False))])], ())])),Return(BooleanLiteral(True)),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_case_45(self):
        input = """Var: x;
        Function: test
        Body:
            While True Do
                v = receive(socket, max_len);
                If v Then
                    handle();
                Else
                    raise(error("failed"));
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None),FuncDecl(Id('test'), [],([],[While(BooleanLiteral(True),([],[Assign(Id('v'),CallExpr(Id('receive'),[Id('socket'),Id('max_len')])),If([(Id('v'),[],[CallStmt(Id('handle'),[])])], ([],[CallStmt(Id('raise'),[CallExpr(Id('error'),[StringLiteral("""failed""")])])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_case_46(self):
        input = """
        Var: b = False, arr[0o10] = {120, 0x123};
        Function: test
        Body:
            Do
                While True Do
                    lock();
                    send(i + 1);
                    unlock();
                EndWhile.
            While True EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('b'), [],BooleanLiteral(False)),VarDecl(Id('arr'), [8],ArrayLiteral([IntLiteral(120),IntLiteral(291)])),FuncDecl(Id('test'), [],([],[Dowhile(([],[While(BooleanLiteral(True),([],[CallStmt(Id('lock'),[]),CallStmt(Id('send'),[BinaryOp('+',Id('i'),IntLiteral(1))]),CallStmt(Id('unlock'),[])]))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_case_47(self):
        input = """
        Var: kk = {123, 0x13, 0o13, "dasd", {}};
        Function: main
        Body:
            While exp == exp() && !error() Do
                print("kfkfkf" * 4);
                If cond() Then
                    process();
                    log();
                    Break;
                ElseIf k Then
                    handle();
                    error();
                    log();
                Else
                    log();
                    close();
                    finish();
                EndIf.
            EndWhile. 
        EndBody."""
        expect = Program([VarDecl(Id('kk'), [],ArrayLiteral([IntLiteral(123),IntLiteral(19),IntLiteral(11),StringLiteral("""dasd"""),ArrayLiteral([])])),FuncDecl(Id('main'), [],([],[While(BinaryOp('==',Id('exp'),BinaryOp('&&',CallExpr(Id('exp'),[]),UnaryOp('!',CallExpr(Id('error'),[])))),([],[CallStmt(Id('print'),[BinaryOp('*',StringLiteral("""kfkfkf"""),IntLiteral(4))]),If([(CallExpr(Id('cond'),[]),[],[CallStmt(Id('process'),[]),CallStmt(Id('log'),[]),Break()]),(Id('k'),[],[CallStmt(Id('handle'),[]),CallStmt(Id('error'),[]),CallStmt(Id('log'),[])])], ([],[CallStmt(Id('log'),[]),CallStmt(Id('close'),[]),CallStmt(Id('finish'),[])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_case_48(self):
        input = """
        Var: x;
        Function: test
        Body:
            Var: x = 10;
            Var: mm[10] = {1, 0x123, 0o123, "dasd"};
            If k == 10 Then
                While True Do
                    move_left();
                    Do 
                        For(i = 0, i < upper(), step) Do
                            While k > 10 Do
                                print("das", 123, exp(p + 2));
                            EndWhile.
                        EndFor.
                    While k == True EndDo.
                EndWhile.
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id('x'), [], None),FuncDecl(Id('test'), [],([VarDecl(Id('x'), [],IntLiteral(10)),VarDecl(Id('mm'), [10],ArrayLiteral([IntLiteral(1),IntLiteral(291),IntLiteral(83),StringLiteral("""dasd""")]))],[If([(BinaryOp('==',Id('k'),IntLiteral(10)),[],[While(BooleanLiteral(True),([],[CallStmt(Id('move_left'),[]),Dowhile(([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),CallExpr(Id('upper'),[])),Id('step'), ([],[While(BinaryOp('>',Id('k'),IntLiteral(10)),([],[CallStmt(Id('print'),[StringLiteral("""das"""),IntLiteral(123),CallExpr(Id('exp'),[BinaryOp('+',Id('p'),IntLiteral(2))])])]))]))]),BinaryOp('==',Id('k'),BooleanLiteral(True)))]))])], ())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_case_44(self):
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    
    