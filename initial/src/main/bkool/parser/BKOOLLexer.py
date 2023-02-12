# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,14,76,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,
        4,3,45,8,3,11,3,12,3,46,1,4,4,4,50,8,4,11,4,12,4,51,1,5,1,5,1,6,
        1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,65,8,10,11,10,12,10,66,1,10,
        1,10,1,11,1,11,1,12,1,12,1,13,1,13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,1,0,3,2,0,65,90,97,
        122,1,0,48,57,3,0,9,10,13,13,32,32,78,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,
        1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,34,1,0,0,0,5,38,1,0,0,0,7,44,
        1,0,0,0,9,49,1,0,0,0,11,53,1,0,0,0,13,55,1,0,0,0,15,57,1,0,0,0,17,
        59,1,0,0,0,19,61,1,0,0,0,21,64,1,0,0,0,23,70,1,0,0,0,25,72,1,0,0,
        0,27,74,1,0,0,0,29,30,5,109,0,0,30,31,5,97,0,0,31,32,5,105,0,0,32,
        33,5,110,0,0,33,2,1,0,0,0,34,35,5,105,0,0,35,36,5,110,0,0,36,37,
        5,116,0,0,37,4,1,0,0,0,38,39,5,118,0,0,39,40,5,111,0,0,40,41,5,105,
        0,0,41,42,5,100,0,0,42,6,1,0,0,0,43,45,7,0,0,0,44,43,1,0,0,0,45,
        46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,8,1,0,0,0,48,50,7,1,0,
        0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,10,
        1,0,0,0,53,54,5,40,0,0,54,12,1,0,0,0,55,56,5,41,0,0,56,14,1,0,0,
        0,57,58,5,123,0,0,58,16,1,0,0,0,59,60,5,125,0,0,60,18,1,0,0,0,61,
        62,5,59,0,0,62,20,1,0,0,0,63,65,7,2,0,0,64,63,1,0,0,0,65,66,1,0,
        0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,6,10,0,0,69,
        22,1,0,0,0,70,71,9,0,0,0,71,24,1,0,0,0,72,73,9,0,0,0,73,26,1,0,0,
        0,74,75,9,0,0,0,75,28,1,0,0,0,4,0,46,51,66,1,6,0,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


