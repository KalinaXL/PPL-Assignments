# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


# ID: 1813085
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u020c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\38\68\u016d\n8\r8\168\u016e")
        buf.write("\38\38\39\39\79\u0175\n9\f9\169\u0178\139\3:\3:\3:\3:")
        buf.write("\7:\u017e\n:\f:\16:\u0181\13:\3:\3:\3:\3:\3:\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\3;\3;\5;\u0191\n;\3<\3<\3<\5<\u0196\n<\3")
        buf.write("=\6=\u0199\n=\r=\16=\u019a\3=\3=\3=\3=\3=\5=\u01a2\n=")
        buf.write("\3>\3>\7>\u01a6\n>\f>\16>\u01a9\13>\3>\3>\3>\3?\3?\3@")
        buf.write("\3@\7@\u01b2\n@\f@\16@\u01b5\13@\3@\3@\3@\3A\3A\7A\u01bc")
        buf.write("\nA\fA\16A\u01bf\13A\3A\3A\3B\3B\3B\3B\7B\u01c7\nB\fB")
        buf.write("\16B\u01ca\13B\3B\5B\u01cd\nB\3C\3C\3D\3D\3E\3E\3F\3F")
        buf.write("\7F\u01d7\nF\fF\16F\u01da\13F\3F\6F\u01dd\nF\rF\16F\u01de")
        buf.write("\5F\u01e1\nF\3G\3G\3G\6G\u01e6\nG\rG\16G\u01e7\3H\3H\3")
        buf.write("H\6H\u01ed\nH\rH\16H\u01ee\3I\3I\7I\u01f3\nI\fI\16I\u01f6")
        buf.write("\13I\3J\3J\5J\u01fa\nJ\3J\6J\u01fd\nJ\rJ\16J\u01fe\3K")
        buf.write("\3K\3K\5K\u0204\nK\3L\3L\3L\3L\3L\5L\u020b\nL\4\u017f")
        buf.write("\u01c8\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\3\2\17\5\2\13\f\17\17\"\"\3\2c|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\3\2\629\4\2\62;CH\3\2\63;\4\2ZZzz\4\2QQq")
        buf.write("q\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^")
        buf.write("\2\u021a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2")
        buf.write("\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2\13\u00a1\3\2\2\2\r")
        buf.write("\u00a3\3\2\2\2\17\u00a5\3\2\2\2\21\u00a7\3\2\2\2\23\u00a9")
        buf.write("\3\2\2\2\25\u00ab\3\2\2\2\27\u00ad\3\2\2\2\31\u00b2\3")
        buf.write("\2\2\2\33\u00b8\3\2\2\2\35\u00c1\3\2\2\2\37\u00c4\3\2")
        buf.write("\2\2!\u00c9\3\2\2\2#\u00d0\3\2\2\2%\u00d8\3\2\2\2\'\u00de")
        buf.write("\3\2\2\2)\u00e5\3\2\2\2+\u00ee\3\2\2\2-\u00f2\3\2\2\2")
        buf.write("/\u00fb\3\2\2\2\61\u00fe\3\2\2\2\63\u0108\3\2\2\2\65\u010f")
        buf.write("\3\2\2\2\67\u0114\3\2\2\29\u011a\3\2\2\2;\u0120\3\2\2")
        buf.write("\2=\u0124\3\2\2\2?\u0129\3\2\2\2A\u012b\3\2\2\2C\u012d")
        buf.write("\3\2\2\2E\u0130\3\2\2\2G\u0132\3\2\2\2I\u0134\3\2\2\2")
        buf.write("K\u0137\3\2\2\2M\u0139\3\2\2\2O\u013c\3\2\2\2Q\u013e\3")
        buf.write("\2\2\2S\u0140\3\2\2\2U\u0143\3\2\2\2W\u0146\3\2\2\2Y\u0149")
        buf.write("\3\2\2\2[\u014c\3\2\2\2]\u014f\3\2\2\2_\u0151\3\2\2\2")
        buf.write("a\u0153\3\2\2\2c\u0156\3\2\2\2e\u0159\3\2\2\2g\u015d\3")
        buf.write("\2\2\2i\u0160\3\2\2\2k\u0163\3\2\2\2m\u0167\3\2\2\2o\u016c")
        buf.write("\3\2\2\2q\u0172\3\2\2\2s\u0179\3\2\2\2u\u0190\3\2\2\2")
        buf.write("w\u0195\3\2\2\2y\u0198\3\2\2\2{\u01a3\3\2\2\2}\u01ad\3")
        buf.write("\2\2\2\177\u01af\3\2\2\2\u0081\u01b9\3\2\2\2\u0083\u01c2")
        buf.write("\3\2\2\2\u0085\u01ce\3\2\2\2\u0087\u01d0\3\2\2\2\u0089")
        buf.write("\u01d2\3\2\2\2\u008b\u01e0\3\2\2\2\u008d\u01e2\3\2\2\2")
        buf.write("\u008f\u01e9\3\2\2\2\u0091\u01f0\3\2\2\2\u0093\u01f7\3")
        buf.write("\2\2\2\u0095\u0203\3\2\2\2\u0097\u020a\3\2\2\2\u0099\u009a")
        buf.write("\7*\2\2\u009a\4\3\2\2\2\u009b\u009c\7+\2\2\u009c\6\3\2")
        buf.write("\2\2\u009d\u009e\7]\2\2\u009e\b\3\2\2\2\u009f\u00a0\7")
        buf.write("_\2\2\u00a0\n\3\2\2\2\u00a1\u00a2\7}\2\2\u00a2\f\3\2\2")
        buf.write("\2\u00a3\u00a4\7\177\2\2\u00a4\16\3\2\2\2\u00a5\u00a6")
        buf.write("\7=\2\2\u00a6\20\3\2\2\2\u00a7\u00a8\7.\2\2\u00a8\22\3")
        buf.write("\2\2\2\u00a9\u00aa\7<\2\2\u00aa\24\3\2\2\2\u00ab\u00ac")
        buf.write("\7\60\2\2\u00ac\26\3\2\2\2\u00ad\u00ae\7D\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7f\2\2\u00b0\u00b1\7{\2\2\u00b1\30")
        buf.write("\3\2\2\2\u00b2\u00b3\7D\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7m\2\2\u00b7\32")
        buf.write("\3\2\2\2\u00b8\u00b9\7E\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0\34")
        buf.write("\3\2\2\2\u00c1\u00c2\7F\2\2\u00c2\u00c3\7q\2\2\u00c3\36")
        buf.write("\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7u\2\2\u00c7\u00c8\7g\2\2\u00c8 \3\2\2\2\u00c9\u00ca")
        buf.write("\7G\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\u00ce\7K\2\2\u00ce\u00cf\7h\2\2\u00cf\"")
        buf.write("\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7f\2\2\u00d3\u00d4\7D\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7f\2\2\u00d6\u00d7\7{\2\2\u00d7$\3\2\2\2\u00d8\u00d9")
        buf.write("\7G\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db\u00dc")
        buf.write("\7K\2\2\u00dc\u00dd\7h\2\2\u00dd&\3\2\2\2\u00de\u00df")
        buf.write("\7G\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7f\2\2\u00e1\u00e2")
        buf.write("\7H\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4(\3")
        buf.write("\2\2\2\u00e5\u00e6\7G\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7f\2\2\u00e8\u00e9\7Y\2\2\u00e9\u00ea\7j\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7g\2\2\u00ed*\3")
        buf.write("\2\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1,\3\2\2\2\u00f2\u00f3\7H\2\2\u00f3\u00f4")
        buf.write("\7w\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa.\3\2\2\2\u00fb\u00fc\7K\2\2\u00fc\u00fd")
        buf.write("\7h\2\2\u00fd\60\3\2\2\2\u00fe\u00ff\7R\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7t\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7o\2\2\u0103\u0104\7g\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7t\2\2\u0107\62\3\2\2\2\u0108\u0109")
        buf.write("\7T\2\2\u0109\u010a\7g\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7w\2\2\u010c\u010d\7t\2\2\u010d\u010e\7p\2\2\u010e\64")
        buf.write("\3\2\2\2\u010f\u0110\7V\2\2\u0110\u0111\7j\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0113\7p\2\2\u0113\66\3\2\2\2\u0114\u0115")
        buf.write("\7Y\2\2\u0115\u0116\7j\2\2\u0116\u0117\7k\2\2\u0117\u0118")
        buf.write("\7n\2\2\u0118\u0119\7g\2\2\u01198\3\2\2\2\u011a\u011b")
        buf.write("\7G\2\2\u011b\u011c\7p\2\2\u011c\u011d\7f\2\2\u011d\u011e")
        buf.write("\7F\2\2\u011e\u011f\7q\2\2\u011f:\3\2\2\2\u0120\u0121")
        buf.write("\7X\2\2\u0121\u0122\7c\2\2\u0122\u0123\7t\2\2\u0123<\3")
        buf.write("\2\2\2\u0124\u0125\7o\2\2\u0125\u0126\7c\2\2\u0126\u0127")
        buf.write("\7k\2\2\u0127\u0128\7p\2\2\u0128>\3\2\2\2\u0129\u012a")
        buf.write("\7?\2\2\u012a@\3\2\2\2\u012b\u012c\7/\2\2\u012cB\3\2\2")
        buf.write("\2\u012d\u012e\7/\2\2\u012e\u012f\7\60\2\2\u012fD\3\2")
        buf.write("\2\2\u0130\u0131\7#\2\2\u0131F\3\2\2\2\u0132\u0133\7,")
        buf.write("\2\2\u0133H\3\2\2\2\u0134\u0135\7,\2\2\u0135\u0136\7\60")
        buf.write("\2\2\u0136J\3\2\2\2\u0137\u0138\7^\2\2\u0138L\3\2\2\2")
        buf.write("\u0139\u013a\7^\2\2\u013a\u013b\7\60\2\2\u013bN\3\2\2")
        buf.write("\2\u013c\u013d\7\'\2\2\u013dP\3\2\2\2\u013e\u013f\7-\2")
        buf.write("\2\u013fR\3\2\2\2\u0140\u0141\7-\2\2\u0141\u0142\7\60")
        buf.write("\2\2\u0142T\3\2\2\2\u0143\u0144\7(\2\2\u0144\u0145\7(")
        buf.write("\2\2\u0145V\3\2\2\2\u0146\u0147\7~\2\2\u0147\u0148\7~")
        buf.write("\2\2\u0148X\3\2\2\2\u0149\u014a\7?\2\2\u014a\u014b\7?")
        buf.write("\2\2\u014bZ\3\2\2\2\u014c\u014d\7#\2\2\u014d\u014e\7?")
        buf.write("\2\2\u014e\\\3\2\2\2\u014f\u0150\7>\2\2\u0150^\3\2\2\2")
        buf.write("\u0151\u0152\7@\2\2\u0152`\3\2\2\2\u0153\u0154\7>\2\2")
        buf.write("\u0154\u0155\7?\2\2\u0155b\3\2\2\2\u0156\u0157\7@\2\2")
        buf.write("\u0157\u0158\7?\2\2\u0158d\3\2\2\2\u0159\u015a\7?\2\2")
        buf.write("\u015a\u015b\7\61\2\2\u015b\u015c\7?\2\2\u015cf\3\2\2")
        buf.write("\2\u015d\u015e\7>\2\2\u015e\u015f\7\60\2\2\u015fh\3\2")
        buf.write("\2\2\u0160\u0161\7@\2\2\u0161\u0162\7\60\2\2\u0162j\3")
        buf.write("\2\2\2\u0163\u0164\7>\2\2\u0164\u0165\7?\2\2\u0165\u0166")
        buf.write("\7\60\2\2\u0166l\3\2\2\2\u0167\u0168\7@\2\2\u0168\u0169")
        buf.write("\7?\2\2\u0169\u016a\7\60\2\2\u016an\3\2\2\2\u016b\u016d")
        buf.write("\t\2\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0171\b8\2\2\u0171p\3\2\2\2\u0172\u0176\t\3\2\2")
        buf.write("\u0173\u0175\t\4\2\2\u0174\u0173\3\2\2\2\u0175\u0178\3")
        buf.write("\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177r")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\7,\2\2\u017a")
        buf.write("\u017b\7,\2\2\u017b\u017f\3\2\2\2\u017c\u017e\13\2\2\2")
        buf.write("\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0182\u0183\7,\2\2\u0183\u0184\7,\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185\u0186\b:\2\2\u0186t\3\2\2\2\u0187\u0188")
        buf.write("\7V\2\2\u0188\u0189\7t\2\2\u0189\u018a\7w\2\2\u018a\u0191")
        buf.write("\7g\2\2\u018b\u018c\7H\2\2\u018c\u018d\7c\2\2\u018d\u018e")
        buf.write("\7n\2\2\u018e\u018f\7u\2\2\u018f\u0191\7g\2\2\u0190\u0187")
        buf.write("\3\2\2\2\u0190\u018b\3\2\2\2\u0191v\3\2\2\2\u0192\u0196")
        buf.write("\5\u008bF\2\u0193\u0196\5\u008fH\2\u0194\u0196\5\u008d")
        buf.write("G\2\u0195\u0192\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196x\3\2\2\2\u0197\u0199\5\u0085C\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u01a1\3\2\2\2\u019c\u019d\5\u0091")
        buf.write("I\2\u019d\u019e\5\u0093J\2\u019e\u01a2\3\2\2\2\u019f\u01a2")
        buf.write("\5\u0091I\2\u01a0\u01a2\5\u0093J\2\u01a1\u019c\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2z\3\2\2")
        buf.write("\2\u01a3\u01a7\7$\2\2\u01a4\u01a6\5\u0097L\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01aa\u01ab\7$\2\2\u01ab\u01ac\b>\3\2\u01ac|\3\2\2\2")
        buf.write("\u01ad\u01ae\13\2\2\2\u01ae~\3\2\2\2\u01af\u01b3\7$\2")
        buf.write("\2\u01b0\u01b2\5\u0097L\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\5\u0095")
        buf.write("K\2\u01b7\u01b8\b@\4\2\u01b8\u0080\3\2\2\2\u01b9\u01bd")
        buf.write("\7$\2\2\u01ba\u01bc\5\u0097L\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\b")
        buf.write("A\5\2\u01c1\u0082\3\2\2\2\u01c2\u01c3\7,\2\2\u01c3\u01c4")
        buf.write("\7,\2\2\u01c4\u01c8\3\2\2\2\u01c5\u01c7\13\2\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01cb\u01cd\7,\2\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u0084\3\2\2\2\u01ce\u01cf\t\5\2\2\u01cf")
        buf.write("\u0086\3\2\2\2\u01d0\u01d1\t\6\2\2\u01d1\u0088\3\2\2\2")
        buf.write("\u01d2\u01d3\t\7\2\2\u01d3\u008a\3\2\2\2\u01d4\u01d8\t")
        buf.write("\b\2\2\u01d5\u01d7\5\u0085C\2\u01d6\u01d5\3\2\2\2\u01d7")
        buf.write("\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01e1\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dd\7")
        buf.write("\62\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\3\2\2\2")
        buf.write("\u01e0\u01d4\3\2\2\2\u01e0\u01dc\3\2\2\2\u01e1\u008c\3")
        buf.write("\2\2\2\u01e2\u01e3\7\62\2\2\u01e3\u01e5\t\t\2\2\u01e4")
        buf.write("\u01e6\5\u0089E\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2")
        buf.write("\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u008e")
        buf.write("\3\2\2\2\u01e9\u01ea\7\62\2\2\u01ea\u01ec\t\n\2\2\u01eb")
        buf.write("\u01ed\5\u0087D\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2")
        buf.write("\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u0090")
        buf.write("\3\2\2\2\u01f0\u01f4\7\60\2\2\u01f1\u01f3\5\u0085C\2\u01f2")
        buf.write("\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f4\u01f5\3\2\2\2\u01f5\u0092\3\2\2\2\u01f6\u01f4\3")
        buf.write("\2\2\2\u01f7\u01f9\t\13\2\2\u01f8\u01fa\t\f\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2")
        buf.write("\u01fb\u01fd\5\u0085C\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0094\3\2\2\2\u0200\u0201\7^\2\2\u0201\u0204\n\r\2\2")
        buf.write("\u0202\u0204\7^\2\2\u0203\u0200\3\2\2\2\u0203\u0202\3")
        buf.write("\2\2\2\u0204\u0096\3\2\2\2\u0205\u0206\7)\2\2\u0206\u020b")
        buf.write("\7$\2\2\u0207\u0208\7^\2\2\u0208\u020b\t\r\2\2\u0209\u020b")
        buf.write("\n\16\2\2\u020a\u0205\3\2\2\2\u020a\u0207\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020b\u0098\3\2\2\2\31\2\u016e\u0176\u017f")
        buf.write("\u0190\u0195\u019a\u01a1\u01a7\u01b3\u01bd\u01c8\u01cc")
        buf.write("\u01d8\u01de\u01e0\u01e7\u01ee\u01f4\u01f9\u01fe\u0203")
        buf.write("\u020a\6\b\2\2\3>\2\3@\3\3A\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    SEMI = 7
    COMMA = 8
    COLON = 9
    DOT = 10
    BODY = 11
    BREAK = 12
    CONTINUE = 13
    DO = 14
    ELSE = 15
    ELSEIF = 16
    ENDBODY = 17
    ENDIF = 18
    ENDFOR = 19
    ENDWHILE = 20
    FOR = 21
    FUNCTION = 22
    IF = 23
    PARAMETER = 24
    RETURN = 25
    THEN = 26
    WHILE = 27
    ENDDO = 28
    VAR = 29
    MAIN = 30
    ASSIGN = 31
    SUBTRACT = 32
    SUBTRACT_F = 33
    NOT = 34
    MULTIPLY = 35
    MULTIPLY_F = 36
    DIVIDE = 37
    DIVIDE_F = 38
    MODULO = 39
    ADD = 40
    ADD_F = 41
    AND = 42
    OR = 43
    EQUAL = 44
    NOT_EQUAL = 45
    LT = 46
    GT = 47
    LTE = 48
    GTE = 49
    NOT_EQUAL_F = 50
    LT_F = 51
    GT_F = 52
    LTE_F = 53
    GTE_F = 54
    WS = 55
    IDENTIFIER = 56
    COMMENT = 57
    BOOLEAN = 58
    INTEGER = 59
    FLOAT = 60
    STRING = 61
    ERROR_CHAR = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", "':'", 
            "'.'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'While'", "'EndDo'", "'Var'", "'main'", "'='", "'-'", "'-.'", 
            "'!'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'+'", "'+.'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COMMA", "COLON", "DOT", "BODY", "BREAK", "CONTINUE", 
            "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
            "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "WHILE", 
            "ENDDO", "VAR", "MAIN", "ASSIGN", "SUBTRACT", "SUBTRACT_F", 
            "NOT", "MULTIPLY", "MULTIPLY_F", "DIVIDE", "DIVIDE_F", "MODULO", 
            "ADD", "ADD_F", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", "GT", 
            "LTE", "GTE", "NOT_EQUAL_F", "LT_F", "GT_F", "LTE_F", "GTE_F", 
            "WS", "IDENTIFIER", "COMMENT", "BOOLEAN", "INTEGER", "FLOAT", 
            "STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "SEMI", 
                  "COMMA", "COLON", "DOT", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "WHILE", "ENDDO", "VAR", "MAIN", "ASSIGN", "SUBTRACT", 
                  "SUBTRACT_F", "NOT", "MULTIPLY", "MULTIPLY_F", "DIVIDE", 
                  "DIVIDE_F", "MODULO", "ADD", "ADD_F", "AND", "OR", "EQUAL", 
                  "NOT_EQUAL", "LT", "GT", "LTE", "GTE", "NOT_EQUAL_F", 
                  "LT_F", "GT_F", "LTE_F", "GTE_F", "WS", "IDENTIFIER", 
                  "COMMENT", "BOOLEAN", "INTEGER", "FLOAT", "STRING", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "DEC_INT", "HEX_INT", 
                  "OCT_INT", "DEC_PART", "EXP_PART", "ILLEGAL_ESC", "CHAR" ]

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
            actions[60] = self.STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.UNCLOSE_STRING_action 
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

     


