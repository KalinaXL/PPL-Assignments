.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is length I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is idx I from Label0 to Label1
	iconst_0
	istore_2
	getstatic MCClass/x [I
	iload_1
	invokestatic MCClass/sort([II)V
Label2:
	iload_2
	iload_1
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	getstatic MCClass/x [I
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static sort([II)V
.var 0 is arr [I from Label0 to Label1
.var 1 is length I from Label0 to Label1
Label0:
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label2:
	iload_2
	iload_1
	iconst_1
	isub
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
.var 3 is j I from Label6 to Label7
	iconst_0
	istore_3
	iload_2
	iconst_1
	iadd
	istore_3
Label10:
Label11:
	aload_0
	iload_2
	iaload
	aload_0
	iload_3
	iaload
	if_icmple Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label14
Label17:
	aload_0
	iload_2
	iload_3
	invokestatic MCClass/swap([III)V
Label18:
	goto Label13
Label14:
Label13:
	iload_3
	iconst_1
	iadd
	istore_3
Label12:
Label8:
	iload_3
	iload_1
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifgt Label10
Label9:
	iload_2
	iconst_1
	iadd
	istore_2
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 8
.limit locals 4
.end method

.method public static swap([III)V
.var 0 is arr [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
.var 3 is temp I from Label0 to Label1
	iconst_0
	istore_3
	aload_0
	iload_1
	iaload
	istore_3
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload_3
	iastore
Label1:
	return
.limit stack 4
.limit locals 4
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
	bipush 100
	iastore
	dup
	iconst_1
	bipush 90
	iastore
	dup
	iconst_2
	bipush 80
	iastore
	dup
	iconst_3
	bipush 70
	iastore
	dup
	iconst_4
	bipush 60
	iastore
	dup
	iconst_5
	bipush 50
	iastore
	dup
	bipush 6
	bipush 40
	iastore
	dup
	bipush 7
	bipush 30
	iastore
	dup
	bipush 8
	bipush 20
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
