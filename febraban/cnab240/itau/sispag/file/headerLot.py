from ....row import Row
from ....characterType import numeric, alphaNumeric
from ....libs.enums import RegistrationType


class HeaderLot:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "1"),            # 02.1
            (7, 8, 1, numeric, "1"),            # 03.1
            (8, 9, 1, alphaNumeric, "C"),       # 04.1
            (13, 16, 3, numeric, "040"),        # 07.1
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (17, 18, 1, numeric,
             RegistrationType.PESSOA_FISICA if len(user.identifier) == 11 else RegistrationType.PESSOA_JURIDICA), # 09.1
            (18, 32, 14, numeric, user.identifier),     # 10.1
            (72, 102, 30, alphaNumeric, user.name)      # 17.1
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0,   3,  3, numeric, bank.bankId),
            (52,  57,  5, numeric, bank.branchCode),
            (58,  70, 12, numeric, bank.accountNumber),
            (71,  72,  1, numeric, bank.accountVerifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderAddress(self, address):
        structs = [
            (142, 192, 50, alphaNumeric, f"{address.streetLine1} {address.streetLine2} {address.district}"),
            (192, 212, 20, alphaNumeric, address.city),
            (212, 220,  8, numeric, address.zipCode),
            (220, 222,  2, alphaNumeric, address.stateCode),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInfo(self, kind, method):
        structs = [
            (9, 11, 2, numeric, kind),
            (11, 13, 2, numeric, method)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
