import unittest
from src.domain.customer.name import Name
from src.domain.customer.customer import Customer
from src.infrastructure.repository.account_repository import AccountRepository
from src.use_case.account.register_new_account import RegisterNewAccount

class TestCheckingAccount(unittest.TestCase):

    def setUp(self):
        self.accountRepository = AccountRepository()
        self.registerNewAccount = RegisterNewAccount(self.accountRepository)



    def test_customer_could_register_new_checking_account_with_personal_details(self):
        idAccount = 1
        idCustomer = 1
        name = Name.create("Andres", "Rodriguez", "111", "57111")
        customer = Customer.create(idCustomer, name)
        self.registerNewAccount.execute(idAccount, customer)
        account = self.accountRepository.findById(idAccount)
        self.assertEqual(account.id, idAccount)


if __name__ == '__main__':
    unittest.main()
