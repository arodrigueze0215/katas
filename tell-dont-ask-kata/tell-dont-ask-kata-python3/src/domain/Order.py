import decimal

from src.domain.OrderStatus import OrderStatus
from src.domain.exceptions.OrderCannotBeShippedError import OrderCannotBeShippedError
from src.domain.exceptions.OrderCannotBeShippedTwiceError import OrderCannotBeShippedTwiceError
from src.domain.exceptions.ShippedOrdersCannotBeChangedError import ShippedOrdersCannotBeChangedError
from src.domain.exceptions.RejectedOrderCannotBeApprovedError import RejectedOrderCannotBeApprovedError
from src.domain.exceptions.ApprovedOrderCannotBeRejectedError import ApprovedOrderCannotBeRejectedError


class Order(object):
    def get_total(self):
        return self.total

    def set_total(self, total: decimal.Decimal):
        self.total = total

    def get_currency(self):
        return self.currency

    def set_currency(self, currency: str):
        self.currency = currency

    def get_items(self):
        return self.items

    def set_items(self, items: list):
        self.items = items

    def get_tax(self):
        return self.tax

    def set_tax(self, tax: decimal.Decimal):
        self.tax = tax

    def get_status(self):
        return self.status

    def set_status(self, status: OrderStatus):
        self.status = status

    def get_id(self):
        return self.id

    def set_id(self, id: int):
        self.id = id

    def shipment(self):
        if self.get_status() is OrderStatus.CREATED or self.get_status() is OrderStatus.REJECTED:
            raise OrderCannotBeShippedError()

        if self.get_status() is OrderStatus.SHIPPED:
            raise OrderCannotBeShippedTwiceError()

        self.set_status(OrderStatus.SHIPPED)

    def approval(self, isApproved):
        if self.get_status() is OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedError()

        if self.get_status() is OrderStatus.REJECTED:
            raise RejectedOrderCannotBeApprovedError()

        if self.get_status() is OrderStatus.APPROVED:
            raise ApprovedOrderCannotBeRejectedError()

        self.set_status(isApproved)
