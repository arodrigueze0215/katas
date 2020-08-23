from src.domain.customer.name import Name
from src.domain.customer.contact_number import ContactNumber
from src.domain.customer.person_number import PersonNumber
class Customer(object):
    
    def __init__(self, idCustomer, name: Name, personNumber: PersonNumber, contactNumber: ContactNumber):
        self.idCustomer = idCustomer
        self.name = name
        self.person_number = personNumber
        self.contact_number = contactNumber

    @staticmethod
    def create(idCustomer, name: Name, personNumber: PersonNumber, contactNumber: ContactNumber):
        customer = Customer(idCustomer, name, personNumber, contactNumber)
        return customer