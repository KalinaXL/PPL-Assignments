# import unittest
# from TestUtils import TestChecker
# from StaticError import *
# from AST import *

# class CheckSuite(unittest.TestCase):

#     def test_undeclared_function(self):
#         """Simple program: main"""
#         input = """Function: main
#                    Body: 
#                         foo();
#                    EndBody."""
#         expect = str(Undeclared(Function(),"foo"))
#         self.assertTrue(TestChecker.test(input,expect,400))

#     def test_diff_numofparam_stmt(self):
#         """Complex program"""
#         input = """Function: main  
#                    Body:
#                         printStrLn();
#                     EndBody."""
#         expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
#         self.assertTrue(TestChecker.test(input,expect,401))
    
#     def test_diff_numofparam_expr(self):
#         """More complex program"""
#         input = """Function: main 
#                     Body:
#                         printStrLn(read(4));
#                     EndBody."""
#         expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
#         self.assertTrue(TestChecker.test(input,expect,402))

#     def test_undeclared_function_use_ast(self):
#         """Simple program: main """
#         input = Program([FuncDecl(Id("main"),[],([],[
#             CallExpr(Id("foo"),[])]))])
#         expect = str(Undeclared(Function(),"foo"))
#         self.assertTrue(TestChecker.test(input,expect,403))

#     def test_diff_numofparam_expr_use_ast(self):
#         """More complex program"""
#         input = Program([
#                 FuncDecl(Id("main"),[],([],[
#                     CallStmt(Id("printStrLn"),[
#                         CallExpr(Id("read"),[IntLiteral(4)])
#                         ])]))])
#         expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
#         self.assertTrue(TestChecker.test(input,expect,404))

