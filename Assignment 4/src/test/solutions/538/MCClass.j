.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static fibonaci(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	dup
	ifgt Label8
	iload_0
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
Label8:
	ifle Label3
Label9:
	iload_0
	ireturn
Label10:
	goto Label2
Label3:
Label2:
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fibonaci(I)I
	iload_0
	iconst_2
	isub
	invokestatic MCClass/fibonaci(I)I
	iadd
	ireturn
Label1:
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 22
	invokestatic MCClass/fibonaci(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
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
