from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentJ:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "1"),            # Lote do Registro
            (7, 8, 1, numeric, "3"),            # Tipo de Registro
            (13, 14, 1, alphaNumeric, "J"),     # Código de Segmento
            (14, 17, 3, numeric, "0"),          # Tipo de Movimento
            (114, 144, 30, numeric, "0"),
            (167, 182, 15, numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBarCode(self, barCode):
        if len(barCode) < 47:
            difference_caracters = 47 - len(barCode)
            barCode = barCode + ('0' * difference_caracters)

        barCode = barCode[0:4] + barCode[32:49] + barCode[4:9] + barCode[10:21] + barCode[21:31]

        structs = [
            (17,  61,  44, numeric, barCode)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDueDate(self, dueDate):
        structs = [
            (91, 99, 8, numeric, dueDate.strftime("%d%m%Y")),  # Data de Vencimento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def amountInCents(self):
        return int(self.content[152:167])

    def setAmountInCents(self, amount):
        structs = [
            (99, 114, 15, numeric, amount),     # Valor Nominal do Título   - 11.3J
            (152, 167, 15, numeric, amount),    # Valor do Pagamento        - 15.3J
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setScheduleDate(self, date):
        structs = [
            (144, 152,  8, numeric, date)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (182, 202, 20, alphaNumeric, identifier),       # 17.3J
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
