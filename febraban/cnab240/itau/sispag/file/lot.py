from .headerLot import HeaderLot
from .trailerLot import TrailerLot


class Lot:

    def __init__(self):
        self.headerLot = HeaderLot()
        self.registers = []
        self.trailerLot = TrailerLot()
        self.amount = 0
        self.index = 1

    def add(self, register, sum_amount=True):
        register.setPositionInLot(index=self.index)
        self.registers.append(register)
        if sum_amount:
            self.amount += register.amountInCents()
        self.index += 1

    def setHeaderLotType(self, kind="20", method="41"):
        self.headerLot.setInfo(kind, method)

    def setSender(self, user):
        self.headerLot.setSender(user)
        self.headerLot.setSenderBank(user.bank)
        self.headerLot.setSenderAddress(user.address)
        self.trailerLot.setSenderBank(user.bank)
