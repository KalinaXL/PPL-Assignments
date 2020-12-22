.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_2
	istore_1
	iload_1
	iconst_3
	invokestatic MCClass/foo(I)I
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
Label7:
	ldc "A"
	invokestatic io/print(Ljava/lang/String;)V
Label8:
	goto Label2
Label3:
	iload_1
	iconst_2
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label3
Label11:
	ldc "B"
	invokestatic io/print(Ljava/lang/String;)V
	ldc "-423"
	invokestatic io/int_of_string(Ljava/lang/String;)I
	invokestatic MCClass/foo(I)I
	istore_1
Label12:
	goto Label2
Label4:
Label13:
	ldc "-234"
	invokestatic io/int_of_string(Ljava/lang/String;)I
	invokestatic MCClass/foo(I)I
	istore_1
	iload_1
	invokestatic io/float_to_int(I)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label14:
Label2:
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static foo(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	ireturn
Label1:
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
