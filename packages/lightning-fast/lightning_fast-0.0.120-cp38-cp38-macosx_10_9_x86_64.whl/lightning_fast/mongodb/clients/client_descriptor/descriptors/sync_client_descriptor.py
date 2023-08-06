from pymongo import MongoClient

from lightning_fast.mongodb.clients.client_descriptor.base.client_descriptor_base import (
    ClientDescriptorBase,
)


class SyncMongodbClient(ClientDescriptorBase):
    """
    通过继承 ClientDescriptorBase 类来实现一个同步的 MongoDB 客户端。
    此客户端使用了 pymongo 来提供同步操作。

    实现了 ClientDescriptorBase 类的 _create_client 方法，返回一个 pymongo.MongoClient 类型的实例。
    """
    def _create_client(self) -> MongoClient:
        return MongoClient(self.mongodb_url, connect=False)
