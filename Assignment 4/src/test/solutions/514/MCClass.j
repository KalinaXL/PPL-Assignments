.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/x [F
	iconst_0
	faload
	getstatic MCClass/x [F
	iconst_1
	faload
	invokestatic MCClass/swap(FF)V
	getstatic MCClass/x [F
	iconst_0
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/x [F
	iconst_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static swap(FF)V
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
.var 2 is i F from Label0 to Label1
	ldc 3.2
	fstore_2
	fload_0
	fstore_2
	fload_1
	fstore_0
	fload_2
	fstore_1
Label1:
	return
.limit stack 1
.limit locals 3
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
	iconst_5
	newarray float
	dup
	iconst_0
	ldc 0.1
	fastore
	dup
	iconst_1
	ldc 1.2
	fastore
	dup
	iconst_2
	ldc 2.4
	fastore
	dup
	iconst_3
	ldc 3.5
	fastore
	dup
	iconst_4
	ldc 4.3
	fastore
	putstatic MCClass/x [F
Label1:
	return
.limit stack 5
.limit locals 0
.end method
