.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static fibonaci(I)V
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is x [I from Label0 to Label1
	bipush 21
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_0
	iastore
	dup
	bipush 6
	iconst_0
	iastore
	dup
	bipush 7
	iconst_0
	iastore
	dup
	bipush 8
	iconst_0
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	dup
	bipush 10
	iconst_0
	iastore
	dup
	bipush 11
	iconst_0
	iastore
	dup
	bipush 12
	iconst_0
	iastore
	dup
	bipush 13
	iconst_0
	iastore
	dup
	bipush 14
	iconst_0
	iastore
	dup
	bipush 15
	iconst_0
	iastore
	dup
	bipush 16
	iconst_0
	iastore
	dup
	bipush 17
	iconst_0
	iastore
	dup
	bipush 18
	iconst_0
	iastore
	dup
	bipush 19
	iconst_0
	iastore
	dup
	bipush 20
	iconst_0
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_2
	istore_2
Label2:
	iload_2
	iload_0
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	aload_1
	iload_2
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	aload_1
	iload_2
	iconst_2
	isub
	iaload
	iadd
	iastore
	iload_2
	iconst_1
	iadd
	istore_2
Label7:
	goto Label2
Label3:
	aload_1
	iload_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 20
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
