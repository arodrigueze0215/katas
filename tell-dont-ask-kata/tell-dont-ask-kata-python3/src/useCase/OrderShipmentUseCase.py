from src.domain.OrderStatus import OrderStatus
from src.repository.OrderRepository import OrderRepository
from src.service.ShipmentService import ShipmentService
from src.useCase.OrderShipmentRequest import OrderShipmentRequest


class OrderShipmentUseCase(object):
    def __init__(self, order_repository: OrderRepository, shipment_service: ShipmentService):
        self.order_repository = order_repository
        self.shipment_service = shipment_service

    def run(self, request: OrderShipmentRequest):
        order = self.order_repository.get_by_id(request.get_order_id())
        order.shipment()
        self.shipment_service.ship(order)
        self.order_repository.save(order)
