.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static fibonaci(I)V
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_2
	istore_1
.var 2 is f I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is g I from Label0 to Label1
	iconst_1
	istore_3
	iconst_2
	istore_1
Label4:
	iload_1
	iload_0
	iconst_1
	iadd
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_2
	iload_3
	iadd
	istore_3
	iload_3
	iload_2
	isub
	istore_2
Label8:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 30
	invokestatic MCClass/fibonaci(I)V
Label1:
	return
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
