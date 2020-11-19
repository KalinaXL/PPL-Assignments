import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
	def test_ast_000(self):
		input = """
		Var: x = 1; 
		Function: main 
		Body: 
			s = "abcdef"; 
			print("Hello World"); 
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),FuncDecl(Id("main"),[],([],[Assign(Id("s"),StringLiteral("abcdef")),CallStmt(Id("print"),[StringLiteral("Hello World")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,0))

	def test_ast_001(self):
		input = """
		Var: x[2][3] = {{1e3,0xFF,0o17},{"a","b","c"}};
		"""
		expect = Program([VarDecl(Id("x"),[2,3],ArrayLiteral([ArrayLiteral([FloatLiteral(1000.0),IntLiteral(255),IntLiteral(15)]),ArrayLiteral([StringLiteral("a"),StringLiteral("b"),StringLiteral("c")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,1))

	def test_ast_002(self):
		input = """
		Var: x,y,z,t,q = 1;
		"""
		expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],None),VarDecl(Id("q"),[],IntLiteral(1))])

		self.assertTrue(TestAST.checkASTGen(input,expect,2))

	def test_ast_003(self):
		input = """
		Var: x = 1; 
		Function: main 
		Body: 
			s = "abcdef"; 
			print("Hello World"); 
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),FuncDecl(Id("main"),[],([],[Assign(Id("s"),StringLiteral("abcdef")),CallStmt(Id("print"),[StringLiteral("Hello World")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,3))

	def test_ast_004(self):
		input = """
		Function: main
		Parameter: a,b,c
		Body:
			a = a + 1; **Comment**
			print(a);
			If (a>0) Then print("a>0");
				ElseIf a>-5 Then print("a>-5");
			Else print("a<=-5");
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[Assign(Id("a"),BinaryOp('+',Id("a"),IntLiteral(1))),CallStmt(Id("print"),[Id("a")]),If([(BinaryOp('>',Id("a"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("a>0")])]),(BinaryOp('>',Id("a"),UnaryOp('-',IntLiteral(5))),[],[CallStmt(Id("print"),[StringLiteral("a>-5")])])], ([],[CallStmt(Id("print"),[StringLiteral("a<=-5")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,4))

	def test_ast_005(self):
		input = """
		Var: x = "init"; 
		Function: main 
		Parameter: x
		Body: 
			s = 0;
			For (x = 1, x>1, 2) Do
				s = s + foo(x);
			EndFor. 
			print("Solution: ");
			print(s);
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],StringLiteral("init")),FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("s"),IntLiteral(0)),For(Id("x"),IntLiteral(1),BinaryOp('>',Id("x"),IntLiteral(1)),IntLiteral(2),([],[Assign(Id("s"),BinaryOp('+',Id("s"),CallExpr(Id("foo"),[Id("x")])))])),CallStmt(Id("print"),[StringLiteral("Solution: ")]),CallStmt(Id("print"),[Id("s")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,5))

	def test_ast_006(self):
		input = """
		Function: main
		Body:
			**Empty program**
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,6))

	def test_ast_007(self):
		input = """
		Function: main
		Parameter: x
		Body:
			Var: a[5],b,c=9,d;
			a[3+foo(2)] = a[x[2][3]] + 4;
			For (b=0,b<c,b+1) Do
				d = d + 1;
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(9)),VarDecl(Id("d"),[],None)],[Assign(ArrayCell(Id("a"),[BinaryOp('+',IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id("a"),[ArrayCell(Id("x"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),For(Id("b"),IntLiteral(0),BinaryOp('<',Id("b"),Id("c")),BinaryOp('+',Id("b"),IntLiteral(1)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1)))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,7))

	def test_ast_008(self):
		input = """
		Function: main
		Body:
			Var: a,b=9,c;
			a = b*b;
			If (a>b) Then print("|b|>1");
			Else print("0<=|b|<=1");
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(9)),VarDecl(Id("c"),[],None)],[Assign(Id("a"),BinaryOp('*',Id("b"),Id("b"))),If([(BinaryOp('>',Id("a"),Id("b")),[],[CallStmt(Id("print"),[StringLiteral("|b|>1")])])], ([],[CallStmt(Id("print"),[StringLiteral("0<=|b|<=1")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,8))

	def test_ast_009(self):
		input = """
		Function: isPrimeNumber
		Parameter: x
		Body:
			Var: i;
			If (x<2) Then 
				Return False;
			EndIf.
			For (i = 2,i<x-1,i+1) Do
				If (x%i==0) Then 
					Return False;
				EndIf.
			EndFor.
			Return True;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("isPrimeNumber"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("i"),[],None)],[If([(BinaryOp('<',Id("x"),IntLiteral(2)),[],[Return(BooleanLiteral(False))])], ([],[])),For(Id("i"),IntLiteral(2),BinaryOp('<',Id("i"),BinaryOp('-',Id("x"),IntLiteral(1))),BinaryOp('+',Id("i"),IntLiteral(1)),([],[If([(BinaryOp('==',BinaryOp('%',Id("x"),Id("i")),IntLiteral(0)),[],[Return(BooleanLiteral(False))])], ([],[]))])),Return(BooleanLiteral(True))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,9))

	def test_ast_010(self):
		input = """
		Function: fibo
		Parameter: n
		Body:
			Var: fibo_list[100],i;

			If n<2 Then 
				Return 1;
			EndIf.
			
			fibo_list[0] = 1;
			fibo_list[1] = 1;
			For (i = 2, i<=n, i+1) Do
				fibo_list[i] = fibo_list[i-1] + fibo_list[i-2];
			EndFor.
			Return fibo_list[n];
		EndBody.
		"""
		expect = Program([FuncDecl(Id("fibo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("fibo_list"),[100],None),VarDecl(Id("i"),[],None)],[If([(BinaryOp('<',Id("n"),IntLiteral(2)),[],[Return(IntLiteral(1))])], ([],[])),Assign(ArrayCell(Id("fibo_list"),[IntLiteral(0)]),IntLiteral(1)),Assign(ArrayCell(Id("fibo_list"),[IntLiteral(1)]),IntLiteral(1)),For(Id("i"),IntLiteral(2),BinaryOp('<=',Id("i"),Id("n")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(ArrayCell(Id("fibo_list"),[Id("i")]),BinaryOp('+',ArrayCell(Id("fibo_list"),[BinaryOp('-',Id("i"),IntLiteral(1))]),ArrayCell(Id("fibo_list"),[BinaryOp('-',Id("i"),IntLiteral(2))])))])),Return(ArrayCell(Id("fibo_list"),[Id("n")]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,10))

	def test_ast_011(self):
		input = """
		Function: factor
		Parameter: x
		Body:
			Var: t = 1, i;
			For (i = 1, i <= x, i + 1) Do
				t = t * i;
			EndFor.
			Return t;
		EndBody.

		Function: main
		Body:
			print(factor(10));
		EndBody.		
		"""
		expect = Program([FuncDecl(Id("factor"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("t"),[],IntLiteral(1)),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(1),BinaryOp('<=',Id("i"),Id("x")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(Id("t"),BinaryOp('*',Id("t"),Id("i")))])),Return(Id("t"))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("factor"),[IntLiteral(10)])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,11))

	def test_ast_012(self):
		input = """
		Function: sort
		Parameter: a,n
		Body:
			Var: i,j;
			For (i = 0, i < n-1, i + 1) Do
				For (j = i + 1, j < n, j + 1 ) Do
					If a[i] > a[j] Then 
						Var: t;
						t = a[i];
						a[i] = a[j];
						a[j] = t;
					EndIf.
				EndFor.
			EndFor.
			Return 1;
		EndBody.

		Function: main
		Body:
			Var: arr[10] = {1,2,0,4,3,5,7,4,8,9};
			sort(arr);
		EndBody.
		"""
		expect = Program([FuncDecl(Id("sort"),[VarDecl(Id("a"),[],None),VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),BinaryOp('-',Id("n"),IntLiteral(1))),BinaryOp('+',Id("i"),IntLiteral(1)),([],[For(Id("j"),BinaryOp('+',Id("i"),IntLiteral(1)),BinaryOp('<',Id("j"),Id("n")),BinaryOp('+',Id("j"),IntLiteral(1)),([],[If([(BinaryOp('>',ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[Id("j")])),[VarDecl(Id("t"),[],None)],[Assign(Id("t"),ArrayCell(Id("a"),[Id("i")])),Assign(ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[Id("j")])),Assign(ArrayCell(Id("a"),[Id("j")]),Id("t"))])], ([],[]))]))])),Return(IntLiteral(1))])),FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(0),IntLiteral(4),IntLiteral(3),IntLiteral(5),IntLiteral(7),IntLiteral(4),IntLiteral(8),IntLiteral(9)]))],[CallStmt(Id("sort"),[Id("arr")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,12))

	def test_ast_013(self):
		input = """
		Function: main
		Body:
			**Don't care about position of Break and Continue**
			Var: a = 10,b,c,i;
			For (i = 0, i < a, i + 1 ) Do
				If (b != 0) Then foo(c);
				Else Break;		**valid**
				EndIf.
			EndFor.
			
			If (i == a-1) Then Break;  **invalid**
			Else Continue;			   **invalid**
			EndIf.

		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),Id("a")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[If([(BinaryOp('!=',Id("b"),IntLiteral(0)),[],[CallStmt(Id("foo"),[Id("c")])])], ([],[Break()]))])),If([(BinaryOp('==',Id("i"),BinaryOp('-',Id("a"),IntLiteral(1))),[],[Break()])], ([],[Continue()]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,13))

	def test_ast_014(self):
		input = """
		Function: recur_fibo
		Parameter: n
		Body:
			If n<2 Then 
				Return 1;
			EndIf.
			Return recur_fibo(n-1) + recur_fibo(n-2);
		EndBody.
		"""
		expect = Program([FuncDecl(Id("recur_fibo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp('<',Id("n"),IntLiteral(2)),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('+',CallExpr(Id("recur_fibo"),[BinaryOp('-',Id("n"),IntLiteral(1))]),CallExpr(Id("recur_fibo"),[BinaryOp('-',Id("n"),IntLiteral(2))])))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,14))

	def test_ast_015(self):
		input = """
		Function: main
		Body:
			**test Do While statement**
			Var: x = 10,y,i = 0;
			Do
				print(i);
				i = i + 1;
			While (i < x)
			EndDo.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],None),VarDecl(Id("i"),[],IntLiteral(0))],[Dowhile(([],[CallStmt(Id("print"),[Id("i")]),Assign(Id("i"),BinaryOp('+',Id("i"),IntLiteral(1)))]),BinaryOp('<',Id("i"),Id("x")))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,15))

	def test_ast_016(self):
		input = """
		** Empty array **
		Var: a[2] = {};
		"""
		expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,16))

	def test_ast_017(self):
		input = """
		Function: main
		Body:
			**do something with array**
			Var: a[2][3] = {{1,2,3},{4,5,6}};
			Var: key = 2;
			a[1][1] = 1;

			If (a[2][4] < key) 			**Ignore out of range**
				Then printLn("2-4");  
			ElseIf (a[1-1][0] < key) Then 
				printLn("0-0");
			ElseIf (a[1][key*2 - 1] < key) Then 
				printLn("1-2");
			Else 
				printLn("NOT FOUND");
			EndIf.

		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("key"),[],IntLiteral(2))],[Assign(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1)]),IntLiteral(1)),If([(BinaryOp('<',ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(4)]),Id("key")),[],[CallStmt(Id("printLn"),[StringLiteral("2-4")])]),(BinaryOp('<',ArrayCell(Id("a"),[BinaryOp('-',IntLiteral(1),IntLiteral(1)),IntLiteral(0)]),Id("key")),[],[CallStmt(Id("printLn"),[StringLiteral("0-0")])]),(BinaryOp('<',ArrayCell(Id("a"),[IntLiteral(1),BinaryOp('-',BinaryOp('*',Id("key"),IntLiteral(2)),IntLiteral(1))]),Id("key")),[],[CallStmt(Id("printLn"),[StringLiteral("1-2")])])], ([],[CallStmt(Id("printLn"),[StringLiteral("NOT FOUND")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,17))

	def test_ast_018(self):
		input = """
		Function: main
		Body:
			Var: str;
			print("Nhap chuoi: ");
			str = read();
			print("Chuoi da nhap: ");
			printLn(str);
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("str"),[],None)],[CallStmt(Id("print"),[StringLiteral("Nhap chuoi: ")]),Assign(Id("str"),CallExpr(Id("read"),[])),CallStmt(Id("print"),[StringLiteral("Chuoi da nhap: ")]),CallStmt(Id("printLn"),[Id("str")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,18))

	def test_ast_019(self):
		input = """
		Var: x = 100;
		Function: main
		Body:
			Var: arr[3] = {10,50,90,3,100,7,6,5,5,5};
			print("Initial:");
			printArr(arr);
			sort(arr,6 \\ 2 * 3 + 1);
			print("Sorted:");
			printArr(arr);
		EndBody.

		Function: sort
		Parameter: arr
		Body:
			** Do something **
		EndBody. 
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(100)),FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(10),IntLiteral(50),IntLiteral(90),IntLiteral(3),IntLiteral(100),IntLiteral(7),IntLiteral(6),IntLiteral(5),IntLiteral(5),IntLiteral(5)]))],[CallStmt(Id("print"),[StringLiteral("Initial:")]),CallStmt(Id("printArr"),[Id("arr")]),CallStmt(Id("sort"),[Id("arr"),BinaryOp('+',BinaryOp('*',BinaryOp('\\',IntLiteral(6),IntLiteral(2)),IntLiteral(3)),IntLiteral(1))]),CallStmt(Id("print"),[StringLiteral("Sorted:")]),CallStmt(Id("printArr"),[Id("arr")])])),FuncDecl(Id("sort"),[VarDecl(Id("arr"),[],None)],([],[]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,19))

	def test_ast_020(self):
		input = """
		Function: main
		Body:
			Var: n = 100;
			printLn("This program is missing a dot");
			If isPrime(n) == True Then
				print("Is a prime number");
			Else
				print("Is not a prime number");
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("n"),[],IntLiteral(100))],[CallStmt(Id("printLn"),[StringLiteral("This program is missing a dot")]),If([(BinaryOp('==',CallExpr(Id("isPrime"),[Id("n")]),BooleanLiteral(True)),[],[CallStmt(Id("print"),[StringLiteral("Is a prime number")])])], ([],[CallStmt(Id("print"),[StringLiteral("Is not a prime number")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,20))

	def test_ast_021(self):
		input = """
		Function: myEmotion
		Body:
			goodMorning();
			
			str = read();
			doSomething(str);
			
			n = randInt();
			If n % 2 == 0 Then
				angry();
			ElseIf n > 10 Then
				happy();
			Else
				normal();
			EndIf.
		EndBody.

		Function: goodMorning
		Body:
			**do something**
		EndBody.

		Function: doSomething
		Parameter: str
		Body:
			**do something**
		EndBody.

		Function: randInt
		Body:
			**do something**
		EndBody.
		"""
		expect = Program([FuncDecl(Id("myEmotion"),[],([],[CallStmt(Id("goodMorning"),[]),Assign(Id("str"),CallExpr(Id("read"),[])),CallStmt(Id("doSomething"),[Id("str")]),Assign(Id("n"),CallExpr(Id("randInt"),[])),If([(BinaryOp('==',BinaryOp('%',Id("n"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("angry"),[])]),(BinaryOp('>',Id("n"),IntLiteral(10)),[],[CallStmt(Id("happy"),[])])], ([],[CallStmt(Id("normal"),[])]))])),FuncDecl(Id("goodMorning"),[],([],[])),FuncDecl(Id("doSomething"),[VarDecl(Id("str"),[],None)],([],[])),FuncDecl(Id("randInt"),[],([],[]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,21))

	def test_ast_022(self):
		input = """
		Function: main
		Body:
			Var: arr[10], i;
			For (i = 0, i < 10, i + 1) Do
				arr[i] = randInt();
			EndFor.
			sort(arr);
			printArr(arr);
		EndBody.

		Function: sort
		Parameter: arr
		Body:
			Var: n;
			n = randInt();
			If (n == 0) Then
				quickSort(arr);
			ElseIf (n == 1) Then
				mergeSort(arr);
			ElseIf (n == 2) Then
				bubbleSort(arr);
			ElseIf (n == 3) Then
				heapSort(arr);
			ElseIf (n == 4) Then
				insertionSort(arr);
			ElseIf (n == 5) Then
				selectionSort(arr);
			Else 
				mixSort(arr);
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10],None),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(ArrayCell(Id("arr"),[Id("i")]),CallExpr(Id("randInt"),[]))])),CallStmt(Id("sort"),[Id("arr")]),CallStmt(Id("printArr"),[Id("arr")])])),FuncDecl(Id("sort"),[VarDecl(Id("arr"),[],None)],([VarDecl(Id("n"),[],None)],[Assign(Id("n"),CallExpr(Id("randInt"),[])),If([(BinaryOp('==',Id("n"),IntLiteral(0)),[],[CallStmt(Id("quickSort"),[Id("arr")])]),(BinaryOp('==',Id("n"),IntLiteral(1)),[],[CallStmt(Id("mergeSort"),[Id("arr")])]),(BinaryOp('==',Id("n"),IntLiteral(2)),[],[CallStmt(Id("bubbleSort"),[Id("arr")])]),(BinaryOp('==',Id("n"),IntLiteral(3)),[],[CallStmt(Id("heapSort"),[Id("arr")])]),(BinaryOp('==',Id("n"),IntLiteral(4)),[],[CallStmt(Id("insertionSort"),[Id("arr")])]),(BinaryOp('==',Id("n"),IntLiteral(5)),[],[CallStmt(Id("selectionSort"),[Id("arr")])])], ([],[CallStmt(Id("mixSort"),[Id("arr")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,22))

	def test_ast_023(self):
		input = """
		Function: main
		Body:
			Var: arr[10] = {0,1,3,2,4,5,6,5,1,0};
			Var: key,i,isExist = False;
			key = int_of_string(read());
			For (i = 0, i < 10, i + 1) Do
				If arr[i] == key Then
					print("index of key is ");
					print(i);
					isExist = True;
					Break;
				EndIf.
			EndFor.
			If isExist == False Then
				print("key is not found");
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10],ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(3),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(5),IntLiteral(1),IntLiteral(0)])),VarDecl(Id("key"),[],None),VarDecl(Id("i"),[],None),VarDecl(Id("isExist"),[],BooleanLiteral(False))],[Assign(Id("key"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[If([(BinaryOp('==',ArrayCell(Id("arr"),[Id("i")]),Id("key")),[],[CallStmt(Id("print"),[StringLiteral("index of key is ")]),CallStmt(Id("print"),[Id("i")]),Assign(Id("isExist"),BooleanLiteral(True)),Break()])], ([],[]))])),If([(BinaryOp('==',Id("isExist"),BooleanLiteral(False)),[],[CallStmt(Id("print"),[StringLiteral("key is not found")])])], ([],[]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,23))

	def test_ast_024(self):
		input = """
		Function: main
		Body:
			Var: arr[10] = {0,1,3,2,4,5,6,5,1,0};
			Var: min,max,iMin = 0, iMax = 0, i;
			min = arr[0]; max = arr[0];
			For (i = 9, i >= 0, i-1) Do
				If arr[i] < min Then
					min = arr[i];
					iMin = i;
				EndIf.
				If arr[i] > max Then
					max = arr[i];
					iMax = i;
				EndIf.
			EndFor.
			print("Min = "); print(string_of_int(min)); print(" at index = "); printLn(string_of_int(iMin));
			print("Max = "); print(string_of_int(max)); print(" at index = "); printLn(string_of_int(iMax));
			Return 0;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10],ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(3),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(5),IntLiteral(1),IntLiteral(0)])),VarDecl(Id("min"),[],None),VarDecl(Id("max"),[],None),VarDecl(Id("iMin"),[],IntLiteral(0)),VarDecl(Id("iMax"),[],IntLiteral(0)),VarDecl(Id("i"),[],None)],[Assign(Id("min"),ArrayCell(Id("arr"),[IntLiteral(0)])),Assign(Id("max"),ArrayCell(Id("arr"),[IntLiteral(0)])),For(Id("i"),IntLiteral(9),BinaryOp('>=',Id("i"),IntLiteral(0)),BinaryOp('-',Id("i"),IntLiteral(1)),([],[If([(BinaryOp('<',ArrayCell(Id("arr"),[Id("i")]),Id("min")),[],[Assign(Id("min"),ArrayCell(Id("arr"),[Id("i")])),Assign(Id("iMin"),Id("i"))])], ([],[])),If([(BinaryOp('>',ArrayCell(Id("arr"),[Id("i")]),Id("max")),[],[Assign(Id("max"),ArrayCell(Id("arr"),[Id("i")])),Assign(Id("iMax"),Id("i"))])], ([],[]))])),CallStmt(Id("print"),[StringLiteral("Min = ")]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("min")])]),CallStmt(Id("print"),[StringLiteral(" at index = ")]),CallStmt(Id("printLn"),[CallExpr(Id("string_of_int"),[Id("iMin")])]),CallStmt(Id("print"),[StringLiteral("Max = ")]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("max")])]),CallStmt(Id("print"),[StringLiteral(" at index = ")]),CallStmt(Id("printLn"),[CallExpr(Id("string_of_int"),[Id("iMax")])]),Return(IntLiteral(0))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,24))

	def test_ast_025(self):
		input = """
		Function: main
		Body:
			**Bai toan doi tien**

			Var: n,i,d = 0;
			n = int_of_string(read());
			print("Can ");
			While n > 500 Do
				d = d + 1;
				n = n - 500;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 500k,");
				d = 0;
			EndIf.

			While n > 200 Do
				d = d + 1;
				n = n - 200;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 200k,");
				d = 0;
			EndIf.
			
			While n > 100 Do
				d = d + 1;
				n = n - 100;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 100k,");
				d = 0;
			EndIf.
			
			While n > 50 Do
				d = d + 1;
				n = n - 50;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 50k,");
				d = 0;
			EndIf.
			
			While n > 20 Do
				d = d + 1;
				n = n - 20;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 20k,");
				d = 0;
			EndIf.

			While n > 10 Do
				d = d + 1;
				n = n - 10;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 10k,");
				d = 0;
			EndIf.

			While n > 5 Do
				d = d + 1;
				n = n - 5;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 5k,");
				d = 0;
			EndIf.

			While n > 2 Do
				d = d + 1;
				n = n - 2;
			EndWhile.
			If d > 0 Then 
				print(d);
				print(" to 2k,");
				d = 0;
			EndIf.

			While n > 1 Do
				d = d + 1;
				n = n - 1;
			EndWhile.
			If d > 0 Then 
				print(d);
				printLn(" to 1k.");
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("n"),[],None),VarDecl(Id("i"),[],None),VarDecl(Id("d"),[],IntLiteral(0))],[Assign(Id("n"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),CallStmt(Id("print"),[StringLiteral("Can ")]),While(BinaryOp('>',Id("n"),IntLiteral(500)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(500)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 500k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(200)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(200)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 200k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(100)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(100)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 100k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(50)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(50)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 50k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(20)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(20)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 20k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(10)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(10)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 10k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(5)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(5)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 5k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(2)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(2)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("print"),[StringLiteral(" to 2k,")]),Assign(Id("d"),IntLiteral(0))])], ([],[])),While(BinaryOp('>',Id("n"),IntLiteral(1)),([],[Assign(Id("d"),BinaryOp('+',Id("d"),IntLiteral(1))),Assign(Id("n"),BinaryOp('-',Id("n"),IntLiteral(1)))])),If([(BinaryOp('>',Id("d"),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("d")]),CallStmt(Id("printLn"),[StringLiteral(" to 1k.")])])], ([],[]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,25))

	def test_ast_026(self):
		input = """
		Function: main
		Body:
			Var: arr[10] = {1,8,2,0,3,4,1,6,8,10};
			minHeap = buildMinHeap(arr);
			min = pop(minHeap);
			maxHeap = buildMaxHeap(arr);
			max = pop(maxHeap);
			arr = heapSort(minHeap);
			printArr(arr);
		EndBody.

		Function: buildMinHeap
		Parameter: arr
		Body:
			** Do something **
		EndBody.

		Function: buildMaxHeap
		Parameter: arr
		Body:
			** Do something **
		EndBody.

		Function: pop
		Parameter: heap
		Body:
			** Do something **
		EndBody.

		Function: heapSort
		Parameter: heap
		Body:
			** Do something **
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(8),IntLiteral(2),IntLiteral(0),IntLiteral(3),IntLiteral(4),IntLiteral(1),IntLiteral(6),IntLiteral(8),IntLiteral(10)]))],[Assign(Id("minHeap"),CallExpr(Id("buildMinHeap"),[Id("arr")])),Assign(Id("min"),CallExpr(Id("pop"),[Id("minHeap")])),Assign(Id("maxHeap"),CallExpr(Id("buildMaxHeap"),[Id("arr")])),Assign(Id("max"),CallExpr(Id("pop"),[Id("maxHeap")])),Assign(Id("arr"),CallExpr(Id("heapSort"),[Id("minHeap")])),CallStmt(Id("printArr"),[Id("arr")])])),FuncDecl(Id("buildMinHeap"),[VarDecl(Id("arr"),[],None)],([],[])),FuncDecl(Id("buildMaxHeap"),[VarDecl(Id("arr"),[],None)],([],[])),FuncDecl(Id("pop"),[VarDecl(Id("heap"),[],None)],([],[])),FuncDecl(Id("heapSort"),[VarDecl(Id("heap"),[],None)],([],[]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,26))

	def test_ast_027(self):
		input = """
		Function: main
		Body:
			Var: inp;
			print("Nhap vao mot so: ");
			inp = int_of_string(read());
			out = predict(inp);
			print(out);
		EndBody.

		Function: predict
		Parameter: number
		Body:
			Return "Ban la nguoi thong minh";
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("inp"),[],None)],[CallStmt(Id("print"),[StringLiteral("Nhap vao mot so: ")]),Assign(Id("inp"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("out"),CallExpr(Id("predict"),[Id("inp")])),CallStmt(Id("print"),[Id("out")])])),FuncDecl(Id("predict"),[VarDecl(Id("number"),[],None)],([],[Return(StringLiteral("Ban la nguoi thong minh"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,27))

	def test_ast_028(self):
		input = """
		Function: main
		Body:
			** Do something with index **
			Var: i,k,arr[5] = {8,2,5,4,5};
			k = sort(arr)[0];
			i = sort(sort(arr))[2][3];
		EndBody.

		Function: sort
		Parameter: arr
		Body:
			** do something **
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None),VarDecl(Id("k"),[],None),VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(8),IntLiteral(2),IntLiteral(5),IntLiteral(4),IntLiteral(5)]))],[Assign(Id("k"),ArrayCell(CallExpr(Id("sort"),[Id("arr")]),[IntLiteral(0)])),Assign(Id("i"),ArrayCell(CallExpr(Id("sort"),[CallExpr(Id("sort"),[Id("arr")])]),[IntLiteral(2),IntLiteral(3)]))])),FuncDecl(Id("sort"),[VarDecl(Id("arr"),[],None)],([],[]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,28))

	def test_ast_029(self):
		input = """
		Function: main
		Body:
			** test non-associated operator **
			Var: x,y;
			x = 1 + (2 + 3) - 4 * 5;  ** OK **
			x = 1 + 2 + 3 - 4 * 5;    ** OK **
			y = (1 > 2) < 2;          ** OK **
			**y = 1 > 2 < 2;		 Fail **	
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),BinaryOp('-',BinaryOp('+',IntLiteral(1),BinaryOp('+',IntLiteral(2),IntLiteral(3))),BinaryOp('*',IntLiteral(4),IntLiteral(5)))),Assign(Id("x"),BinaryOp('-',BinaryOp('+',BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp('*',IntLiteral(4),IntLiteral(5)))),Assign(Id("y"),BinaryOp('<',BinaryOp('>',IntLiteral(1),IntLiteral(2)),IntLiteral(2)))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,29))

	def test_ast_030(self):
		input = """
		Function: main
		Body:
			Var: arr[5] = {1,2,3,4,5};
			** test index operator **
			x  = foo(foo(foo(arr)))[4]; 				
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))],[Assign(Id("x"),ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("arr")])])]),[IntLiteral(4)]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,30))

	def test_ast_031(self):
		input = """
		Function: main
		Body:
			Var: arr[5] = {1,2,3,4,5};
			** test index operator **
			x = (((((foo(foo(foo(arr))))))))[10]; 
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))],[Assign(Id("x"),ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("arr")])])]),[IntLiteral(10)]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,31))

	def test_ast_032(self):
		input = """
		Function: main
		Body:
			Var: arr[5] = {1,2,3,4,5};
			** test index operator **
			x = arr[-10]; 					
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))],[Assign(Id("x"),ArrayCell(Id("arr"),[UnaryOp('-',IntLiteral(10))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,32))

	def test_ast_033(self):
		input = """
		Function: main
		Body:
			Var: arr[5] = {1,2,3,4,5};
			** test index operator **
			x = arr[-----10];	
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))],[Assign(Id("x"),ArrayCell(Id("arr"),[UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',IntLiteral(10))))))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,33))

	def test_ast_034(self):
		input = """
		Var: x = 1;
		Var: y;
		Var: arr[1][2][3][10][0] = 0xFF;
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],None),VarDecl(Id("arr"),[1,2,3,10,0],IntLiteral(255))])

		self.assertTrue(TestAST.checkASTGen(input,expect,34))

	def test_ast_035(self):
		input = """
		Function: main
		Body:
			** operators **
			Var: arr[5] = {1,2,3,4,5}, i,j,k = True, l, m, n = "String";
			x = 1 * 5 + 2 - 7 * arr[9 * i + j] \\. 2.0 -. 1.0 && True || k;
			x = i >=. j;
			x = ! k;
			foo(k,l,m,n,arr,100,"Arg",x);
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None),VarDecl(Id("k"),[],BooleanLiteral(True)),VarDecl(Id("l"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],StringLiteral("String"))],[Assign(Id("x"),BinaryOp('||',BinaryOp('&&',BinaryOp('-.',BinaryOp('-',BinaryOp('+',BinaryOp('*',IntLiteral(1),IntLiteral(5)),IntLiteral(2)),BinaryOp('\\.',BinaryOp('*',IntLiteral(7),ArrayCell(Id("arr"),[BinaryOp('+',BinaryOp('*',IntLiteral(9),Id("i")),Id("j"))])),FloatLiteral(2.0))),FloatLiteral(1.0)),BooleanLiteral(True)),Id("k"))),Assign(Id("x"),BinaryOp('>=.',Id("i"),Id("j"))),Assign(Id("x"),UnaryOp('!',Id("k"))),CallStmt(Id("foo"),[Id("k"),Id("l"),Id("m"),Id("n"),Id("arr"),IntLiteral(100),StringLiteral("Arg"),Id("x")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,35))

	def test_ast_036(self):
		input = """
		Function: main
		Body:
			** comment inside statement **
			Var: x **comment**,y;
			For (x = 1,**comment**x>1,x + **comment**1) **While**Do
				********
				**comment**
				y = **comment** a + 1;
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[For(Id("x"),IntLiteral(1),BinaryOp('>',Id("x"),IntLiteral(1)),BinaryOp('+',Id("x"),IntLiteral(1)),([],[Assign(Id("y"),BinaryOp('+',Id("a"),IntLiteral(1)))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,36))

	def test_ast_037(self):
		input = """
		** duplicate declare **
		Var: x = 1;
		Function: main
		Body:
			Var: x;
			Var: x = 2;
			For (x = 0,1,1) Do
				Var: x;
			EndFor.
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],IntLiteral(2))],[For(Id("x"),IntLiteral(0),IntLiteral(1),IntLiteral(1),([VarDecl(Id("x"),[],None)],[]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,37))

	def test_ast_038(self):
		input = """
		Function: main
		Body:
			** test built-in functions, ignore args (type,number)
				just consider syntax **
			printLn("string");
			printLn({1,2,3});
			print(a,b,1,True,100.e1);
			printStrLn("string and new line");
			read();
			x = read();
			read(a);			
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printLn"),[StringLiteral("string")]),CallStmt(Id("printLn"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]),CallStmt(Id("print"),[Id("a"),Id("b"),IntLiteral(1),BooleanLiteral(True),FloatLiteral(1000.0)]),CallStmt(Id("printStrLn"),[StringLiteral("string and new line")]),CallStmt(Id("read"),[]),Assign(Id("x"),CallExpr(Id("read"),[])),CallStmt(Id("read"),[Id("a")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,38))

	def test_ast_039(self):
		input = """
		Function: main
		Body:
			** test type conversion functions **
			** just consider syntax **
			a = int_of_foat(100.e10);
			a = int_of_string(read());
			If bool_of_string("True") Then
				a = int_of_string();
				a = string_of_int(100);
				a = float_of_string("string");
				a = string_of_float(1e0);
				a = string_of_bool(True);
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),CallExpr(Id("int_of_foat"),[FloatLiteral(1000000000000.0)])),Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[])),Assign(Id("a"),CallExpr(Id("string_of_int"),[IntLiteral(100)])),Assign(Id("a"),CallExpr(Id("float_of_string"),[StringLiteral("string")])),Assign(Id("a"),CallExpr(Id("string_of_float"),[FloatLiteral(1.0)])),Assign(Id("a"),CallExpr(Id("string_of_bool"),[BooleanLiteral(True)]))])], ([],[]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,39))

	def test_ast_040(self):
		input = """
		** index is Octal,hexa number **
		Var: arr[0o6][0XAF];
		"""
		expect = Program([VarDecl(Id("arr"),[6,175],None)])

		self.assertTrue(TestAST.checkASTGen(input,expect,40))

	def test_ast_041(self):
		input = """
		Function: main
		Body:
			** case-sensitive 
			*  it will fail in next phase
			**
			Var: x = 10,walkVar;
			walkVar = x \\. 10;
			For (walkvar = 0, walKVAr < x, walkVar + 1) Do
				x = (x + walkvar * random());
			EndFor.
			Return x;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("walkVar"),[],None)],[Assign(Id("walkVar"),BinaryOp('\\.',Id("x"),IntLiteral(10))),For(Id("walkvar"),IntLiteral(0),BinaryOp('<',Id("walKVAr"),Id("x")),BinaryOp('+',Id("walkVar"),IntLiteral(1)),([],[Assign(Id("x"),BinaryOp('+',Id("x"),BinaryOp('*',Id("walkvar"),CallExpr(Id("random"),[]))))])),Return(Id("x"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,41))

	def test_ast_042(self):
		input = """
		Function: main
		Body:
			Var: x = 10,i;
			For (i = 0, i < x, i + 1) Do
				x = (x + i * random());
			EndFor.
			Return x;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),Id("x")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(Id("x"),BinaryOp('+',Id("x"),BinaryOp('*',Id("i"),CallExpr(Id("random"),[]))))])),Return(Id("x"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,42))

	def test_ast_043(self):
		input = """
		Function: main
		Body:
			** case-sensitive 
			*  it will fail in next phase
			**
			Var: x = 10,walkVar;
			walkVar = x \\. 10;
			For (walkvar = 0, walKVAr < x, walkVar + 1) Do
				x = (x + walkvar * random());
			EndFor.
			Return x;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("walkVar"),[],None)],[Assign(Id("walkVar"),BinaryOp('\\.',Id("x"),IntLiteral(10))),For(Id("walkvar"),IntLiteral(0),BinaryOp('<',Id("walKVAr"),Id("x")),BinaryOp('+',Id("walkVar"),IntLiteral(1)),([],[Assign(Id("x"),BinaryOp('+',Id("x"),BinaryOp('*',Id("walkvar"),CallExpr(Id("random"),[]))))])),Return(Id("x"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,43))

	def test_ast_044(self):
		input = """
		Function: main
		Body:
			** super super associated operators **
			a = ((((((((((((a == 1 ) == (True < False)) > 2) > (3 || True || False || True || 1 || {"a",1e3})))))))))); **OK**
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp('>',BinaryOp('>',BinaryOp('==',BinaryOp('==',Id("a"),IntLiteral(1)),BinaryOp('<',BooleanLiteral(True),BooleanLiteral(False))),IntLiteral(2)),BinaryOp('||',BinaryOp('||',BinaryOp('||',BinaryOp('||',BinaryOp('||',IntLiteral(3),BooleanLiteral(True)),BooleanLiteral(False)),BooleanLiteral(True)),IntLiteral(1)),ArrayLiteral([StringLiteral("a"),FloatLiteral(1000.0)]))))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,44))

	def test_ast_045(self):
		input = """
		** duplicate function name **
		Function: main
		Body:
			print("The first main function");
		EndBody.
		
		Function: main
		Body:
			print("The second main function");
		EndBody.
		
		Function: main
		Body:
			print("The third main function");
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("The first main function")])])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("The second main function")])])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("The third main function")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,45))

	def test_ast_046(self):
		input = """
		**declare function with some parameters
		* but call it without arg
		**

		Function: foo
		Parameter: a,b,c
		Body:
			If (a > 1) Then 
				Return a;
			EndIf.
			Return a + foo(1,b,c);
		EndBody.

		Function: main
		Body:
			foo(1,2,3); **OK**
			x = foo(1);	**OK**
			foo();		**OK**
		EndBody.
		"""
		expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[If([(BinaryOp('>',Id("a"),IntLiteral(1)),[],[Return(Id("a"))])], ([],[])),Return(BinaryOp('+',Id("a"),CallExpr(Id("foo"),[IntLiteral(1),Id("b"),Id("c")])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Assign(Id("x"),CallExpr(Id("foo"),[IntLiteral(1)])),CallStmt(Id("foo"),[])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,46))

	def test_ast_047(self):
		input = """
		Function: main
		Parameter: x,y,z
		Body:
			Var: num;
			num = int_of_string(read());
			If x > num Then
				Return x;
			ElseIf y > num Then
				Return y;
			ElseIf z > num Then
				Return z;
			EndIf.
			Return -1;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([VarDecl(Id("num"),[],None)],[Assign(Id("num"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('>',Id("x"),Id("num")),[],[Return(Id("x"))]),(BinaryOp('>',Id("y"),Id("num")),[],[Return(Id("y"))]),(BinaryOp('>',Id("z"),Id("num")),[],[Return(Id("z"))])], ([],[])),Return(UnaryOp('-',IntLiteral(1)))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,47))

	def test_ast_048(self):
		input = """
		Function: main
		Body:
			Var: a = 1;
			While (a == 1) Do
				print("I\\'m looping");
			EndWhile.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(1))],[While(BinaryOp('==',Id("a"),IntLiteral(1)),([],[CallStmt(Id("print"),[StringLiteral("I\\'m looping")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,48))

	def test_ast_049(self):
		input = """
		Function: main
		Parameter: x,y,z
		Body:
			Var: num;
			num = int_of_string(read());
			If x > num Then
				Return x;
			ElseIf y > num Then
				Return y;
			ElseIf z > num Then
				Return z;
			EndIf.
			Return -1;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([VarDecl(Id("num"),[],None)],[Assign(Id("num"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('>',Id("x"),Id("num")),[],[Return(Id("x"))]),(BinaryOp('>',Id("y"),Id("num")),[],[Return(Id("y"))]),(BinaryOp('>',Id("z"),Id("num")),[],[Return(Id("z"))])], ([],[])),Return(UnaryOp('-',IntLiteral(1)))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,49))

	def test_ast_050(self):
		input = """
		**empty**
		"""
		expect = Program([])

		self.assertTrue(TestAST.checkASTGen(input,expect,50))

	def test_ast_051(self):
		input = """
		Function: main
		Body:
			Var: x;
			x = int_of_string(read());
			y = int_of_string(read());
			z = int_of_string(read());
			If (x > 5) Then
				print(y);
			ElseIf (x < 3) Then 
				**missing expr**
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("y"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("z"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('>',Id("x"),IntLiteral(5)),[],[CallStmt(Id("print"),[Id("y")])]),(BinaryOp('<',Id("x"),IntLiteral(3)),[],[])], ([],[]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,51))

	def test_ast_052(self):
		input = """
		Var: a = {1,**HELLO TUI NE**2,3,"abc"}, b**HELLO TUI NE**,c,d**HELLO TUI NE**[**HELLO TUI NE**100] = **HELLO TUI NE**{};
		Function**HELLO TUI NE**: main
		Parameter: **HELLO TUI NE** arr
		Body:
			**comment everywhere** 
			Var **HELLO TUI NE** : x;
			x = **HELLO TUI NE** int_of_string(read());
			y = int_of_string**HELLO TUI NE**(read());
			z = int_of_string(**HELLO TUI NE**read());
			If (**HELLO TUI NE**x >**HELLO TUI NE** 5) Then**HELLO TUI NE**
				print**HELLO TUI NE**(y)**HELLO TUI NE**;
			ElseIf **HELLO TUI NE** (x < 3) Then 
				print(z);
			EndIf.
			**HELLO TUI NE****HELLO TUI NE****HELLO TUI NE****HELLO TUI NE**
		EndBody.
		"""
		expect = Program([VarDecl(Id("a"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),StringLiteral("abc")])),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[100],ArrayLiteral([])),FuncDecl(Id("main"),[VarDecl(Id("arr"),[],None)],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("y"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("z"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('>',Id("x"),IntLiteral(5)),[],[CallStmt(Id("print"),[Id("y")])]),(BinaryOp('<',Id("x"),IntLiteral(3)),[],[CallStmt(Id("print"),[Id("z")])])], ([],[]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,52))

	def test_ast_053(self):
		input = """
		Var: x[0xFF][15][0o7] = {1,2,3,"string",{}};
		"""
		expect = Program([VarDecl(Id("x"),[255,15,7],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),StringLiteral("string"),ArrayLiteral([])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,53))

	def test_ast_054(self):
		input = """
		Function: main
		Body:
			Var: isEmpty = True;
			Var: x[10] = {};
			print(string_of_bool(isEmpty));
			x = insert(x,0,1);
			isEmpty = False;
			print(string_of_bool(isEmpty));
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("isEmpty"),[],BooleanLiteral(True)),VarDecl(Id("x"),[10],ArrayLiteral([]))],[CallStmt(Id("print"),[CallExpr(Id("string_of_bool"),[Id("isEmpty")])]),Assign(Id("x"),CallExpr(Id("insert"),[Id("x"),IntLiteral(0),IntLiteral(1)])),Assign(Id("isEmpty"),BooleanLiteral(False)),CallStmt(Id("print"),[CallExpr(Id("string_of_bool"),[Id("isEmpty")])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,54))

	def test_ast_055(self):
		input = """
		Function: main
		Parameter: x,y,foo
		Body:
			x = x + 1;
			y = y \\. 2;
			(foo())[1] = 1;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("foo"),[],None)],([],[Assign(Id("x"),BinaryOp('+',Id("x"),IntLiteral(1))),Assign(Id("y"),BinaryOp('\\.',Id("y"),IntLiteral(2))),Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1)]),IntLiteral(1))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,55))

	def test_ast_056(self):
		input = """
		Function: main
		Body:
			Var: abc_,x_[10][10] = {1e7}, x;
			x = main();
			x = x + 1;
			(foo(foo(foo(foo(x,1,3+6),1),3),3+9*5-8))[15] = 7;
			Return 0;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("abc_"),[],None),VarDecl(Id("x_"),[10,10],ArrayLiteral([FloatLiteral(10000000.0)])),VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallExpr(Id("main"),[])),Assign(Id("x"),BinaryOp('+',Id("x"),IntLiteral(1))),Assign(ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("x"),IntLiteral(1),BinaryOp('+',IntLiteral(3),IntLiteral(6))]),IntLiteral(1)]),IntLiteral(3)]),BinaryOp('-',BinaryOp('+',IntLiteral(3),BinaryOp('*',IntLiteral(9),IntLiteral(5))),IntLiteral(8))]),[IntLiteral(15)]),IntLiteral(7)),Return(IntLiteral(0))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,56))

	def test_ast_057(self):
		input = """
		Function: main
		Body:
			Var: arr[10][10][0xFF];
			Var: x = 10;
			x = arr[arr[arr[1]]][1][15 + x];
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10,10,255],None),VarDecl(Id("x"),[],IntLiteral(10))],[Assign(Id("x"),ArrayCell(Id("arr"),[ArrayCell(Id("arr"),[ArrayCell(Id("arr"),[IntLiteral(1)])]),IntLiteral(1),BinaryOp('+',IntLiteral(15),Id("x"))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,57))

	def test_ast_058(self):
		input = """
		Function: main
		Body:
			Var: arr[10][10][0xFF];
			Var: x = 10;
			x = (((((((((arr))))[(((arr[((arr[1]))])))][1])))[15 + x]));
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[10,10,255],None),VarDecl(Id("x"),[],IntLiteral(10))],[Assign(Id("x"),ArrayCell(ArrayCell(Id("arr"),[ArrayCell(Id("arr"),[ArrayCell(Id("arr"),[IntLiteral(1)])]),IntLiteral(1)]),[BinaryOp('+',IntLiteral(15),Id("x"))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,58))

	def test_ast_059(self):
		input = """
		Function: main
		Body:
			Var: x = 10,arr[10][40];
			((foo(foo(1))))[1+x][2*x] = 14;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("arr"),[10,40],None)],[Assign(ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(1)])]),[BinaryOp('+',IntLiteral(1),Id("x")),BinaryOp('*',IntLiteral(2),Id("x"))]),IntLiteral(14))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,59))

	def test_ast_060(self):
		input = """
		Function: main
		Parameter: x
		Body:
			Var: x,y,z;
			If (x > 10) Then print("x>10");
			ElseIf (y>10) Then print("y>10 & x<10");
			EndIf.
			foo()[z] = y;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[If([(BinaryOp('>',Id("x"),IntLiteral(10)),[],[CallStmt(Id("print"),[StringLiteral("x>10")])]),(BinaryOp('>',Id("y"),IntLiteral(10)),[],[CallStmt(Id("print"),[StringLiteral("y>10 & x<10")])])], ([],[])),Assign(ArrayCell(CallExpr(Id("foo"),[]),[Id("z")]),Id("y"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,60))

	def test_ast_061(self):
		input = """
		Function: main
		Body:
			Var: arr[20],n;
			For (x = 1, x<10, x + 1) Do
				arr[((x*2+7)*9)%20] = random(0,1) + n;
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[20],None),VarDecl(Id("n"),[],None)],[For(Id("x"),IntLiteral(1),BinaryOp('<',Id("x"),IntLiteral(10)),BinaryOp('+',Id("x"),IntLiteral(1)),([],[Assign(ArrayCell(Id("arr"),[BinaryOp('%',BinaryOp('*',BinaryOp('+',BinaryOp('*',Id("x"),IntLiteral(2)),IntLiteral(7)),IntLiteral(9)),IntLiteral(20))]),BinaryOp('+',CallExpr(Id("random"),[IntLiteral(0),IntLiteral(1)]),Id("n")))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,61))

	def test_ast_062(self):
		input = """
		Function: main
		Body:
			Var: n;
			While True Do
				n = int_of_string(read());
				If (n>10) Then Break;
				Else print("n<10, Try again");
				EndIf.
			EndWhile.
			print("Accepted");
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("n"),[],None)],[While(BooleanLiteral(True),([],[Assign(Id("n"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('>',Id("n"),IntLiteral(10)),[],[Break()])], ([],[CallStmt(Id("print"),[StringLiteral("n<10, Try again")])]))])),CallStmt(Id("print"),[StringLiteral("Accepted")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,62))

	def test_ast_063(self):
		input = """
		Function: main
		Parameter: arr[10][10]
		Body:
			print("Initial...");
			s = 0;
			For (i=0, i<10, i+1) Do
				For (j=0, j<10, j+1) Do
					arr[i][j] = random();
				EndFor.
			EndFor.

			print("Done");
			For (i=9, i>=0, i-1) Do
				For (j=0, j<10, j+1) Do
					print(string_of_int(arr[i][j]));
					print(" ");
				EndFor.
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("arr"),[10,10],None)],([],[CallStmt(Id("print"),[StringLiteral("Initial...")]),Assign(Id("s"),IntLiteral(0)),For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp('<',Id("j"),IntLiteral(10)),BinaryOp('+',Id("j"),IntLiteral(1)),([],[Assign(ArrayCell(Id("arr"),[Id("i"),Id("j")]),CallExpr(Id("random"),[]))]))])),CallStmt(Id("print"),[StringLiteral("Done")]),For(Id("i"),IntLiteral(9),BinaryOp('>=',Id("i"),IntLiteral(0)),BinaryOp('-',Id("i"),IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp('<',Id("j"),IntLiteral(10)),BinaryOp('+',Id("j"),IntLiteral(1)),([],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[ArrayCell(Id("arr"),[Id("i"),Id("j")])])]),CallStmt(Id("print"),[StringLiteral(" ")])]))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,63))

	def test_ast_064(self):
		input = """
		Var: x = 5,y,z;
		Var: a,b;
		Function: main
		Parameter: x,a,d
		Body:
			Var: z = 10, arr[10][20];
			print(string_of_int(x));
			print(string_of_int(y));
			print(string_of_int(z));
			print(string_of_int(a));
			print(string_of_int(b));
			print(string_of_int(d));
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("d"),[],None)],([VarDecl(Id("z"),[],IntLiteral(10)),VarDecl(Id("arr"),[10,20],None)],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("x")])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("y")])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("z")])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("a")])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("b")])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("d")])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,64))

	def test_ast_065(self):
		input = """
		Var: x = 10,y = 1, z = 2;
		Function: main
		Body:
			Var: x = 10;
			Return foo(x);
		EndBody.

		Function: foo
		Parameter: n
		Body:
			Return n + x;
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],IntLiteral(2)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10))],[Return(CallExpr(Id("foo"),[Id("x")]))])),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp('+',Id("n"),Id("x")))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,65))

	def test_ast_066(self):
		input = """
		Var: x = 10;
		Function: main
		Body:
			Var: x = 10,i;
			For (i = 0, i<10, i+1) Do
				Var: x = 15;
				print(string_of_int(x));
			EndFor.
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([VarDecl(Id("x"),[],IntLiteral(15))],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("x")])])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,66))

	def test_ast_067(self):
		input = """
		Var: x = 10;
		Function: main
		Body:
			Var: y = 10,z,arr,i,j;
			While (y<15) Do
				Var: x = 7;
				print(string_of_int(x));
				y = y + 1;
			EndWhile.

			For (i=0, i<10, i+1) Do
				Var: x = 9;
				print(string_of_int(x));
			EndFor.
			print(string_of_int(x));
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),FuncDecl(Id("main"),[],([VarDecl(Id("y"),[],IntLiteral(10)),VarDecl(Id("z"),[],None),VarDecl(Id("arr"),[],None),VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None)],[While(BinaryOp('<',Id("y"),IntLiteral(15)),([VarDecl(Id("x"),[],IntLiteral(7))],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("x")])]),Assign(Id("y"),BinaryOp('+',Id("y"),IntLiteral(1)))])),For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([VarDecl(Id("x"),[],IntLiteral(9))],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("x")])])])),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("x")])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,67))

	def test_ast_068(self):
		input = """
		Var: x = 2;
		Function: main
		Body:
			Var: y = 10;
			Var: x = 5;
			y = foo(((foo(foo(x)))));
			Return 0;
		EndBody.

		Function: foo
		Parameter: x
		Body:
			Var: y = 3;
			Return y*x;
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(2)),FuncDecl(Id("main"),[],([VarDecl(Id("y"),[],IntLiteral(10)),VarDecl(Id("x"),[],IntLiteral(5))],[Assign(Id("y"),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("x")])])])),Return(IntLiteral(0))])),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("y"),[],IntLiteral(3))],[Return(BinaryOp('*',Id("y"),Id("x")))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,68))

	def test_ast_069(self):
		input = """
		Var: x = 10;
		Function: main
		Body:
			Var: x = 6;
			print(string_of_int(fibo(x*2)));
		EndBody.

		Function: fibo
		Parameter: n
		Body:
			If n<2 Then Return 1;
			EndIf.
			Return fibo(n-1) + fibo(n-2);
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(6))],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[CallExpr(Id("fibo"),[BinaryOp('*',Id("x"),IntLiteral(2))])])])])),FuncDecl(Id("fibo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp('<',Id("n"),IntLiteral(2)),[],[Return(IntLiteral(1))])], ([],[])),Return(BinaryOp('+',CallExpr(Id("fibo"),[BinaryOp('-',Id("n"),IntLiteral(1))]),CallExpr(Id("fibo"),[BinaryOp('-',Id("n"),IntLiteral(2))])))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,69))

	def test_ast_070(self):
		input = """
		Function: main
		Body:
			Var: n,f,s,t;
			While ((n>999) || (n<100)) Do
				print("Nhap n: ");
				n = int_of_string(read());
			EndWhile.
			t = n % 10;
			n = n \\ 10;
			s = n % 10;
			f = n \\ 10;
			print(string_of_int(f));
			print(" tram ");
			print(string_of_int(s));
			print(" chuc ");
			print(string_of_int(t));
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("n"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("s"),[],None),VarDecl(Id("t"),[],None)],[While(BinaryOp('||',BinaryOp('>',Id("n"),IntLiteral(999)),BinaryOp('<',Id("n"),IntLiteral(100))),([],[CallStmt(Id("print"),[StringLiteral("Nhap n: ")]),Assign(Id("n"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])]))])),Assign(Id("t"),BinaryOp('%',Id("n"),IntLiteral(10))),Assign(Id("n"),BinaryOp('\\',Id("n"),IntLiteral(10))),Assign(Id("s"),BinaryOp('%',Id("n"),IntLiteral(10))),Assign(Id("f"),BinaryOp('\\',Id("n"),IntLiteral(10))),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("f")])]),CallStmt(Id("print"),[StringLiteral(" tram ")]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("s")])]),CallStmt(Id("print"),[StringLiteral(" chuc ")]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("t")])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,70))

	def test_ast_071(self):
		input = """
		Function: main
		Body:
			Var: arr,i;
			arr = split(read()," ");
			n = length(arr);
			For (i=0, i<n, i+1) Do
				printLn(arr[i]);
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[],None),VarDecl(Id("i"),[],None)],[Assign(Id("arr"),CallExpr(Id("split"),[CallExpr(Id("read"),[]),StringLiteral(" ")])),Assign(Id("n"),CallExpr(Id("length"),[Id("arr")])),For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),Id("n")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[CallStmt(Id("printLn"),[ArrayCell(Id("arr"),[Id("i")])])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,71))

	def test_ast_072(self):
		input = """
		Var: x = 10, t = 100;
		Function: main
		Body:
			Var: x,y;
			x = int_of_string(read());
			y = int_of_string(read());
			Return pow(x,y);
		EndBody.

		Function: pow
		Parameter: x,y
		Body:
			Var: t = 1;
			For (i=0,i<y,i+1) Do
				t = t*x;
			EndFor.
			Return t;
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("t"),[],IntLiteral(100)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("y"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Return(CallExpr(Id("pow"),[Id("x"),Id("y")]))])),FuncDecl(Id("pow"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([VarDecl(Id("t"),[],IntLiteral(1))],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),Id("y")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(Id("t"),BinaryOp('*',Id("t"),Id("x")))])),Return(Id("t"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,72))

	def test_ast_073(self):
		input = """
		Function: main
		Body:
			Var: x,i,res = 0;
			x = int_of_string(read());
			For (i=0, i<x*x*x, i+1) Do
				Var: z;
				z = random();
				If z>10 Then Break;
					ElseIf z>5 Then res = res * i;
					Else res = res + i;
				EndIf.
			EndFor.
			Return res;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("i"),[],None),VarDecl(Id("res"),[],IntLiteral(0))],[Assign(Id("x"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),BinaryOp('*',BinaryOp('*',Id("x"),Id("x")),Id("x"))),BinaryOp('+',Id("i"),IntLiteral(1)),([VarDecl(Id("z"),[],None)],[Assign(Id("z"),CallExpr(Id("random"),[])),If([(BinaryOp('>',Id("z"),IntLiteral(10)),[],[Break()]),(BinaryOp('>',Id("z"),IntLiteral(5)),[],[Assign(Id("res"),BinaryOp('*',Id("res"),Id("i")))])], ([],[Assign(Id("res"),BinaryOp('+',Id("res"),Id("i")))]))])),Return(Id("res"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,73))

	def test_ast_074(self):
		input = """
		Function: main
		Body:
			Var: arr = {1,2,3,4,5,6,7,8};
			foo(arr,8);
			Return;
		EndBody.

		Function: foo
		Parameter: a,n
		Body:
			If a[0] == 8 Then print("8");
			Else 
				Var: i,temp[100];
				print(string_of_int(a[0]));

				For (i=1,i<n,i+1) Do
					temp[i-1] = a[i] * 2 + 1;
				EndFor.
			EndIf.
				Return foo(temp,n-1);
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8)]))],[CallStmt(Id("foo"),[Id("arr"),IntLiteral(8)]),Return(None)])),FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("n"),[],None)],([],[If([(BinaryOp('==',ArrayCell(Id("a"),[IntLiteral(0)]),IntLiteral(8)),[],[CallStmt(Id("print"),[StringLiteral("8")])])], ([VarDecl(Id("i"),[],None),VarDecl(Id("temp"),[100],None)],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[ArrayCell(Id("a"),[IntLiteral(0)])])]),For(Id("i"),IntLiteral(1),BinaryOp('<',Id("i"),Id("n")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(ArrayCell(Id("temp"),[BinaryOp('-',Id("i"),IntLiteral(1))]),BinaryOp('+',BinaryOp('*',ArrayCell(Id("a"),[Id("i")]),IntLiteral(2)),IntLiteral(1)))]))])),Return(CallExpr(Id("foo"),[Id("temp"),BinaryOp('-',Id("n"),IntLiteral(1))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,74))

	def test_ast_075(self):
		input = """
		Function: main
		Body:
			Var: hp = 1000.0,i = 0;
			While hp>0 Do
				Var: dame;
				dame = random();
				hp = hp - dame;
				print(string_of_int(i));
				print(" Dame: ");
				printLn(string_of_float(dame));
			EndWhile.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("hp"),[],FloatLiteral(1000.0)),VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp('>',Id("hp"),IntLiteral(0)),([VarDecl(Id("dame"),[],None)],[Assign(Id("dame"),CallExpr(Id("random"),[])),Assign(Id("hp"),BinaryOp('-',Id("hp"),Id("dame"))),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("i")])]),CallStmt(Id("print"),[StringLiteral(" Dame: ")]),CallStmt(Id("printLn"),[CallExpr(Id("string_of_float"),[Id("dame")])])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,75))

	def test_ast_076(self):
		input = """
		Var: x = 10, y = 2, arr[5] = {1,2,3,4,5};
		Function: main
		Body:
			Var: x = 15;
			print(string_of_int(y));
			print(string_of_int(((foo(x)))[foo(x)[y]]));
		EndBody.

		Function: foo
		Parameter: t
		Body:
			Return arr;
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("arr"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(15))],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("y")])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[ArrayCell(CallExpr(Id("foo"),[Id("x")]),[ArrayCell(CallExpr(Id("foo"),[Id("x")]),[Id("y")])])])])])),FuncDecl(Id("foo"),[VarDecl(Id("t"),[],None)],([],[Return(Id("arr"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,76))

	def test_ast_077(self):
		input = """
		Var: x = 1;
		Var: y,z,t,arr[10] = {1,2,3};
		Var: abc = "This is legal string",x;
		Var: helloworld;
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],None),VarDecl(Id("arr"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("abc"),[],StringLiteral("This is legal string")),VarDecl(Id("x"),[],None),VarDecl(Id("helloworld"),[],None)])

		self.assertTrue(TestAST.checkASTGen(input,expect,77))

	def test_ast_078(self):
		input = """
		Function: foo
		Body:
			Return 0;
		EndBody.

		Function: foo1
		Body:
			Return 1;
		EndBody.

		Function: foo2
		Body:
			Return 2;
		EndBody.

		Function: foo3
		Body:
			Return 3;
		EndBody.

		Function: foo4
		Body:
			Return 4;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("foo"),[],([],[Return(IntLiteral(0))])),FuncDecl(Id("foo1"),[],([],[Return(IntLiteral(1))])),FuncDecl(Id("foo2"),[],([],[Return(IntLiteral(2))])),FuncDecl(Id("foo3"),[],([],[Return(IntLiteral(3))])),FuncDecl(Id("foo4"),[],([],[Return(IntLiteral(4))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,78))

	def test_ast_079(self):
		input = """
		Function: foo
		Body:
			Return 0;
		EndBody.

		Function: foo
		Body:
			Return 1;
		EndBody.

		Function: foo
		Body:
			Return 2;
		EndBody.

		Function: foo
		Body:
			Return 3;
		EndBody.

		Function: foo
		Body:
			Return 4;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("foo"),[],([],[Return(IntLiteral(0))])),FuncDecl(Id("foo"),[],([],[Return(IntLiteral(1))])),FuncDecl(Id("foo"),[],([],[Return(IntLiteral(2))])),FuncDecl(Id("foo"),[],([],[Return(IntLiteral(3))])),FuncDecl(Id("foo"),[],([],[Return(IntLiteral(4))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,79))

	def test_ast_080(self):
		input = """
		**overload**
		Function: foo
		Parameter: x
		Body:
			Return x*x;
		EndBody.
		
		Function: foo
		Parameter: x,y
		Body:
			Return x+y;
		EndBody.

		Function: main
		Body:
			print(string_of_int(foo(10)));
			print(string_of_int(foo(10,15)));
		EndBody.
		"""
		expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[Return(BinaryOp('*',Id("x"),Id("x")))])),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[Return(BinaryOp('+',Id("x"),Id("y")))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[CallExpr(Id("foo"),[IntLiteral(10)])])]),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[CallExpr(Id("foo"),[IntLiteral(10),IntLiteral(15)])])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,80))

	def test_ast_081(self):
		input = """
		Function: main
		Body:
			Var: h_aogi_qiqit_nnnnawh;
			Var: khong_bietDat_tEN_GI = "KhoNgbIEtVieTGi";
			Var: i;
			For (i=0,i<1000,i+1) Do
				For (j=0,j<i,j+1) Do
					print("Haiz ");
				EndFor.
				printLn(" ");
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("h_aogi_qiqit_nnnnawh"),[],None),VarDecl(Id("khong_bietDat_tEN_GI"),[],StringLiteral("KhoNgbIEtVieTGi")),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(1000)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp('<',Id("j"),Id("i")),BinaryOp('+',Id("j"),IntLiteral(1)),([],[CallStmt(Id("print"),[StringLiteral("Haiz ")])])),CallStmt(Id("printLn"),[StringLiteral(" ")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,81))

	def test_ast_082(self):
		input = """
		Function: main
		Body:
			Var: fi,fo,in;
			fi = open("input.txt","r");
			in = fread(fi);
			close(fi);

			fo = open("output.txt","w");
			fwrite(fo,in);
			close(fo);
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("fi"),[],None),VarDecl(Id("fo"),[],None),VarDecl(Id("in"),[],None)],[Assign(Id("fi"),CallExpr(Id("open"),[StringLiteral("input.txt"),StringLiteral("r")])),Assign(Id("in"),CallExpr(Id("fread"),[Id("fi")])),CallStmt(Id("close"),[Id("fi")]),Assign(Id("fo"),CallExpr(Id("open"),[StringLiteral("output.txt"),StringLiteral("w")])),CallStmt(Id("fwrite"),[Id("fo"),Id("in")]),CallStmt(Id("close"),[Id("fo")])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,82))

	def test_ast_083(self):
		input = """
		Var: day_name[7] = {"Mon","Tue","Wed","Thu","Fri","Sat","Sun"};
		Function: main
		Body:
			Var: x;
			x = int_of_string(read());
			If (x<1) Then Return;
			EndIf.
			print(day_name[x%7]);
		EndBody.
		"""
		expect = Program([VarDecl(Id("day_name"),[7],ArrayLiteral([StringLiteral("Mon"),StringLiteral("Tue"),StringLiteral("Wed"),StringLiteral("Thu"),StringLiteral("Fri"),StringLiteral("Sat"),StringLiteral("Sun")])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('<',Id("x"),IntLiteral(1)),[],[Return(None)])], ([],[])),CallStmt(Id("print"),[ArrayCell(Id("day_name"),[BinaryOp('%',Id("x"),IntLiteral(7))])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,83))

	def test_ast_084(self):
		input = """
		Function: main
		Body:
			Var: stack = {},i;
			For (i=0, i<20, i+1) Do
				Var: n;
				n = random();
				If n>0 Then push(stack,n);
				Else 
					i = i + top(stack);
					pop(stack);
				EndIf.
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("stack"),[],ArrayLiteral([])),VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(20)),BinaryOp('+',Id("i"),IntLiteral(1)),([VarDecl(Id("n"),[],None)],[Assign(Id("n"),CallExpr(Id("random"),[])),If([(BinaryOp('>',Id("n"),IntLiteral(0)),[],[CallStmt(Id("push"),[Id("stack"),Id("n")])])], ([],[Assign(Id("i"),BinaryOp('+',Id("i"),CallExpr(Id("top"),[Id("stack")]))),CallStmt(Id("pop"),[Id("stack")])]))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,84))

	def test_ast_085(self):
		input = """
		Var: x,y,z;
		Function: main
		Parameter: y,b
		Body:
			Var: x,arr[10];
			x = arr[1] * arr[0] + arr[2] \\ arr[4];
			If (random() > 10) Then print("1");
				ElseIf (random() > 10) Then print("2");
				ElseIf (random() > 10) Then print("3");
				Else print(string_of_float(random()));
			EndIf.
		EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[VarDecl(Id("y"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("arr"),[10],None)],[Assign(Id("x"),BinaryOp('+',BinaryOp('*',ArrayCell(Id("arr"),[IntLiteral(1)]),ArrayCell(Id("arr"),[IntLiteral(0)])),BinaryOp('\\',ArrayCell(Id("arr"),[IntLiteral(2)]),ArrayCell(Id("arr"),[IntLiteral(4)])))),If([(BinaryOp('>',CallExpr(Id("random"),[]),IntLiteral(10)),[],[CallStmt(Id("print"),[StringLiteral("1")])]),(BinaryOp('>',CallExpr(Id("random"),[]),IntLiteral(10)),[],[CallStmt(Id("print"),[StringLiteral("2")])]),(BinaryOp('>',CallExpr(Id("random"),[]),IntLiteral(10)),[],[CallStmt(Id("print"),[StringLiteral("3")])])], ([],[CallStmt(Id("print"),[CallExpr(Id("string_of_float"),[CallExpr(Id("random"),[])])])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,85))

	def test_ast_086(self):
		input = """
		Function: main
		Body:
			Var: i,j,t,z=0;
			For (i=0,i<10,i+1) Do
				j = 0;
				While (j<20) Do
					t = 0;
					Do
						print(string_of_int(t));
						t = t + 1;
					While (t < 5)
					EndDo.
					j = j + 1;
				EndWhile.
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None),VarDecl(Id("t"),[],None),VarDecl(Id("z"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(Id("j"),IntLiteral(0)),While(BinaryOp('<',Id("j"),IntLiteral(20)),([],[Assign(Id("t"),IntLiteral(0)),Dowhile(([],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("t")])]),Assign(Id("t"),BinaryOp('+',Id("t"),IntLiteral(1)))]),BinaryOp('<',Id("t"),IntLiteral(5))),Assign(Id("j"),BinaryOp('+',Id("j"),IntLiteral(1)))]))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,86))

	def test_ast_087(self):
		input = """
		Function: main
		Body:
			Var: i,j,t = 10,z=2,isBreak=False;
			For (i=0, i<20, i+1) Do
				For (j=0, j<10, j+1) Do
					If (rand() > t) Then 
						Var: x ;
						Var: y = 1;
						x = rand();
						y = rand();
						print(string_of_float(x-y));
						isBreak = True;
						Break;
					ElseIf (rand()>z) Then 
						isBreak = True;
						Break;
					Else print(string_of_int(j*i + j + i));
					EndIf.
				EndFor.
				If (isBreak == True) Then 
					Var: str = "Bye";
					print(str);
					isBreak = False;
					Break;
				EndIf.
			EndFor.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None),VarDecl(Id("t"),[],IntLiteral(10)),VarDecl(Id("z"),[],IntLiteral(2)),VarDecl(Id("isBreak"),[],BooleanLiteral(False))],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(20)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp('<',Id("j"),IntLiteral(10)),BinaryOp('+',Id("j"),IntLiteral(1)),([],[If([(BinaryOp('>',CallExpr(Id("rand"),[]),Id("t")),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(1))],[Assign(Id("x"),CallExpr(Id("rand"),[])),Assign(Id("y"),CallExpr(Id("rand"),[])),CallStmt(Id("print"),[CallExpr(Id("string_of_float"),[BinaryOp('-',Id("x"),Id("y"))])]),Assign(Id("isBreak"),BooleanLiteral(True)),Break()]),(BinaryOp('>',CallExpr(Id("rand"),[]),Id("z")),[],[Assign(Id("isBreak"),BooleanLiteral(True)),Break()])], ([],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[BinaryOp('+',BinaryOp('+',BinaryOp('*',Id("j"),Id("i")),Id("j")),Id("i"))])])]))])),If([(BinaryOp('==',Id("isBreak"),BooleanLiteral(True)),[VarDecl(Id("str"),[],StringLiteral("Bye"))],[CallStmt(Id("print"),[Id("str")]),Assign(Id("isBreak"),BooleanLiteral(False)),Break()])], ([],[]))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,87))

	def test_ast_088(self):
		input = """
		Var: a,b=1,c=2,arr[0xFF],x,y,z=False;
		Function: main
		Parameter: b,d
		Body:
			Var: c=5,i = 0;
			For (i = 0, i<b, i+c) Do
				print(sing_of_int(i));
				print(" ");
				printLn(string_of_int(c));
			EndFor.
		EndBody.
		"""
		expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(1)),VarDecl(Id("c"),[],IntLiteral(2)),VarDecl(Id("arr"),[255],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],BooleanLiteral(False)),FuncDecl(Id("main"),[VarDecl(Id("b"),[],None),VarDecl(Id("d"),[],None)],([VarDecl(Id("c"),[],IntLiteral(5)),VarDecl(Id("i"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),Id("b")),BinaryOp('+',Id("i"),Id("c")),([],[CallStmt(Id("print"),[CallExpr(Id("sing_of_int"),[Id("i")])]),CallStmt(Id("print"),[StringLiteral(" ")]),CallStmt(Id("printLn"),[CallExpr(Id("string_of_int"),[Id("c")])])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,88))

	def test_ast_089(self):
		input = """
		Function: main
		Body:
			((((((foo((foo(1))))[12])[0o71]))))[12] = 1;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(ArrayCell(ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(1)])]),[IntLiteral(12)]),[IntLiteral(57)]),[IntLiteral(12)]),IntLiteral(1))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,89))

	def test_ast_090(self):
		input = """
		Function: main
		Body:
			Var: n = 10, res = 0;
			If (random()>n) Then 
				Var: x = 1;
				Var: t = 2;
				res = x && t;
			ElseIf (random() > n) Then
				Var: x = 2;
				Var: n = 3;
				res = res + 2;
				If (random() > n) Then
					Var: x = 4;
					print(string_of_int(n));
					res = res + 9;
				EndIf.
			EndIf. 
			print(string_of_int(res));
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("n"),[],IntLiteral(10)),VarDecl(Id("res"),[],IntLiteral(0))],[If([(BinaryOp('>',CallExpr(Id("random"),[]),Id("n")),[VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("t"),[],IntLiteral(2))],[Assign(Id("res"),BinaryOp('&&',Id("x"),Id("t")))]),(BinaryOp('>',CallExpr(Id("random"),[]),Id("n")),[VarDecl(Id("x"),[],IntLiteral(2)),VarDecl(Id("n"),[],IntLiteral(3))],[Assign(Id("res"),BinaryOp('+',Id("res"),IntLiteral(2))),If([(BinaryOp('>',CallExpr(Id("random"),[]),Id("n")),[VarDecl(Id("x"),[],IntLiteral(4))],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("n")])]),Assign(Id("res"),BinaryOp('+',Id("res"),IntLiteral(9)))])], ([],[]))])], ([],[])),CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[Id("res")])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,90))

	def test_ast_091(self):
		input = """
		Function: main
		Body:
			Var: arr[2][0xFF][0O11765466546];
			a[x+2*foo(2 + foo(foo(foo(x)))) + random()] = a[12 * x - foo(foo(foo(x)))[12] + a[x]];
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[2,255,1339452774],None)],[Assign(ArrayCell(Id("a"),[BinaryOp('+',BinaryOp('+',Id("x"),BinaryOp('*',IntLiteral(2),CallExpr(Id("foo"),[BinaryOp('+',IntLiteral(2),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("x")])])]))]))),CallExpr(Id("random"),[]))]),ArrayCell(Id("a"),[BinaryOp('+',BinaryOp('-',BinaryOp('*',IntLiteral(12),Id("x")),ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("x")])])]),[IntLiteral(12)])),ArrayCell(Id("a"),[Id("x")]))]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,91))

	def test_ast_092(self):
		input = """
		Function: main
		Body:
			Var: x = 1;
			x = -----------------------------------15;
			Do
				x = -----------x;
			While True
			EndDo.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(1))],[Assign(Id("x"),UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',IntLiteral(15))))))))))))))))))))))))))))))))))))),Dowhile(([],[Assign(Id("x"),UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',Id("x")))))))))))))]),BooleanLiteral(True))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,92))

	def test_ast_093(self):
		input = """
		Function: main
		Body:
			If ((1>0) && (5<=15) || (1. > -4)) Then print("HELLO");
			Else print("KHONG HELLO :)");
			EndIf.
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp('||',BinaryOp('&&',BinaryOp('>',IntLiteral(1),IntLiteral(0)),BinaryOp('<=',IntLiteral(5),IntLiteral(15))),BinaryOp('>',FloatLiteral(1.0),UnaryOp('-',IntLiteral(4)))),[],[CallStmt(Id("print"),[StringLiteral("HELLO")])])], ([],[CallStmt(Id("print"),[StringLiteral("KHONG HELLO :)")])]))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,93))

	def test_ast_094(self):
		input = """
		Function: main
		Body:
			Var: b = False;
			Var: i,n = 0;
			n = int_of_string(read());
			For (i=0,i<n,i+1) Do
				b = (!b) && (b||b);
			EndFor.
			print(string_of_bool(b));
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],BooleanLiteral(False)),VarDecl(Id("i"),[],None),VarDecl(Id("n"),[],IntLiteral(0))],[Assign(Id("n"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),Id("n")),BinaryOp('+',Id("i"),IntLiteral(1)),([],[Assign(Id("b"),BinaryOp('&&',UnaryOp('!',Id("b")),BinaryOp('||',Id("b"),Id("b"))))])),CallStmt(Id("print"),[CallExpr(Id("string_of_bool"),[Id("b")])])]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,94))

	def test_ast_095(self):
		input = """
		Function: main
		Body:
			For (i = 0, i<10, i+1) Do
			EndFor.
			Break;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp('<',Id("i"),IntLiteral(10)),BinaryOp('+',Id("i"),IntLiteral(1)),([],[])),Break()]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,95))

	def test_ast_096(self):
		input = """
		Function: main
		Body:
			Var: x,y,arr = {1,2,3,4,5,6},y[1] = 1;
			print();
			read();
			While (True) Do
				** do something **
			EndWhile.
			Return;
		EndBody.		
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("arr"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)])),VarDecl(Id("y"),[1],IntLiteral(1))],[CallStmt(Id("print"),[]),CallStmt(Id("read"),[]),While(BooleanLiteral(True),([],[])),Return(None)]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,96))

	def test_ast_097(self):
		input = """
		Function: main
		Body:
				** super super associated operators **
				a = (((((((a > 1) > 2) >. 3) >=. 4) && True) =/= True) == True) != False + 9*True*10*1.5*False;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp('!=',BinaryOp('==',BinaryOp('=/=',BinaryOp('&&',BinaryOp('>=.',BinaryOp('>.',BinaryOp('>',BinaryOp('>',Id("a"),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BooleanLiteral(True)),BooleanLiteral(True)),BooleanLiteral(True)),BinaryOp('+',BooleanLiteral(False),BinaryOp('*',BinaryOp('*',BinaryOp('*',BinaryOp('*',IntLiteral(9),BooleanLiteral(True)),IntLiteral(10)),FloatLiteral(1.5)),BooleanLiteral(False)))))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,97))

	def test_ast_098(self):
		input = """
		Var: a,b,c=3,d,e,stringlit = 5;
		Function: main
		Body:
			Var: x = 10,i;
			For (i = x, i > 0, i - 1) Do
				x = (x*0.5 + i * random());
			EndFor.
			Return x;
		EndBody.
		"""
		expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(3)),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("stringlit"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("i"),[],None)],[For(Id("i"),Id("x"),BinaryOp('>',Id("i"),IntLiteral(0)),BinaryOp('-',Id("i"),IntLiteral(1)),([],[Assign(Id("x"),BinaryOp('+',BinaryOp('*',Id("x"),FloatLiteral(0.5)),BinaryOp('*',Id("i"),CallExpr(Id("random"),[]))))])),Return(Id("x"))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,98))

	def test_ast_099(self):
		input = """
		Function: main
		Parameter: x,y,z
		Body:
			Var: num;
			num = int_of_string**HELLO TUI NE**(read());
			If x > num Then
				Return x;
			ElseIf y > num Then
				Return y;
			ElseIf z > num Then
				Return z;
			EndIf.
			Return -1;
		EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([VarDecl(Id("num"),[],None)],[Assign(Id("num"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),If([(BinaryOp('>',Id("x"),Id("num")),[],[Return(Id("x"))]),(BinaryOp('>',Id("y"),Id("num")),[],[Return(Id("y"))]),(BinaryOp('>',Id("z"),Id("num")),[],[Return(Id("z"))])], ([],[])),Return(UnaryOp('-',IntLiteral(1)))]))])

		self.assertTrue(TestAST.checkASTGen(input,expect,99))

