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
	iconst_1
	ifle Label3
Label4:
.var 0 is x [I from Label4 to Label5
	iconst_5
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
	astore_0
.var 1 is i I from Label4 to Label5
	iconst_0
	istore_1
Label6:
	iload_1
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
Label10:
.var 2 is y [F from Label10 to Label11
	iconst_5
	newarray float
	dup
	iconst_0
	ldc 1.2
	fastore
	dup
	iconst_1
	ldc 3.4
	fastore
	dup
	iconst_2
	ldc 4.2
	fastore
	dup
	iconst_3
	ldc 4.9
	fastore
	dup
	iconst_4
	ldc 2.4
	fastore
	astore_2
	aload_0
	iload_1
	iaload
	aload_2
	iload_1
	faload
	invokestatic io/int_of_float(F)I
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
Label16:
	aload_2
	iload_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label17:
	goto Label12
Label13:
Label18:
.var 3 is y Ljava/lang/String; from Label18 to Label19
	ldc "hello"
	astore_3
	aload_3
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label19:
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
Label11:
	goto Label6
Label7:
Label5:
	goto Label2
Label3:
Label2:
Label1:
	return
.limit stack 9
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
