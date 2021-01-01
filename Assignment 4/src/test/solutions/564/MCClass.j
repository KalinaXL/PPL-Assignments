.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/x [I
	bipush 10
	invokestatic MCClass/foo([II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo([II)I
.var 0 is x [I from Label0 to Label1
.var 1 is length I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_0
	ireturn
Label8:
	goto Label2
Label3:
	iload_1
	iconst_1
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label4
Label11:
	aload_0
	iconst_0
	iaload
	ireturn
Label12:
	goto Label2
Label4:
Label13:
	aload_0
	iload_1
	iconst_1
	isub
	iaload
	aload_0
	iload_1
	iconst_2
	isub
	invokestatic MCClass/foo([II)I
	iadd
	ireturn
Label14:
Label2:
Label1:
	ireturn
.limit stack 8
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
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	bipush 10
	iastore
	putstatic MCClass/x [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
