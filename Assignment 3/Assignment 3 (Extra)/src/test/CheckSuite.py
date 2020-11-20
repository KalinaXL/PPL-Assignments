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
        expect = str(TypeMismatchInStatement(While(Id('x'),([],[]))))
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
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
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
        expect = str(TypeCannotBeInferred(CallStmt(Id('foo'),[Id('x'),Id('y')])))
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