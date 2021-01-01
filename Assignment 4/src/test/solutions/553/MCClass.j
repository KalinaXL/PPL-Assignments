.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [F from Label0 to Label1
	bipush 10
	newarray float
	dup
	iconst_0
	ldc 0.1
	fastore
	dup
	iconst_1
	ldc 0.2
	fastore
	dup
	iconst_2
	ldc 0.3
	fastore
	dup
	iconst_3
	ldc 0.4
	fastore
	dup
	iconst_4
	ldc 0.5
	fastore
	dup
	iconst_5
	ldc 0.6
	fastore
	dup
	bipush 6
	ldc 0.7
	fastore
	dup
	bipush 7
	ldc 0.8
	fastore
	dup
	bipush 8
	ldc 0.9
	fastore
	dup
	bipush 9
	ldc 1.0
	fastore
	astore_1
.var 2 is b F from Label0 to Label1
	ldc 1.1
	fstore_2
.var 3 is c F from Label0 to Label1
	ldc 3.3
	fstore_3
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
	aload_1
	bipush 9
	fload_2
	fload_3
	fmul
	fastore
	aload_1
	invokestatic MCClass/foo([F)[F
	astore_1
	aload_1
	invokestatic MCClass/foo([F)[F
	fload_2
	invokestatic io/int_of_float(F)I
	bipush 10
	invokestatic io/float_to_int(I)F
	fastore
	iconst_0
	istore 4
Label4:
	iload 4
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_1
	iload 4
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label4
Label3:
Label1:
	return
.limit stack 5
.limit locals 5
.end method

.method public static foo([F)[F
.var 0 is a [F from Label0 to Label1
Label0:
	aload_0
	areturn
Label1:
.limit stack 1
.limit locals 1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
