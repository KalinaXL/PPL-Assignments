.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static f F
.field static y Z
.field static z Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/i I
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/i I
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/f F
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/f F
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/y Z
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/y Z
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/z Z
	ifgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifgt Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifgt Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifgt Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/z Z
	ifgt Label36
	iconst_1
	goto Label37
Label36:
	iconst_0
Label37:
	ifgt Label38
	iconst_1
	goto Label39
Label38:
	iconst_0
Label39:
	ifgt Label40
	iconst_1
	goto Label41
Label40:
	iconst_0
Label41:
	ifgt Label42
	iconst_1
	goto Label43
Label42:
	iconst_0
Label43:
	ifgt Label44
	iconst_1
	goto Label45
Label44:
	iconst_0
Label45:
	ifgt Label46
	iconst_1
	goto Label47
Label46:
	iconst_0
Label47:
	ifgt Label48
	iconst_1
	goto Label49
Label48:
	iconst_0
Label49:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 73
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
	bipush 10
	putstatic MCClass/i I
	ldc 22.22
	putstatic MCClass/f F
	iconst_1
	putstatic MCClass/y Z
	iconst_0
	putstatic MCClass/z Z
Label1:
	return
.limit stack 3
.limit locals 0
.end method
