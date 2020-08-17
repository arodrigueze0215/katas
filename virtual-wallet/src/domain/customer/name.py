class Name(object):
    """Name Value Object."""

    def __init__(self,name, last_name, phone, cell_phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.cell_phone = cell_phone

    @staticmethod
    def create(name, last_name, phone, cell_phone):
        name = Name(name, last_name, phone, cell_phone)
        return name
