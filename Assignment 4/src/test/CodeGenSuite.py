import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """Function: main
    #                Body: 
    #                     print(string_of_int(120));
    #                EndBody."""
    #     expect = "120"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],([],[
    # 			CallStmt(Id("print"),[
    #                 CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    # 	expect = "120"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_case_03(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: str = "123";
    #         print(str);
    #     EndBody.
    #     """
    # 	expect = "123"
    # 	self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_case_04(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: str[2][3] = {{True, False, True}, {False, True, False}};
    #         If str[0][2] Then
    #             print(string_of_bool(str[0][0]));
    #         EndIf.
    #     EndBody.
    #     """
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_case_05(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: x = 2;
    #         x = 2 * x + foo(3);
    #         print(string_of_int(x));
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    # 	expect = "7"
    # 	self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_case_06(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: x = 2;
    #         If x == foo(3) Then
    #             print("A");
    #         ElseIf x > 2 Then
    #             print("B");
    #             x = foo(int_of_string("-423"));
    #         Else
    #             x = foo(int_of_string("-234"));
    #             print(string_of_float(float_to_int(x)));
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    # 	expect = "-234.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_case_07(self):
    # 	input = """
    #     Var: x[2] = {1, 2};
    #     Function: main
    #     Body:
    #         print(string_of_int(foo()));
    #     EndBody.
    #     Function: foo
    #     Body:
    #         x[0] = 100;
    #         Return x[0];
    #     EndBody.
    #     """
    # 	expect = "100"
    # 	self.assertTrue(TestCodeGen.test(input,expect,506))
    # def test_case_08(self):
    # 	input = """
    #     Var: x[2] = {1, 2};
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         foo()[1] = 222;
    #         print(string_of_int(foo()[1]));
    #         print(string_of_int(x[1]));
    #         print(string_of_int(x[0]));
    #     EndBody.
    #     """
    # 	expect = "2222221"
    # 	self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_case_09(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: a[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            Var: b = 1, c = 3;
            a[9] = b * c;
            a = foo();
            foo()[b] = int_of_float(0.);
            For (b = 0, b < 10, 1) Do
                print(string_of_int(a[b]));
            EndFor.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
    	expect = "0023456789"
    	self.assertTrue(TestCodeGen.test(input,expect,507))