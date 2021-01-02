.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static count_len([I)I
.var 0 is arr [I from Label0 to Label1
Label0:
.var 1 is count I from Label0 to Label1
	iconst_0
	istore_1
Label2:
	aload_0
	iload_1
	iaload
	iconst_0
	if_icmpeq Label4
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
.var 1 is arr [I from Label0 to Label1
	bipush 20
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_0
	iastore
	dup
	bipush 6
	iconst_0
	iastore
	dup
	bipush 7
	iconst_0
	iastore
	dup
	bipush 8
	iconst_0
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	dup
	bipush 10
	iconst_0
	iastore
	dup
	bipush 11
	iconst_0
	iastore
	dup
	bipush 12
	iconst_0
	iastore
	dup
	bipush 13
	iconst_0
	iastore
	dup
	bipush 14
	iconst_0
	iastore
	dup
	bipush 15
	iconst_0
	iastore
	dup
	bipush 16
	iconst_0
	iastore
	dup
	bipush 17
	iconst_0
	iastore
	dup
	bipush 18
	iconst_0
	iastore
	dup
	bipush 19
	iconst_0
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
	bipush 15
	istore_2
Label4:
Label5:
	aload_1
	iload_2
	iload_2
	iconst_1
	iadd
	iastore
	iload_2
	iconst_1
	isub
	istore_2
Label6:
Label2:
	iload_2
	iconst_1
	ineg
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label4
Label3:
	aload_1
	invokestatic MCClass/count_len([I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 3
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
