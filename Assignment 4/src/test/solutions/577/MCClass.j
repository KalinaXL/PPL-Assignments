.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I
.field static i I

.method public static foo()[I
Label0:
	getstatic MCClass/arr [I
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()[I
	bipush 7
	invokestatic MCClass/foo()[I
	bipush 9
	iaload
	iastore
	invokestatic MCClass/foo()[I
	bipush 7
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	invokestatic MCClass/foo()[I
	bipush 9
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
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	dup
	iconst_5
	iconst_5
	iastore
	dup
	bipush 6
	bipush 6
	iastore
	dup
	bipush 7
	bipush 7
	iastore
	dup
	bipush 8
	bipush 8
	iastore
	dup
	bipush 9
	bipush 9
	iastore
	putstatic MCClass/arr [I
	iconst_0
	putstatic MCClass/i I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
