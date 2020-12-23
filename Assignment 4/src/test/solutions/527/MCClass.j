.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label4:
Label5:
	iload_1
	invokestatic MCClass/foo(I)Z
	ifle Label8
Label9:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label10:
	goto Label7
Label8:
Label7:
Label6:
Label2:
	iload_1
	bipush 20
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label4
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static foo(I)Z
.var 0 is number I from Label0 to Label1
Label0:
.var 1 is iter I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is upper I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is sum F from Label0 to Label1
	ldc 0.0
	fstore_3
	iconst_2
	iload_0
	imul
	iconst_1
	isub
	istore_2
	iconst_1
	istore_1
Label4:
	iload_1
	iload_2
	invokestatic io/float_to_int(I)F
	invokestatic io/int_of_float(F)I
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	fload_3
	iload_1
	invokestatic io/float_to_int(I)F
	fadd
	fstore_3
	iload_1
	iconst_1
	iadd
	istore_1
Label8:
Label2:
	iload_1
	ldc 1.24
	invokestatic io/int_of_float(F)I
	iadd
	istore_1
	goto Label4
Label3:
	fload_3
	iload_0
	invokestatic io/float_to_int(I)F
	iload_0
	invokestatic io/float_to_int(I)F
	fmul
	if_icmpeq Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	freturn
Label1:
.limit stack 8
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	bipush 20
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	bipush 10
	iastore
	dup
	bipush 10
	bipush 11
	iastore
	dup
	bipush 11
	bipush 12
	iastore
	dup
	bipush 12
	bipush 13
	iastore
	dup
	bipush 13
	bipush 14
	iastore
	dup
	bipush 14
	bipush 15
	iastore
	dup
	bipush 15
	bipush 16
	iastore
	dup
	bipush 16
	bipush 17
	iastore
	dup
	bipush 17
	bipush 18
	iastore
	dup
	bipush 18
	bipush 19
	iastore
	dup
	bipush 19
	bipush 20
	iastore
	putstatic MCClass/arr [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
