from src.domain.account.account import Account
class AccountRepository(object):
    
    def __init__(self):
        self.store = {}

    def findById(self, idAccount):
        return self.store.get(idAccount)

    def save(self, account: Account):
        self.store[account.id] = account

