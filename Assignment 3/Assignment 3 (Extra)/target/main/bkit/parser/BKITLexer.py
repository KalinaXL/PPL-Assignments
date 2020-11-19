# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


# ID: 1813085
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u020a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+")
        buf.write("\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\6\67")
        buf.write("\u0166\n\67\r\67\16\67\u0167\3\67\3\67\38\38\78\u016e")
        buf.write("\n8\f8\168\u0171\138\39\39\39\39\79\u0177\n9\f9\169\u017a")
        buf.write("\139\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u018a")
        buf.write("\n:\3;\3;\3;\5;\u018f\n;\3<\6<\u0192\n<\r<\16<\u0193\3")
        buf.write("<\3<\3<\3<\3<\5<\u019b\n<\3=\3=\7=\u019f\n=\f=\16=\u01a2")
        buf.write("\13=\3=\3=\3=\3>\3>\3?\3?\7?\u01ab\n?\f?\16?\u01ae\13")
        buf.write("?\3?\3?\3?\3@\3@\7@\u01b5\n@\f@\16@\u01b8\13@\3@\5@\u01bb")
        buf.write("\n@\3@\3@\3A\3A\3A\3A\7A\u01c3\nA\fA\16A\u01c6\13A\3A")
        buf.write("\5A\u01c9\nA\3B\3B\3C\3C\3D\3D\3E\3E\7E\u01d3\nE\fE\16")
        buf.write("E\u01d6\13E\3E\5E\u01d9\nE\3F\3F\3F\3F\7F\u01df\nF\fF")
        buf.write("\16F\u01e2\13F\3G\3G\3G\3G\7G\u01e8\nG\fG\16G\u01eb\13")
        buf.write("G\3H\3H\7H\u01ef\nH\fH\16H\u01f2\13H\3I\3I\5I\u01f6\n")
        buf.write("I\3I\6I\u01f9\nI\rI\16I\u01fa\3J\3J\3J\3J\3J\5J\u0202")
        buf.write("\nJ\3K\3K\3K\3K\3K\5K\u0209\nK\4\u0178\u01c4\2L\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>")
        buf.write("{?}@\177A\u0081B\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\3\2\23\5\2")
        buf.write("\13\f\17\17\"\"\3\2c|\6\2\62;C\\aac|\3\3\f\f\3\2\62;\3")
        buf.write("\2\629\4\2\62;CH\3\2\63;\4\2ZZzz\4\2\63;CH\4\2QQqq\3\2")
        buf.write("\639\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\3\2$$\7\2\f\f\17")
        buf.write("\17$$))^^\2\u0218\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\3\u0097\3\2\2\2\5\u0099\3\2\2\2\7\u009b")
        buf.write("\3\2\2\2\t\u009d\3\2\2\2\13\u009f\3\2\2\2\r\u00a1\3\2")
        buf.write("\2\2\17\u00a3\3\2\2\2\21\u00a5\3\2\2\2\23\u00a7\3\2\2")
        buf.write("\2\25\u00a9\3\2\2\2\27\u00ab\3\2\2\2\31\u00b0\3\2\2\2")
        buf.write("\33\u00b6\3\2\2\2\35\u00bf\3\2\2\2\37\u00c2\3\2\2\2!\u00c7")
        buf.write("\3\2\2\2#\u00ce\3\2\2\2%\u00d6\3\2\2\2\'\u00dc\3\2\2\2")
        buf.write(")\u00e3\3\2\2\2+\u00ec\3\2\2\2-\u00f0\3\2\2\2/\u00f9\3")
        buf.write("\2\2\2\61\u00fc\3\2\2\2\63\u0106\3\2\2\2\65\u010d\3\2")
        buf.write("\2\2\67\u0112\3\2\2\29\u0118\3\2\2\2;\u011e\3\2\2\2=\u0122")
        buf.write("\3\2\2\2?\u0124\3\2\2\2A\u0126\3\2\2\2C\u0129\3\2\2\2")
        buf.write("E\u012b\3\2\2\2G\u012d\3\2\2\2I\u0130\3\2\2\2K\u0132\3")
        buf.write("\2\2\2M\u0135\3\2\2\2O\u0137\3\2\2\2Q\u0139\3\2\2\2S\u013c")
        buf.write("\3\2\2\2U\u013f\3\2\2\2W\u0142\3\2\2\2Y\u0145\3\2\2\2")
        buf.write("[\u0148\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2a\u014f\3")
        buf.write("\2\2\2c\u0152\3\2\2\2e\u0156\3\2\2\2g\u0159\3\2\2\2i\u015c")
        buf.write("\3\2\2\2k\u0160\3\2\2\2m\u0165\3\2\2\2o\u016b\3\2\2\2")
        buf.write("q\u0172\3\2\2\2s\u0189\3\2\2\2u\u018e\3\2\2\2w\u0191\3")
        buf.write("\2\2\2y\u019c\3\2\2\2{\u01a6\3\2\2\2}\u01a8\3\2\2\2\177")
        buf.write("\u01b2\3\2\2\2\u0081\u01be\3\2\2\2\u0083\u01ca\3\2\2\2")
        buf.write("\u0085\u01cc\3\2\2\2\u0087\u01ce\3\2\2\2\u0089\u01d8\3")
        buf.write("\2\2\2\u008b\u01da\3\2\2\2\u008d\u01e3\3\2\2\2\u008f\u01ec")
        buf.write("\3\2\2\2\u0091\u01f3\3\2\2\2\u0093\u0201\3\2\2\2\u0095")
        buf.write("\u0208\3\2\2\2\u0097\u0098\7=\2\2\u0098\4\3\2\2\2\u0099")
        buf.write("\u009a\7.\2\2\u009a\6\3\2\2\2\u009b\u009c\7<\2\2\u009c")
        buf.write("\b\3\2\2\2\u009d\u009e\7\60\2\2\u009e\n\3\2\2\2\u009f")
        buf.write("\u00a0\7]\2\2\u00a0\f\3\2\2\2\u00a1\u00a2\7_\2\2\u00a2")
        buf.write("\16\3\2\2\2\u00a3\u00a4\7*\2\2\u00a4\20\3\2\2\2\u00a5")
        buf.write("\u00a6\7+\2\2\u00a6\22\3\2\2\2\u00a7\u00a8\7}\2\2\u00a8")
        buf.write("\24\3\2\2\2\u00a9\u00aa\7\177\2\2\u00aa\26\3\2\2\2\u00ab")
        buf.write("\u00ac\7D\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7f\2\2\u00ae")
        buf.write("\u00af\7{\2\2\u00af\30\3\2\2\2\u00b0\u00b1\7D\2\2\u00b1")
        buf.write("\u00b2\7t\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7c\2\2\u00b4")
        buf.write("\u00b5\7m\2\2\u00b5\32\3\2\2\2\u00b6\u00b7\7E\2\2\u00b7")
        buf.write("\u00b8\7q\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7w\2\2\u00bd")
        buf.write("\u00be\7g\2\2\u00be\34\3\2\2\2\u00bf\u00c0\7F\2\2\u00c0")
        buf.write("\u00c1\7q\2\2\u00c1\36\3\2\2\2\u00c2\u00c3\7G\2\2\u00c3")
        buf.write("\u00c4\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write(" \3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9\7n\2\2\u00c9")
        buf.write("\u00ca\7u\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7K\2\2\u00cc")
        buf.write("\u00cd\7h\2\2\u00cd\"\3\2\2\2\u00ce\u00cf\7G\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00d1\7f\2\2\u00d1\u00d2\7D\2\2\u00d2")
        buf.write("\u00d3\7q\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5\7{\2\2\u00d5")
        buf.write("$\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7p\2\2\u00d8")
        buf.write("\u00d9\7f\2\2\u00d9\u00da\7K\2\2\u00da\u00db\7h\2\2\u00db")
        buf.write("&\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("\u00df\7f\2\2\u00df\u00e0\7H\2\2\u00e0\u00e1\7q\2\2\u00e1")
        buf.write("\u00e2\7t\2\2\u00e2(\3\2\2\2\u00e3\u00e4\7G\2\2\u00e4")
        buf.write("\u00e5\7p\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7\7Y\2\2\u00e7")
        buf.write("\u00e8\7j\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7n\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb*\3\2\2\2\u00ec\u00ed\7H\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7t\2\2\u00ef,\3\2\2\2\u00f0")
        buf.write("\u00f1\7H\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7e\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7k\2\2\u00f6")
        buf.write("\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8.\3\2\2\2\u00f9")
        buf.write("\u00fa\7K\2\2\u00fa\u00fb\7h\2\2\u00fb\60\3\2\2\2\u00fc")
        buf.write("\u00fd\7R\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7o\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("\u0103\7v\2\2\u0103\u0104\7g\2\2\u0104\u0105\7t\2\2\u0105")
        buf.write("\62\3\2\2\2\u0106\u0107\7T\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("\u0109\7v\2\2\u0109\u010a\7w\2\2\u010a\u010b\7t\2\2\u010b")
        buf.write("\u010c\7p\2\2\u010c\64\3\2\2\2\u010d\u010e\7V\2\2\u010e")
        buf.write("\u010f\7j\2\2\u010f\u0110\7g\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("\66\3\2\2\2\u0112\u0113\7Y\2\2\u0113\u0114\7j\2\2\u0114")
        buf.write("\u0115\7k\2\2\u0115\u0116\7n\2\2\u0116\u0117\7g\2\2\u0117")
        buf.write("8\3\2\2\2\u0118\u0119\7G\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7f\2\2\u011b\u011c\7F\2\2\u011c\u011d\7q\2\2\u011d")
        buf.write(":\3\2\2\2\u011e\u011f\7X\2\2\u011f\u0120\7c\2\2\u0120")
        buf.write("\u0121\7t\2\2\u0121<\3\2\2\2\u0122\u0123\7?\2\2\u0123")
        buf.write(">\3\2\2\2\u0124\u0125\7/\2\2\u0125@\3\2\2\2\u0126\u0127")
        buf.write("\7/\2\2\u0127\u0128\7\60\2\2\u0128B\3\2\2\2\u0129\u012a")
        buf.write("\7#\2\2\u012aD\3\2\2\2\u012b\u012c\7,\2\2\u012cF\3\2\2")
        buf.write("\2\u012d\u012e\7,\2\2\u012e\u012f\7\60\2\2\u012fH\3\2")
        buf.write("\2\2\u0130\u0131\7^\2\2\u0131J\3\2\2\2\u0132\u0133\7^")
        buf.write("\2\2\u0133\u0134\7\60\2\2\u0134L\3\2\2\2\u0135\u0136\7")
        buf.write("\'\2\2\u0136N\3\2\2\2\u0137\u0138\7-\2\2\u0138P\3\2\2")
        buf.write("\2\u0139\u013a\7-\2\2\u013a\u013b\7\60\2\2\u013bR\3\2")
        buf.write("\2\2\u013c\u013d\7(\2\2\u013d\u013e\7(\2\2\u013eT\3\2")
        buf.write("\2\2\u013f\u0140\7~\2\2\u0140\u0141\7~\2\2\u0141V\3\2")
        buf.write("\2\2\u0142\u0143\7?\2\2\u0143\u0144\7?\2\2\u0144X\3\2")
        buf.write("\2\2\u0145\u0146\7#\2\2\u0146\u0147\7?\2\2\u0147Z\3\2")
        buf.write("\2\2\u0148\u0149\7>\2\2\u0149\\\3\2\2\2\u014a\u014b\7")
        buf.write("@\2\2\u014b^\3\2\2\2\u014c\u014d\7>\2\2\u014d\u014e\7")
        buf.write("?\2\2\u014e`\3\2\2\2\u014f\u0150\7@\2\2\u0150\u0151\7")
        buf.write("?\2\2\u0151b\3\2\2\2\u0152\u0153\7?\2\2\u0153\u0154\7")
        buf.write("\61\2\2\u0154\u0155\7?\2\2\u0155d\3\2\2\2\u0156\u0157")
        buf.write("\7>\2\2\u0157\u0158\7\60\2\2\u0158f\3\2\2\2\u0159\u015a")
        buf.write("\7@\2\2\u015a\u015b\7\60\2\2\u015bh\3\2\2\2\u015c\u015d")
        buf.write("\7>\2\2\u015d\u015e\7?\2\2\u015e\u015f\7\60\2\2\u015f")
        buf.write("j\3\2\2\2\u0160\u0161\7@\2\2\u0161\u0162\7?\2\2\u0162")
        buf.write("\u0163\7\60\2\2\u0163l\3\2\2\2\u0164\u0166\t\2\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\b")
        buf.write("\67\2\2\u016an\3\2\2\2\u016b\u016f\t\3\2\2\u016c\u016e")
        buf.write("\t\4\2\2\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170p\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0172\u0173\7,\2\2\u0173\u0174\7,\2\2\u0174")
        buf.write("\u0178\3\2\2\2\u0175\u0177\13\2\2\2\u0176\u0175\3\2\2")
        buf.write("\2\u0177\u017a\3\2\2\2\u0178\u0179\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0178\3\2\2\2\u017b")
        buf.write("\u017c\7,\2\2\u017c\u017d\7,\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017f\b9\2\2\u017fr\3\2\2\2\u0180\u0181\7V\2\2\u0181")
        buf.write("\u0182\7t\2\2\u0182\u0183\7w\2\2\u0183\u018a\7g\2\2\u0184")
        buf.write("\u0185\7H\2\2\u0185\u0186\7c\2\2\u0186\u0187\7n\2\2\u0187")
        buf.write("\u0188\7u\2\2\u0188\u018a\7g\2\2\u0189\u0180\3\2\2\2\u0189")
        buf.write("\u0184\3\2\2\2\u018at\3\2\2\2\u018b\u018f\5\u0089E\2\u018c")
        buf.write("\u018f\5\u008dG\2\u018d\u018f\5\u008bF\2\u018e\u018b\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018fv")
        buf.write("\3\2\2\2\u0190\u0192\5\u0083B\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u019a\3\2\2\2\u0195\u0196\5\u008fH\2\u0196\u0197")
        buf.write("\5\u0091I\2\u0197\u019b\3\2\2\2\u0198\u019b\5\u008fH\2")
        buf.write("\u0199\u019b\5\u0091I\2\u019a\u0195\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019a\u0199\3\2\2\2\u019bx\3\2\2\2\u019c\u01a0")
        buf.write("\7$\2\2\u019d\u019f\5\u0095K\2\u019e\u019d\3\2\2\2\u019f")
        buf.write("\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u01a3\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a4\7")
        buf.write("$\2\2\u01a4\u01a5\b=\3\2\u01a5z\3\2\2\2\u01a6\u01a7\13")
        buf.write("\2\2\2\u01a7|\3\2\2\2\u01a8\u01ac\7$\2\2\u01a9\u01ab\5")
        buf.write("\u0095K\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b0\5\u0093J\2\u01b0\u01b1")
        buf.write("\b?\4\2\u01b1~\3\2\2\2\u01b2\u01b6\7$\2\2\u01b3\u01b5")
        buf.write("\5\u0095K\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01ba\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b9\u01bb\t\5\2\2\u01ba\u01b9\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\b@\5\2\u01bd\u0080")
        buf.write("\3\2\2\2\u01be\u01bf\7,\2\2\u01bf\u01c0\7,\2\2\u01c0\u01c4")
        buf.write("\3\2\2\2\u01c1\u01c3\13\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c6\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c9\7")
        buf.write(",\2\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u0082")
        buf.write("\3\2\2\2\u01ca\u01cb\t\6\2\2\u01cb\u0084\3\2\2\2\u01cc")
        buf.write("\u01cd\t\7\2\2\u01cd\u0086\3\2\2\2\u01ce\u01cf\t\b\2\2")
        buf.write("\u01cf\u0088\3\2\2\2\u01d0\u01d4\t\t\2\2\u01d1\u01d3\5")
        buf.write("\u0083B\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d9\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d7\u01d9\7\62\2\2\u01d8\u01d0")
        buf.write("\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9\u008a\3\2\2\2\u01da")
        buf.write("\u01db\7\62\2\2\u01db\u01dc\t\n\2\2\u01dc\u01e0\t\13\2")
        buf.write("\2\u01dd\u01df\5\u0087D\2\u01de\u01dd\3\2\2\2\u01df\u01e2")
        buf.write("\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u008c\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7\62\2")
        buf.write("\2\u01e4\u01e5\t\f\2\2\u01e5\u01e9\t\r\2\2\u01e6\u01e8")
        buf.write("\5\u0085C\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u008e\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01ec\u01f0\7\60\2\2\u01ed\u01ef")
        buf.write("\5\u0083B\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u0090\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f5\t\16\2\2\u01f4\u01f6")
        buf.write("\t\17\2\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f8\3\2\2\2\u01f7\u01f9\5\u0083B\2\u01f8\u01f7\3\2")
        buf.write("\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u0092\3\2\2\2\u01fc\u01fd\7^\2\2\u01fd")
        buf.write("\u0202\n\20\2\2\u01fe\u0202\7^\2\2\u01ff\u0200\7)\2\2")
        buf.write("\u0200\u0202\n\21\2\2\u0201\u01fc\3\2\2\2\u0201\u01fe")
        buf.write("\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0094\3\2\2\2\u0203")
        buf.write("\u0204\7)\2\2\u0204\u0209\7$\2\2\u0205\u0206\7^\2\2\u0206")
        buf.write("\u0209\t\20\2\2\u0207\u0209\n\22\2\2\u0208\u0203\3\2\2")
        buf.write("\2\u0208\u0205\3\2\2\2\u0208\u0207\3\2\2\2\u0209\u0096")
        buf.write("\3\2\2\2\31\2\u0167\u016f\u0178\u0189\u018e\u0193\u019a")
        buf.write("\u01a0\u01ac\u01b6\u01ba\u01c4\u01c8\u01d4\u01d8\u01e0")
        buf.write("\u01e9\u01f0\u01f5\u01fa\u0201\u0208\6\b\2\2\3=\2\3?\3")
        buf.write("\3@\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEMI = 1
    COMMA = 2
    COLON = 3
    DOT = 4
    OSB = 5
    CSB = 6
    ORB = 7
    CRB = 8
    OCB = 9
    CCB = 10
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
    ASSIGN = 30
    SUBTRACT = 31
    SUBTRACT_F = 32
    NOT = 33
    MULTIPLY = 34
    MULTIPLY_F = 35
    DIVIDE = 36
    DIVIDE_F = 37
    MODULO = 38
    ADD = 39
    ADD_F = 40
    AND = 41
    OR = 42
    EQUAL = 43
    NOT_EQUAL = 44
    LT = 45
    GT = 46
    LTE = 47
    GTE = 48
    NOT_EQUAL_F = 49
    LT_F = 50
    GT_F = 51
    LTE_F = 52
    GTE_F = 53
    WS = 54
    IDENTIFIER = 55
    COMMENT = 56
    BOOLEAN = 57
    INTEGER = 58
    FLOAT = 59
    STRING = 60
    ERROR_CHAR = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    UNTERMINATED_COMMENT = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "':'", "'.'", "'['", "']'", "'('", "')'", "'{'", 
            "'}'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'While'", "'EndDo'", "'Var'", "'='", "'-'", "'-.'", "'!'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'+'", "'+.'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COMMA", "COLON", "DOT", "OSB", "CSB", "ORB", "CRB", 
            "OCB", "CCB", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "WHILE", "ENDDO", "VAR", 
            "ASSIGN", "SUBTRACT", "SUBTRACT_F", "NOT", "MULTIPLY", "MULTIPLY_F", 
            "DIVIDE", "DIVIDE_F", "MODULO", "ADD", "ADD_F", "AND", "OR", 
            "EQUAL", "NOT_EQUAL", "LT", "GT", "LTE", "GTE", "NOT_EQUAL_F", 
            "LT_F", "GT_F", "LTE_F", "GTE_F", "WS", "IDENTIFIER", "COMMENT", 
            "BOOLEAN", "INTEGER", "FLOAT", "STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "SEMI", "COMMA", "COLON", "DOT", "OSB", "CSB", "ORB", 
                  "CRB", "OCB", "CCB", "BODY", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "WHILE", "ENDDO", "VAR", "ASSIGN", "SUBTRACT", "SUBTRACT_F", 
                  "NOT", "MULTIPLY", "MULTIPLY_F", "DIVIDE", "DIVIDE_F", 
                  "MODULO", "ADD", "ADD_F", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LT", "GT", "LTE", "GTE", "NOT_EQUAL_F", "LT_F", "GT_F", 
                  "LTE_F", "GTE_F", "WS", "IDENTIFIER", "COMMENT", "BOOLEAN", 
                  "INTEGER", "FLOAT", "STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "DEC_INT", "HEX_INT", "OCT_INT", "DEC_PART", 
                  "EXP_PART", "ILLEGAL_ESC", "CHAR" ]

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
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.UNCLOSE_STRING_action 
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

                if self.text[-1] == '\n':
                    self.text = self.text[1: -1];
                else:
                    self.text = self.text[1: ];

     


