.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static identity(Ljava/lang/String;)I
.var 0 is x Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokestatic io/float_of_string(Ljava/lang/String;)F
	invokestatic io/int_of_float(F)I
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/arr [I
	getstatic MCClass/arr [I
	getstatic MCClass/arr [I
	getstatic MCClass/arr [I
	ldc "2.424"
	invokestatic MCClass/identity(Ljava/lang/String;)I
	iaload
	iaload
	iaload
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
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
	bipush 8
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	putstatic MCClass/arr [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
