.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	bipush 100
	istore_1
.var 2 is num I from Label0 to Label1
	iconst_0
	istore_2
Label2:
	iload_2
	iload_1
	iconst_1
	iadd
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_2
	invokestatic MCClass/isPrime(I)Z
	ifle Label9
Label10:
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label11:
	goto Label8
Label9:
Label8:
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

.method public static isPrime(I)Z
.var 0 is x I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_2
	istore_1
	iload_0
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iconst_0
	ireturn
Label7:
	goto Label2
Label3:
Label2:
	iconst_2
	istore_1
Label10:
	iload_1
	iload_0
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label9
Label13:
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label16
Label19:
	iconst_0
	ireturn
Label20:
	goto Label15
Label16:
Label15:
Label14:
Label8:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label9:
	iconst_1
	ireturn
Label1:
.limit stack 10
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
