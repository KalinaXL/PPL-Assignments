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
Label9:
Label10:
	getstatic MCClass/x [Z
	iload_1
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label11:
Label7:
	iload_1
	iconst_4
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label9
Label8:
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
