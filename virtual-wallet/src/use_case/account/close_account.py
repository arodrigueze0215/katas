from src.infrastructure.repository.account_repository import AccountRepository
from src.domain.customer.customer import Customer
from src.domain.account.account import Account
from src.domain.account.status import Status
class CloseAccount(object):

    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository

    def execute(self, account: Account):
        account.setClose()
        self.accountRepository.save(account)
            