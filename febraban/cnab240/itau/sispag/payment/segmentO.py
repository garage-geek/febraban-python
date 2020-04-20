# Pagamento de Contas de Concessionárias e Tributos com código de barras # Página 28
from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentO:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "1"),
            (7,  8, 1, numeric, "3"),               # Tipo de Registro
            (13, 14, 1, alphaNumeric, "O"),         # Código de Segmento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setScheduleDate(self, date):
        structs = [
            (99, 107, 8, numeric, date),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBarCode(self, barCode):
        structs = [
            (17,  61,  44, numeric, barCode)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDealerName(self, dealerName):                    # NOME DA CONCESSIONÁRIA / CONTRIBUINTE
        structs = [
            (61, 91, 30, alphaNumeric, dealerName),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDueDate(self, dueDate):
        structs = [
            (91, 99, 8, numeric, dueDate.strftime("%d%m%Y")),   # 10.30
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmountInCents(self, amount):
        structs = [
            (107, 122, 15, numeric, amount),     # 12.30
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (122, 142, 20, alphaNumeric, identifier),   # ID from system
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

