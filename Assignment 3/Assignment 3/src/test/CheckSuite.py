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
            Var: t;
            t = 10 + foo(2);
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)])))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_case_8(self):
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
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),BinaryOp('+.',Id('t'),CallExpr(Id('factorial'),[Id('t')])))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('t'),BinaryOp('+.',Id('t'),CallExpr(Id('factorial'),[Id('t')])))))
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_case_9(self):
        """
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
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None),VarDecl(Id('a'), [5], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('a'),CallExpr(Id('get_arr'),[])),Assign(Id('t'),BinaryOp('-',ArrayCell(Id('a'),[IntLiteral(9)]),CallExpr(Id('factorial'),[Id('t')])))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_case_10(self):
        """
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
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None),VarDecl(Id('a'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),CallExpr(Id('factorial'),[ArrayCell(CallExpr(Id('get_arr'),[]),[IntLiteral(2)])]))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_case_11(self):
        """
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
            t = factorial(get_arr());
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
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None),VarDecl(Id('a'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),CallExpr(Id('factorial'),[CallExpr(Id('get_arr'),[])]))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id('factorial'),[CallExpr(Id('get_arr'),[])])))
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_case_12(self):
        """
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
            t = factorial(get_arr()[foo(2)]) + t + foo(2) + foo(get_arr()[foo(t)]);
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
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),BinaryOp('+',BinaryOp('+',BinaryOp('+',CallExpr(Id('factorial'),[ArrayCell(CallExpr(Id('get_arr'),[]),[CallExpr(Id('foo'),[IntLiteral(2)])])]),Id('t')),CallExpr(Id('foo'),[IntLiteral(2)])),CallExpr(Id('foo'),[ArrayCell(CallExpr(Id('get_arr'),[]),[CallExpr(Id('foo'),[Id('t')])])])))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_case_13(self):
        """
        Var: x, y = 12;
        Function: main
        Parameter: a[10]
        Body:
            test(12);
        EndBody.
        Function: test
        Parameter: n
        Body:
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(12)),FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None)],([],[CallStmt(Id('test'),[IntLiteral(12)])])),FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)],([],[]))])
        expect = str(TypeCannotBeInferred(CallStmt(Id('test'),[IntLiteral(12)])))
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_case_14(self):
        """
        Var: x, y = 12;
        Function: main
        Parameter: a[10]
        Body:
            x = 2 + test(12);
        EndBody.
        Function: test
        Parameter: n
        Body:
            Return n;
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(12)),FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None)],([],[Assign(Id('x'),BinaryOp('+',IntLiteral(2),CallExpr(Id('test'),[IntLiteral(12)])))])),FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)],([],[Return(Id('n'))]))])
        expect = str(TypeCannotBeInferred(Return(Id('n'))))
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_case_15(self):
        """
        Var: x, y = 12;
        Function: main
        Parameter: a[10]
        Body:
            x = 2 + test(12);
        EndBody.
        Function: test
        Parameter: n
        Body:
            n = 0x1;
            printStrLn(read());
        EndBody.
        """
        input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(12)),FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None)],([],[Assign(Id('x'),BinaryOp('+',IntLiteral(2),CallExpr(Id('test'),[IntLiteral(12)])))])),FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),IntLiteral(1)),CallStmt(Id('printStrLn'),[CallExpr(Id('read'),[])])]))])
        expect = str(TypeMismatchInExpression(BinaryOp('+',IntLiteral(2),CallExpr(Id('test'),[IntLiteral(12)]))))
        self.assertTrue(TestChecker.test(input, expect, 414))
