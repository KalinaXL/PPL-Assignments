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
	getstatic MCClass/x [Z
	iconst_1
	baload
	iand
	ifle Label3
	ldc "A"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
Label2:
Label8:
	getstatic MCClass/x [Z
	iload_1
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
	iload_1
	iconst_4
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label8
Label7:
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
	iconst_0
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
