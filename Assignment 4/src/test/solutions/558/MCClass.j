.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is k I from Label0 to Label1
	iconst_4
	istore_1
Label2:
	iload_1
	iconst_0
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_1
	invokestatic MCClass/foo()I
	isub
	istore_1
	iload_1
	iconst_0
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	ldc "OutOutOut"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label3
Label13:
	goto Label8
Label9:
Label8:
	getstatic MCClass/x [Ljava/lang/String;
	iload_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static foo()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 0
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
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "A"
	aastore
	dup
	iconst_1
	ldc "B"
	aastore
	dup
	iconst_2
	ldc "C"
	aastore
	dup
	iconst_3
	ldc "D"
	aastore
	dup
	iconst_4
	ldc "E"
	aastore
	putstatic MCClass/x [Ljava/lang/String;
Label1:
	return
.limit stack 5
.limit locals 0
.end method
