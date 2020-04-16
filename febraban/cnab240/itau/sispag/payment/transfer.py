from .segmentA import SegmentA
from .segmentB import SegmentB
from gespag.contas.cnab240.libs.cleanData import clean_data_return_only_number


class Transfer:

    def __init__(self):
        self.segmentA = SegmentA()

    def toString(self):
        return self.segmentA.content

    def amountInCents(self):
        return self.segmentA.amountInCents()

    def setSender(self, user):
        self.segmentA.setSenderBank(user.bank)

    def setReceiver(self, user):
        self.segmentA.setReceiver(user)
        self.segmentA.setReceiverBank(user.bank)

    def setAmountInCents(self, value):
        self.segmentA.setAmountInCents(clean_data_return_only_number(value))

    def setPositionInLot(self, index):
        self.segmentA.setPositionInLot(index)

    def setScheduleDate(self, date):
        self.segmentA.setScheduleDate(date)

    def setInfo(self, reason="01"):
        self.segmentA.setInfo(reason)

    def setIdentifier(self, identifier):
        self.segmentA.setIdentifier(identifier)


class TransferSegmentB:

    def __init__(self):
        self.segmentB = SegmentB()

    def toString(self):
        return self.segmentB.content

    def setSender(self, user):
        self.segmentB.setSenderBank(user.bank)

    def setReceiver(self, user):
        self.segmentB.setReceiver(user)
        self.segmentB.setSenderAddress(user.address)

    def setPositionInLot(self, index):
        self.segmentB.setPositionInLot(index)


