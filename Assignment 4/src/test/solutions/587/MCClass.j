.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static pow(FI)F
.var 0 is x F from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
.var 2 is p F from Label0 to Label1
	ldc 1.0
	fstore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label2:
	iload_3
	iload_1
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	fload_2
	fload_0
	fmul
	fstore_2
	iload_3
	iconst_1
	iadd
	istore_3
Label7:
	goto Label2
Label3:
	fload_2
	freturn
Label1:
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 2.2
	iconst_0
	invokestatic MCClass/pow(FI)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc 2.2
	iconst_1
	invokestatic MCClass/pow(FI)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc 2.2
	iconst_2
	invokestatic MCClass/pow(FI)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc 2.2
	iconst_3
	invokestatic MCClass/pow(FI)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc 2.2
	iconst_4
	invokestatic MCClass/pow(FI)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
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
