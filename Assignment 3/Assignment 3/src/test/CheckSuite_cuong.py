import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
	def test_checker_000(self):
		input = """
		Var: x,z;
		Var: b,c,a;
		Function: main
		Parameter: x
		Body:
			Var: d,e;
			x = 1.;
		EndBody.

		Function: foo
		Parameter: x
		Body:
			Var: d,q,w;
			x = 1;
			z = x;
			d = 3;
			foo(1);
		EndBody.
		"""
		expect = "successful"
		self.assertTrue(TestChecker.test(input,expect,0))

	def test_checker_001(self):
		input = """
		Var: x;
		Function: main
		Parameter: x,y,z,t,q,w,y
		Body:
			Var: d,e;
			x = 1;
			printStr("Hello world!");
		EndBody.
		"""
		expect = str(Redeclared(Parameter(),'y'))
		self.assertTrue(TestChecker.test(input,expect,1))

	def test_checker_002(self):
		input = """
		Var: x;
		Function: main
		Body:
			If (x>1) Then 
				Var: x,y;
				x = x + y;
			ElseIf (x>0) Then
				Var: z;
				x = x + z;
			Else 
				Var: t,z;
				x = x + y;
			EndIf.
		EndBody.
		"""
		expect = str(Undeclared(Identifier(),'y'))
		self.assertTrue(TestChecker.test(input,expect,2))

	def test_checker_003(self):
		input = """
		Var: x,g;
		Function: main
		Body:
			Var: y = 1,z = 2,t;
			If (x>1) Then
				Var: z = 5;
				If (y>0) Then
					Var: x,d;
					g = 1;
				EndIf.
			EndIf.
		EndBody.
		"""
		expect = "successful"
		self.assertTrue(TestChecker.test(input,expect,3))

	def test_checker_004(self):
		input = """
		Var: x;
		Function: main
		Body:
			Var: x,y;
			x = y;
		EndBody.
		"""
		expect = "Type Cannot Be Inferred: Assign(Id(x),Id(y))"
		self.assertTrue(TestChecker.test(input,expect,4))

	def test_checker_005(self):
		input = """
		Var: x;
		Function: main
		Body:
			Var: y = 5, z, t, n;
			z = --(-(y*3)+8)*15 + 26;
			y = --(-(n*3)+8)*15 + 26;
			t = True && y;
		EndBody.
		"""
		expect = 'Type Mismatch In Expression: BinaryOp(&&,BooleanLiteral(true),Id(y))'
		self.assertTrue(TestChecker.test(input,expect,5))

	def test_checker_006(self):
		input = """
		Var: x;
		Function: main
		Body:
			Var: y = 1, z;
			y = x + z;
		EndBody.
		"""
		expect = 'successful'
		self.assertTrue(TestChecker.test(input,expect,6))

	def test_checker_007(self):
		input = """
		Var: x;
		Function: main
		Body:
			If (x>1) Then
				x = !x;
			EndIf.
		EndBody.
		"""
		expect = 'Type Mismatch In Expression: UnaryOp(!,Id(x))'
		self.assertTrue(TestChecker.test(input,expect,7))

	def test_checker_008(self):
		input = """
		Var: x;
		
		Function: foo
		Parameter: x
		Body:
			x = 1;
			Return x;
		EndBody.
		
		Function: main		
		Body:
			Var: y;
			y = True;
			foo(y);
		EndBody.
		"""
		expect = 'Type Mismatch In Statement: CallStmt(Id(foo),[Id(y)])'
		self.assertTrue(TestChecker.test(input,expect,8))

	def test_checker_009(self):
		input = """
		Var: x;

		Function: foo
		Parameter: a
		Body:
			a = 1;
		EndBody.

		Function: main
		Body:
			Var: x;
			foo(1);
			foo(x);			
		EndBody.
		"""
		expect = 'successful'
		self.assertTrue(TestChecker.test(input,expect,9))

	def test_checker_010(self):
		input = """
		Var: x,y;
		Function: main
		Body:
			x = foo(1);
			y = foo1();
		EndBody.

		Function: foo
		Parameter: x
		Body:
			Return 0;
		EndBody.

		Function: foo1
		Body:
			Return 1.;
		EndBody.
		
		Function: foo2
		Body:
			Return 1.;
		EndBody.
		"""
		expect = 'Unreachable Function: foo2'
		self.assertTrue(TestChecker.test(input,expect,10))

	def test_checker_011(self):
		input = """
		Var: x,y;
		Function: main
		Body:
			y = 1;
			y = foo(x);
		EndBody.

		Function: foo
		Parameter: x
		Body:
			x = 1;
			If (x>0) Then EndIf.
			Return 0;			
		EndBody.
		"""
		expect = None
		self.assertTrue(TestChecker.test(input,expect,11))

	def test_checker_012(self):
		input = """
		Var: x;
		Function: main
		Body:
			foo(1);
			Return True;
		EndBody.

		Function: foo
		Body:
			main();
			Return True;
		EndBody.
		"""
		expect = None
		self.assertTrue(TestChecker.test(input,expect,12))

	# def test_checker_013(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,13))

	# def test_checker_014(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,14))

	# def test_checker_015(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,15))

	# def test_checker_016(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,16))

	# def test_checker_017(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,17))

	# def test_checker_018(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,18))

	# def test_checker_019(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,19))

	# def test_checker_020(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,20))

	# def test_checker_021(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,21))

	# def test_checker_022(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,22))

	# def test_checker_023(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,23))

	# def test_checker_024(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,24))

	# def test_checker_025(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,25))

	# def test_checker_026(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,26))

	# def test_checker_027(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,27))

	# def test_checker_028(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,28))

	# def test_checker_029(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,29))

	# def test_checker_030(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,30))

	# def test_checker_031(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,31))

	# def test_checker_032(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,32))

	# def test_checker_033(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,33))

	# def test_checker_034(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,34))

	# def test_checker_035(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,35))

	# def test_checker_036(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,36))

	# def test_checker_037(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,37))

	# def test_checker_038(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,38))

	# def test_checker_039(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,39))

	# def test_checker_040(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,40))

	# def test_checker_041(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,41))

	# def test_checker_042(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,42))

	# def test_checker_043(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,43))

	# def test_checker_044(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,44))

	# def test_checker_045(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,45))

	# def test_checker_046(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,46))

	# def test_checker_047(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,47))

	# def test_checker_048(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,48))

	# def test_checker_049(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,49))

	# def test_checker_050(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,50))

	# def test_checker_051(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,51))

	# def test_checker_052(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,52))

	# def test_checker_053(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,53))

	# def test_checker_054(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,54))

	# def test_checker_055(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,55))

	# def test_checker_056(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,56))

	# def test_checker_057(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,57))

	# def test_checker_058(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,58))

	# def test_checker_059(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,59))

	# def test_checker_060(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,60))

	# def test_checker_061(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,61))

	# def test_checker_062(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,62))

	# def test_checker_063(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,63))

	# def test_checker_064(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,64))

	# def test_checker_065(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,65))

	# def test_checker_066(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,66))

	# def test_checker_067(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,67))

	# def test_checker_068(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,68))

	# def test_checker_069(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,69))

	# def test_checker_070(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,70))

	# def test_checker_071(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,71))

	# def test_checker_072(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,72))

	# def test_checker_073(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,73))

	# def test_checker_074(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,74))

	# def test_checker_075(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,75))

	# def test_checker_076(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,76))

	# def test_checker_077(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,77))

	# def test_checker_078(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,78))

	# def test_checker_079(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,79))

	# def test_checker_080(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,80))

	# def test_checker_081(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,81))

	# def test_checker_082(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,82))

	# def test_checker_083(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,83))

	# def test_checker_084(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,84))

	# def test_checker_085(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,85))

	# def test_checker_086(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,86))

	# def test_checker_087(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,87))

	# def test_checker_088(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,88))

	# def test_checker_089(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,89))

	# def test_checker_090(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,90))

	# def test_checker_091(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,91))

	# def test_checker_092(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,92))

	# def test_checker_093(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,93))

	# def test_checker_094(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,94))

	# def test_checker_095(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,95))

	# def test_checker_096(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,96))

	# def test_checker_097(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,97))

	# def test_checker_098(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,98))

	# def test_checker_099(self):
	# 	input = """
	# 	Var: x;
	# 	Function: main
	# 	Body:
			
	# 	EndBody.
	# 	"""
	# 	expect = None
	# 	self.assertTrue(TestChecker.test(input,expect,99))

