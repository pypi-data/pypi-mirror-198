from abc import ABCMeta, abstractmethod

import redis

from lightning_fast.config_factory.config_constructor import Config


class PoolDescriptorBase(metaclass=ABCMeta):
    """
    描述符基类，用于创建Redis连接池对象。
    此描述符其宿主必须有config属性，此属性是Config的实例，
    则此描述符的行为是：
    初始化时传入config
    赋值时生成连接字符串
    引用时创建连接

    Attributes:
        redis_url (str): Redis连接池的连接字符串。
        redis_client (redis.Redis): Redis连接池对象。
        redis_config (Config): Redis相关配置信息。
        redis_name (str): Redis配置信息中的名称。

    """

    def __init__(self, redis_name: str):
        """
        创建描述符实例时，初始化实例属性。

        Args:
            redis_name (str): Redis配置信息中的名称。

        """
        self.redis_url = None
        self.redis_client = None
        self.redis_config = None
        self.redis_name = redis_name

    def __set_name__(self, owner, name):
        """
        创建此描述符实例的时候, 直接拿宿主的config属性复制到描述符里边。

        Raises:
            AttributeError: 宿主对象缺少config属性。
            TypeError: config属性不是Config类的实例。
            AttributeError: config属性缺少redis信息。
        """
        try:
            config: Config = getattr(owner, "config")
        except AttributeError:
            raise AttributeError(f"{owner} must have 'config' attribute.")
        if not isinstance(config, Config):
            raise TypeError(f"config must be instance of Config")
        try:
            self.redis_config = getattr(config, "redis")
        except AttributeError:
            raise AttributeError(f"config must have 'redis' attribute.")
        self._set_redis(self.redis_name)

    def __set__(self, instance, redis_name: str):
        """
        根据Redis配置信息创建连接字符串。

        Args:
            redis_name (str): Redis配置信息中的名称。
        """
        self._set_redis(redis_name)

    def __get__(self, instance, owner):
        """
        获取Redis连接池对象。

        Returns:
            redis.Redis: Redis连接池对象。
        """
        if self.redis_client is None:
            self.redis_client = self._create_pool()
        return self.redis_client

    @abstractmethod
    def _create_pool(
        self,
    ) -> redis.ConnectionPool:
        """
        创建Redis连接池对象的抽象方法。

        Returns:
            redis.ConnectionPool: Redis连接池对象。
        """
        pass

    def _set_redis(self, redis_name: str):
        """
        根据Redis配置信息创建连接字符串。

        Args:
            redis_name (str): Redis配置信息中的名称。
        """
        if redis_name in self.redis_config:
            conf = self.redis_config[redis_name]
            redis_host = conf.get("host", "127.0.0.1")
            redis_port = conf.get("port", "6379")
            redis_db = conf.get("db", 0)
            self.redis_url = f"redis://{redis_host}:{redis_port}/{redis_db}"
        else:
            self.redis_url = None
