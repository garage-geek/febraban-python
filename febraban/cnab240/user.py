from gespag.contas.cnab240.libs.cleanData import clean_data_return_only_number


class User:

    def __init__(self, name, identifier, bank=None, address=None, file_id=None):
        self.name = name
        self.identifier = clean_data_return_only_number(identifier)
        self.bank = bank
        self.address = address
        self.file_id = file_id


class UserBank:

    def __init__(self, bankId, branchCode, accountNumber, accountVerifier, bankName=""):
        self.bankId = bankId
        self.bankName = bankName
        self.accountNumber = accountNumber
        self.branchCode = branchCode
        self.accountVerifier = accountVerifier


class UserAddress:

    def __init__(self, streetLine1, city, stateCode, zipCode, district="", streetLine2=""):
        self.streetLine1 = streetLine1
        self.streetLine2 = streetLine2
        self.district = district
        self.city = city
        self.stateCode = stateCode
        self.zipCode = clean_data_return_only_number(zipCode)
