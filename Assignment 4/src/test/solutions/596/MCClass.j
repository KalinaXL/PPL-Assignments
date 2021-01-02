.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static cout([Ljava/lang/String;)V
.var 0 is arr [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label4:
Label5:
	aload_0
	iload_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
Label2:
	iload_1
	iconst_5
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label4
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "AE"
	aastore
	dup
	iconst_1
	ldc "YU"
	aastore
	dup
	iconst_2
	ldc "QW"
	aastore
	dup
	iconst_3
	ldc "OI"
	aastore
	dup
	iconst_4
	ldc "PT"
	aastore
	invokestatic MCClass/cout([Ljava/lang/String;)V
Label1:
	return
.limit stack 5
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
