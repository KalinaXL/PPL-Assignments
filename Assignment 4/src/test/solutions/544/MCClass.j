.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is str [[Z from Label0 to Label1
	iconst_2
	anewarray [Z
	dup
	iconst_0
	iconst_3
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	astore_1
.var 2 is flag Z from Label0 to Label1
	iconst_1
	istore_2
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
	iload_2
	dup
	ifle Label16
	aload_1
	iload_3
	aaload
	iload 4
	baload
	iand
Label16:
	istore_2
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
	iload_2
	ifle Label18
Label19:
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label20:
	goto Label17
Label18:
Label21:
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label22:
Label17:
Label1:
	return
.limit stack 17
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
