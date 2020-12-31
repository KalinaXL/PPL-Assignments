.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label4:
Label5:
.var 2 is flag Z from Label5 to Label6
	iconst_0
	istore_2
.var 3 is j I from Label5 to Label6
	iconst_0
	istore_3
Label7:
	iload_3
	iload_1
	iconst_2
	idiv
	iconst_1
	iadd
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
Label11:
	iload_2
	dup
	ifgt Label13
	iload_3
	iload_1
	invokestatic MCClass/foo(II)Z
	ior
Label13:
	istore_2
	iload_2
	ifle Label15
Label16:
Label17:
	goto Label14
Label15:
Label14:
	iload_3
	iconst_1
	iadd
	istore_3
Label12:
	goto Label7
Label8:
	iload_2
	ifle Label19
Label20:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label21:
	goto Label18
Label19:
Label18:
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
Label2:
	iload_1
	bipush 20
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label4
Label3:
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public static foo(II)Z
.var 0 is number I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
.var 2 is iter I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is upper I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is sum F from Label0 to Label1
	ldc 0.0
	fstore 4
	iconst_2
	iload_0
	imul
	iconst_1
	isub
	istore_3
	iconst_1
	istore_2
Label4:
	iload_2
	iload_3
	invokestatic io/float_to_int(I)F
	invokestatic io/int_of_float(F)I
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	fload 4
	iload_2
	invokestatic io/float_to_int(I)F
	fadd
	fstore 4
	iload_2
	iconst_1
	iadd
	istore_2
Label8:
Label2:
	iload_2
	ldc 1.24
	invokestatic io/int_of_float(F)I
	iadd
	istore_2
	goto Label4
Label3:
	fload 4
	iload_1
	invokestatic io/float_to_int(I)F
	fcmpl
	ifne Label10
	iconst_0
	goto Label9
Label10:
	iconst_1
Label9:
	ifgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ireturn
Label1:
.limit stack 7
.limit locals 5
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
