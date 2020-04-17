from datetime import datetime
from ....itau.sispag import Transfer, ChargePayment, UtilityPayment
from ....libs.fileUtils import FileUtils
from .header import Header
from .headerLot import HeaderLot
from .trailer import Trailer
from .trailerLot import TrailerLot
from .lot import Lot


class File:

    def __init__(self):
        self.header = Header()
        self.headerLot = HeaderLot()
        self.registers = []
        self.trailerLot = TrailerLot()
        self.trailer = Trailer()
        self.amount = 0
        self.index = 1
        self.lots = []

    def addLot(self, lot):
        self.lots.append(lot)

    def toString(self, currentDatetime=None):
        self.header.setGeneratedFileDate(currentDatetime or datetime.now())

        self.trailer.setNumberOfLotsAndRegisters(
            sum=4 + self._count(Transfer) + 2 * self._count(ChargePayment) + self._count(UtilityPayment)
        )
        self.trailerLot.setLotNumberOfRegisters(
            sum=2 + self._count(Transfer) + 2 * self._count(ChargePayment) + self._count(UtilityPayment)
        )

        lots_to_string = ""

        for lot in self.lots:
            registersToString = "\r\n".join([register.toString() for register in lot.registers])

            lot.trailerLot.setSumOfValues(sum=lot.amount)
            lot.trailerLot.setLotNumberOfRegisters(lot.index)

            lots_to_string += "%s\r\n%s\r\n%s\r\n" % (
                lot.headerLot.content,
                registersToString,
                lot.trailerLot.content
            )

        return "%s\r\n%s%s\r\n" % (
            self.header.content,
            lots_to_string,
            self.trailer.content
        )

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.header.setFileSequential(user.file_id)
        self.trailer.setSenderBank(user.bank)

    def output(self, fileName, path="/../", content=None, currentDatetime=None):
        file = FileUtils.create(name=fileName, path=path)
        file.write(self.toString(currentDatetime or datetime.now()) if not content else content)
        file.close()
        return file.name

    def _count(self, cls):
        return len([register for register in self.registers if isinstance(register, cls)])
