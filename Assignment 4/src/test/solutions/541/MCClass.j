.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static divisors(I)V
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	sipush 244
	istore_1
	iconst_1
	istore_1
Label4:
	iload_1
	iload_0
	iconst_1
	iadd
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label13:
	iload_1
	invokestatic io/float_to_int(I)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label14:
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
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 30
	invokestatic MCClass/divisors(I)V
Label1:
	return
.limit stack 1
.limit locals 1
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
