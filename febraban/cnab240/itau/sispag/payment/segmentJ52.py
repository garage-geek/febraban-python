# coding: utf-8

from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentJ52:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 7,   8,  1,      numeric, "3"),     # TIPO DE REGISTRO
            ( 8,  13,  5,      numeric, "1"),     # INDEX DO REGISTRO
            (13,  14,  1, alphaNumeric, "J"),     # CÓDIGO DE SEGMENTO
            (14,  17,  3,      numeric, "0"),     # TIPO DE MOVIMENTO
            (17,  19,  2,      numeric, "52"),    # IDENTIFICAÇÃO DO REGISTRO OPCIONAL
            (75,  91,  16,     numeric, "0"),
            (131, 147, 16,     numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            ( 0,  3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (19, 20,  1,     numeric,  "1" if len(user.identifier) == 11 else "2"),
            (20, 35, 15,     numeric,  user.identifier),
            (35, 75, 40, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            ( 3,  7,  4, numeric, index),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
