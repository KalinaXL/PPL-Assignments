.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[[[[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	iconst_1
	iastore
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_1
	iaload
	iastore
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	iaload
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_1
	iaload
	bipush 20
	isub
	iconst_2
	isub
	bipush 9
	isub
	aaload
	getstatic MCClass/x [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	iaload
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
	iconst_1
	anewarray [[[[I
	dup
	iconst_0
	iconst_1
	anewarray [[[I
	dup
	iconst_0
	iconst_1
	anewarray [[I
	dup
	iconst_0
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	bipush 32
	iastore
	aastore
	dup
	iconst_2
	iconst_2
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 22
	iastore
	aastore
	aastore
	aastore
	aastore
	putstatic MCClass/x [[[[[I
Label1:
	return
.limit stack 23
.limit locals 0
.end method
