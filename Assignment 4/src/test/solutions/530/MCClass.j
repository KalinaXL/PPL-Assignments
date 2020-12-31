.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static partition([III)I
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
Label0:
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is pivot I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is j I from Label0 to Label1
	iconst_0
	istore 5
.var 6 is temp I from Label0 to Label1
	iconst_0
	istore 6
	iload_1
	iconst_1
	isub
	istore_3
	aload_0
	iload_2
	iaload
	istore 4
	iload_1
	istore 5
Label4:
	iload 5
	iload_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_0
	iload 5
	iaload
	iload 4
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label13:
.var 7 is temp I from Label13 to Label14
	iconst_0
	istore 7
	iload_3
	iconst_1
	iadd
	istore_3
	aload_0
	iload_3
	iaload
	istore 7
	aload_0
	iload_3
	aload_0
	iload 5
	iaload
	iastore
	aload_0
	iload 5
	iload 7
	iastore
Label14:
	goto Label9
Label10:
Label9:
Label8:
Label2:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label4
Label3:
	aload_0
	iload_3
	iconst_1
	iadd
	iaload
	istore 6
	aload_0
	iload_3
	iconst_1
	iadd
	iload 4
	iastore
	aload_0
	iload_2
	iload 6
	iastore
	iload_3
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 8
.limit locals 8
.end method

.method public static quick_sort([III)V
.var 0 is x [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
Label0:
.var 3 is idx I from Label0 to Label1
	iconst_0
	istore_3
	iload_1
	iload_2
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	return
Label7:
	goto Label2
Label3:
Label2:
	aload_0
	iload_1
	iload_2
	invokestatic MCClass/partition([III)I
	istore_3
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_0
	iload_1
	iload_3
	iconst_1
	isub
	invokestatic MCClass/quick_sort([III)V
	aload_0
	iload_3
	iconst_1
	iadd
	iload_2
	invokestatic MCClass/quick_sort([III)V
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x [I from Label0 to Label1
	bipush 7
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 80
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 90
	iastore
	dup
	iconst_4
	bipush 40
	iastore
	dup
	iconst_5
	bipush 50
	iastore
	dup
	bipush 6
	bipush 70
	iastore
	astore_1
	aload_1
	iconst_0
	bipush 6
	invokestatic MCClass/quick_sort([III)V
Label1:
	return
.limit stack 5
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
