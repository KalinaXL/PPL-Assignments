.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	getstatic MCClass/x [Z
	iconst_0
	baload
	dup
	ifle Label4
	getstatic MCClass/x [Z
	iconst_1
	baload
	iand
Label4:
	ifle Label3
Label5:
	ldc "A"
	invokestatic io/print(Ljava/lang/String;)V
Label6:
	goto Label2
Label3:
Label2:
Label1:
	return
.limit stack 3
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
	iconst_4
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	dup
	iconst_3
	iconst_1
	bastore
	putstatic MCClass/x [Z
Label1:
	return
.limit stack 9
.limit locals 0
.end method
