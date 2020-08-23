import uuid
from src.domain.account.amount import Amount
from src.domain.account.description import Description
from src.domain.account.transaction_date import TransactionDate
class Debit(object):
    def __init__(self, amountValue, descriptionText):
        self.id = uuid.uuid4()
        self.amount = Amount(amountValue)
        self.description = Description(descriptionText)
        self.transactionDate = TransactionDate.create()

    def getAmount(self):
        return self.amount.value