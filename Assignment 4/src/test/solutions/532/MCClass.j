.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([III)V
.var 0 is arr [I from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
Label0:
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iconst_1
	iadd
	iastore
	iload_2
	istore_1
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x [I from Label0 to Label1
	bipush 7
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 80
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 90
	iastore
	dup
	iconst_4
	bipush 40
	iastore
	dup
	iconst_5
	bipush 50
	iastore
	dup
	bipush 6
	bipush 70
	iastore
	astore_1
.var 2 is a I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is b I from Label0 to Label1
	iconst_4
	istore_3
	aload_1
	iload_2
	iload_3
	invokestatic MCClass/foo([III)V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
