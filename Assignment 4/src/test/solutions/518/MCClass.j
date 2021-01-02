.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[[F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 2 is k I from Label7 to Label8
	iconst_0
	istore_2
Label9:
	iload_2
	iconst_1
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label13:
.var 3 is h I from Label13 to Label14
	iconst_0
	istore_3
Label17:
Label18:
	getstatic MCClass/x [[[F
	iload_1
	aaload
	invokestatic MCClass/foo()I
	iconst_1
	isub
	aaload
	iload_3
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	istore_3
Label19:
Label15:
	iload_3
	iconst_2
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label17
Label16:
	iload_2
	iconst_1
	iadd
	istore_2
Label14:
	goto Label9
Label10:
Label8:
Label2:
	iload_1
	invokestatic MCClass/foo()I
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 8
.limit locals 4
.end method

.method public static foo()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 0
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
	iconst_2
	anewarray [[F
	dup
	iconst_0
	iconst_1
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 2.2
	fastore
	dup
	iconst_1
	ldc 4.3
	fastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.2
	fastore
	dup
	iconst_1
	ldc 3.4
	fastore
	aastore
	aastore
	putstatic MCClass/x [[[F
Label1:
	return
.limit stack 15
.limit locals 0
.end method
