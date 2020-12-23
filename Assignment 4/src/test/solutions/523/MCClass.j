.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I
.field static i I

.method public static foo(I)[I
.var 0 is flag I from Label0 to Label1
Label0:
.var 1 is k [I from Label0 to Label1
	iconst_4
	newarray int
	dup
	iconst_0
	bipush 11
	iastore
	dup
	iconst_1
	bipush 22
	iastore
	dup
	iconst_2
	bipush 33
	iastore
	dup
	iconst_3
	bipush 44
	iastore
	astore_1
	iconst_2
	ineg
	putstatic MCClass/i I
Label2:
	iload_0
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	getstatic MCClass/arr [I
	areturn
Label7:
	goto Label2
Label3:
	aload_1
	areturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
	iconst_3
	istore_1
	iconst_0
	invokestatic MCClass/foo(I)[I
	iconst_1
	invokestatic MCClass/foo(I)[I
	iconst_1
	iaload
	getstatic MCClass/i I
	iastore
	getstatic MCClass/i I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label2:
	iload_1
	iconst_1
	ineg
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	getstatic MCClass/arr [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	invokestatic MCClass/foo(I)[I
	iconst_1
	invokestatic MCClass/foo(I)[I
	iconst_1
	iaload
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	isub
	istore_1
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 5
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
	putstatic MCClass/arr [I
	iconst_2
	putstatic MCClass/i I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
