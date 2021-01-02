.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static mul_mat([[I[[I[[I)V
.var 0 is x [[I from Label0 to Label1
.var 1 is y [[I from Label0 to Label1
.var 2 is result [[I from Label0 to Label1
Label0:
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is j I from Label0 to Label1
	iconst_0
	istore 4
	iconst_0
	istore_3
Label4:
	iload_3
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_0
	istore 4
Label11:
	iload 4
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
.var 5 is sum I from Label14 to Label15
	iconst_0
	istore 5
.var 6 is k I from Label14 to Label15
	iconst_0
	istore 6
Label18:
Label19:
	iload 5
	aload_0
	iload_3
	aaload
	iload 6
	iaload
	aload_1
	iload 6
	aaload
	iload 4
	iaload
	imul
	iadd
	istore 5
	iload 6
	iconst_1
	iadd
	istore 6
Label20:
Label16:
	iload 6
	iconst_4
	if_icmpge Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifgt Label18
Label17:
	aload_2
	iload_3
	aaload
	iload 4
	iload 5
	iastore
Label15:
Label9:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label11
Label10:
Label8:
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
Label1:
	return
.limit stack 9
.limit locals 7
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x [[I from Label0 to Label1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_5
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	aastore
	dup
	iconst_1
	iconst_4
	newarray int
	dup
	iconst_0
	bipush 6
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_5
	iastore
	dup
	iconst_3
	iconst_2
	iastore
	aastore
	astore_1
.var 2 is y [[I from Label0 to Label1
	iconst_4
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 623
	iastore
	dup
	iconst_1
	bipush 123
	iastore
	dup
	iconst_2
	sipush 312
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 132
	iastore
	dup
	iconst_1
	sipush 423
	iastore
	dup
	iconst_2
	bipush 123
	iastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 243
	iastore
	dup
	iconst_1
	sipush 314
	iastore
	dup
	iconst_2
	sipush 643
	iastore
	aastore
	dup
	iconst_3
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 363
	iastore
	dup
	iconst_1
	sipush 798
	iastore
	dup
	iconst_2
	sipush 432
	iastore
	aastore
	astore_2
.var 3 is result [[I from Label0 to Label1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
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
	aastore
	dup
	iconst_1
	iconst_3
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
	aastore
	astore_3
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is j I from Label0 to Label1
	iconst_0
	istore 5
	aload_1
	aload_2
	aload_3
	invokestatic MCClass/mul_mat([[I[[I[[I)V
	iconst_0
	istore 4
Label4:
	iload 4
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_0
	istore 5
Label11:
	iload 5
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_3
	iload 4
	aaload
	iload 5
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label15:
Label9:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label11
Label10:
Label8:
Label2:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label4
Label3:
Label1:
	return
.limit stack 18
.limit locals 6
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
