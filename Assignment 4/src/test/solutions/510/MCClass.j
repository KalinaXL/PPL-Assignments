.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is idx I from Label0 to Label1
	iconst_0
	istore_1
	invokestatic MCClass/foo()V
Label2:
	iload_1
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MCClass/x [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static foo()V
Label0:
.var 0 is i I from Label0 to Label1
	iconst_3
	istore_0
	iconst_3
	istore_0
Label4:
	iload_0
	invokestatic MCClass/cond(I)Z
	ifle Label3
	getstatic MCClass/x [I
	iload_0
	bipush 22
	iastore
Label2:
	iload_0
	invokestatic MCClass/up()I
	iadd
	istore_0
	goto Label4
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static cond(I)Z
.var 0 is x I from Label0 to Label1
Label0:
.var 1 is upper_bound I from Label0 to Label1
	bipush 6
	istore_1
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

.method public static up()I
Label0:
	iconst_5
	iconst_2
	idiv
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
