.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is str [[Ljava/lang/String; from Label0 to Label1
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "true"
	aastore
	dup
	iconst_1
	ldc "01"
	aastore
	dup
	iconst_2
	ldc "02"
	aastore
	aastore
	dup
	iconst_1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "10"
	aastore
	dup
	iconst_1
	ldc "11"
	aastore
	dup
	iconst_2
	ldc "12"
	aastore
	aastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label4:
Label5:
	aload_1
	iload_2
	iconst_3
	idiv
	aaload
	iload_2
	iconst_3
	irem
	aaload
	invokestatic io/bool_of_string(Ljava/lang/String;)Z
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
Label2:
	iload_2
	bipush 6
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
.limit stack 10
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
