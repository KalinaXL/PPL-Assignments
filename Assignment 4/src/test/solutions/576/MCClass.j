.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_3
	istore_1
	iconst_2
	iload_1
	iadd
	istore_1
	iconst_2
	invokestatic MCClass/foo(I)I
	istore_1
	iconst_3
	invokestatic MCClass/foo(I)I
	iconst_1
	iadd
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static foo(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	istore_0
	iconst_5
	ireturn
Label1:
.limit stack 2
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
	iconst_1
	putstatic MCClass/x I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