#     def test_diff_numofparam_stmt_use_ast(self):
#         """Complex program"""
#         input = Program([
#                 FuncDecl(Id("main"),[],([],[
#                     CallStmt(Id("printStrLn"),[])]))])
#         expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
#         self.assertTrue(TestChecker.test(input,expect,405))
#     def test_case_7(self):
#         """
#         Var: x, y;
#         Function: foo
#         Parameter: n
#         Body:
#             n = 10 * 2 - 1;
#             Return n;
#         EndBody.
#         Function: main
#         Body:
#             Var: t;
#             t = 10 + foo(2);
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)])))]))])
#         expect = str()
#         self.assertTrue(TestChecker.test(input, expect, 406))
#     def test_case_8(self):
#         """
#         Var: x, y;
#         Function: foo
#         Parameter: n
#         Body:
#             n = 10 * 2 - 1;
#             Return n;
#         EndBody.
#         Function: main
#         Body:
#             Var: t;
#             t = 10 + foo(2);
#             t = t +. factorial(t);
#         EndBody.
#         Function: factorial
#         Parameter: n
#         Body:
#             If (n == 0) || (n == 1) Then
#                 Return 1;
#             EndIf.
#             Return n * factorial(n - 1);
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),BinaryOp('+.',Id('t'),CallExpr(Id('factorial'),[Id('t')])))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])
#         expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('t'),CallExpr(Id('factorial'),[Id('t')]))))
#         self.assertTrue(TestChecker.test(input, expect, 407))
#     def test_case_9(self):
#         """
#         Var: x, y, arr[5];
#         Function: foo
#         Parameter: n
#         Body:
#             n = 10 * 2 - 1;
#             Return n;
#         EndBody.
#         Function: main
#         Body:
#             Var: t, a[5];
#             t = 10 + foo(2);
#             a = get_arr();
#             t = a[9] - factorial(t);
#         EndBody.
#         Function: factorial
#         Parameter: n
#         Body:
#             If (n == 0) || (n == 1) Then
#                 Return 1;
#             EndIf.
#             Return n * factorial(n - 1);
#         EndBody.
#         Function: get_arr
#         Body:
#             arr = {1, 2, 3, 4, 5};
#             Return arr;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None),VarDecl(Id('a'), [5], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('a'),CallExpr(Id('get_arr'),[])),Assign(Id('t'),BinaryOp('-',ArrayCell(Id('a'),[IntLiteral(9)]),CallExpr(Id('factorial'),[Id('t')])))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
#         expect = str()
#         self.assertTrue(TestChecker.test(input, expect, 408))
#     def test_case_10(self):
#         """
#         Var: x, y, arr[5];
#         Function: foo
#         Parameter: n
#         Body:
#             n = 10 * 2 - 1;
#             Return n;
#         EndBody.
#         Function: main
#         Body:
#             Var: t, a;
#             t = 10 + foo(2);
#             t = factorial(get_arr()[2]);
#         EndBody.
#         Function: factorial
#         Parameter: n
#         Body:
#             If (n == 0) || (n == 1) Then
#                 Return 1;
#             EndIf.
#             Return n * factorial(n - 1);
#         EndBody.
#         Function: get_arr
#         Body:
#             arr = {1, 2, 3, 4, 5};
#             Return arr;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None),VarDecl(Id('a'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),CallExpr(Id('factorial'),[ArrayCell(CallExpr(Id('get_arr'),[]),[IntLiteral(2)])]))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
#         expect = str()
#         self.assertTrue(TestChecker.test(input, expect, 409))
#     def test_case_11(self):
#         """
#         Var: x, y, arr[5];
#         Function: foo
#         Parameter: n
#         Body:
#             n = 10 * 2 - 1;
#             Return n;
#         EndBody.
#         Function: main
#         Body:
#             Var: t, a;
#             t = 10 + foo(2);
#             t = factorial(get_arr());
#         EndBody.
#         Function: factorial
#         Parameter: n
#         Body:
#             If (n == 0) || (n == 1) Then
#                 Return 1;
#             EndIf.
#             Return n * factorial(n - 1);
#         EndBody.
#         Function: get_arr
#         Body:
#             arr = {1, 2, 3, 4, 5};
#             Return arr;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None),VarDecl(Id('a'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),CallExpr(Id('factorial'),[CallExpr(Id('get_arr'),[])]))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
#         expect = str(TypeMismatchInExpression(CallExpr(Id('factorial'),[CallExpr(Id('get_arr'),[])])))
#         self.assertTrue(TestChecker.test(input, expect, 410))
#     def test_case_12(self):
#         """
#         Var: x, y, arr[5];
#         Function: foo
#         Parameter: n
#         Body:
#             n = 10 * 2 - 1;
#             Return n;
#         EndBody.
#         Function: main
#         Body:
#             Var: t;
#             t = 10 + foo(2);
#             t = factorial(get_arr()[foo(2)]) + t + foo(2) + foo(get_arr()[foo(t)]);
#         EndBody.
#         Function: factorial
#         Parameter: n
#         Body:
#             If (n == 0) || (n == 1) Then
#                 Return 1;
#             EndIf.
#             Return n * factorial(n - 1);
#         EndBody.
#         Function: get_arr
#         Body:
#             arr = {1, 2, 3, 4, 5};
#             Return arr;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),VarDecl(Id('arr'), [5], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('t'), [], None)],[Assign(Id('t'),BinaryOp('+',IntLiteral(10),CallExpr(Id('foo'),[IntLiteral(2)]))),Assign(Id('t'),BinaryOp('+',BinaryOp('+',BinaryOp('+',CallExpr(Id('factorial'),[ArrayCell(CallExpr(Id('get_arr'),[]),[CallExpr(Id('foo'),[IntLiteral(2)])])]),Id('t')),CallExpr(Id('foo'),[IntLiteral(2)])),CallExpr(Id('foo'),[ArrayCell(CallExpr(Id('get_arr'),[]),[CallExpr(Id('foo'),[Id('t')])])])))])),FuncDecl(Id('factorial'), [VarDecl(Id('n'), [], None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('n'),IntLiteral(0)),BinaryOp('==',Id('n'),IntLiteral(1))),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('*',Id('n'),CallExpr(Id('factorial'),[BinaryOp('-',Id('n'),IntLiteral(1))])))])),FuncDecl(Id('get_arr'), [],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Return(Id('arr'))]))])
#         expect = str()
#         self.assertTrue(TestChecker.test(input, expect, 411))
#     def test_case_13(self):
#         """
#         Var: x, y = 12;
#         Function: main
#         Parameter: a[10]
#         Body:
#             test(12);
#         EndBody.
#         Function: test
#         Parameter: n
#         Body:
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(12)),FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None)],([],[CallStmt(Id('test'),[IntLiteral(12)])])),FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)],([],[]))])
#         expect = str(TypeCannotBeInferred(CallStmt(Id('test'),[IntLiteral(12)])))
#         self.assertTrue(TestChecker.test(input, expect, 412))
#     def test_case_14(self):
#         """
#         Var: x, y = 12;
#         Function: main
#         Parameter: a[10]
#         Body:
#             x = 2 + test(12);
#         EndBody.
#         Function: test
#         Parameter: n
#         Body:
#             Return n;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(12)),FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None)],([],[Assign(Id('x'),BinaryOp('+',IntLiteral(2),CallExpr(Id('test'),[IntLiteral(12)])))])),FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)],([],[Return(Id('n'))]))])
#         expect = str(TypeCannotBeInferred(Return(Id('n'))))
#         self.assertTrue(TestChecker.test(input, expect, 413))
#     def test_case_15(self):
#         """
#         Var: x, y = 12;
#         Function: main
#         Parameter: a[10]
#         Body:
#             x = 2 + test(12);
#         EndBody.
#         Function: test
#         Parameter: n
#         Body:
#             n = 0x1;
#             printStrLn(read());
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(12)),FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None)],([],[Assign(Id('x'),BinaryOp('+',IntLiteral(2),CallExpr(Id('test'),[IntLiteral(12)])))])),FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),IntLiteral(1)),CallStmt(Id('printStrLn'),[CallExpr(Id('read'),[])])]))])
#         expect = str(TypeMismatchInExpression(BinaryOp('+',IntLiteral(2),CallExpr(Id('test'),[IntLiteral(12)]))))
#         self.assertTrue(TestChecker.test(input, expect, 414))
#     def test_case_16(self):
#         """
#         Var: x, y = "s", t;
#         Function: main
#         Body:
#             test(2);
#         EndBody.
#         Function: test
#         Parameter: k
#         Body:
#             Return k + 1;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],StringLiteral("""s""")),VarDecl(Id('t'), [], None),FuncDecl(Id('main'), [],([],[CallStmt(Id('test'),[IntLiteral(2)])])),FuncDecl(Id('test'), [VarDecl(Id('k'), [], None)],([],[Return(BinaryOp('+',Id('k'),IntLiteral(1)))]))])
#         expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[IntLiteral(2)])))
#         self.assertTrue(TestChecker.test(input, expect, 415))
#     def test_case_17(self):
#         """
#         Var: x, y = "s", t, arr[10];
#         Function: main
#         Body:
#             x = 1;
#             t = x + foo(x);
#         EndBody.
#         Function: foo
#         Parameter: x
#         Body:
#             Return 1;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],StringLiteral("""s""")),VarDecl(Id('t'), [], None),VarDecl(Id('arr'), [10], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),IntLiteral(1)),Assign(Id('t'),BinaryOp('+',Id('x'),CallExpr(Id('foo'),[Id('x')])))])),FuncDecl(Id('foo'), [VarDecl(Id('x'), [], None)],([],[Return(IntLiteral(1))]))])
#         expect = str(TypeCannotBeInferred(Assign(Id('t'),BinaryOp('+',Id('x'),CallExpr(Id('foo'),[Id('x')])))))
#         self.assertTrue(TestChecker.test(input, expect, 416))
#     def test_case_18(self):
#         """
#         Var: x[10];
#         Function: main
#         Body:
#             test()[0] = 1;A
#             test()[1] = "s";
#         EndBody.
#         Function: test
#         Body:
#             Return x;
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [10], None),FuncDecl(Id('main'), [],([],[Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(0)]),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(1)]),StringLiteral("""s"""))])),FuncDecl(Id('test'), [],([],[Return(Id('x'))]))])
#         expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(1)]),StringLiteral("""s"""))))
#         self.assertTrue(TestChecker.test(input, expect, 417))
#     def test_case_19(self):
#         """
#         Var: x[10];
#         Function: main
#         Body:
#             x[0] = 1;
#             x[1] = "s";
#         EndBody.
#         """
#         input = Program([VarDecl(Id('x'), [10], None),FuncDecl(Id('main'), [],([],[Assign(ArrayCell(Id('x'),[IntLiteral(0)]),IntLiteral(1)),Assign(ArrayCell(Id('x'),[IntLiteral(1)]),StringLiteral("""s"""))]))])
#         expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(1)]),StringLiteral("""s"""))))
#         self.assertTrue(TestChecker.test(input, expect, 418))
#     def test_case_20(self):
#         input = """
#         Var: x[10];
#         Function: main
#         Body:
#             test();
#         EndBody.
#         Function: test
#         Parameter: arr[12][3]
#         Body:
#             arr[0] = {1, 2, 3};
#         EndBody.
#         """
#         expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[])))
#         self.assertTrue(TestChecker.test(input, expect, 419))
#     def test_case_21(self):
#         input = """
#         Var: x[10];
#         Function: main
#         Body:
#             test();
#         EndBody.
#         Function: test
#         Parameter: arr[12]
#         Body:
#             Return 1;
#         EndBody.
#         Function: test
#         Body:
#         EndBody.
#         """
#         expect = str(Redeclared(Function(), 'test'))
#         self.assertTrue(TestChecker.test(input, expect, 420))
#     def test_case_22(self):
#         input = """
#         Function: foo
#         Parameter: x,y
#         Body:
#             x = 1;
#             foo(1, 0);
#         EndBody.
#         Function: main
#         Body:
#         EndBody.
#         """
#         expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[FloatLiteral(1.1),IntLiteral(0)])))
#         self.assertTrue(TestChecker.test(input, expect, 421))
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