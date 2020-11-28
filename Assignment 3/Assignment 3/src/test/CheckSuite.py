import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_case_7(self):
        input = """
        Function: test
        Body:
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_case_8(self):
        input = """
        Function: test
        Body:
        EndBody.
        Function: main
        Body:
            Var: x = 1;
            x = test();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),CallExpr(Id('test'),[]))))
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_case_9(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = test();
        EndBody.
        Function: test
        Body:
            Return 1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('x'),CallExpr(Id('test'),[]))))
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_case_10(self):
        input = """
        Function: main
        Body:
        EndBody.
        Function: test
        Parameter: x
        Body:
            x = 1;
            test(1.4);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[FloatLiteral(1.4)])))
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_case_11(self):
        input = """
        Function: main
        Body:
            Var: x;
            test(x);
        EndBody.
        Function: test
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id('test'),[Id('x')])))
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_case_12(self):
        input = """
        Function: main
        Body:
            test(1, 2.2);
            test(1, 2);
        EndBody.
        Function: test
        Parameter: x, y
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_case_13(self):
        input = """
        Function: main
        Body:
            Var: main;
            main();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[])))
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_case_14(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            x[0] = 1;
            x[1] = "s";
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(1)]),StringLiteral("""s"""))))
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_case_15(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            test()[0] = 1;
            test()[1] = "s";
        EndBody.
        Function: test
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(1)]),StringLiteral("""s"""))))
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_case_16(self):
        input = """
        Var: x[10];
        Function: main
        Body:
        EndBody.
        Function: test
        Body:
            Var: x;
            If x Then
                Return 1;
            EndIf.
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_case_16(self):
        input = """
        Var: x[10];
        Function: main
        Body:
        EndBody.
        Function: test
        Body:
            Var: x, y;
            If foo()[1] Then
                Return 1;
            EndIf.
            Return y;
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_case_17(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: y
        Body:
            Var: x;
            If foo()[1] Then
                Return 1;
            ElseIf f(1) Then
            EndIf.
            Return y;
        EndBody.
        Function: main
        Body:
            Var: k;
            k = test(1.5);
        EndBody.
        Function: foo
        Body:
            Return {True, False, True};
        EndBody.
        Function: f
        Parameter: k
        Body:
            Return k == 1;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('test'),[FloatLiteral(1.5)])))
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_case_18(self):
        input = """
        Var: x[10][10];
        Function: main
        Body:
            Var: k;
            If 1 == f()[1][2] Then
            ElseIf x[0][0] Then
            EndIf.
        EndBody.
        Function: f
        Body:
            Var: x[10][10];
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_case_19(self):
        input = """
        Var: x[10][10];
        Function: main
        Parameter: flag
        Body:
            If flag == f(1)[0][1] Then
            EndIf.
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return foo();
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_case_20(self):
        input = """
        Var: x[10][10];
        Function: main
        Parameter: flag
        Body:
            f("s")[2][3] = 100;
            If f("a")[0][1] == foo()[1][2] Then
                f(flag)[1][3] = 0o10;
            EndIf.
            flag = 12;
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return foo();
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('flag'),IntLiteral(12))))
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_case_21(self):
        input = """
        Var: x[10][10];
        Function: main
        Parameter: flag
        Body:
            Var: v;
            v = f(flag);
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return foo();
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('v'),CallExpr(Id('f'),[Id('flag')]))))
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_case_22(self):
        input = """
        Var: x[10][10], m, k;
        Function: test
        Body:
            Return m + k;
        EndBody.
        Function: main
        Parameter: flag
        Body:
            test();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[])))
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_case_23(self):
        input = """
        Var: x[10][10], m, k;
        Function: test
        Body:
            Return m + k + x[0][1];
        EndBody.
        Function: main
        Parameter: flag
        Body:
            flag = test();
            x[3][2] = 1.2;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(3),IntLiteral(2)]),FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_case_24(self):
        input = """
        Var: x[10][10], m, k;
        Function: main
        Parameter: flag
        Body:
            For(flag = 1, f("a"), foo()) Do
            EndFor.
            Return flag;
        EndBody.
        Function: f
        Parameter: p
        Body:
            Return main(p) == 1;
        EndBody.
        Function: foo
        Body:
            Return x[0][1] * m + k;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[Id('p')])))
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_case_25(self):
        input = """
        Function: f1
        Parameter: x
        Body:
            Return {0};
        EndBody.
        Function: main
        Body:
            Var: a[1];
            Var: n;
            f1(f2(f3(n)))[0] = a[f3(f2(n))];
        EndBody.
        Function: f2
        Parameter: x
        Body:
            Return 0;
        EndBody.
        Function: f3
        Parameter: x
        Body:
            Return 0;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f1'),[CallExpr(Id('f2'),[CallExpr(Id('f3'),[Id('n')])])]),[IntLiteral(0)]),ArrayCell(Id('a'),[CallExpr(Id('f3'),[CallExpr(Id('f2'),[Id('n')])])]))))
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_case_26(self):
        input = """
        Var: x, y;
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: t;
            t = 10 + foo(2);
            t = t +. factorial(t);
        EndBody.
        Function: factorial
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return 1;
            EndIf.
            Return n * factorial(n - 1);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('t'),CallExpr(Id('factorial'),[Id('t')]))))
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_case_27(self):
        input = """
        Var: x, y, arr[5];
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: t, a[5];
            t = 10 + foo(2);
            a = get_arr();
            t = a[9] - factorial(t);
        EndBody.
        Function: factorial
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return 1;
            EndIf.
            Return n * factorial(n - 1);
        EndBody.
        Function: get_arr
        Body:
            arr = {1, 2, 3, 4, 5};
            Return arr;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_case_28(self):
        input = """
        Var: x, y, arr[5];
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: t, a;
            t = 10 + foo(2);
            t = factorial(get_arr()[2]);
        EndBody.
        Function: factorial
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return 1;
            EndIf.
            Return n * factorial(n - 1);
        EndBody.
        Function: get_arr
        Body:
            arr = {1, 2, 3, 4, 5};
            Return arr;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('t'),CallExpr(Id('factorial'),[ArrayCell(CallExpr(Id('get_arr'),[]),[IntLiteral(2)])]))))
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_case_29(self):
        input = """
        Var: x, y, arr[5];
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: t, a;
            t = 10 + foo(2);
            t = factorial(t);
            arr = get_arr();
        EndBody.
        Function: factorial
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return 1;
            EndIf.
            Return n * factorial(n - 1);
        EndBody.
        Function: get_arr
        Body:
            Var: arr = {1, 2, 3, 4, 5, 6};
            Return arr;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('arr'))))
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_case_30(self):
        input = """
        Var: x, y, arr[5];
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: t;
            t = 10 + foo(2);
            arr[0] = t;
            t = factorial(foo(factorial(foo(arr[3])))) + t + foo(2) + foo(get_arr()[foo(t)]);
        EndBody.
        Function: factorial
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return 1;
            EndIf.
            Return n * factorial(n - 1);
        EndBody.
        Function: get_arr
        Body:
            arr = {1, 2, 3, 4, 5};
            Return arr;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_case_31(self):
        input = """
        Var: a, b[4][12], c;
        Function: test
        Body:
            func()[2][1] = 14;
        EndBody.
        Function: func
        Body:
            Return b;
        EndBody.
        Function: main
        Body:
            func()[3][1] = 0;
            b[0][0] = c;
            test();
            func()[c][2 + 1 * 1] = b[0][c];
            If False Then
                While True Do
                EndWhile.
                Break;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_case_32(self):
        input = """
        Var: a, b[4][2], c;
        Function: test
        Body:
            func()[2][1] = 14;
        EndBody.
        Function: func
        Body:
            Return b;
        EndBody.
        Function: main
        Body:
            func()[3][1] = 0;
            b[0][0] = "s";
            test();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(0),IntLiteral(0)]),StringLiteral("""s"""))))
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_case_33(self):
        input = """
        Var: x, y = "s", t, arr[10];
        Function: main
        Body:

        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: arr[2];
            If x Then
                Return int_of_string(string_of_bool(x));
            ElseIf f(x) Then
                Return foo(bool_of_string(arr[0]));
            EndIf.
        EndBody.
        Function: f
        Parameter: x
        Body:
            If bool_of_string(string_of_bool(x)) Then
                Return x;
            EndIf.
            Return;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_case_34(self):
        input = """
        Var: a, b[2][4][2];
        Function: main
        Body:
            Var: temp;
           printStrLn(a);
           test(temp);
        EndBody.
        Function: test
        Parameter: p
        Body:
            printStr(read());
        EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id('test'),[Id('temp')])))
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_case_35(self):
        input = """
        Var: a, b[2][2], c;
        Function: main
        Body:
           b[f()][f()] = 123;
        EndBody.
        Function: f
        Body:
            Var: c[2][3];
            b = c;
            Return 1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('b'),Id('c'))))
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_case_36(self):
        input = """
        Var: a, b[2][2], c;
        Function: test
        Parameter: k
        Body:
            Do
                test(1);
            While k EndDo.
        EndBody.
        Function: main
        Body:
           b[f()][f()] = 123;
        EndBody.
        Function: f
        Body:
            Var: c[2][3];
            Return 1;
        EndBody.
        """
        expect =  str(TypeMismatchInStatement(CallStmt(Id('test'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_case_37(self):
        input = """
        Var: a, b;
        Function: main
        Parameter: x, y, k, t, a, x
        Body:
        EndBody.
        """
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_case_38(self):
        input = """
        Var: a, b;
        Function: main
        Parameter: x, y
        Body:
        EndBody.
        Function: a
        Body:
        EndBody.
        """
        expect = str(Redeclared(Function(), 'a'))
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_case_39(self):
        input = """
        Var: a, b;
        Function: main
        Parameter: x, y
        Body:
            Var: main;
            main(1, "a");
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[IntLiteral(1),StringLiteral("""a""")])))
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_case_40(self):
        input = """
        Var: a, b;
        Function: f
        Parameter: a, b
        Body:
            Var: flags[2][4];
            flags[0][0] = (9. =/= t()) || f(a * b, a)[1][2];
            Return flags;
        EndBody.
        Function: main
        Parameter: x, y
        Body:
            Do
                a = x + y;
                b = float_of_int(a);
            While f(x, y)[1][2] EndDo.
        EndBody.
        Function: t
        Body:
            Return t() *. 0.1;
        EndBody.
        Function: mm
        Body:
            a = int_of_float(b);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_case_41(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y
        Body:
            For(a = f()[1][2], c()[1 + 2][fe()][fe()][fe()], arr[1][1]) Do
            EndFor.
        EndBody.
        Function: f
        Body:
            Return arr;
        EndBody.
        Function: c
        Body:
            Var: a[2][3][4][5];
            Return a;
        EndBody.
        Function: fe
        Body:
            Return float_of_int(b);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('float_of_int'),[Id('b')]))))
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_case_42(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y
        Body:
            f()[2][3] = a * 2;
            arr[0][2] = "PPL!!! hard!!!";
        EndBody.
        Function: f
        Body:
            Return arr;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('arr'))))
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_case_43(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y
        Body:
            reaD()[2][3] = a * 2;
            arr[0][2] = "PPL!!! hard!!!";
        EndBody.
        """
        expect = str(Undeclared(Function(), 'reaD'))
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_case_44(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y
        Body:
            arr[0][2] = "PPL!!! hard!!!";
            b = a * c[2][3];
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'c'))
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_case_45(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y
        Body:
            arr[0][2] = "PPL!!! hard!!!";
            b = a * int_of_string(arr[1][2]);
        EndBody.
        Function: test
        Parameter: m
        Body:
            Return arr[a + b];
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('arr'),[BinaryOp('+',Id('a'),Id('b'))])))
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_case_46(self):
        input = """
        Var: a, b, arr[10][10], main;
        Function: foo
        Parameter: x, y
        Body:
            arr[0][2] = "PPL!!! hard!!!";
            b = a * int_of_string(arr[1][2]);
        EndBody.
        Function: test
        Parameter: m
        Body:
            Return arr[a + b][int_of_float(float_of_string(arr[1][0]))];
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_case_47(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            arr[0][2] = "PPL!!! hard!!!";
            b = a * int_of_string(arr[1][2]);
            foo();
        EndBody.
        Function: test
        Parameter: m
        Body:
            Return arr[a + b][int_of_float(float_of_string(arr[1][0]))];
        EndBody.
        Function: foo
        Body:
            Return;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_case_48(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            arr[0][2] = "PPL!!! hard!!!";
            b = a * int_of_string(arr[1][2]);
            foo();
        EndBody.
        Function: test
        Parameter: m
        Body:
            test(int_of_float(float_of_int(m)));
        EndBody.
        Function: foo
        Body:
            Return test(b);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('test'),[Id('b')]))))
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_case_49(self):
        input = """
        Var: a, b, arr[10][10];
        Function: foo
        Body:
            Return;
        EndBody.
        Function: main
        Parameter: x, y, main
        Body:
            Var: k;
            arr[0][2] = "PPL!!! hard!!!";
            b = a * int_of_string(arr[1][2]);
            foo();
            k = foo();
        EndBody.
        Function: test
        Parameter: m
        Body:
            test(int_of_float(float_of_int(m)));
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('k'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_case_50(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            foo(a + b);
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            foo(1, 2.2);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[BinaryOp('+',Id('a'),Id('b'))])))
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_case_51(self):
        input = """
        Var: a, b, arr[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            If main && x Then
                Return y + 1;
            EndIf.
            Return arr[0][0];
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            arr[0][1] = "s";
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('arr'),[IntLiteral(0),IntLiteral(1)]),StringLiteral("""s"""))))
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_case_52(self):
        input = """
        Var: a, b, arr[10][10], array[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            If main && x Then
                Return y + 1;
            EndIf.
            Return arr[0][0];
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            array[2][3] = x =/= y;
            arr = array;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('arr'),Id('array'))))
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_case_53(self):
        input = """
        Var: a, b, arr[10][10], array[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            arr = array;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('arr'),Id('array'))))
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_case_54(self):
        input = """
        Var: a, b, arr[3][2];
        Function: main
        Parameter: x, y, main
        Body:
            a[2][3] = b * y - x % main;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 453))
