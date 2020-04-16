from ....row import Row
from ....characterType import numeric, alphaNumeric
from gespag.contas.cnab240.libs.enums import RegistrationType


class SegmentJ52:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "1"),            # Lote do Registro - 02.4.J52
            (7, 8, 1, numeric, "3"),            # Tipo de Registro - 03.4.J52
            (13, 14, 1, alphaNumeric, "J"),     # Código de Segmento - 05.4.J52
            (14, 17, 3, numeric, "0"),          # Tipo de Movimento - 05.4.J52
            (17, 19, 2, numeric, "52"),         # 08.4.J52
            (131, 147, 16, numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),    # 01.4.J52
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (19, 20,  1, numeric,
             RegistrationType.PESSOA_FISICA if len(user.identifier) == 11 else RegistrationType.PESSOA_JURIDICA), # 09.4.J52
            (20, 35, 15, numeric, user.identifier),     # 10.4.J52
            (35, 75, 40, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReceiverTaxId(self, receiverTaxId):
        structs = [
            (75, 76, 1, numeric,
             RegistrationType.PESSOA_FISICA if len(receiverTaxId) == 11 else RegistrationType.PESSOA_JURIDICA), # 12.4.J52
            (76, 91, 15, numeric, receiverTaxId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
