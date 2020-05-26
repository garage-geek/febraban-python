from ....libs import occurrences
from ....libs import enums


class PaymentResponseStatus:
    success = "success"
    failed = "failed"
    scheduled = "scheduled"
    unknown = "unknown"


class payment_type:
    transfer = "transfer"
    chargePayment = "charge-payment"
    taxPayment = "tax-payment"
    barCodePayment = "bar-code-payment"


class PaymentFileHeader:

    def __init__(self):
        self.bankId = ""
        self.identifier = ""
        self.lot = ""               # 19.0
        self.code = ""              # codigo convenio com banco  - 07.0
        self.branch_number = ""
        self.account_number = ""
        self.account_verifier = ""

    def parseHeader(self, line):

        self.bankId = int(line[0:3].strip())
        self.lot = int(line[158:164].strip())
        self.identifier = int(line[18:32].strip())
        self.code = line[32:52].strip()
        self.branch_number = int(line[52:57].strip())
        self.account_number = int(line[58:70].strip())
        self.account_verifier = line[70:71].strip()


class PaymentResponse:

    def __init__(self, bankId, identifier=None, occurrences=None, content=None, authentication=None,
                 amount_in_cents=None, payment_type=None):
        self.bankId = bankId
        self.identifier = identifier
        self.occurrences = occurrences
        self.content = content or []
        self.authentication = authentication
        self.amount_in_cents = amount_in_cents
        self.type = payment_type
        self.ocurrences_list = self.get_ocurrences_list()

    def occurrencesText(self):
        return [self.ocurrences_list[occurrenceId] for occurrenceId in self.occurrences]

    def occurrencesTextAtIndex(self, index):
        occurrenceId = self.occurrences[index]
        return self.ocurrences_list[occurrenceId]

    def status(self):
        if "00" in self.occurrences:
            return PaymentResponseStatus.success
        if "BD" in self.occurrences:
            return PaymentResponseStatus.scheduled
        if [code in self.occurrences for code in ["RJ", "DV"]].count(True) > 0:
            return PaymentResponseStatus.failed
        return PaymentResponseStatus.unknown

    def contentText(self, breakLine="\n"):
        return breakLine.join(self.content)

    def get_ocurrences_list(self):
        if self.bankId == enums.Banks.ITAU:
            return occurrences.itau_occurrences

        return occurrences.febraban_occurrences


class PaymentParser:

    def __init__(self):
        self.bankId = ''

    @classmethod
    def parseFile(cls, file, bankId):
        lines = file.readlines()
        cls.bankId = bankId
        return cls.parseLines(lines)

    @classmethod
    def parseText(cls, text):
        lines = text.splitlines()[:-1]
        return cls.parseLines(lines)

    @classmethod
    def parseLines(cls, lines):
        result = []
        currentResponse = None
        
        for line in lines:
            if line[7] in ["0", "1", "9"]:
                continue

            if line[7] == "3" and line[13] in ["A", "J", "O"]:
                if currentResponse is not None:
                    result.append(currentResponse)
                currentResponse = PaymentResponse()

            if line[7] == "3" and line[13] == "A":
                currentResponse.content.append(line)
                currentResponse.identifier = cls._getIdentifierSegmentA(line)
                currentResponse.occurrences = cls._getOccurrences(line)
                currentResponse.amount_in_cents = cls._getAmountSegmentA(line)
                currentResponse.type = payment_type.transfer

            elif line[7] == "3" and line[13] == "J":
                currentResponse.content.append(line)
                currentResponse.identifier = cls._getIdentifierSegmentJ(line)
                currentResponse.occurrences = cls._getOccurrences(line)
                currentResponse.amount_in_cents = cls._getAmountSegmentJ(line)
                currentResponse.type = payment_type.chargePayment

            elif line[7] == "3" and line[13] == "O":
                currentResponse.content.append(line)
                currentResponse.identifier = cls._getIdentifierSegmentO(line)
                currentResponse.occurrences = cls._getOccurrences(line)
                currentResponse.amount_in_cents = cls._getAmountSegmentO(line)
                currentResponse.type = payment_type.barCodePayment

            elif line[7] == "3" and line[13] == "Z":
                currentResponse.content.append(line)
                currentResponse.authentication = cls._getAuthentication(line)

            if line[7] == "5":
                result.append(currentResponse)
                currentResponse = None

        return result

    @classmethod
    def _getOccurrences(cls, line):
        occurrencesString = line[230:240].strip()
        return cls._splitString(occurrencesString)

    @classmethod
    def _splitString(cls, string):
        return [string[i:i+2] for i in range(0, len(string), 2)]

    @classmethod
    def _getAmountSegmentA(cls, line):
        return int(line[119:134].strip())

    @classmethod
    def _getAmountSegmentJ(cls, line):
        return int(line[152:167].strip())

    @classmethod
    def _getAmountSegmentO(cls, line):
        return int(line[144:159].strip())

    @classmethod
    def _getIdentifierSegmentA(self, line):
        return line[73:93].strip()

    @classmethod
    def _getIdentifierSegmentJ(self, line):
        return line[182:202].strip()

    @classmethod
    def _getIdentifierSegmentO(self, line):
        return line[174:194].strip()

    @classmethod
    def _getAuthentication(cls, line):
        return line[14:78].strip()
