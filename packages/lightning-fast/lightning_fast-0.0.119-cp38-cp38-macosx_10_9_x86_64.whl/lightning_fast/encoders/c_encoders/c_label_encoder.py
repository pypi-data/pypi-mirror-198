import os
from ctypes import CDLL, POINTER, c_int, c_char_p, c_char, cast
from functools import lru_cache

import numpy as np

from lightning_fast.c_structs.custom_structure import UniqueWords
from lightning_fast.encoders.c_encoders.c_utils import DataConverter
from lightning_fast.config import ROOT_PATH


class CEncoderPath(object):
    """
    用于查找并缓存C编码器动态链接库的路径
    """
    def __init__(self):
        """
        初始化CEncoderPath实例，设置编码器所在目录。
        """
        self.source_dir = ROOT_PATH / "c_dynamic_library"

    @property
    @lru_cache()
    def all_libs(self):
        """
        获取C编码器动态链接库目录下所有动态链接库的文件名，缓存结果以加速下次访问
        """
        return os.listdir(self.source_dir)

    @property
    @lru_cache()
    def label_encoder_path(self):
        """
        获取标签编码器的动态链接库路径，查找的顺序为：

        - liblabel_encoder.dylib
        - liblabel_encoder.so
        - liblabel_encoder.dll

        如果未能找到，则抛出 FileNotFoundError 异常。
        """
        for file in self.all_libs:
            if file.startswith("liblabel_encoder"):
                return self.source_dir / file
        raise FileNotFoundError(f"Can not find lib file 'liblabel_encoder.*'")


class CLabelEncoder(object):
    """
    使用C语言实现的标签编码器。

    Attributes:
        _c_label_encoder: ctypes.POINTER 指向 C 语言编写的 UniqueWords 结构体的指针，用于保存编码器的内部状态。
        _c_encoder_module: ctypes.CDLL 表示加载的动态链接库文件。

    Notes:
        - 必须要自己手动调用 free_encoder 来释放产生的 encoder 内存。
    """

    def __init__(self):
        self._c_label_encoder = None
        self._c_encoder_module = None
        self.init_c_encoder_module()

    def init_c_encoder_module(self):
        """
        初始化 ctypes.CDLL 对象，并设置函数参数和返回值的数据类型。
        """
        self._c_encoder_module = CDLL(CEncoderPath().label_encoder_path)

        # 设置参数和返回值的数据类型
        self._c_encoder_module.get_encoder_by_string.argtypes = [c_char_p, c_char]
        self._c_encoder_module.get_encoder_by_string.restype = POINTER(UniqueWords)
        self._c_encoder_module.free_unique_words.argtypes = [
            POINTER(POINTER(UniqueWords))
        ]
        self._c_encoder_module.print_unique_words_summary.argtypes = [
            POINTER(POINTER(UniqueWords))
        ]
        self._c_encoder_module.save_encoder.argtypes = [
            POINTER(POINTER(UniqueWords)),
            c_char_p,
        ]
        self._c_encoder_module.load_encoder.argtypes = [c_char_p]
        self._c_encoder_module.load_encoder.restype = POINTER(UniqueWords)
        self._c_encoder_module.encode_words_by_string.argtypes = [
            POINTER(POINTER(UniqueWords)),
            c_char_p,
            c_int,
            c_char,
        ]
        self._c_encoder_module.encode_words_by_string.restype = POINTER(c_int)

    def fit(self, words):
        """
        Train the label encoder on the input words.

        Parameters
        ----------
        words : list of str
            List of input words.
        """
        c_words = DataConverter.string_list_to_c_string(words)
        self._c_label_encoder = self._c_encoder_module.get_encoder_by_string(
            c_words, c_char("\t".encode("utf-8"))
        )

    def transform(self, words):
        """
        Transforms a list of string words into a numpy array of integers using the C encoder module.

        Args:
            words (list): The list of string words to be encoded.

        Returns:
            np.array: The resulting numpy array of encoded integers.
        """
        c_words = DataConverter.string_list_to_c_string(words)
        result = self._c_encoder_module.encode_words_by_string(
            self._c_label_encoder, c_words, len(words), c_char("\t".encode("utf-8"))
        )
        buffer_as_ctypes_array = cast(result, POINTER(c_int * len(words)))[0]
        return np.frombuffer(buffer_as_ctypes_array, np.int32)

    def save_encoder(self, save_path):
        """
        Saves the C label encoder to a file.

        Args:
            save_path (str): The file path to save the encoder.
        """
        self._c_encoder_module.save_encoder(
            self._c_label_encoder, c_char_p(str(save_path).encode("utf-8"))
        )

    def load_encoder(self, load_path):
        """
        Loads the C label encoder from a file.

        Args:
            load_path (str): The file path to load the encoder.
        """
        self._c_label_encoder = self._c_encoder_module.load_encoder(
            c_char_p(str(load_path).encode("utf-8"))
        )

    def free_encoder(self):
        """
        Frees the unique words of the C label encoder.
        """
        self._c_encoder_module.free_unique_words(self._c_label_encoder)

    @property
    def c_module_empty(self):
        """
        Checks whether the C encoder module is empty.

        Returns:
            bool: True if the C encoder module is empty, False otherwise.
        """
        return not self._c_encoder_module

    @property
    def c_encoder_empty(self):
        """
        Checks whether the C label encoder is empty.

        Returns:
            bool: True if the C label encoder is empty, False otherwise.
        """
        return not self._c_label_encoder

    def print_encoder(self):
        """
        Prints the summary of unique words in the C label encoder.
        """
        self._c_encoder_module.print_unique_words_summary(self._c_label_encoder)
