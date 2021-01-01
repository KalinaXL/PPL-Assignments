.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	ldc "A"
	invokestatic io/print(Ljava/lang/String;)V
Label9:
	goto Label2
Label3:
	iload_1
	iconst_4
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label4
Label12:
	ldc "B"
	invokestatic io/print(Ljava/lang/String;)V
Label13:
	goto Label2
Label4:
	iload_1
	bipush 6
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label5
Label16:
	ldc "C"
	invokestatic io/print(Ljava/lang/String;)V
Label17:
	goto Label2
Label5:
Label2:
	ldc "XL"
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
