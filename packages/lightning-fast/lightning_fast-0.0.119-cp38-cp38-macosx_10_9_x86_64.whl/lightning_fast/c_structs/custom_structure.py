from ctypes import (
    Structure,
    c_int,
    c_char_p,
)

from lightning_fast.c_structs.uthash import UT_hash_handle


class UniqueWords(Structure):
    # 代表一个单独的单词
    pass


# 定义 UniqueWords 结构体中的三个成员变量
UniqueWords._fields_ = [
    # 单词的字符串表示
    ("word", c_char_p),
    # 单词出现的次数
    ("value", c_int),
    # UT_hash表所需的哈希表管理字段
    ("hh", UT_hash_handle),
]
