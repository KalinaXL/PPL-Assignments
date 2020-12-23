.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is min I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is max I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_1
	istore_3
	getstatic MCClass/arr [I
	iconst_0
	iaload
	istore_1
	getstatic MCClass/arr [I
	iconst_0
	iaload
	istore_2
Label2:
	iload_3
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_1
	getstatic MCClass/arr [I
	iload_3
	iaload
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	getstatic MCClass/arr [I
	iload_3
	iaload
	istore_1
Label13:
	goto Label8
Label9:
Label8:
	iload_2
	getstatic MCClass/arr [I
	iload_3
	iaload
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
Label18:
	iload_3
	bipush 9
	if_icmpne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label21
Label24:
	iload_2
	iload_1
	if_icmple Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label27
Label30:
	ldc "aaassd"
	invokestatic io/print(Ljava/lang/String;)V
Label31:
	goto Label26
Label27:
Label26:
Label25:
	goto Label20
Label21:
Label20:
	getstatic MCClass/arr [I
	iload_3
	iaload
	istore_2
Label19:
	goto Label14
Label15:
Label14:
	iload_3
	iconst_1
	iadd
	istore_3
Label7:
	goto Label2
Label3:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 4
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
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	bipush 10
	iastore
	putstatic MCClass/arr [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
