.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F
.field static b Z
.field static arr [[Ljava/lang/String;

.method public static f()[[Ljava/lang/String;
Label0:
	getstatic MCClass/arr [[Ljava/lang/String;
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/f()[[Ljava/lang/String;
	iconst_1
	aaload
	iconst_0
	ldc "a * 2"
	aastore
	getstatic MCClass/arr [[Ljava/lang/String;
	iconst_0
	aaload
	iconst_1
	ldc "PPL!!! hard!!!"
	aastore
	getstatic MCClass/arr [[Ljava/lang/String;
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/arr [[Ljava/lang/String;
	iconst_0
	aaload
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/arr [[Ljava/lang/String;
	iconst_1
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/arr [[Ljava/lang/String;
	iconst_1
	aaload
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
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
	putstatic MCClass/a F
	iconst_0
	putstatic MCClass/b Z
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Subject"
	aastore
	dup
	iconst_1
	ldc "Mandatory"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "PPL"
	aastore
	dup
	iconst_1
	ldc "Harmonic mean"
	aastore
	aastore
	putstatic MCClass/arr [[Ljava/lang/String;
Label1:
	return
.limit stack 11
.limit locals 0
.end method
