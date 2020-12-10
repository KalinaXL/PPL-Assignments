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

    def test_0(self):
        input = """
        Var: epsilon = 1e-6;
        Function: isInteger
        Parameter: d
        Body:
            Return d - round(d) <. epsilon;
        EndBody.
        Function: main
        Parameter: argc, argv
        Body:
            If (argc != 2) Then
                Return -1;
            Else
                If isInteger(atof(argv[2])) Then
                    print("True");
                Else
                    print("False");
                EndIf.
            EndIf.
        EndBody.
        """
        expect = str(Undeclared(Function(), 'round'))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_1(self):
        input = """
        Var: epsilon = 1e-6;
        Function: isInteger
        Parameter: d
        Body:
            ** Return d - round(d) <. epsilon; **
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_2(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a = 5;
            a = b;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a = b;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a = foo() + 1;
            b = 7.0;
            b = foo();
        EndBody.
        Function: foo
        Body:

        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('b'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,404))  
    
    def test_5(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a = foo() + 1;
            b = 7.0;
            b = float_of_int(foo());
        EndBody.
        Function: foo
        Body:
            Return 0o10;
        EndBody.
        """
        expect = ''
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        input = """
        Function: main
        Parameter: a, b
        Body:
            a = foo() + 1;
            b = 7.0;
            foo();
        EndBody.
        Function: foo
        Body:

        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        input = """
        Var: main[1][2][3];
        Function: main
        Parameter: a, b
        Body:
            **empty**
        EndBody.
        """
        expect = str(Redeclared(Function(),'main'))
        self.assertTrue(TestChecker.test(input,expect,407)) 

    def test_8(self):
        input = """
        Var: x = 5, y;
        Function: main
        Parameter: a, b
        Body:
            y = float_of_string(read());
            Return x + y;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_9(self):
        input = """
        Var: x = 5, y;
        Function: procedure
        Body:
            Return;
            ** now procedure is VoidType **
        EndBody.
        Function: main
        Parameter: a, b
        Body:
            a = procedure() * 5;
            ** call a void function as a expr raise error **
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('*',CallExpr(Id('procedure'),[]),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        input = """
        Var: x[10];
        Function: test
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            test()[1] = 1;
            test()[2] = "a";
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        input = """
        Var: x[10];
        Function: test
        Body:
            Return 5;
            Return 5 * 7.;
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('*',IntLiteral(5),FloatLiteral(7.0))))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        input = """
        Var: x[10];
        Function: test
        Body:
            Return 5;
            Return 6.9;
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(6.9))))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            x[0] = 1;
            x[1] = "s";
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(1)]),StringLiteral('s'))))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        input = """
        Function: main
        Body:
            Var: x, y, a;
            y = a + foo(x);
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'),BinaryOp('+',Id('a'),CallExpr(Id('foo'),[Id('x')])))))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        input = """
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
            Var: foo;
            foo();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        input = """
        Var: x, y = 12;
        Function: main
        Parameter: a[10]
        Body:
            x = 2 + test(12);
        EndBody.
        Function: test
        Parameter: n
        Body:
            n = 1.5;
            printStrLn(read());
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('n'),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        Function: foo
        Parameter: x,y
        Body:
            x = 1;
            foo(1.1, 0);
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[FloatLiteral(1.1),IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
        Function: foo
        Parameter: x,y
        Body:
        EndBody.
        Function: main
        Body:
            foo(1, 2);
            foo(1., 2.);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[FloatLiteral(1.0),FloatLiteral(2.0)])))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        Var: a;
        Function: main
        Body:
            a = foo();
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('a'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        Function: foo
        Parameter: x,y
        Body:
            x = 1;
            foo(1, 0);
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        Var: x[3] = {1, 2, 3};
        Function: main
        Body:
            x[0] = 6;
            x[1] = 9;
            x[2] = 6.9;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(2)]),FloatLiteral(6.9))))
        self.assertTrue(TestChecker.test(input, expect, 421))
    

    def test_22(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            test()[1] = 1;
            test()[2] = "a";
        EndBody.
        Function: test
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(1)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        input = """
        Var: x[10], y, z;
        Function: main
        Body:
            y = 1 + x[1];
            z = x[1];
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        input = """
        Var: x[10], y, z;
        Function: main
        Body:
            y = 1 + -foo(0.0);
            x[1] = 69;
        EndBody.
        Function: foo
        Parameter: n
        Body:
            Return n;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('n'))))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        input = """
        Function: main
        Body:
            Var: i, n;
            For (i = 0.0, i < n, 1) Do 

            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),FloatLiteral(0.0),BinaryOp('<',Id('i'),Id('n')),IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input = """
        Function: main
        Body:
            Var: x, y;
            x = 1; ** x type infer to IntType **
            x = y; ** y type infer to IntType **
            Return y; ** main type infer to IntType **
            Return main() * 6.9;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('*',CallExpr(Id('main'),[]),FloatLiteral(6.9))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        input = """
        Function: main
        Body:
            Var: x, y;
            x = 1; ** x type infer to IntType **
            x = foo()[1]; ** foo type infer to Array[] of int **
            Return foo()[1]; ** main type infer to IntType **
            Return 6.9;
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('x'),ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        input = """
        Function: main
        Body:
            Var: x[5], y;
            x[1] = 1; ** x type infer to IntType **
            x = foo1(); ** foo type infer to IntType **
            foo1()[1] = foo2()[1]; ** main type infer to IntType **
            Return foo2()[5];
            Return 6.9;
        EndBody.
        Function: foo1
        Body:
        EndBody.
        Function: foo2
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo1'),[]),[IntLiteral(1)]),ArrayCell(CallExpr(Id('foo2'),[]),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        input = """
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
            Var: x;
            x = foo();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input = """
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
            Var: x = 5;
            foo();
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input = """
        Function: main
        Body:
            Var: x = 5;
            foo(1, 2, 3);
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            Return 0;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_32(self):
        input = """
        Function: main
        Body:
            Var: i;
            For (i = 0, i < 10, 1) Do
            EndFor.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        input = """
        Function: main
        Body:
            Var: i;
            For (i = 0, i < 10, 0.5) Do
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),FloatLiteral(0.5),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_34(self):
        input = """
        Function: main
        Body:
            Var: i;
            For (i = 0, i <. 10.0, 1) Do
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('<.',Id('i'),FloatLiteral(10.0))))
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_35(self):
        input = """
        Function: main
        Body:
            Var: i;
            For (i = 0., i < 10, 1) Do
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),FloatLiteral(0.0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_36(self):
        input = """
        Function: main
        Body:
            Var: i;
            For (i = 0, i < 10, 1) Do
                Var: a, b, c;
                a = 5;
                b = 9;
                c = 10.0;
                a = c;
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('c'))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        input = """
        Function: main
        Body:
            Var: i;
            For (i = 0, i < 10, 1) Do
                Var: a, b, c;
                a = i;
                c = 4.5;
                a = c;
            EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('c'))))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        input = """
        Function: main
        Body:
            While (x > 0) Do
                x = x + 1;
            EndWhile.
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        input = """
        Function: main
        Body:
            Var: x;
            While (x > 0) Do
                Var: x;
                x = 1.5;
                Return x;
            EndWhile.
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        input = """
        Function: main
        Body:
            Var: x, y;
            If (y < foo(x)) Then 
                y = y + 1;
            EndIf.
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(If([(BinaryOp('<',Id('y'),CallExpr(Id('foo'),[Id('x')])),[],[Assign(Id('y'),BinaryOp('+',Id('y'),IntLiteral(1)))])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        input = """
        Function: main
        Body:
            Var: x, y;
            If (True) Then 
                y = y + 1;
            ElseIf (y < foo(x)) Then
            EndIf.
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(If([(BooleanLiteral(True),[],[Assign(Id('y'),BinaryOp('+',Id('y'),IntLiteral(1)))]),(BinaryOp('<',Id('y'),CallExpr(Id('foo'),[Id('x')])),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        input = """
        Function: main
        Body:
            Var: x, y, i;
            For (i = 0, i < 69, 1 + foo(x)) Do
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(69)),BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[Id('x')])),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_43(self):
        input = """
        Function: main
        Body:
            Var: x, y, i;
            While (y < foo(x)) Do
            EndWhile.
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(While(BinaryOp('<',Id('y'),CallExpr(Id('foo'),[Id('x')])),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        input = """
        Function: main
        Body:
            Var: x, y, i;
            Do
                x = x || y;
                x = foo(y);
            While (x)
            EndDo.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return False;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,444))
    

    def test_45(self):
        input = """
        Function: main
        Body:
            Var: x, y, i;
            For (i = 0, i < foo(x), 1) Do
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[Id('x')])),IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        input = """
        Var: arr[5] = {1, 2, 3, 4, 5};
        Function: main
        Body:
            arr = foo(1);
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: arr[5] = {5, 4, 3, 2, 1};
            Return arr;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        input = """
        Var: arr[5] = {1, 2, 3, 4, 5};
        Function: main
        Body:
            arr = foo(1);
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: arr[5] = {5, 4, 3, 2, 1};
            Return arr;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_48(self):
        input = """
        Var: arr[5] = {1, 2, 3, 4, 5};
        Function: main
        Body:
            arr[0] = foo(1)[0];
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: arr[5] = {5, 4, 3, 2, 1};
            Return arr;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('arr'),[IntLiteral(0)]),ArrayCell(CallExpr(Id('foo'),[IntLiteral(1)]),[IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self):
        input = """
        Var: arr[5] = {1, 2, 3, 4, 5};
        Function: main
        Body:
            arr[0] = foo(1)[0];
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Var: arr[5] = {5, 4, 3, 2, 1};
            Return arr;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('arr'),[IntLiteral(0)]),ArrayCell(CallExpr(Id('foo'),[IntLiteral(1)]),[IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input = """
        Var: arr[5] = {1, 2, 3, 4, 5};
        Function: foo
        Parameter: x
        Body:
            Var: arr[5] = {5, 4, 3, 2, 1};
            x = x + arr[0];
            Return arr;
        EndBody.
        Function: main
        Body:
            arr = foo(main());
            Return;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_51(self):
        input = """
        Var: arr[5] = {1, 2, 3, 4, 5};
        Function: foo
        Parameter: x
        Body:
            Var: arr[5] = {5, 4, 3, 2, 1};
            x = x + arr[0];
            Return arr;
        EndBody.
        Function: main
        Body:
            Var: x, y;
            For (x = 0, y, 2) Do
                Return y;
            EndFor.
            arr = foo(main());
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[CallExpr(Id('main'),[])])))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            x = x + foo(x, 0);
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            Return x + y;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            x = x + foo(x, 6.9);
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            Return x + int_of_float(y);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_54(self):
        input = """
        Var: arr[1][1] = {{0}};
        Function: main
        Parameter: x
        Body:
            arr = {{1}};
            Return arr[0];
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('arr'),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_55(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            a[9] = b * c;
            a = foo();
            foo()[b] = 0.;
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[Id('b')]),FloatLiteral(0.0))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_56(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            a[9] = b * c;
            a = foo();
            foo()[b] = int_of_string(string_of_float(0.));
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_57(self):
        input = """
        Var: x[9];
        Function: main
        Body:
            Var: a[10], b, c;
            a[9] = b * c;
            a = foo();
            foo()[main()] = int_of_string(string_of_float(0.));
            Return foo()[6];
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test_58(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            a[9] = b * c;
            a = foo();
            foo()[main()] = string_of_float(0.);
            Return foo()[69];
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[CallExpr(Id('main'),[])]),CallExpr(Id('string_of_float'),[FloatLiteral(0.0)]))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_59(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            While (b || (c < b)) Do
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('<',Id('c'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_60(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            While (a[0] || (c < b)) Do
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_61(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            While (a[0] || (c < b)) Do
                If True Then
                    If False Then
                        b = b - c;
                    Else
                        Do
                            b = b + c;
                        While x[0]
                        EndDo.
                    EndIf.
                EndIf.
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_62(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], b, c;
            While (a[0] || (c < b)) Do
                If True Then
                    If False Then
                        b = b - c;
                    Else
                        Do
                            a = x;
                        While True || False
                        EndDo.
                    EndIf.
                EndIf.
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_63(self):
        input = """
        Function: void
        Body:
            Return;
        EndBody.
        Function: main
        Body:
            foo();
        EndBody.
        Function: foo
        Body:
            Return void();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('void'),[]))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_64(self):
        input = """
        Function: void
        Body:
            Return;
        EndBody.
        Function: main
        Body:
            foo();
        EndBody.
        Function: foo
        Body:
            Return;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_65(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            Return main(y, x);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('main'),[Id('y'),Id('x')]))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_66(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            Return x * main(y, x);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_67(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            Return main(y, x) * x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(BinaryOp('*',CallExpr(Id('main'),[Id('y'),Id('x')]),Id('x')))))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_68(self):
        input = """
        Function: fibo
        Parameter: n
        Body:
            If n < 2 Then
                Return 1;
            EndIf.
            Return fibo(n - 1) + fibo(n - 2);
        EndBody.
        Function: main
        Parameter: n
        Body:
            Return fibo(n);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_69(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            Return main(main(1, 2), x);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_70(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            Return main(main(y, 2), x);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('main'),[CallExpr(Id('main'),[Id('y'),IntLiteral(2)]),Id('x')]))))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            Return main(1, main(y, x));
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        input = """
        Function: main
        Body:
            Var: a;
            a = foo;
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Return x + 5;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'foo'))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input = """
        Function: main
        Body:
            Var: a;
            a = 1 + foo(3.5);
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Return x + 5;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('x'),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        input = """
        Var: a;
        Function: main
        Body:
            foo();
            a = 1;
        EndBody.
        Function: foo
        Body:
            a = 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input = """
        Function: main
        Parameter: a,b,c
        Body:
            Var: d, e;
            e = main(b, main(d, c, a), a + d);
            e = 3.0;
            Return 3;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('e'),CallExpr(Id('main'),[Id('b'),CallExpr(Id('main'),[Id('d'),Id('c'),Id('a')]),BinaryOp('+',Id('a'),Id('d'))]))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input = """
        Var: a[10], b[5];
        Function: main
        Body:
            Do
                printStrLn(b[0]);
            While f(a[0]) EndDo.
        EndBody.
        Function: f
        Parameter: k
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Dowhile(([],[CallStmt(Id('printStrLn'),[ArrayCell(Id('b'),[IntLiteral(0)])])]),CallExpr(Id('f'),[ArrayCell(Id('a'),[IntLiteral(0)])]))))
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_77(self):
        input = """
        Var: a[10], b[5];
        Function: main
        Body:
            Do
                printStrLn(b[0]);
            While f(a[0]) EndDo.
        EndBody.
        Function: f
        Parameter: k
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Dowhile(([],[CallStmt(Id('printStrLn'),[ArrayCell(Id('b'),[IntLiteral(0)])])]),CallExpr(Id('f'),[ArrayCell(Id('a'),[IntLiteral(0)])]))))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = """
        Var: a[10], b[5];
        Function: f
        Parameter: k
        Body:
            k = 1;
            Return True;
        EndBody.
        Function: main
        Body:
            Do
                printStrLn(b[0]);
            While f(a[0]) EndDo.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """
        Var: a[10], b[5];
        Function: f
        Parameter: k
        Body:
            Return k;
        EndBody.
        Function: main
        Body:
            Do
                printStrLn(b[0]);
            While f(a[0]) EndDo.
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('k'))))
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """
        Function: main
        Body:
            Var: a;
            foo = a;
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Return x + 5;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'foo'))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input = """
        Function: foo
        Body:
            Return;
        EndBody.
        Function: main
        Body:
            main(foo());
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[CallExpr(Id('foo'),[])])))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input = """
        Var: a[10], b[5];
        Function: f
        Parameter: k
        Body:
            Return k && k;
        EndBody.
        Function: main
        Body:
            Do
                printStrLn(b[0]);
            While f(a[0]) EndDo.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
        Var: x[3] = {1, 2, 3};
        Function: main
        Body:
            x = {4, 5, 6};
            x = {};
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),ArrayLiteral([]))))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = """
        Var: x[3], y, z;
        Function: foo
        Body:
            x[1] = 1;
            Return x;
        EndBody.
        Function: main
        Body:
            foo()[1] = {1, 2, 3};
        EndBody.
        
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_85(self):
        input = """
        Var: a;
        Function: main
        Body:
            a = 1;
        EndBody.
        Function: foo
        Body:
            a = 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input = """
        Var: x, a, b;
        Function: main
        Parameter: x
        Body:
            Var: k;
            k = foo(1 * a - b, x || False) && k;
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
            Return test();
            Return x;
        EndBody.
        Function: test
        Body:
            x = test();
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_87(self):
        input = """
        Var: x, a, b;
        Function: main
        Body:
            Var: k;
            k = foo(1 * a - b, x *. x) && k;
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
            Return test();
            Return x;
        EndBody.
        Function: test
        Body:
            x = test();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        input = """
        Var: x, a, b;
        Function: main
        Body:
            Var: k;
            k = foo(1 * a - b, x || x) && k;
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
            Return test();
            Return x;
        EndBody.
        Function: test
        Body:
            x = test();
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        input = """
        Var: arr[10], i;
        Function: main
        Body:
            arr[i] = i;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self):
        input = """
        Var: arr[10], i;
        Function: main
        Body:
            arr[i] = i && True;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('&&',Id('i'),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_91(self):
        input = """
        Var: arr[10], i;
        Function: main
        Body:
            arr[arr[i]] = arr[arr[i]];
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        input = """
        Var: arr[10], i;
        Function: main
        Body:
            arr[main()] = arr[i];
            Return i + main();
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('arr'),[CallExpr(Id('main'),[])]),ArrayCell(Id('arr'),[Id('i')]))))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
        input = """
        Var: arr[10], i;
        Function: foo
        Body:
            If (i > 0) Then
                Return arr;
            EndIf.
        EndBody.
        Function: main
        Body:
            foo()[foo()[1]] = i;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('arr'))))
        self.assertTrue(TestChecker.test(input,expect,493))   
    
    def test_94(self):
        input = """
        Var: arr[10], i;
        Function: foo
        Body:
            If (arr[i] > 0) Then
                Return arr;
            EndIf.
        EndBody.
        Function: main
        Body:
            foo()[foo()[1]] = i;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,494)) 

    def test_95(self):
        input = """
        Var: arr[10], i;
        Function: foo
        Body:
            Do
                Return arr;
            While (arr[i] > 0)
            EndDo.
        EndBody.
        Function: main
        Body:
            foo()[foo()[1]] = i;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('arr'))))
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_96(self):
        input = """
        Var: arr[10], i;
        Function: foo
        Body:
            While (arr[i] > 0) Do
                Return arr;            
            EndWhile.
        EndBody.
        Function: main
        Body:
            foo()[foo()[1]] = i;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,496))  

    def test_97(self):
        input = """
        Var: arr[10], i;
        Function: main
        Body:
            foo()[10] = foo()[9];
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(10)]),ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(9)]))))
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_98(self):
        input = """
        Function: main
        Body:
            Var: main;
            main();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[])))
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_99(self):
        input = """
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,498))