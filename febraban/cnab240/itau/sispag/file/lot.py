from .headerLot import HeaderLot
from .trailerLot import TrailerLot
from ....libs.enums import *


class Lot:

    def __init__(self):
        self.headerLot = HeaderLot()
        self.registers = []
        self.trailerLot = TrailerLot()
        self.amount = 0
        self.index = 1
        self.segment = ""

    def add(self, register, sum_amount=True):
        register.setPositionInLot(index=self.index)
        self.registers.append(register)
        if sum_amount:
            self.amount += register.amountInCents()
        self.index += 1

    def setHeaderLotType(self,
                         kind=HeaderLoteServiceType.PAGAMENTO_FORNECEDOR,
                         method=HeaderLoteEntryWay.TED_OUTRA_TITULARIDADE,
                         segment=Segment.PAGAMENTO_CREDITO_CONTA_TED_DOC_CHEQUE
                         ):
        self.headerLot.setInfo(kind, method)
        self.segment = segment

    def setSender(self, user):
        self.headerLot.setSender(user)
        self.headerLot.setSenderBank(user.bank)
        self.headerLot.setSenderAddress(user.address)
        self.trailerLot.setSenderBank(user.bank)
