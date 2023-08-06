from redis import ConnectionPool

from lightning_fast.redis_connection.pool.base.pool_descriptor_base import (
    PoolDescriptorBase,
)


class SyncRedisPool(PoolDescriptorBase):
    """
    同步 Redis 连接池描述符。此描述符的宿主必须有 config 属性，此属性是 Config 的实例，
    当此描述符被创建时，将自动从宿主的 config 属性中读取 Redis 的配置。

    Parameters
    ----------
    redis_name : str
        Redis 配置名称，用于从 Config 中读取 Redis 的配置信息。

    Attributes
    ----------
    redis_url : str
        Redis 连接字符串，由 Redis 配置信息生成。
    redis_client : redis.Redis or None
        Redis 客户端连接实例，当引用此属性时会自动创建连接。
    redis_config : dict or None
        Redis 配置信息，从 Config 中读取。
    redis_name : str
        Redis 配置名称，用于从 Config 中读取 Redis 的配置信息。

    Methods
    -------
    __set_name__(self, owner, name)
        创建此描述符实例时，将宿主的 config 属性复制到描述符中。
    __set__(self, instance, redis_name: str)
        设置 Redis 配置名称时，根据名称生成连接字符串。
    __get__(self, instance, owner) -> redis.Redis or None
        获取 Redis 客户端连接实例时，如果连接不存在，将自动创建连接。
    _create_pool(self) -> ConnectionPool
        创建 Redis 连接池实例。

    Raises
    ------
    AttributeError
        如果宿主没有 config 属性。
    TypeError
        如果 config 属性不是 Config 的实例。
    AttributeError
        如果 config 属性中没有 Redis 配置信息。

    See Also
    --------
    lightning_fast.redis_connection.pool.base.pool_descriptor_base.PoolDescriptorBase : 基础连接池描述符类。

    """

    def _create_pool(self) -> ConnectionPool:
        """
        创建 Redis 连接池实例。

        Returns
        -------
        redis.ConnectionPool
            Redis 连接池实例。

        """
        return ConnectionPool.from_url(self.redis_url)
