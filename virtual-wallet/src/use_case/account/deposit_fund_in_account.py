from src.infrastructure.repository.account_repository import AccountRepository
from src.domain.customer.customer import Customer
from src.domain.account.account import Account
class DepositFundInAccount(object):

    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository

    def execute(self, account: Account, amount, description):
        account.makeCredit(amount, description)
        self.accountRepository.save(account)