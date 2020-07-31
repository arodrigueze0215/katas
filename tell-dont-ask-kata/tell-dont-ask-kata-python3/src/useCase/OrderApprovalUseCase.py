from src.domain.OrderStatus import OrderStatus
from src.repository.OrderRepository import OrderRepository
from src.useCase.OrderApprovalRequest import OrderApprovalRequest


class OrderApprovalUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def run(self, request: OrderApprovalRequest):
        order = self.order_repository.get_by_id(request.get_order_id())
        order.approval(request.is_approved())
        self.order_repository.save(order)
