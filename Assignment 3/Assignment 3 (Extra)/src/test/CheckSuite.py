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
        """Complex program"""
        input = Program([
                FuncDecl(Id("no_main"),[],([VarDecl(Id('main'), [], None)],[
                    CallStmt(Id("printStrLn"),[StringLiteral("Hello World")])]))])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_case_8(self):
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(Id('i'),([],[]))]))])
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_case_9(self):
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(Id('x'),([],[]))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_case_10(self):
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(BinaryOp('==',Id('y'),IntLiteral(2)),([VarDecl(Id('x'), [],IntLiteral(2)),VarDecl(Id('x'), [], None)],[]))]))])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_case_11(self):
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(BinaryOp('==',Id('y'),IntLiteral(2)),([VarDecl(Id('i'), [], IntLiteral(1))],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(2)),Id('y'), ([],[Break()])),Break()]))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_case_12(self):
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])]))],[]))])
        expect = str(InvalidArrayLiteral(ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_case_13(self):
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])]))],[]))])
        expect = str(InvalidArrayLiteral(ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_case_14(self):
        """
        Var: x, y;
        Function: main
        Body:
            x = 2 - 3 * y \ 5;
            While (y == 0o23) Do
                Var: k = "string";
                k = x;
            EndWhile.
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('\\',BinaryOp('*',IntLiteral(3),Id('y')),IntLiteral(5)))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[Assign(Id('k'),Id('x'))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('k'),Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_case_15(self):
        input = """
        Var: x, y;
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
            x = 2 - 3 * y \ 5;
            While (y == 0o23) Do
                Var: k = "string";
                Continue;
            EndWhile.
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [],([],[])),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('\\',BinaryOp('*',IntLiteral(3),Id('y')),IntLiteral(5)))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[Continue()]))]))])
        expect = str(UnreachableFunction('foo'))
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_case_16(self):
        """
        Var: x, y;
        Function: main
        Body:
            x = 2 - 3 * y;
            While (y == 0o23) Do
                Var: k = "string";
                If x == y Then
                    If x == 3 Then
                    ElseIf y == 4 Then
                        Break;
                        x = y;
                    EndIf.
                EndIf.
            EndWhile.
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('*',IntLiteral(3),Id('y')))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[If([(BinaryOp('==',Id('x'),Id('y')),[],[If([(BinaryOp('==',Id('x'),IntLiteral(3)),[],[]),(BinaryOp('==',Id('y'),IntLiteral(4)),[],[Break(),Assign(Id('x'),Id('y'))])], ([],[]))])], ([],[]))]))]))])
        expect = str(UnreachableStatement(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test_case_17(self):
        """
        Var: x, y;
        Function: foo
        Body:
            foo();
        EndBody.
        Function: main
        Body:
            foo();   
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [],([],[CallStmt(Id('foo'),[])])),FuncDecl(Id('main'), [],([],[CallStmt(Id('foo'),[])]))])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_case_18(self):
        """
        Var: x, y;
        Function: foo
        Body:
            Return f();
        EndBody.
        Function: main
        Body:
            foo();   
        EndBody.
        Function: f
        Body:
            Return 1;
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [],([],[Return(CallExpr(Id('f'),[]))])),FuncDecl(Id('main'), [],([],[CallStmt(Id('foo'),[])])),FuncDecl(Id('f'), [],([],[Return(IntLiteral(1))]))])
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('f'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test_case_19(self):
        """
        Var: x, y;
        Function: foo
        Parameter: a, b
        Body:
            a = 2;
            b = a * a;
        EndBody.
        Function: main
        Body:
            Var: x, y;
            x = y * 10;
            foo(x);   
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('a'), [], None),VarDecl(Id('b'), [], None)],([],[Assign(Id('a'),IntLiteral(2)),Assign(Id('b'),BinaryOp('*',Id('a'),Id('a')))])),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None)],[Assign(Id('x'),BinaryOp('*',Id('y'),IntLiteral(10))),CallStmt(Id('foo'),[Id('x')])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test_case_20(self):
        """
        Var: x, y;
        Function: foo
        Parameter: a, b
        Body:
            a = 2;
            b = a * a;
        EndBody.
        Function: main
        Body:
            Var: x, y;
            foo(x);   
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('a'), [], None),VarDecl(Id('b'), [], None)],([],[Assign(Id('a'),IntLiteral(2)),Assign(Id('b'),BinaryOp('*',Id('a'),Id('a')))])),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None)],[CallStmt(Id('foo'),[Id('x'),Id('y')])]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test_case_21(self):
        """
        Var: x, y;
        Function: foo
        Parameter: a[10][10], b
        Body:
            Var: c[10] = {0, 1, 2};
            a[9] = c;
        EndBody.
        Function: main
        Body:
            Var: x, y;
            foo(x, y);   
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('a'), [10,10], None),VarDecl(Id('b'), [], None)],([VarDecl(Id('c'), [10],ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(2)]))],[Assign(ArrayCell(Id('a'),[IntLiteral(9)]),Id('c'))])),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None)],[CallStmt(Id('foo'),[Id('x'),Id('y')])]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(9)])))
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test_case_22(self):
        """
        Var: x, y;
        Function: foo
        Body:
            Var: c[10] = {0, 1, 2};
            Return c;
        EndBody.
        Function: main
        Body:
            foo()[2] = {1, 2, 3};  
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [],([VarDecl(Id('c'), [10],ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(2)]))],[Return(Id('c'))])),FuncDecl(Id('main'), [],([],[Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))])
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test_case_23(self):
        """
        Var: x, y;
        Function: main
        Body:
            Var: x[3][3];
             x = {{1, 2, 3}, {1,2,3}};  
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [3,3], None)],[Assign(Id('x'),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))))
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_case_24(self):
        """
        Var: x, y;
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: x[10][10][10][5];
            Var: n;
            Var: k = 0x12;
            x[n + 2][foo(k) + 2][2 + 15][8 \ 2] = 20;
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [10,10,10,5], None),VarDecl(Id('n'), [], None),VarDecl(Id('k'), [],IntLiteral(18))],[Assign(ArrayCell(Id('x'),[BinaryOp('+',Id('n'),IntLiteral(2)),BinaryOp('+',CallExpr(Id('foo'),[Id('k')]),IntLiteral(2)),BinaryOp('+',IntLiteral(2),IntLiteral(15)),BinaryOp('\\',IntLiteral(8),IntLiteral(2))]),IntLiteral(20))]))])
        expect = str(IndexOutOfRange(ArrayCell(Id('x'),[BinaryOp('+',Id('n'),IntLiteral(2)),BinaryOp('+',CallExpr(Id('foo'),[Id('k')]),IntLiteral(2)),BinaryOp('+',IntLiteral(2),IntLiteral(15)),BinaryOp('\\',IntLiteral(8),IntLiteral(2))])))
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_case_25(self):
        """
        Var: x, y = "s", t, arr[10];
        Function: main
        Body:
            x = 1;
            t = x + foo(x);
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return 1;
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],StringLiteral("""s""")),VarDecl(Id('t'), [], None),VarDecl(Id('arr'), [10], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),IntLiteral(1)),Assign(Id('t'),BinaryOp('+',Id('x'),CallExpr(Id('foo'),[Id('x')])))])),FuncDecl(Id('foo'), [VarDecl(Id('x'), [], None)],([],[Return(IntLiteral(1))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_case_26(self):
        input = """
        Var: x, y = "s", t, arr[10];
        Function: main
        Body:
            arr[0] = 1.2;
            arr[2] = 1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('arr'),[IntLiteral(2)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_case_27(self):
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
            Return True;
        EndBody.
        """
        expect = str(FunctionNotReturn('foo'))
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test_case_28(self):
        input = """
        Var: x, y = "s", t, arr[10];
        Function: main
        Body:
            t = test() *. 10.;
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
            Return arr[1];
        EndBody.
        Function: f
        Parameter: x
        Body:
            If bool_of_string(string_of_bool(x)) Then
                Return x;
            EndIf.
            Return 1 == 2;
        EndBody.
        Function: test
        Body:
            Var: m;
            While x Do
                While 1 == 2 Do
                    If x && (2 == 1) Then
                        If (foo(x) == 1) || f(x) Then
                            Return 2.;
                        EndIf.
                        Return m *. 2e-1;
                    EndIf.
                    Break;
                    m = 10.2;
                EndWhile.
            EndWhile.    
            Return m;        
        EndBody.
        """
        expect = str(UnreachableStatement(Assign(Id('m'),FloatLiteral(10.2))))
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_case_29(self):
        input = """
        Var: a, b[5], c;
        Function: test
        Body:
            a = 10;
            b = {1, 2, 6, 10, 3};
            c = b[2];
        EndBody.
        Function: main
        Body:
            test();
        EndBody.
        Function: f
        Body:
        EndBody.
        """
        expect = str(UnreachableFunction('f'))
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_case_30(self):
        input = """
        Var: a, b[4][2], c;
        Function: main
        Body:
            b = {{2, 3}, {2, 4}, {8, 2}, {2.3, 2e-2}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(2),IntLiteral(4)]),ArrayLiteral([IntLiteral(8),IntLiteral(2)]),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(0.02)])])))
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_case_31(self):
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
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('func'),[]),[IntLiteral(2),IntLiteral(1)]),IntLiteral(14))))
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_case_32(self):
        input = """
        Var: a, b[4][2], c;
        Function: func
        Body:
            b[0][1] = 2;
            Return b;
        EndBody.
        Function: test
        Body:
            func()[2][1] = 14;
        EndBody.
        Function: main
        Body:
            func()[3][1] = 0;
            b[0][0] = c;
            test();
            func()[c][2 + 2 * 1] = b[0][c];
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('func'),[]),[Id('c'),BinaryOp('+',IntLiteral(2),BinaryOp('*',IntLiteral(2),IntLiteral(1)))])))
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_case_33(self):
        input = """
        Var: a, b[4][12], c;
        Function: func
        Body:
            b[3][0] = 123;
            Return b;
        EndBody.
        Function: test
        Body:
            func()[2][1] = 14;
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
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_case_34(self):
        input = """
        Var: a, b[2][2], c;
        Function: main
        Body:
            b = {{2, 3}, {2., "d"}};
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([FloatLiteral(2.0),StringLiteral("""d""")])))
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
        Var: a, b[2][12], c;
        Function: main
        Body:
           b[f()][f()] = 123;
        EndBody.
        Function: f
        Body:
            Var: c[2][12];
            c[1][2] = "10";
            b = c;
            Return 1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('b'),Id('c'))))
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_case_37(self):
        input = """
        Var: a, b[2][12], c;
        Function: f
        Body:
            If c Then
                Return 1;
            Else
                Return b[0][2 + 9];
            EndIf.
            Return foo()[2][1];
        EndBody.
        Function: main
        Body:
           a = f();
        EndBody.
        Function: foo
        Body:
            Var: c[2][12];
            Return c;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_case_38(self):
        input = """
        Var: a, b[2][12], c[2][12];
        Function: foo
        Body:
            c[0][1] = "s";
            Return c;
        EndBody.
        Function: f
        Body:
            Var: flag, c;
            If c Then
                Return 1;
            ElseIf c Then
                Return b[0][2 + 9];
            EndIf.
            Return foo()[2+3][1]; 
        EndBody.
        Function: main
        Body:
           a = f();
        EndBody.
       
        Function: t
        Body:
            c[0][11] = "string";
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('foo'),[]),[BinaryOp('+',IntLiteral(2),IntLiteral(3)),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_case_39(self):
        input = """
        Var: a, b[2][4][2];
        Function: f
        Body:
            b[0][0][0] = 22;
            Return b;
        EndBody.
        Function: main
        Body:
           f()[2][3][3] = 123;
           a = test(f()[0][0][1]) \ 9 ;
        EndBody.
        Function: test
        Parameter: k
        Body:
            Return k * f()[0][2][1];
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(2),IntLiteral(3),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_case_40(self):
        input = """
        Var: a, b[2][4][2];
        Function: main
        Body:
           f(a)[2][3][3] = 123;
           a = test(f(2)[0][0][1]) \ 9 ;
        EndBody.
        Function: f
        Parameter: a
        Body:
            Return b;
        EndBody.
        Function: test
        Parameter: k
        Body:
            Return k * f()[0][2][3];
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f'),[Id('a')]),[IntLiteral(2),IntLiteral(3),IntLiteral(3)]),IntLiteral(123))))
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_case_41(self):
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
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_case_42(self):
        input = """
        Var: a, b[2][4][2];
        Function: main
        Body:
            Var: temp;
           printStrLn(a);
           Do
                If bool_of_string(a) Then
                    Break;
                    test(a);
                EndIf.
            While b[0][1][1] EndDo.
        EndBody.
        Function: test
        Parameter: p
        Body:
            printStr(read());
            Return;
        EndBody.
        """
        expect = str(UnreachableStatement(CallStmt(Id('test'),[Id('a')])))
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_case_43(self):
        input = """
        Var: x, y;
        Function: main
        Body:
            If x Then
                If x Then 
                    Return 0;
                EndIf.
                If x Then
                    Return y;
                ElseIf x Then
                    If x Then
                        Return 1;
                    Else
                        Return 0;
                    EndIf.
                    y = 10;
                EndIf.
            Else
                Return 1;
            EndIf.
            y = 1;
        EndBody.
        """
        expect = str(UnreachableStatement(Assign(Id('y'),IntLiteral(10))))
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_case_44(self):
        input = """
        Var: x, y;
        Function: main
        Body:
            If x Then
                If x Then 
                    Return 0;
                EndIf.
                If x Then
                    Return y;
                ElseIf x Then
                    If x Then
                        Return y;
                    Else
                        Return 0;
                    EndIf.
                EndIf.
            Else
                Return 1;
            EndIf.
            y = y * 2;
        EndBody.
        """
        expect = str(FunctionNotReturn('main'))
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_case_45(self):
        input = """
        Var: x, y;
        Function: main
        Body:
            Var: k, t, z;
            While x Do
                If x Then
                    y = 2;
                    Break;
                ElseIf k == t Then
                    z = 20;
                    Continue;
                Else
                    Break;
                EndIf.
                t = y + z;
            EndWhile.
        EndBody.
        """
        expect = str(UnreachableStatement(Assign(Id('t'),BinaryOp('+',Id('y'),Id('z')))))
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_case_46(self):
        input = """
        Var: x, y;
        Function: main
        Body:
            Var: k, t, z;
            While x Do
                If x Then
                    y = 2;
                    Return 0;
                ElseIf k == t Then
                    z = 20;
                    Return y;
                Else
                    Return t;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = str(FunctionNotReturn('main'))
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_case_47(self):
        input = """
        Var: x[10], y;
        Function: main
        Body:
            x[0] = test() + y;
        EndBody.
        Function: test
        Body:
            Var: a, b, c;
            If a + b == c Then
                Return a;
            ElseIf a == b Then
                Return c;
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn('test'))
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_case_48(self):
        input = """
        Var: x[10], y, m;
        Function: main
        Body:
            x[0] = test() +. y;
        EndBody.
        Function: test
        Body:
            Var: a, b, c;
            For (a = int_of_float(test()), b && c, m) Do
                Var: z, y, x;
                If z == y Then
                    Break;
                ElseIf x Then
                    Continue;
                ElseIf c Then
                    Return float_of_int(a);
                Else
                    Return 1.2;
                EndIf.
                b = True;
            EndFor.
            Return float_of_int(m);
        EndBody.
        """
        expect = str(UnreachableStatement(Assign(Id('b'),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_case_49(self):
        input = """
        Var: x[10], y, m;
        Function: main
        Body:
            x[0] = test() +. y;
        EndBody.
        Function: test
        Body:
            Var: a, b, c;
            For (a = int_of_float(test()), b && c, m) Do
                Var: z, y, x;
                If z == y Then
                    Break;
                ElseIf x Then
                    Continue;
                ElseIf c Then
                    Return float_of_int(a);
                Else
                    Return 1.2;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = str(FunctionNotReturn('test'))
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_case_50(self):
        input = """
        Var: x[10], y, m;
        Function: main
        Body:
            x[0] = test() + y;
        EndBody.
        Function: test
        Body:
            Var: a, b, c;
            Do
                If c Then
                    If c Then
                    ElseIf False Then
                        If a > b Then
                            Break;
                        Else
                            Return 0;
                        EndIf.
                        a = b;
                    EndIf.
                EndIf.
            While a == b EndDo.
            Return a * b;
        EndBody.
        """
        expect = str(UnreachableStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_case_51(self):
        input = """
        Var: x[10], y, m;
        Function: main
        Body:
            x[0] = y + 10;
        EndBody.
        Function: test
        Body:
            Var: a, b, c;
            If x[2] == a Then
                printStrLn(b);
            EndIf.
            For(a = 0, c < m, m \ 10) Do
                printStr(string_of_int(a * c - m));
            EndFor.
        EndBody.
        """
        expect = str(UnreachableFunction('test'))
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_case_52(self):
        input = """
        Function: main
        Body:
            foo(1,2); 
        EndBody.

        Function: foo
        Parameter: n 
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_case_53(self):
        input = """
        Function: foo
        Parameter: n 
        Body:
            If (n == 0) || (n - 1 == 0) Then
                Return 1;
            EndIf.
            Return n * foo(n - 1);
        EndBody.
        Function: main
        Body:
            Var: k;
            k = foo(k)[1 + 2];
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('foo'),[Id('k')]),[BinaryOp('+',IntLiteral(1),IntLiteral(2))])))
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_case_54(self):
        input = """
        Function: main
        Parameter: x
        Body:
            x = foo(x,2); 
        EndBody.

        Function: foo
        Parameter: n 
        Body:
            Var: k, arr[10];
            If n < foo() Then
                Return k;
            EndIf.
            Return arr[5];
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[Id('x'),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_case_55(self):
        input = """
        Var: x;
        Function: main
        Parameter: y
        Body:
            x = foo(5) * y; 
        EndBody.

        Function: foo
        Parameter: n 
        Body:
            Var: k, arr[10];
            If n < foo(x) Then
                Return k;
            ElseIf k == arr[1] Then
                Return k * 2 - arr[foo(k)];
            Else
                Return x;
            EndIf.
            Return arr[5];
        EndBody.
        """
        expect = str(UnreachableStatement(Return(ArrayCell(Id('arr'),[IntLiteral(5)]))))
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_case_56(self):
        input = """
        Var: x, a[4][5][2][5][6];
        Function: main
        Parameter: y
        Body:
            x = foo(5) * y; 
            y = a[x][0 + x][0 + 2][y * 3 - x][y];
        EndBody.

        Function: foo
        Parameter: n 
        Body:
            Var: k, arr[10];
            If n < foo(x) Then
                Return k;
            ElseIf k == arr[1] Then
                Return k * 2 - arr[foo(k)];
            EndIf.
            Return arr[5 + 2];
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(Id('a'),[Id('x'),BinaryOp('+',IntLiteral(0),Id('x')),BinaryOp('+',IntLiteral(0),IntLiteral(2)),BinaryOp('-',BinaryOp('*',Id('y'),IntLiteral(3)),Id('x')),Id('y')])))
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_case_57(self):
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
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_case_58(self):
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
        expect =  str(TypeMismatchInStatement(Dowhile(([],[CallStmt(Id('test'),[IntLiteral(1)])]),Id('k'))))
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_case_59(self):
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
            Var: arr = {1, 2, 3, 4, 5};
            Return arr;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('arr'),CallExpr(Id('get_arr'),[]))))
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_case_60(self):
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
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_case_61(self):
        input = """
        Var: x[10];
        Function: main
        Parameter: flag
        Body:
            Var: s;
            s = read();
            For(flag = 0, flag < length(s), 1) Do
                x[s] = x[s] + 1;
            EndFor.
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'),[Id('s')])))
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_case_62(self):
        input = """
        Var: x[10];
        Function: main
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(x);
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('length'),[Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test_case_63(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(flag);
            Return flag;
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        Function: main
        Body:
            Var: z;
            z = test(x[0]);
            x[0] = t;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 't'))
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_case_64(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(flag);
            Return flag;
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        Function: foo
        Body:
            Var: z;
            z = test(x[0]);
            x[1] = z;
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_case_65(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(flag);
            Return flag;
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        Function: main
        Body:
            Var: z;
            z = test(x[0]);
            x[1] = z;
            printStrLn(string_of_int(length(z)));
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_case_66(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: y, z;
            x[2] = x[0o3] || (y > z);
            While x[2] && x[3] Do
                Do
                    printStrLn(string_of_int(y * z));
                    If x[0] Then
                        Return 1;
                    ElseIf x[1] Then
                        Return z;
                    Else
                        Var: k;
                        k = 10;
                    EndIf.
                    z = y;
                While x[4] EndDo.
            EndWhile.
        EndBody.
        """
        expect = str(FunctionNotReturn('main'))
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_case_67(self):
        input = """
        Var: x[10];
        Function: foo
        Parameter: a, b
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            t = 4;
            a[0] = t;
            a = foo(t, 4);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test_case_68(self):
        input = """
        Var: x[10];
        Function: foo
        Parameter: a, b
        Body:
            b = x[5] * b % 4;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            t = 4;
            a = foo(t, 4);
            z = foo(a[2], t)[2];
            a[2] = float_of_int(z);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[IntLiteral(2)]),CallExpr(Id('float_of_int'),[Id('z')]))))
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test_case_69(self):
        input = """
        Var: x[10];
        Function: foo
        Parameter: a, b
        Body:
            b = x[5] * b % 4;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            t = 4;
            foo(t, t)[2] = a[2];
            a[int_of_float(4.3 *. 2.4 \. 0.1)] = z || (t > x[1]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[CallExpr(Id('int_of_float'),[BinaryOp('\.',BinaryOp('*.',FloatLiteral(4.3),FloatLiteral(2.4)),FloatLiteral(0.1))])]),BinaryOp('||',Id('z'),BinaryOp('>',Id('t'),ArrayCell(Id('x'),[IntLiteral(1)]))))))
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test_case_70(self):
        input = """
        Var: x[10];
        Function: foo
        Body:
            x[2] = 2;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            a[9] = t * z % x[1];
            a[2] = foo()[2];
            foo()[4] = 4.3;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(4)]),FloatLiteral(4.3))))
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test_case_71(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], t, z;
            a[9] = t * z;
            a = foo();
            foo()[2] = 3.4;
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2)]),FloatLiteral(3.4))))
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_case_72(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], t, z;
            a[t] = t +. 2.;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('t'),FloatLiteral(2.0))))
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_case_73(self):
        input = """
        Function: main
        Parameter: x
        Body:
            Var: y, z;
            y = x && (x == z);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('==',Id('x'),Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_case_74(self):
        input = """
        Var: a[2] = {0, 1};
        Function: foo
        Parameter: x
        Body:
            Return a;
        EndBody.

        Function: main
            Body:
                foo(0)[0] = foo(0.0)[1 * a[1]]; 
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_case_75(self):
        input = """
        Var: a[2] = {0, 1};
        Function: foo
        Parameter: x
        Body:
        EndBody.

        Function: main
            Body:
                foo(0);
                foo("a"); 
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[StringLiteral("""a""")])))
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_case_76(self):
        input = """
        Function: foo
        Body:
        EndBody.

        Function: main
        Parameter: x
        Body:
            main(main(foo()));
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 475))