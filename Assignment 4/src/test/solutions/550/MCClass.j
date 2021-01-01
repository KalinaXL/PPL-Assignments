.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	bipush 7
	istore_1
	iload_1
	iconst_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label9:
	ldc "A"
	invokestatic io/print(Ljava/lang/String;)V
Label10:
	goto Label2
Label3:
	iload_1
	iconst_4
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label4
Label13:
	ldc "B"
	invokestatic io/print(Ljava/lang/String;)V
Label14:
	goto Label2
Label4:
	iload_1
	bipush 6
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label5
Label17:
	ldc "C"
	invokestatic io/print(Ljava/lang/String;)V
Label18:
	goto Label2
Label5:
	iload_1
	bipush 8
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label6
Label21:
	ldc "D"
	invokestatic io/print(Ljava/lang/String;)V
Label22:
	goto Label2
Label6:
Label2:
	ldc "XL"
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 9
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
