import unittest
from hamcrest import *
from src.domain.Order import Order
from src.domain.OrderStatus import OrderStatus
from src.domain.exceptions.OrderCannotBeShippedError import OrderCannotBeShippedError
from src.domain.exceptions.OrderCannotBeShippedTwiceError import OrderCannotBeShippedTwiceError
from src.domain.exceptions.ApprovedOrderCannotBeRejectedError import ApprovedOrderCannotBeRejectedError
from src.domain.exceptions.RejectedOrderCannotBeApprovedError import RejectedOrderCannotBeApprovedError
from src.domain.exceptions.ShippedOrdersCannotBeChangedError import ShippedOrdersCannotBeChangedError

class TestOrder(unittest.TestCase):
    def test_cannot_approve_rejected_order(self):
        initialOrder = Order()
        initialOrder.set_status(OrderStatus.REJECTED)
        initialOrder.set_id(1)
        with self.assertRaises(RejectedOrderCannotBeApprovedError):
            initialOrder.approval(True)

    def test_cannot_reject_approved_order(self):
        initial_order = Order()
        initial_order.set_status(OrderStatus.APPROVED)
        initial_order.set_id(1)
        with self.assertRaises(ApprovedOrderCannotBeRejectedError):
            initialOrder.approval(False)

    def test_shipped_orders_cannot_be_approved(self):
        initialOrder = Order()
        initialOrder.set_status(OrderStatus.SHIPPED)
        initialOrder.set_id(1)
        with self.assertRaises(ShippedOrdersCannotBeChangedError):
            initialOrder.approval(True)

    def test_cannot_reject_approved_order(self):
        initialOrder = Order()
        initialOrder.set_id(1)
        initialOrder.set_status(OrderStatus.CREATED)
        with self.assertRaises(OrderCannotBeShippedError):
            initialOrder.shipment()


    def test_rejected_orders_cannot_be_shipped(self):
        initialOrder = Order()
        initialOrder.set_id(1)
        initialOrder.set_status(OrderStatus.SHIPPED)
        with self.assertRaises(OrderCannotBeShippedTwiceError):
            initialOrder.shipment()



if __name__ == '__main__':
    unittest.main()
