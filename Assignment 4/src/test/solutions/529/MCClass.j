.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	fneg
	ldc 1.0
	fcmpl
	ifne Label3
	iconst_0
	goto Label2
Label3:
	iconst_1
Label2:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 1.0
	fcmpl
	ifne Label5
	iconst_0
	goto Label4
Label5:
	iconst_1
Label4:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 2.0
	fneg
	ldc 2.0
	fneg
	fcmpl
	ifgt Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 2.0
	ldc 1.0
	fcmpl
	ifgt Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 1.0
	fneg
	fcmpl
	ifge Label11
	iconst_0
	goto Label10
Label11:
	iconst_1
Label10:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 1.0
	fcmpl
	ifge Label13
	iconst_0
	goto Label12
Label13:
	iconst_1
Label12:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	fneg
	ldc 1.0
	fcmpl
	ifgt Label15
	iconst_0
	goto Label14
Label15:
	iconst_1
Label14:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 1.0
	fcmpl
	ifgt Label17
	iconst_0
	goto Label16
Label17:
	iconst_1
Label16:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 1.0
	fcmpl
	ifge Label19
	iconst_1
	goto Label18
Label19:
	iconst_0
Label18:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 1.0
	fneg
	fcmpl
	ifge Label21
	iconst_1
	goto Label20
Label21:
	iconst_0
Label20:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 2.0
	fcmpl
	ifge Label23
	iconst_1
	goto Label22
Label23:
	iconst_0
Label22:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc 1.0
	ldc 2.0
	fcmpl
	ifge Label25
	iconst_0
	goto Label24
Label25:
	iconst_1
Label24:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 13
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
