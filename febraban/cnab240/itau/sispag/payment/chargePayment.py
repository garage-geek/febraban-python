from .segmentJ import SegmentJ
from .segmentJ52 import SegmentJ52
from ....libs.cleanData import clean_data_return_only_number


class ChargePayment:

    def __init__(self):
        self.segmentJ = SegmentJ()
        self.segmentJ52 = SegmentJ52()
        self.amount = 0

    def toString(self):
        return "\r\n".join((
            self.segmentJ.content,
            self.segmentJ52.content,
        ))

    def setSender(self, user):
        """Sets the sender for the payment. The sender represents a user, its bank and its address."""
        self.segmentJ.setSenderBank(user.bank)
        self.segmentJ52.setSender(user)
        self.segmentJ52.setSenderBank(user.bank)

    def setReceiverTaxId(self, receiverTaxId):
        """Sets the receiver for the payment. Only the receiver's taxId is necessary."""
        self.segmentJ52.setReceiverTaxId(receiverTaxId)

    def setIdentifier(self, identifier):
        """Sets the charge identifier that will be returned from the bank. Used for matching results."""
        self.segmentJ.setIdentifier(identifier)

    def setScheduleDate(self, paymentDate):
        """Sets the payment date to be sent to the bank."""
        self.segmentJ.setScheduleDate(paymentDate)

    def setDueDate(self, paymentDate):
        """Sets the payment date to be sent to the bank."""
        self.segmentJ.setDueDate(paymentDate)

    def setBarCode(self, barCode):
        self.segmentJ.setBarCode(barCode)

    def setAmountInCents(self, value):
        self.segmentJ.setAmountInCents(clean_data_return_only_number(value))

    def setPositionInLot(self, index):
        index = 2 * index - 1
        self.segmentJ.setPositionInLot(index)
        self.segmentJ52.setPositionInLot(index + 1)
