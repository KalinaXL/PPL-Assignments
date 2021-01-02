.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I
.field static a [I
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/a [I
	iconst_0
	invokestatic MCClass/test()I
	getstatic MCClass/b [I
	iconst_2
	iaload
	imul
	iastore
	iconst_0
	putstatic MCClass/x I
Label4:
	getstatic MCClass/x I
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	getstatic MCClass/a [I
	getstatic MCClass/x I
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	getstatic MCClass/x I
	iconst_1
	iadd
	putstatic MCClass/x I
	goto Label4
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static f(II)[I
.var 0 is z I from Label0 to Label1
.var 1 is t I from Label0 to Label1
Label0:
	getstatic MCClass/a [I
	iconst_1
	sipush 750
	iastore
	getstatic MCClass/a [I
	areturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static test()I
Label0:
	iconst_2
	iconst_5
	invokestatic MCClass/f(II)[I
	getstatic MCClass/x I
	iaload
	ireturn
Label1:
.limit stack 2
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
	iconst_1
	putstatic MCClass/x I
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 100
	iastore
	dup
	iconst_2
	bipush 100
	iastore
	putstatic MCClass/a [I
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	bipush 6
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	dup
	iconst_3
	bipush 8
	iastore
	dup
	iconst_4
	bipush 10
	iastore
	putstatic MCClass/b [I
Label1:
	return
.limit stack 6
.limit locals 0
.end method
