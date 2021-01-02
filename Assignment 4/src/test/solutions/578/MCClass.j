.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x F
.field static a [Z
.field static b [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label4:
Label5:
	getstatic MCClass/b [Ljava/lang/String;
	getstatic MCClass/x F
	invokestatic io/int_of_float(F)I
	aaload
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/x F
	ldc 1.0
	fadd
	putstatic MCClass/x F
	getstatic MCClass/x F
	ldc 2.001
	fcmpl
	ifgt Label10
	iconst_0
	goto Label9
Label10:
	iconst_1
Label9:
	ifle Label8
Label11:
	goto Label3
Label12:
	goto Label7
Label8:
Label7:
Label6:
Label2:
	getstatic MCClass/a [Z
	iconst_1
	baload
	invokestatic MCClass/f(Z)Z
	dup
	ifgt Label13
	getstatic MCClass/a [Z
	iconst_2
	baload
	invokestatic MCClass/f(Z)Z
	ior
Label13:
	ifgt Label4
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static f(Z)Z
.var 0 is k Z from Label0 to Label1
Label0:
	getstatic MCClass/b [Ljava/lang/String;
	iconst_1
	ldc "dasd"
	aastore
	iconst_1
	ireturn
Label1:
.limit stack 3
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
	ldc 0.0
	putstatic MCClass/x F
	iconst_4
	newarray boolean
	dup
	iconst_0
	iconst_0
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
	putstatic MCClass/a [Z
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "A1"
	aastore
	dup
	iconst_1
	ldc "B2"
	aastore
	dup
	iconst_2
	ldc "C3"
	aastore
	dup
	iconst_3
	ldc "D4"
	aastore
	dup
	iconst_4
	ldc "E5"
	aastore
	putstatic MCClass/b [Ljava/lang/String;
Label1:
	return
.limit stack 10
.limit locals 0
.end method
