import socket


class IpTools:
    """
    一些辅助ip查询相关的工具
    """

    @classmethod
    def get_ip(cls) -> str:
        """
        实现了一个辅助IP查询的工具函数。get_ip是一个类方法，用于查询本机的对外IP地址。
        在实现中，我们通过创建一个UDP套接字来连接到一个虚拟IP地址“10.255.255.255”，从而获取本机的对外IP地址。
        如果无法获取，则返回默认值“127.0.0.1”。函数返回的是一个字符串类型的IP地址。
        :return: ip字符串
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable, A type private address.
            s.connect(("10.255.255.255", 1))
            ip = s.getsockname()[0]
        except OSError:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip
