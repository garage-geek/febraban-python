from .libs.cleanData import clean_data_return_only_number, clean_data_return_only_alphanumeric


class User:

    def __init__(self, name, identifier, bank=None, address=None, file_id=None):
        self.name = clean_data_return_only_alphanumeric(name)
        self.identifier = clean_data_return_only_number(identifier)
        self.bank = bank
        self.address = address
        self.file_id = file_id


class UserBank:

    def __init__(self, bankId, branchCode, accountNumber, accountVerifier, bankName="", code=""):
        self.bankId = bankId
        self.bankName = bankName
        self.accountNumber = accountNumber
        self.branchCode = branchCode
        self.accountVerifier = accountVerifier
        self.code = code        # código do convênio com o banco


class UserAddress:

    def __init__(self, streetLine1, city, stateCode, zipCode, district="", streetLine2=""):
        self.streetLine1 = streetLine1
        self.streetLine2 = streetLine2
        self.district = district
        self.city = city
        self.stateCode = stateCode
        self.zipCode = clean_data_return_only_number(zipCode)
