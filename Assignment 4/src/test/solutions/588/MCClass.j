.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static gcd(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	imul
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_0
	iload_1
	iadd
	ireturn
Label7:
	goto Label2
Label3:
Label2:
Label8:
	iload_1
	iconst_0
	if_icmpeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	iload_0
	iload_1
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
Label18:
	iload_0
	iload_1
	isub
	istore_0
Label19:
	goto Label14
Label15:
Label20:
	iload_1
	iload_0
	isub
	istore_1
Label21:
Label14:
Label13:
	goto Label8
Label9:
	iload_0
	ireturn
Label1:
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	bipush 20
	invokestatic MCClass/gcd(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	bipush 22
	invokestatic MCClass/gcd(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	bipush 10
	bipush 26
	invokestatic MCClass/gcd(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	bipush 56
	bipush 42
	invokestatic MCClass/gcd(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
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
