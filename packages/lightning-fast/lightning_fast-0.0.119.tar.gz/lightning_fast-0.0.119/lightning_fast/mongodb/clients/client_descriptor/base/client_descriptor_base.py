from abc import ABCMeta, abstractmethod
from typing import Union

import motor.motor_asyncio
from pymongo import MongoClient

from lightning_fast.config_factory.config_constructor import Config


class ClientDescriptorBase(metaclass=ABCMeta):
    """
    描述符需要宿主对象有一个 `config` 属性，该属性是 `Config` 的实例。
    在初始化时，当将值分配给 `mongodb_name` 属性时，会生成连接字符串。
    在访问描述符时，将创建一个连接。即：
    1. 初始化时传入config
    2. 赋值时生成连接字符串
    3. 引用时创建连接

    Parameters
    ----------
    mongodb_name : str
    要连接的 MongoDB 实例的名称。
    """

    def __init__(self, mongodb_name: str):
        self.mongodb_url = None
        self.mongodb_client = None
        self.mongodbs_config = None
        self.mongodb_name = mongodb_name

    def __set_name__(self, owner, name):
        """
        创建此描述符实例的时候, 直接拿宿主的`config.mongodbs`属性复制到描述符`mongodbs_config` 属性。
        """
        try:
            config = getattr(owner, "config")
        except AttributeError:
            raise AttributeError(f"{owner} must have 'config' attribute.")
        if not isinstance(config, Config):
            raise TypeError(f"config must be instance of Config")
        try:
            self.mongodbs_config = getattr(config, "mongodbs")
        except AttributeError:
            raise AttributeError(f"config must have 'mongodbs' attribute.")
        self._set_mongodb(self.mongodb_name)

    def __set__(self, instance, mongodb_name: str):
        """
        在将值分配给 `mongodb_name` 时，将配置中的字段名转换为 MongoDB 连接字符串。
        """
        self._set_mongodb(mongodb_name)

    def __get__(self, instance, owner):
        """
        在访问描述符时，将创建一个 MongoDB 客户端。
        """
        if self.mongodb_url is None:
            return self.mongodb_url
        if self.mongodb_client is None:
            self.mongodb_client = self._create_client()
        return self.mongodb_client

    @abstractmethod
    def _create_client(
        self,
    ) -> Union[MongoClient, motor.motor_asyncio.AsyncIOMotorClient]:
        pass

    def _set_mongodb(self, mongodb_name: str):
        """
        当将值分配给 `mongodb_name` 时，将配置中的字段名转换为 MongoDB 连接字符串。
        """
        if mongodb_name in self.mongodbs_config:
            conf = self.mongodbs_config[mongodb_name]
            if "uri" in conf:
                self.mongodb_url = conf["uri"]
            elif "user_name" in conf and "password" in conf:
                self.mongodb_url = (
                    f"mongodb://{conf['user_name']}:{conf['password']}@{conf['host']}/"
                )
            else:
                self.mongodb_url = None
        else:
            self.mongodb_url = None
