import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body: 
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main  
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))
    # def test_case_7(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("no_main"),[],([VarDecl(Id('main'), [], None)],[
    #                 CallStmt(Id("printStrLn"),[StringLiteral("Hello World")])]))])
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input,expect,406))
    # def test_case_8(self):
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(Id('i'),([],[]))]))])
    #     expect = str(Undeclared(Identifier(), 'i'))
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    # def test_case_9(self):
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(Id('x'),([],[]))]))])
    #     expect = str(TypeMismatchInStatement(While(Id('x'),([],[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    # def test_case_10(self):
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(BinaryOp('==',Id('y'),IntLiteral(2)),([VarDecl(Id('x'), [],IntLiteral(2)),VarDecl(Id('x'), [], None)],[]))]))])
    #     expect = str(Redeclared(Variable(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    # def test_case_11(self):
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([],[While(BinaryOp('==',Id('y'),IntLiteral(2)),([VarDecl(Id('i'), [], IntLiteral(1))],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(2)),Id('y'), ([],[Break()])),Break()]))]))])
    #     expect = str(UnreachableStatement(Break()))
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    # def test_case_12(self):
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])]))],[]))])
    #     expect = str(InvalidArrayLiteral(ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])))
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    # def test_case_13(self):
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [],IntLiteral(2)),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])]))],[]))])
    #     expect = str(InvalidArrayLiteral(ArrayLiteral([FloatLiteral(2.2),IntLiteral(3)])))
    #     self.assertTrue(TestChecker.test(input, expect, 412))
    # def test_case_14(self):
    #     """
    #     Var: x, y;
    #     Function: main
    #     Body:
    #         x = 2 - 3 * y \ 5;
    #         While (y == 0o23) Do
    #             Var: k = "string";
    #             k = x;
    #         EndWhile.
    #     EndBody.
    #     """
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('\\',BinaryOp('*',IntLiteral(3),Id('y')),IntLiteral(5)))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[Assign(Id('k'),Id('x'))]))]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('k'),Id('x'))))
    #     self.assertTrue(TestChecker.test(input, expect, 413))
    # def test_case_15(self):
        # input = """
        # Var: x, y;
        # Function: foo
        # Body:
        # EndBody.
        # Function: main
        # Body:
        #     x = 2 - 3 * y \ 5;
        #     While (y == 0o23) Do
        #         Var: k = "string";
        #         Continue;
        #     EndWhile.
        # EndBody.
        # """
        # input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [],([],[])),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('\\',BinaryOp('*',IntLiteral(3),Id('y')),IntLiteral(5)))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[Continue()]))]))])
        # expect = str(UnreachableFunction('foo'))
        # self.assertTrue(TestChecker.test(input, expect, 414))
    # def test_case_16(self):
    #     """
    #     Var: x, y;
    #     Function: main
    #     Body:
    #         x = 2 - 3 * y;
    #         While (y == 0o23) Do
    #             Var: k = "string";
    #             If x == y Then
    #                 If x == 3 Then
    #                 ElseIf y == 4 Then
    #                     Break;
    #                     x = y;
    #                 EndIf.
    #             EndIf.
    #         EndWhile.
    #     EndBody.
    #     """
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('*',IntLiteral(3),Id('y')))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[If([(BinaryOp('==',Id('x'),Id('y')),[],[If([(BinaryOp('==',Id('x'),IntLiteral(3)),[],[]),(BinaryOp('==',Id('y'),IntLiteral(4)),[],[Break(),Assign(Id('x'),Id('y'))])], ([],[]))])], ([],[]))]))]))])
    #     expect = str(UnreachableStatement(Assign(Id('x'),Id('y'))))
    #     self.assertTrue(TestChecker.test(input, expect, 415))
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
        expect = str(UnreachableStatement(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 415))
