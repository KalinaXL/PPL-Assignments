.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I
.field static i I

.method public static f()I
Label0:
	getstatic MCClass/i I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	sipush 5555
	putstatic MCClass/i I
	getstatic MCClass/i I
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/f()I
	putstatic MCClass/i I
	getstatic MCClass/i I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
	iconst_4
	newarray int
	dup
	iconst_0
	sipush 1111
	iastore
	dup
	iconst_1
	sipush 2222
	iastore
	dup
	iconst_2
	sipush 3333
	iastore
	dup
	iconst_3
	sipush 4444
	iastore
	putstatic MCClass/arr [I
	sipush 7777
	putstatic MCClass/i I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
