# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\7\2X\n")
        buf.write("\2\f\2\16\2[\13\2\3\2\3\2\3\3\3\3\5\3a\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4h\n\4\3\5\3\5\3\5\3\5\3\5\5\5o\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\7\6w\n\6\f\6\16\6z\13\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\7\7\u0082\n\7\f\7\16\7\u0085\13\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\7\b\u008d\n\b\f\b\16\b\u0090\13\b\3\t\3")
        buf.write("\t\3\t\5\t\u0095\n\t\3\n\3\n\3\n\5\n\u009a\n\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00a0\n\13\3\f\3\f\5\f\u00a4\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00ab\n\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u00b2\n\16\f\16\16\16\u00b5\13\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\6\17\u00bd\n\17\r\17\16\17\u00be\3")
        buf.write("\20\3\20\5\20\u00c3\n\20\3\21\3\21\3\21\5\21\u00c8\n\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\7\23\u00cf\n\23\f\23\16\23\u00d2")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00da\n\24\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00e0\n\25\3\25\3\25\3\25\7\25")
        buf.write("\u00e5\n\25\f\25\16\25\u00e8\13\25\3\25\7\25\u00eb\n\25")
        buf.write("\f\25\16\25\u00ee\13\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\7\27\u00fa\n\27\f\27\16\27\u00fd")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u0108\n\30\3\31\3\31\3\31\3\31\5\31\u010e\n\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\6\32\u0118\n\32\r")
        buf.write("\32\16\32\u0119\3\33\3\33\3\33\7\33\u011f\n\33\f\33\16")
        buf.write("\33\u0122\13\33\3\33\5\33\u0125\n\33\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\7\34\u012d\n\34\f\34\16\34\u0130\13\34\3")
        buf.write("\34\7\34\u0133\n\34\f\34\16\34\u0136\13\34\3\35\3\35\3")
        buf.write("\35\3\35\7\35\u013c\n\35\f\35\16\35\u013f\13\35\3\35\7")
        buf.write("\35\u0142\n\35\f\35\16\35\u0145\13\35\3\36\3\36\7\36\u0149")
        buf.write("\n\36\f\36\16\36\u014c\13\36\3\36\7\36\u014f\n\36\f\36")
        buf.write("\16\36\u0152\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u015a\n\37\f\37\16\37\u015d\13\37\3\37\7\37\u0160\n\37")
        buf.write("\f\37\16\37\u0163\13\37\3\37\3\37\3\37\3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\7!\u0174\n!\f!\16!\u0177\13!\3!")
        buf.write("\7!\u017a\n!\f!\16!\u017d\13!\3!\3!\3!\3\"\3\"\7\"\u0184")
        buf.write("\n\"\f\"\16\"\u0187\13\"\3\"\7\"\u018a\n\"\f\"\16\"\u018d")
        buf.write("\13\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\7")
        buf.write("%\u019d\n%\f%\16%\u01a0\13%\3&\3&\3&\5&\u01a5\n&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\5(\u01ae\n(\3(\3(\3(\2\5\n\f\16)\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLN\2\7\3\2-\67\3\2+,\4\2!\")*\3\2$(\3\2!")
        buf.write("\"\2\u01bf\2S\3\2\2\2\4`\3\2\2\2\6g\3\2\2\2\bn\3\2\2\2")
        buf.write("\np\3\2\2\2\f{\3\2\2\2\16\u0086\3\2\2\2\20\u0094\3\2\2")
        buf.write("\2\22\u0099\3\2\2\2\24\u009f\3\2\2\2\26\u00a3\3\2\2\2")
        buf.write("\30\u00aa\3\2\2\2\32\u00ac\3\2\2\2\34\u00b8\3\2\2\2\36")
        buf.write("\u00c2\3\2\2\2 \u00c4\3\2\2\2\"\u00c9\3\2\2\2$\u00cb\3")
        buf.write("\2\2\2&\u00d9\3\2\2\2(\u00db\3\2\2\2*\u00f2\3\2\2\2,\u00f6")
        buf.write("\3\2\2\2.\u0107\3\2\2\2\60\u010d\3\2\2\2\62\u0117\3\2")
        buf.write("\2\2\64\u011b\3\2\2\2\66\u0129\3\2\2\28\u0137\3\2\2\2")
        buf.write(":\u0146\3\2\2\2<\u0153\3\2\2\2>\u0167\3\2\2\2@\u016f\3")
        buf.write("\2\2\2B\u0181\3\2\2\2D\u0193\3\2\2\2F\u0196\3\2\2\2H\u0199")
        buf.write("\3\2\2\2J\u01a1\3\2\2\2L\u01a8\3\2\2\2N\u01ab\3\2\2\2")
        buf.write("PR\5\32\16\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T")
        buf.write("Y\3\2\2\2US\3\2\2\2VX\5(\25\2WV\3\2\2\2X[\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\2\2\3]\3\3")
        buf.write("\2\2\2^a\5\6\4\2_a\79\2\2`^\3\2\2\2`_\3\2\2\2a\5\3\2\2")
        buf.write("\2bh\7<\2\2ch\7=\2\2dh\7;\2\2eh\7>\2\2fh\5&\24\2gb\3\2")
        buf.write("\2\2gc\3\2\2\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2h\7\3\2\2")
        buf.write("\2ij\5\n\6\2jk\t\2\2\2kl\5\n\6\2lo\3\2\2\2mo\5\n\6\2n")
        buf.write("i\3\2\2\2nm\3\2\2\2o\t\3\2\2\2pq\b\6\1\2qr\5\f\7\2rx\3")
        buf.write("\2\2\2st\f\4\2\2tu\t\3\2\2uw\5\f\7\2vs\3\2\2\2wz\3\2\2")
        buf.write("\2xv\3\2\2\2xy\3\2\2\2y\13\3\2\2\2zx\3\2\2\2{|\b\7\1\2")
        buf.write("|}\5\16\b\2}\u0083\3\2\2\2~\177\f\4\2\2\177\u0080\t\4")
        buf.write("\2\2\u0080\u0082\5\16\b\2\u0081~\3\2\2\2\u0082\u0085\3")
        buf.write("\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\r")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\b\b\1\2\u0087")
        buf.write("\u0088\5\20\t\2\u0088\u008e\3\2\2\2\u0089\u008a\f\4\2")
        buf.write("\2\u008a\u008b\t\5\2\2\u008b\u008d\5\20\t\2\u008c\u0089")
        buf.write("\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\17\3\2\2\2\u0090\u008e\3\2\2\2\u0091")
        buf.write("\u0095\5\22\n\2\u0092\u0093\7#\2\2\u0093\u0095\5\20\t")
        buf.write("\2\u0094\u0091\3\2\2\2\u0094\u0092\3\2\2\2\u0095\21\3")
        buf.write("\2\2\2\u0096\u009a\5\24\13\2\u0097\u0098\t\6\2\2\u0098")
        buf.write("\u009a\5\22\n\2\u0099\u0096\3\2\2\2\u0099\u0097\3\2\2")
        buf.write("\2\u009a\23\3\2\2\2\u009b\u00a0\5\26\f\2\u009c\u009d\5")
        buf.write("\26\f\2\u009d\u009e\5\62\32\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u009b\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\25\3\2\2\2\u00a1")
        buf.write("\u00a4\5\30\r\2\u00a2\u00a4\5J&\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a4\27\3\2\2\2\u00a5\u00a6\7\t")
        buf.write("\2\2\u00a6\u00a7\5\b\5\2\u00a7\u00a8\7\n\2\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00ab\5\4\3\2\u00aa\u00a5\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00ad\7\37\2\2\u00ad")
        buf.write("\u00ae\7\5\2\2\u00ae\u00b3\5 \21\2\u00af\u00b0\7\4\2\2")
        buf.write("\u00b0\u00b2\5 \21\2\u00b1\u00af\3\2\2\2\u00b2\u00b5\3")
        buf.write("\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\7\3\2\2\u00b7")
        buf.write("\33\3\2\2\2\u00b8\u00bc\79\2\2\u00b9\u00ba\7\7\2\2\u00ba")
        buf.write("\u00bb\7<\2\2\u00bb\u00bd\7\b\2\2\u00bc\u00b9\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3")
        buf.write("\2\2\2\u00bf\35\3\2\2\2\u00c0\u00c3\79\2\2\u00c1\u00c3")
        buf.write("\5\34\17\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3")
        buf.write("\37\3\2\2\2\u00c4\u00c7\5\36\20\2\u00c5\u00c6\7 \2\2\u00c6")
        buf.write("\u00c8\5\"\22\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2")
        buf.write("\2\u00c8!\3\2\2\2\u00c9\u00ca\5\6\4\2\u00ca#\3\2\2\2\u00cb")
        buf.write("\u00d0\5\"\22\2\u00cc\u00cd\7\4\2\2\u00cd\u00cf\5\"\22")
        buf.write("\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1%\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d3\u00d4\7\13\2\2\u00d4\u00d5\5$\23\2\u00d5")
        buf.write("\u00d6\7\f\2\2\u00d6\u00da\3\2\2\2\u00d7\u00d8\7\13\2")
        buf.write("\2\u00d8\u00da\7\f\2\2\u00d9\u00d3\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00da\'\3\2\2\2\u00db\u00dc\7\30\2\2\u00dc\u00dd")
        buf.write("\7\5\2\2\u00dd\u00df\79\2\2\u00de\u00e0\5*\26\2\u00df")
        buf.write("\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\7\r\2\2\u00e2\u00e6\7\5\2\2\u00e3\u00e5\5")
        buf.write("\32\16\2\u00e4\u00e3\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ec\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e9\u00eb\5.\30\2\u00ea\u00e9\3")
        buf.write("\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write("\u00f0\7\23\2\2\u00f0\u00f1\7\6\2\2\u00f1)\3\2\2\2\u00f2")
        buf.write("\u00f3\7\32\2\2\u00f3\u00f4\7\5\2\2\u00f4\u00f5\5,\27")
        buf.write("\2\u00f5+\3\2\2\2\u00f6\u00fb\5\36\20\2\u00f7\u00f8\7")
        buf.write("\4\2\2\u00f8\u00fa\5\36\20\2\u00f9\u00f7\3\2\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc-\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0108\5\60\31")
        buf.write("\2\u00ff\u0108\5\64\33\2\u0100\u0108\5<\37\2\u0101\u0108")
        buf.write("\5@!\2\u0102\u0108\5B\"\2\u0103\u0108\5D#\2\u0104\u0108")
        buf.write("\5F$\2\u0105\u0108\5L\'\2\u0106\u0108\5N(\2\u0107\u00fe")
        buf.write("\3\2\2\2\u0107\u00ff\3\2\2\2\u0107\u0100\3\2\2\2\u0107")
        buf.write("\u0101\3\2\2\2\u0107\u0102\3\2\2\2\u0107\u0103\3\2\2\2")
        buf.write("\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3")
        buf.write("\2\2\2\u0108/\3\2\2\2\u0109\u010e\79\2\2\u010a\u010b\5")
        buf.write("\b\5\2\u010b\u010c\5\62\32\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u0109\3\2\2\2\u010d\u010a\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\7 \2\2\u0110\u0111\5\b\5\2\u0111\u0112\7")
        buf.write("\3\2\2\u0112\61\3\2\2\2\u0113\u0114\7\7\2\2\u0114\u0115")
        buf.write("\5\b\5\2\u0115\u0116\7\b\2\2\u0116\u0118\3\2\2\2\u0117")
        buf.write("\u0113\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u0119\u011a\3\2\2\2\u011a\63\3\2\2\2\u011b\u011c\7\31")
        buf.write("\2\2\u011c\u0120\5\66\34\2\u011d\u011f\58\35\2\u011e\u011d")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0123\u0125\5:\36\2\u0124\u0123\3\2\2\2\u0124\u0125\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\7\24\2\2\u0127")
        buf.write("\u0128\7\6\2\2\u0128\65\3\2\2\2\u0129\u012a\5\b\5\2\u012a")
        buf.write("\u012e\7\34\2\2\u012b\u012d\5\32\16\2\u012c\u012b\3\2")
        buf.write("\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u0134\3\2\2\2\u0130\u012e\3\2\2\2\u0131")
        buf.write("\u0133\5.\30\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\67\3\2")
        buf.write("\2\2\u0136\u0134\3\2\2\2\u0137\u0138\7\22\2\2\u0138\u0139")
        buf.write("\5\b\5\2\u0139\u013d\7\34\2\2\u013a\u013c\5\32\16\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u0143\3\2\2\2\u013f\u013d\3")
        buf.write("\2\2\2\u0140\u0142\5.\30\2\u0141\u0140\3\2\2\2\u0142\u0145")
        buf.write("\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("9\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u014a\7\21\2\2\u0147")
        buf.write("\u0149\5\32\16\2\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2")
        buf.write("\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u0150")
        buf.write("\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014f\5.\30\2\u014e")
        buf.write("\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151;\3\2\2\2\u0152\u0150\3\2\2")
        buf.write("\2\u0153\u0154\7\27\2\2\u0154\u0155\7\t\2\2\u0155\u0156")
        buf.write("\5> \2\u0156\u0157\7\n\2\2\u0157\u015b\7\20\2\2\u0158")
        buf.write("\u015a\5\32\16\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2")
        buf.write("\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u0161")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0160\5.\30\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0164\u0165\7\25\2\2\u0165\u0166\7\6\2\2\u0166")
        buf.write("=\3\2\2\2\u0167\u0168\79\2\2\u0168\u0169\7 \2\2\u0169")
        buf.write("\u016a\5\b\5\2\u016a\u016b\7\4\2\2\u016b\u016c\5\b\5\2")
        buf.write("\u016c\u016d\7\4\2\2\u016d\u016e\5\b\5\2\u016e?\3\2\2")
        buf.write("\2\u016f\u0170\7\35\2\2\u0170\u0171\5\b\5\2\u0171\u0175")
        buf.write("\7\20\2\2\u0172\u0174\5\32\16\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u017b\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a\5")
        buf.write(".\30\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u017f\7\26\2\2\u017f\u0180\7\6\2")
        buf.write("\2\u0180A\3\2\2\2\u0181\u0185\7\20\2\2\u0182\u0184\5\32")
        buf.write("\16\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u018b\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0188\u018a\5.\30\2\u0189\u0188\3\2\2\2")
        buf.write("\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f")
        buf.write("\7\35\2\2\u018f\u0190\5\b\5\2\u0190\u0191\7\36\2\2\u0191")
        buf.write("\u0192\7\6\2\2\u0192C\3\2\2\2\u0193\u0194\7\16\2\2\u0194")
        buf.write("\u0195\7\3\2\2\u0195E\3\2\2\2\u0196\u0197\7\17\2\2\u0197")
        buf.write("\u0198\7\3\2\2\u0198G\3\2\2\2\u0199\u019e\5\b\5\2\u019a")
        buf.write("\u019b\7\4\2\2\u019b\u019d\5\b\5\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019fI\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2")
        buf.write("\79\2\2\u01a2\u01a4\7\t\2\2\u01a3\u01a5\5H%\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a7\7\n\2\2\u01a7K\3\2\2\2\u01a8\u01a9\5J&\2\u01a9")
        buf.write("\u01aa\7\3\2\2\u01aaM\3\2\2\2\u01ab\u01ad\7\33\2\2\u01ac")
        buf.write("\u01ae\5\b\5\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b0\7\3\2\2\u01b0O\3\2\2")
        buf.write("\2-SY`gnx\u0083\u008e\u0094\u0099\u009f\u00a3\u00aa\u00b3")
        buf.write("\u00be\u00c2\u00c7\u00d0\u00d9\u00df\u00e6\u00ec\u00fb")
        buf.write("\u0107\u010d\u0119\u0120\u0124\u012e\u0134\u013d\u0143")
        buf.write("\u014a\u0150\u015b\u0161\u0175\u017b\u0185\u018b\u019e")
        buf.write("\u01a4\u01ad")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'.'", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'While'", "'EndDo'", 
                     "'Var'", "'='", "'-'", "'-.'", "'!'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'+'", "'+.'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>", "SEMI", "COMMA", "COLON", "DOT", "OSB", 
                      "CSB", "ORB", "CRB", "OCB", "CCB", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "WHILE", "ENDDO", "VAR", "ASSIGN", 
                      "SUBTRACT", "SUBTRACT_F", "NOT", "MULTIPLY", "MULTIPLY_F", 
                      "DIVIDE", "DIVIDE_F", "MODULO", "ADD", "ADD_F", "AND", 
                      "OR", "EQUAL", "NOT_EQUAL", "LT", "GT", "LTE", "GTE", 
                      "NOT_EQUAL_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "WS", 
                      "IDENTIFIER", "COMMENT", "BOOLEAN", "INTEGER", "FLOAT", 
                      "STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_operands = 1
    RULE_literal = 2
    RULE_expression = 3
    RULE_exp1 = 4
    RULE_exp2 = 5
    RULE_exp3 = 6
    RULE_exp4 = 7
    RULE_exp5 = 8
    RULE_exp6 = 9
    RULE_exp7 = 10
    RULE_exp8 = 11
    RULE_variable_declaration = 12
    RULE_array_name = 13
    RULE_variable_name = 14
    RULE_variable_initializer = 15
    RULE_variable_value = 16
    RULE_array_value = 17
    RULE_array_value_list = 18
    RULE_function_declaration = 19
    RULE_parameters = 20
    RULE_parameter_list = 21
    RULE_post_statement = 22
    RULE_assignment = 23
    RULE_indices = 24
    RULE_if_statement = 25
    RULE_if_start = 26
    RULE_elseif_statement = 27
    RULE_else_statement = 28
    RULE_for_statement = 29
    RULE_for_condition = 30
    RULE_while_statement = 31
    RULE_do_while_statement = 32
    RULE_break_statement = 33
    RULE_continue_statement = 34
    RULE_in_parameters = 35
    RULE_call_function = 36
    RULE_call_statement = 37
    RULE_return_statement = 38

    ruleNames =  [ "program", "operands", "literal", "expression", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "variable_declaration", "array_name", "variable_name", 
                   "variable_initializer", "variable_value", "array_value", 
                   "array_value_list", "function_declaration", "parameters", 
                   "parameter_list", "post_statement", "assignment", "indices", 
                   "if_statement", "if_start", "elseif_statement", "else_statement", 
                   "for_statement", "for_condition", "while_statement", 
                   "do_while_statement", "break_statement", "continue_statement", 
                   "in_parameters", "call_function", "call_statement", "return_statement" ]

    EOF = Token.EOF
    SEMI=1
    COMMA=2
    COLON=3
    DOT=4
    OSB=5
    CSB=6
    ORB=7
    CRB=8
    OCB=9
    CCB=10
    BODY=11
    BREAK=12
    CONTINUE=13
    DO=14
    ELSE=15
    ELSEIF=16
    ENDBODY=17
    ENDIF=18
    ENDFOR=19
    ENDWHILE=20
    FOR=21
    FUNCTION=22
    IF=23
    PARAMETER=24
    RETURN=25
    THEN=26
    WHILE=27
    ENDDO=28
    VAR=29
    ASSIGN=30
    SUBTRACT=31
    SUBTRACT_F=32
    NOT=33
    MULTIPLY=34
    MULTIPLY_F=35
    DIVIDE=36
    DIVIDE_F=37
    MODULO=38
    ADD=39
    ADD_F=40
    AND=41
    OR=42
    EQUAL=43
    NOT_EQUAL=44
    LT=45
    GT=46
    LTE=47
    GTE=48
    NOT_EQUAL_F=49
    LT_F=50
    GT_F=51
    LTE_F=52
    GTE_F=53
    WS=54
    IDENTIFIER=55
    COMMENT=56
    BOOLEAN=57
    INTEGER=58
    FLOAT=59
    STRING=60
    ERROR_CHAR=61
    ILLEGAL_ESCAPE=62
    UNCLOSE_STRING=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def function_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_declarationContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 78
                self.variable_declaration()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 84
                self.function_declaration()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operands)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.OCB, BKITParser.BOOLEAN, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.literal()
                pass
            elif token in [BKITParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(BKITParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def array_value_list(self):
            return self.getTypedRuleContext(BKITParser.Array_value_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(BKITParser.BOOLEAN)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.OCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.array_value_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKITParser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def LTE(self):
            return self.getToken(BKITParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKITParser.GTE, 0)

        def NOT_EQUAL_F(self):
            return self.getToken(BKITParser.NOT_EQUAL_F, 0)

        def LT_F(self):
            return self.getToken(BKITParser.LT_F, 0)

        def GT_F(self):
            return self.getToken(BKITParser.GT_F, 0)

        def LTE_F(self):
            return self.getToken(BKITParser.LTE_F, 0)

        def GTE_F(self):
            return self.getToken(BKITParser.GTE_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.exp1(0)
                self.state = 104
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL) | (1 << BKITParser.LT) | (1 << BKITParser.GT) | (1 << BKITParser.LTE) | (1 << BKITParser.GTE) | (1 << BKITParser.NOT_EQUAL_F) | (1 << BKITParser.LT_F) | (1 << BKITParser.GT_F) | (1 << BKITParser.LTE_F) | (1 << BKITParser.GTE_F))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 105
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 113
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 114
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 115
                    self.exp2(0) 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADD_F(self):
            return self.getToken(BKITParser.ADD_F, 0)

        def SUBTRACT(self):
            return self.getToken(BKITParser.SUBTRACT, 0)

        def SUBTRACT_F(self):
            return self.getToken(BKITParser.SUBTRACT_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 124
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 125
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.ADD) | (1 << BKITParser.ADD_F))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 126
                    self.exp3(0) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MULTIPLY(self):
            return self.getToken(BKITParser.MULTIPLY, 0)

        def MULTIPLY_F(self):
            return self.getToken(BKITParser.MULTIPLY_F, 0)

        def DIVIDE(self):
            return self.getToken(BKITParser.DIVIDE, 0)

        def DIVIDE_F(self):
            return self.getToken(BKITParser.DIVIDE_F, 0)

        def MODULO(self):
            return self.getToken(BKITParser.MODULO, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 135
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 136
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MULTIPLY) | (1 << BKITParser.MULTIPLY_F) | (1 << BKITParser.DIVIDE) | (1 << BKITParser.DIVIDE_F) | (1 << BKITParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 137
                    self.exp4() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp4)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ORB, BKITParser.OCB, BKITParser.SUBTRACT, BKITParser.SUBTRACT_F, BKITParser.IDENTIFIER, BKITParser.BOOLEAN, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.exp5()
                pass
            elif token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(BKITParser.NOT)
                self.state = 145
                self.exp4()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUBTRACT(self):
            return self.getToken(BKITParser.SUBTRACT, 0)

        def SUBTRACT_F(self):
            return self.getToken(BKITParser.SUBTRACT_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ORB, BKITParser.OCB, BKITParser.IDENTIFIER, BKITParser.BOOLEAN, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.exp6()
                pass
            elif token in [BKITParser.SUBTRACT, BKITParser.SUBTRACT_F]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUBTRACT or _la==BKITParser.SUBTRACT_F):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def indices(self):
            return self.getTypedRuleContext(BKITParser.IndicesContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp6)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.exp7()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.exp7()
                self.state = 155
                self.indices()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(BKITParser.Exp8Context,0)


        def call_function(self):
            return self.getTypedRuleContext(BKITParser.Call_functionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp7)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.exp8()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.call_function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORB(self):
            return self.getToken(BKITParser.ORB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def CRB(self):
            return self.getToken(BKITParser.CRB, 0)

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKITParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp8)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ORB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(BKITParser.ORB)
                self.state = 164
                self.expression()
                self.state = 165
                self.match(BKITParser.CRB)
                pass
            elif token in [BKITParser.OCB, BKITParser.IDENTIFIER, BKITParser.BOOLEAN, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_initializerContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_initializerContext,i)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = BKITParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BKITParser.VAR)
            self.state = 171
            self.match(BKITParser.COLON)
            self.state = 172
            self.variable_initializer()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 173
                self.match(BKITParser.COMMA)
                self.state = 174
                self.variable_initializer()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def OSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.OSB)
            else:
                return self.getToken(BKITParser.OSB, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def CSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CSB)
            else:
                return self.getToken(BKITParser.CSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_name" ):
                return visitor.visitArray_name(self)
            else:
                return visitor.visitChildren(self)




    def array_name(self):

        localctx = BKITParser.Array_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BKITParser.IDENTIFIER)
            self.state = 186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 183
                self.match(BKITParser.OSB)
                self.state = 184
                self.match(BKITParser.INTEGER)
                self.state = 185
                self.match(BKITParser.CSB)
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.OSB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def array_name(self):
            return self.getTypedRuleContext(BKITParser.Array_nameContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_name" ):
                return visitor.visitVariable_name(self)
            else:
                return visitor.visitChildren(self)




    def variable_name(self):

        localctx = BKITParser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable_name)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.array_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(BKITParser.Variable_nameContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def variable_value(self):
            return self.getTypedRuleContext(BKITParser.Variable_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_initializer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_initializer" ):
                return visitor.visitVariable_initializer(self)
            else:
                return visitor.visitChildren(self)




    def variable_initializer(self):

        localctx = BKITParser.Variable_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_variable_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.variable_name()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 195
                self.match(BKITParser.ASSIGN)
                self.state = 196
                self.variable_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_value" ):
                return visitor.visitVariable_value(self)
            else:
                return visitor.visitChildren(self)




    def variable_value(self):

        localctx = BKITParser.Variable_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variable_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_valueContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_valueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = BKITParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.variable_value()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 202
                self.match(BKITParser.COMMA)
                self.state = 203
                self.variable_value()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCB(self):
            return self.getToken(BKITParser.OCB, 0)

        def array_value(self):
            return self.getTypedRuleContext(BKITParser.Array_valueContext,0)


        def CCB(self):
            return self.getToken(BKITParser.CCB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array_value_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_list" ):
                return visitor.visitArray_value_list(self)
            else:
                return visitor.visitChildren(self)




    def array_value_list(self):

        localctx = BKITParser.Array_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_value_list)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(BKITParser.OCB)
                self.state = 210
                self.array_value()
                self.state = 211
                self.match(BKITParser.CCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(BKITParser.OCB)
                self.state = 214
                self.match(BKITParser.CCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def parameters(self):
            return self.getTypedRuleContext(BKITParser.ParametersContext,0)


        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = BKITParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BKITParser.FUNCTION)
            self.state = 218
            self.match(BKITParser.COLON)
            self.state = 219
            self.match(BKITParser.IDENTIFIER)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 220
                self.parameters()


            self.state = 223
            self.match(BKITParser.BODY)
            self.state = 224
            self.match(BKITParser.COLON)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 225
                self.variable_declaration()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 231
                self.post_statement()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self.match(BKITParser.ENDBODY)
            self.state = 238
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = BKITParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BKITParser.PARAMETER)
            self.state = 241
            self.match(BKITParser.COLON)
            self.state = 242
            self.parameter_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_nameContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = BKITParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.variable_name()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 245
                self.match(BKITParser.COMMA)
                self.state = 246
                self.variable_name()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Post_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BKITParser.AssignmentContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKITParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKITParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BKITParser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(BKITParser.Do_while_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKITParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKITParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(BKITParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKITParser.Return_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_post_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPost_statement" ):
                return visitor.visitPost_statement(self)
            else:
                return visitor.visitChildren(self)




    def post_statement(self):

        localctx = BKITParser.Post_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_post_statement)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.do_while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 259
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 260
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def indices(self):
            return self.getTypedRuleContext(BKITParser.IndicesContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BKITParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 264
                self.expression()
                self.state = 265
                self.indices()
                pass


            self.state = 269
            self.match(BKITParser.ASSIGN)
            self.state = 270
            self.expression()
            self.state = 271
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.OSB)
            else:
                return self.getToken(BKITParser.OSB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def CSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CSB)
            else:
                return self.getToken(BKITParser.CSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_indices

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndices" ):
                return visitor.visitIndices(self)
            else:
                return visitor.visitChildren(self)




    def indices(self):

        localctx = BKITParser.IndicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_indices)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 273
                    self.match(BKITParser.OSB)
                    self.state = 274
                    self.expression()
                    self.state = 275
                    self.match(BKITParser.CSB)

                else:
                    raise NoViableAltException(self)
                self.state = 279 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def if_start(self):
            return self.getTypedRuleContext(BKITParser.If_startContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Elseif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKITParser.IF)
            self.state = 282
            self.if_start()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 283
                self.elseif_statement()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 289
                self.else_statement()


            self.state = 292
            self.match(BKITParser.ENDIF)
            self.state = 293
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_startContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_if_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_start" ):
                return visitor.visitIf_start(self)
            else:
                return visitor.visitChildren(self)




    def if_start(self):

        localctx = BKITParser.If_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expression()
            self.state = 296
            self.match(BKITParser.THEN)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 297
                self.variable_declaration()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 303
                self.post_statement()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = BKITParser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elseif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(BKITParser.ELSEIF)
            self.state = 310
            self.expression()
            self.state = 311
            self.match(BKITParser.THEN)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 312
                self.variable_declaration()
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 318
                self.post_statement()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = BKITParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(BKITParser.ELSE)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 325
                self.variable_declaration()
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 331
                self.post_statement()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def ORB(self):
            return self.getToken(BKITParser.ORB, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def CRB(self):
            return self.getToken(BKITParser.CRB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKITParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BKITParser.FOR)
            self.state = 338
            self.match(BKITParser.ORB)
            self.state = 339
            self.for_condition()
            self.state = 340
            self.match(BKITParser.CRB)
            self.state = 341
            self.match(BKITParser.DO)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 342
                self.variable_declaration()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 348
                self.post_statement()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 354
            self.match(BKITParser.ENDFOR)
            self.state = 355
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BKITParser.IDENTIFIER)
            self.state = 358
            self.match(BKITParser.ASSIGN)
            self.state = 359
            self.expression()
            self.state = 360
            self.match(BKITParser.COMMA)
            self.state = 361
            self.expression()
            self.state = 362
            self.match(BKITParser.COMMA)
            self.state = 363
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = BKITParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(BKITParser.WHILE)
            self.state = 366
            self.expression()
            self.state = 367
            self.match(BKITParser.DO)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 368
                self.variable_declaration()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 374
                self.post_statement()
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 380
            self.match(BKITParser.ENDWHILE)
            self.state = 381
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declarationContext,i)


        def post_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Post_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Post_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = BKITParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(BKITParser.DO)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 384
                self.variable_declaration()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 390
                    self.post_statement() 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 396
            self.match(BKITParser.WHILE)
            self.state = 397
            self.expression()
            self.state = 398
            self.match(BKITParser.ENDDO)
            self.state = 399
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(BKITParser.BREAK)
            self.state = 402
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(BKITParser.CONTINUE)
            self.state = 405
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class In_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_in_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIn_parameters" ):
                return visitor.visitIn_parameters(self)
            else:
                return visitor.visitChildren(self)




    def in_parameters(self):

        localctx = BKITParser.In_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_in_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expression()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 408
                self.match(BKITParser.COMMA)
                self.state = 409
                self.expression()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def ORB(self):
            return self.getToken(BKITParser.ORB, 0)

        def CRB(self):
            return self.getToken(BKITParser.CRB, 0)

        def in_parameters(self):
            return self.getTypedRuleContext(BKITParser.In_parametersContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_function" ):
                return visitor.visitCall_function(self)
            else:
                return visitor.visitChildren(self)




    def call_function(self):

        localctx = BKITParser.Call_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_call_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(BKITParser.IDENTIFIER)
            self.state = 416
            self.match(BKITParser.ORB)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 417
                self.in_parameters()


            self.state = 420
            self.match(BKITParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_function(self):
            return self.getTypedRuleContext(BKITParser.Call_functionContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = BKITParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.call_function()
            self.state = 423
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(BKITParser.RETURN)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ORB) | (1 << BKITParser.OCB) | (1 << BKITParser.SUBTRACT) | (1 << BKITParser.SUBTRACT_F) | (1 << BKITParser.NOT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0):
                self.state = 426
                self.expression()


            self.state = 429
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.exp1_sempred
        self._predicates[5] = self.exp2_sempred
        self._predicates[6] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




