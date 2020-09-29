# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


# ID: 1813085
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3/\6")
        buf.write("/\u0146\n/\r/\16/\u0147\3/\3/\3\60\3\60\7\60\u014e\n\60")
        buf.write("\f\60\16\60\u0151\13\60\3\61\3\61\3\61\3\61\7\61\u0157")
        buf.write("\n\61\f\61\16\61\u015a\13\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u016a")
        buf.write("\n\62\3\63\3\63\3\63\5\63\u016f\n\63\3\64\3\64\7\64\u0173")
        buf.write("\n\64\f\64\16\64\u0176\13\64\3\64\6\64\u0179\n\64\r\64")
        buf.write("\16\64\u017a\5\64\u017d\n\64\3\65\3\65\3\65\6\65\u0182")
        buf.write("\n\65\r\65\16\65\u0183\3\66\3\66\3\66\6\66\u0189\n\66")
        buf.write("\r\66\16\66\u018a\3\67\6\67\u018e\n\67\r\67\16\67\u018f")
        buf.write("\3\67\3\67\3\67\3\67\3\67\5\67\u0197\n\67\38\38\78\u019b")
        buf.write("\n8\f8\168\u019e\138\38\38\38\39\39\3:\3:\7:\u01a7\n:")
        buf.write("\f:\16:\u01aa\13:\3:\3:\3:\3;\3;\7;\u01b1\n;\f;\16;\u01b4")
        buf.write("\13;\3;\3;\3<\3<\3<\3<\7<\u01bc\n<\f<\16<\u01bf\13<\3")
        buf.write("<\5<\u01c2\n<\3=\3=\3>\3>\3?\3?\3@\3@\7@\u01cc\n@\f@\16")
        buf.write("@\u01cf\13@\3A\3A\5A\u01d3\nA\3A\6A\u01d6\nA\rA\16A\u01d7")
        buf.write("\3B\3B\3B\5B\u01dd\nB\3C\3C\3C\3C\3C\5C\u01e4\nC\4\u0158")
        buf.write("\u01bd\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2")
        buf.write("\3\2\17\5\2\13\f\17\17\"\"\3\2c|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\4\2ZZzz\4\2QQqq\3\2\62;\3\2\629\4\2\62;CH\4\2GGgg\4")
        buf.write("\2--//\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\2\u01f6\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3\u0087\3\2")
        buf.write("\2\2\5\u0089\3\2\2\2\7\u008b\3\2\2\2\t\u008d\3\2\2\2\13")
        buf.write("\u0092\3\2\2\2\r\u0098\3\2\2\2\17\u00a1\3\2\2\2\21\u00a4")
        buf.write("\3\2\2\2\23\u00a9\3\2\2\2\25\u00b0\3\2\2\2\27\u00b8\3")
        buf.write("\2\2\2\31\u00be\3\2\2\2\33\u00c5\3\2\2\2\35\u00ce\3\2")
        buf.write("\2\2\37\u00d2\3\2\2\2!\u00db\3\2\2\2#\u00de\3\2\2\2%\u00e8")
        buf.write("\3\2\2\2\'\u00ef\3\2\2\2)\u00f4\3\2\2\2+\u00fa\3\2\2\2")
        buf.write("-\u0100\3\2\2\2/\u0104\3\2\2\2\61\u0106\3\2\2\2\63\u0109")
        buf.write("\3\2\2\2\65\u010b\3\2\2\2\67\u010d\3\2\2\29\u0110\3\2")
        buf.write("\2\2;\u0112\3\2\2\2=\u0115\3\2\2\2?\u0117\3\2\2\2A\u0119")
        buf.write("\3\2\2\2C\u011c\3\2\2\2E\u011f\3\2\2\2G\u0122\3\2\2\2")
        buf.write("I\u0125\3\2\2\2K\u0128\3\2\2\2M\u012a\3\2\2\2O\u012c\3")
        buf.write("\2\2\2Q\u012f\3\2\2\2S\u0132\3\2\2\2U\u0136\3\2\2\2W\u0139")
        buf.write("\3\2\2\2Y\u013c\3\2\2\2[\u0140\3\2\2\2]\u0145\3\2\2\2")
        buf.write("_\u014b\3\2\2\2a\u0152\3\2\2\2c\u0169\3\2\2\2e\u016e\3")
        buf.write("\2\2\2g\u017c\3\2\2\2i\u017e\3\2\2\2k\u0185\3\2\2\2m\u018d")
        buf.write("\3\2\2\2o\u0198\3\2\2\2q\u01a2\3\2\2\2s\u01a4\3\2\2\2")
        buf.write("u\u01ae\3\2\2\2w\u01b7\3\2\2\2y\u01c3\3\2\2\2{\u01c5\3")
        buf.write("\2\2\2}\u01c7\3\2\2\2\177\u01c9\3\2\2\2\u0081\u01d0\3")
        buf.write("\2\2\2\u0083\u01dc\3\2\2\2\u0085\u01e3\3\2\2\2\u0087\u0088")
        buf.write("\7=\2\2\u0088\4\3\2\2\2\u0089\u008a\7.\2\2\u008a\6\3\2")
        buf.write("\2\2\u008b\u008c\7<\2\2\u008c\b\3\2\2\2\u008d\u008e\7")
        buf.write("D\2\2\u008e\u008f\7q\2\2\u008f\u0090\7f\2\2\u0090\u0091")
        buf.write("\7{\2\2\u0091\n\3\2\2\2\u0092\u0093\7D\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097")
        buf.write("\7m\2\2\u0097\f\3\2\2\2\u0098\u0099\7E\2\2\u0099\u009a")
        buf.write("\7q\2\2\u009a\u009b\7p\2\2\u009b\u009c\7v\2\2\u009c\u009d")
        buf.write("\7k\2\2\u009d\u009e\7p\2\2\u009e\u009f\7w\2\2\u009f\u00a0")
        buf.write("\7g\2\2\u00a0\16\3\2\2\2\u00a1\u00a2\7F\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\20\3\2\2\2\u00a4\u00a5\7G\2\2\u00a5\u00a6")
        buf.write("\7n\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\22")
        buf.write("\3\2\2\2\u00a9\u00aa\7G\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7K\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\24\3\2\2\2\u00b0\u00b1\7G\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7f\2\2\u00b3\u00b4\7D\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7f\2\2\u00b6\u00b7\7{\2\2\u00b7\26")
        buf.write("\3\2\2\2\u00b8\u00b9\7G\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7f\2\2\u00bb\u00bc\7K\2\2\u00bc\u00bd\7h\2\2\u00bd\30")
        buf.write("\3\2\2\2\u00be\u00bf\7G\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7f\2\2\u00c1\u00c2\7H\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\32\3\2\2\2\u00c5\u00c6\7G\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7f\2\2\u00c8\u00c9\7Y\2\2\u00c9\u00ca")
        buf.write("\7j\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\34\3\2\2\2\u00ce\u00cf\7H\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7t\2\2\u00d1\36\3\2\2\2\u00d2\u00d3")
        buf.write("\7H\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7e\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7p\2\2\u00da \3\2\2\2\u00db\u00dc")
        buf.write("\7K\2\2\u00dc\u00dd\7h\2\2\u00dd\"\3\2\2\2\u00de\u00df")
        buf.write("\7R\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7o\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7t\2\2\u00e7$\3")
        buf.write("\2\2\2\u00e8\u00e9\7T\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee&\3\2\2\2\u00ef\u00f0\7V\2\2\u00f0\u00f1")
        buf.write("\7j\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7p\2\2\u00f3(\3")
        buf.write("\2\2\2\u00f4\u00f5\7Y\2\2\u00f5\u00f6\7j\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7g\2\2\u00f9*\3")
        buf.write("\2\2\2\u00fa\u00fb\7G\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7f\2\2\u00fd\u00fe\7F\2\2\u00fe\u00ff\7q\2\2\u00ff,\3")
        buf.write("\2\2\2\u0100\u0101\7X\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103.\3\2\2\2\u0104\u0105\7/\2\2\u0105\60\3\2")
        buf.write("\2\2\u0106\u0107\7/\2\2\u0107\u0108\7\60\2\2\u0108\62")
        buf.write("\3\2\2\2\u0109\u010a\7#\2\2\u010a\64\3\2\2\2\u010b\u010c")
        buf.write("\7,\2\2\u010c\66\3\2\2\2\u010d\u010e\7,\2\2\u010e\u010f")
        buf.write("\7\60\2\2\u010f8\3\2\2\2\u0110\u0111\7^\2\2\u0111:\3\2")
        buf.write("\2\2\u0112\u0113\7^\2\2\u0113\u0114\7\60\2\2\u0114<\3")
        buf.write("\2\2\2\u0115\u0116\7\'\2\2\u0116>\3\2\2\2\u0117\u0118")
        buf.write("\7-\2\2\u0118@\3\2\2\2\u0119\u011a\7-\2\2\u011a\u011b")
        buf.write("\7\60\2\2\u011bB\3\2\2\2\u011c\u011d\7(\2\2\u011d\u011e")
        buf.write("\7(\2\2\u011eD\3\2\2\2\u011f\u0120\7~\2\2\u0120\u0121")
        buf.write("\7~\2\2\u0121F\3\2\2\2\u0122\u0123\7?\2\2\u0123\u0124")
        buf.write("\7?\2\2\u0124H\3\2\2\2\u0125\u0126\7#\2\2\u0126\u0127")
        buf.write("\7?\2\2\u0127J\3\2\2\2\u0128\u0129\7>\2\2\u0129L\3\2\2")
        buf.write("\2\u012a\u012b\7@\2\2\u012bN\3\2\2\2\u012c\u012d\7>\2")
        buf.write("\2\u012d\u012e\7?\2\2\u012eP\3\2\2\2\u012f\u0130\7@\2")
        buf.write("\2\u0130\u0131\7?\2\2\u0131R\3\2\2\2\u0132\u0133\7?\2")
        buf.write("\2\u0133\u0134\7\61\2\2\u0134\u0135\7?\2\2\u0135T\3\2")
        buf.write("\2\2\u0136\u0137\7>\2\2\u0137\u0138\7\60\2\2\u0138V\3")
        buf.write("\2\2\2\u0139\u013a\7@\2\2\u013a\u013b\7\60\2\2\u013bX")
        buf.write("\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7?\2\2\u013e\u013f")
        buf.write("\7\60\2\2\u013fZ\3\2\2\2\u0140\u0141\7@\2\2\u0141\u0142")
        buf.write("\7?\2\2\u0142\u0143\7\60\2\2\u0143\\\3\2\2\2\u0144\u0146")
        buf.write("\t\2\2\2\u0145\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\b/\2\2\u014a^\3\2\2\2\u014b\u014f\t\3\2\2")
        buf.write("\u014c\u014e\t\4\2\2\u014d\u014c\3\2\2\2\u014e\u0151\3")
        buf.write("\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150`")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\7,\2\2\u0153")
        buf.write("\u0154\7,\2\2\u0154\u0158\3\2\2\2\u0155\u0157\13\2\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0159\3")
        buf.write("\2\2\2\u0158\u0156\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015c\7,\2\2\u015c\u015d\7,\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u015f\b\61\2\2\u015fb\3\2\2\2\u0160\u0161")
        buf.write("\7V\2\2\u0161\u0162\7t\2\2\u0162\u0163\7w\2\2\u0163\u016a")
        buf.write("\7g\2\2\u0164\u0165\7H\2\2\u0165\u0166\7c\2\2\u0166\u0167")
        buf.write("\7n\2\2\u0167\u0168\7u\2\2\u0168\u016a\7g\2\2\u0169\u0160")
        buf.write("\3\2\2\2\u0169\u0164\3\2\2\2\u016ad\3\2\2\2\u016b\u016f")
        buf.write("\5g\64\2\u016c\u016f\5k\66\2\u016d\u016f\5i\65\2\u016e")
        buf.write("\u016b\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2\2")
        buf.write("\u016ff\3\2\2\2\u0170\u0174\t\5\2\2\u0171\u0173\5y=\2")
        buf.write("\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u017d\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u0179\7\62\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u017d\3\2\2\2\u017c\u0170\3\2\2\2\u017c\u0178\3")
        buf.write("\2\2\2\u017dh\3\2\2\2\u017e\u017f\7\62\2\2\u017f\u0181")
        buf.write("\t\6\2\2\u0180\u0182\5}?\2\u0181\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("j\3\2\2\2\u0185\u0186\7\62\2\2\u0186\u0188\t\7\2\2\u0187")
        buf.write("\u0189\5{>\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018bl\3\2\2\2\u018c")
        buf.write("\u018e\5y=\2\u018d\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0196\3\2\2\2")
        buf.write("\u0191\u0192\5\177@\2\u0192\u0193\5\u0081A\2\u0193\u0197")
        buf.write("\3\2\2\2\u0194\u0197\5\177@\2\u0195\u0197\5\u0081A\2\u0196")
        buf.write("\u0191\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0197n\3\2\2\2\u0198\u019c\7$\2\2\u0199\u019b\5\u0085")
        buf.write("C\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u01a0\7$\2\2\u01a0\u01a1\b8\3\2\u01a1")
        buf.write("p\3\2\2\2\u01a2\u01a3\13\2\2\2\u01a3r\3\2\2\2\u01a4\u01a8")
        buf.write("\7$\2\2\u01a5\u01a7\5\u0085C\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\5")
        buf.write("\u0083B\2\u01ac\u01ad\b:\4\2\u01adt\3\2\2\2\u01ae\u01b2")
        buf.write("\7$\2\2\u01af\u01b1\5\u0085C\2\u01b0\u01af\3\2\2\2\u01b1")
        buf.write("\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\b")
        buf.write(";\5\2\u01b6v\3\2\2\2\u01b7\u01b8\7,\2\2\u01b8\u01b9\7")
        buf.write(",\2\2\u01b9\u01bd\3\2\2\2\u01ba\u01bc\13\2\2\2\u01bb\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01be\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01c0\u01c2\7,\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c2x\3\2\2\2\u01c3\u01c4\t\b\2\2\u01c4z\3\2\2")
        buf.write("\2\u01c5\u01c6\t\t\2\2\u01c6|\3\2\2\2\u01c7\u01c8\t\n")
        buf.write("\2\2\u01c8~\3\2\2\2\u01c9\u01cd\7\60\2\2\u01ca\u01cc\5")
        buf.write("y=\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u0080\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01d0\u01d2\t\13\2\2\u01d1\u01d3\t\f\2")
        buf.write("\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5")
        buf.write("\3\2\2\2\u01d4\u01d6\5y=\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8")
        buf.write("\u0082\3\2\2\2\u01d9\u01da\7^\2\2\u01da\u01dd\n\r\2\2")
        buf.write("\u01db\u01dd\7^\2\2\u01dc\u01d9\3\2\2\2\u01dc\u01db\3")
        buf.write("\2\2\2\u01dd\u0084\3\2\2\2\u01de\u01df\7)\2\2\u01df\u01e4")
        buf.write("\7$\2\2\u01e0\u01e1\7^\2\2\u01e1\u01e4\t\r\2\2\u01e2\u01e4")
        buf.write("\n\16\2\2\u01e3\u01de\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u0086\3\2\2\2\31\2\u0147\u014f\u0158")
        buf.write("\u0169\u016e\u0174\u017a\u017c\u0183\u018a\u018f\u0196")
        buf.write("\u019c\u01a8\u01b2\u01bd\u01c1\u01cd\u01d2\u01d7\u01dc")
        buf.write("\u01e3\6\b\2\2\38\2\3:\3\3;\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEMI = 1
    COMMA = 2
    COLON = 3
    BODY = 4
    BREAK = 5
    CONTINUE = 6
    DO = 7
    ELSE = 8
    ELSEIF = 9
    ENDBODY = 10
    ENDIF = 11
    ENDFOR = 12
    ENDWHILE = 13
    FOR = 14
    FUNCTION = 15
    IF = 16
    PARAMETER = 17
    RETURN = 18
    THEN = 19
    WHILE = 20
    ENDDO = 21
    VAR = 22
    SUBTRACT = 23
    SUBTRACT_F = 24
    NEGATION = 25
    MULTIPLY = 26
    MULTIPLY_F = 27
    DIVIDE = 28
    DIVIDE_F = 29
    MODULO = 30
    ADD = 31
    ADD_F = 32
    AND = 33
    OR = 34
    EQUAL = 35
    NOT_EQUAL = 36
    LT = 37
    GT = 38
    LTE = 39
    GTE = 40
    NOT_EQUAL_F = 41
    LT_F = 42
    GT_F = 43
    LTE_F = 44
    GTE_F = 45
    WS = 46
    IDENTIFIER = 47
    COMMENT = 48
    BOOLEAN = 49
    INTEGER = 50
    DEC_INT = 51
    HEX_INT = 52
    OCT_INT = 53
    FLOAT = 54
    STRING = 55
    ERROR_CHAR = 56
    ILLEGAL_ESCAPE = 57
    UNCLOSE_STRING = 58
    UNTERMINATED_COMMENT = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "':'", "'Body'", "'Break'", "'Continue'", "'Do'", 
            "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'While'", "'EndDo'", "'Var'", "'-'", "'-.'", "'!'", "'*'", 
            "'*.'", "'\\'", "'\\.'", "'%'", "'+'", "'+.'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COMMA", "COLON", "BODY", "BREAK", "CONTINUE", "DO", 
            "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
            "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "WHILE", 
            "ENDDO", "VAR", "SUBTRACT", "SUBTRACT_F", "NEGATION", "MULTIPLY", 
            "MULTIPLY_F", "DIVIDE", "DIVIDE_F", "MODULO", "ADD", "ADD_F", 
            "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", "GT", "LTE", "GTE", 
            "NOT_EQUAL_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "WS", "IDENTIFIER", 
            "COMMENT", "BOOLEAN", "INTEGER", "DEC_INT", "HEX_INT", "OCT_INT", 
            "FLOAT", "STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "SEMI", "COMMA", "COLON", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "WHILE", "ENDDO", "VAR", "SUBTRACT", "SUBTRACT_F", 
                  "NEGATION", "MULTIPLY", "MULTIPLY_F", "DIVIDE", "DIVIDE_F", 
                  "MODULO", "ADD", "ADD_F", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LT", "GT", "LTE", "GTE", "NOT_EQUAL_F", "LT_F", "GT_F", 
                  "LTE_F", "GTE_F", "WS", "IDENTIFIER", "COMMENT", "BOOLEAN", 
                  "INTEGER", "DEC_INT", "HEX_INT", "OCT_INT", "FLOAT", "STRING", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "DEC_PART", "EXP_PART", 
                  "ILLEGAL_ESC", "CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1: -1];

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1: ];

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:];

     


