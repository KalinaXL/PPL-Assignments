.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([I)I
.var 0 is x [I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
Label2:
	aload_0
	iload_1
	iaload
	aload_0
	iconst_0
	iaload
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
Label7:
	goto Label2
Label3:
	iload_1
	ireturn
Label1:
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	newarray int
	dup
	iconst_0
	bipush 100
	iastore
	dup
	iconst_1
	bipush 42
	iastore
	dup
	iconst_2
	iconst_4
	iastore
	dup
	iconst_3
	iconst_2
	iastore
	dup
	iconst_4
	bipush 63
	iastore
	dup
	iconst_5
	bipush 42
	iastore
	dup
	bipush 6
	bipush 53
	iastore
	dup
	bipush 7
	bipush 22
	iastore
	dup
	bipush 8
	sipush 731
	iastore
	dup
	bipush 9
	sipush 431
	iastore
	invokestatic MCClass/foo([I)I
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
