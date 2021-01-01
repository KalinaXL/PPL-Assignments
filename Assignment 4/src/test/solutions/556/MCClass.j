.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label4:
Label5:
	getstatic MCClass/x [Ljava/lang/String;
	iload_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	bipush 9
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
Label11:
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	goto Label7
Label8:
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
Label2:
	iload_1
	bipush 10
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label4
Label3:
Label1:
	return
.limit stack 5
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
	bipush 10
	anewarray java/lang/String
	dup
	iconst_0
	ldc "This"
	aastore
	dup
	iconst_1
	ldc "is"
	aastore
	dup
	iconst_2
	ldc "a"
	aastore
	dup
	iconst_3
	ldc "simple"
	aastore
	dup
	iconst_4
	ldc "testcase"
	aastore
	dup
	iconst_5
	ldc "and"
	aastore
	dup
	bipush 6
	ldc "it"
	aastore
	dup
	bipush 7
	ldc "passes"
	aastore
	dup
	bipush 8
	ldc "doesn\'t"
	aastore
	dup
	bipush 9
	ldc "it?"
	aastore
	putstatic MCClass/x [Ljava/lang/String;
Label1:
	return
.limit stack 5
.limit locals 0
.end method
