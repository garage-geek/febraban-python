from ....characterType import numeric, alphaNumeric
from ....row import Row
from ....libs.enums import RegistrationType


class SegmentB:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def amountInCents(self):
        return int(self.content[119:134])

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "1"),
            (7, 8, 1, numeric, "3"),
            (13, 14, 1, alphaNumeric, "B"),
            (14, 17, 3, alphaNumeric, ""),

        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),              # Código do banco debitado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index)                        # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReceiver(self, user):
        structs = [
            (17, 18, 1, numeric,
             RegistrationType.PESSOA_FISICA if len(user.identifier) == 11 else RegistrationType.PESSOA_JURIDICA), # 07.3B
            (18, 32, 14, numeric, user.identifier),       # 08.3B
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderAddress(self, address):
        structs = [
            (32, 62, 50, alphaNumeric, f"{address.streetLine1} {address.streetLine2}"),
            (82, 97, 15, alphaNumeric, address.district),       # 12.3B
            (97, 117, 20, alphaNumeric, address.city),          # 13.3B
            (117, 122,  8, numeric, address.zipCode),
            (125, 127,  2, alphaNumeric, address.stateCode),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)



