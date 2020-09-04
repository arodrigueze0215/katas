from src.core.infrastructure.repository.account_repository import AccountRepository
from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
class RegisterNewAccount(object):
    
    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository


    def execute(self, idAccount, customer: Customer):
        account = Account(idAccount, customer.idCustomer)
        self.accountRepository.save(account)
