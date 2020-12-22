.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[[Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 2 is k I from Label7 to Label8
	iconst_0
	istore_2
Label9:
	iload_2
	iconst_1
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label13:
.var 3 is h I from Label13 to Label14
	iconst_0
	istore_3
Label17:
Label18:
	getstatic MCClass/x [[[Z
	iload_1
	aaload
	invokestatic MCClass/foo()I
	iconst_1
	isub
	aaload
	iload_3
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	istore_3
Label19:
Label15:
	iload_3
	iconst_2
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label17
Label16:
	iload_2
	iconst_1
	iadd
	istore_2
Label14:
	goto Label9
Label10:
Label8:
Label2:
	iload_1
	invokestatic MCClass/foo()I
	iadd
	istore_1
	goto Label4
Label3:
	getstatic MCClass/x [[[Z
	invokestatic MCClass/foo()I
	aaload
	invokestatic MCClass/foo()I
	iconst_1
	isub
	aaload
	invokestatic MCClass/foo()I
	baload
	ifle Label23
Label24:
.var 2 is str Ljava/lang/String; from Label24 to Label25
	ldc "string"
	astore_2
	getstatic MCClass/x [[[Z
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	baload
	ifle Label27
Label28:
.var 3 is str F from Label28 to Label29
	ldc 2203.2203
	fstore_3
	fload_3
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label29:
	goto Label26
Label27:
Label26:
	aload_2
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label25:
	goto Label22
Label23:
Label22:
Label1:
	return
.limit stack 9
.limit locals 4
.end method

.method public static foo()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
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
	iconst_2
	anewarray [[Z
	dup
	iconst_0
	iconst_1
	anewarray [Z
	dup
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray [Z
	dup
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	aastore
	putstatic MCClass/x [[[Z
Label1:
	return
.limit stack 19
.limit locals 0
.end method
