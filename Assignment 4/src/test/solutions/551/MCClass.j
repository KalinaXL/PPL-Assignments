.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo()F
Label0:
	getstatic MCClass/x [F
	iconst_0
	ldc 100.222
	fneg
	fastore
	getstatic MCClass/x [F
	iconst_0
	faload
	freturn
Label1:
.limit stack 3
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
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.2
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	putstatic MCClass/x [F
Label1:
	return
.limit stack 5
.limit locals 0
.end method
