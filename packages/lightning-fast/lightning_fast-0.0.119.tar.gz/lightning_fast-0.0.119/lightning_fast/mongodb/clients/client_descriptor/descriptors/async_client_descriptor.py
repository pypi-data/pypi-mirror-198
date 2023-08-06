import motor.motor_asyncio

from lightning_fast.mongodb.clients.client_descriptor.base.client_descriptor_base import (
    ClientDescriptorBase,
)


class AsyncMongodbClient(ClientDescriptorBase):
    """
    通过继承 ClientDescriptorBase 类来实现一个异步的 MongoDB 客户端。
    此客户端使用了 MotorAsync 来提供异步操作。

    实现了 ClientDescriptorBase 类的 _create_client 方法，返回一个 motor.motor_asyncio.AsyncIOMotorClient 类型的实例。
    """
    def _create_client(self) -> motor.motor_asyncio.AsyncIOMotorClient:
        return motor.motor_asyncio.AsyncIOMotorClient(self.mongodb_url)
