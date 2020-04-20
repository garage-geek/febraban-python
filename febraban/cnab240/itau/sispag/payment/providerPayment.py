from .segmentO import SegmentO
from ....libs.cleanData import clean_data_return_only_number


"""
Registro Detalhe - Segmento O - Pagamento de Contas e Tributos com Código de Barras (Obrigatório - Remessa / Retorno)
"""


class ProviderPayment:

    def __init__(self):
        self.segmentO = SegmentO()
        self.amount = 0

    def toString(self):
        return "\r\n".join((
            self.segmentO.content,
        ))

    def amountInCents(self):
        return self.segmentO.amountInCents()

    def setSender(self, user):
        """Sets the sender for the payment. The sender represents a user, its bank and its address."""
        self.segmentO.setSenderBank(user.bank)

    def setReceiverTaxId(self, receiverTaxId):
        """Sets the receiver for the payment. Only the receiver's taxId is necessary."""
        self.segmentO.setReceiverTaxId(receiverTaxId)

    def setIdentifier(self, identifier):
        """Sets the charge identifier that will be returned from the bank. Used for matching results."""
        self.segmentO.setIdentifier(identifier)

    def setScheduleDate(self, paymentDate):
        """Sets the payment date to be sent to the bank."""
        self.segmentO.setScheduleDate(paymentDate)

    def setDueDate(self, paymentDate):
        """Sets the payment date to be sent to the bank."""
        self.segmentO.setDueDate(paymentDate)

    def setBarCode(self, barCode):
        self.segmentO.setBarCode(barCode)

    def setDealerName(self, dealerName):
        self.segmentO.setDealerName(dealerName)

    def setAmountInCents(self, value):
        self.segmentO.setAmountInCents(clean_data_return_only_number(value))

    def setPositionInLot(self, index):
        self.segmentO.setPositionInLot(index)
