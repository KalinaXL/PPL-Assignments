.source MCClass.java
.class public MCClass
.super java.lang.Object

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
	bipush 7
	istore_2
.var 3 is b I from Label0 to Label1
	iconst_4
	istore_3
	iload_2
	bipush 7
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	dup
	ifle Label8
	aload_1
	iload_2
	iaload
	bipush 10
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
Label8:
	ifle Label3
Label9:
Label10:
	goto Label2
Label3:
Label2:
Label1:
	return
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
