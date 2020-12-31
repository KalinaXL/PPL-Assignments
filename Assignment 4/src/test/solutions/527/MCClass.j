.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
	iconst_1
	istore_1
Label4:
	iload_1
	bipush 20
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	invokestatic MCClass/pnum(I)Z
	ifle Label10
Label11:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	goto Label9
Label10:
Label9:
Label8:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static pnum(I)Z
.var 0 is x I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is sum I from Label0 to Label1
	iconst_0
	istore_2
	iconst_1
	istore_1
Label4:
	iload_1
	iload_0
	iconst_1
	isub
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 3 is k I from Label7 to Label8
	iconst_0
	istore_3
	iload_0
	iload_1
	invokestatic MCClass/is_divide(II)Z
	ifle Label10
Label11:
	iload_1
	istore_3
Label12:
	goto Label9
Label10:
Label9:
	iload_2
	iload_3
	iadd
	istore_2
Label8:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iload_2
	iload_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ireturn
Label1:
.limit stack 5
.limit locals 4
.end method

.method public static is_divide(II)Z
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iconst_1
	ireturn
Label7:
	goto Label2
Label3:
Label8:
	iconst_0
	ireturn
Label9:
Label2:
Label1:
	ireturn
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
	putstatic MCClass/arr [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
