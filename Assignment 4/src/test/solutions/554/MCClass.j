.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is c I from Label0 to Label1
	iconst_3
	istore_2
	getstatic MCClass/x [I
	bipush 9
	iload_1
	iload_2
	imul
	iastore
Label4:
Label5:
	getstatic MCClass/x [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
Label2:
	iload_1
	bipush 10
	invokestatic MCClass/check(II)Z
	ifgt Label4
Label3:
	invokestatic MCClass/foo()[I
	putstatic MCClass/x [I
	iconst_0
	bipush 8
	imul
	istore_1
	invokestatic MCClass/foo()[I
	iload_1
	ldc 20.5
	invokestatic io/int_of_float(F)I
	iastore
Label7:
	iload_1
	bipush 10
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
Label11:
	invokestatic MCClass/foo()[I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label12:
	goto Label7
Label8:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static foo()[I
Label0:
	getstatic MCClass/x [I
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static check(II)Z
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
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
	putstatic MCClass/x [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
