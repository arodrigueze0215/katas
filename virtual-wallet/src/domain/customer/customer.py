from src.domain.customer.name import Name
class Customer(object):
    
    def __init__(self, idCustomer, name: Name):
        self.idCustomer = idCustomer
        self.name = name

    @staticmethod
    def create(idCustomer, name: Name):
        customer = Customer(idCustomer, name)
        return customer