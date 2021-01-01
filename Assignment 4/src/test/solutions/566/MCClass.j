.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is u I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is y I from Label0 to Label1
	iconst_3
	istore_3
.var 4 is z I from Label0 to Label1
	iconst_3
	istore 4
	invokestatic MCClass/test()V
Label1:
	return
.limit stack 1
.limit locals 5
.end method

.method public static test()V
Label0:
.var 0 is i I from Label0 to Label1
	iconst_0
	istore_0
	iconst_0
	istore_0
Label4:
	iload_0
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 1 is s [I from Label7 to Label8
	bipush 9
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
	astore_1
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	iconst_2
	iadd
	istore_0
	iload_0
	iconst_5
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label13:
	goto Label3
Label14:
	goto Label9
Label10:
Label15:
	goto Label2
Label16:
Label9:
Label8:
Label2:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label4
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
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
