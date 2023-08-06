from abc import abstractmethod
import pathlib
import re
import sys
from typing import Optional

import luigi


class TaskBase(luigi.Task):
    """
    封装 `luigi.Task` 类，提供生成文件路径等功能。
    使用类相同路径在data目录下创建生成文件路径
    使用task名字与参数构建生成文件名字。
    如果想自定义文件后缀，则类中覆盖output_file_type
    此Base自行继承并复写base_dir与data_dir, 否则不可用

    Attributes:
        output_file_type (str): 输出文件的默认格式，如果需要自定义文件格式，需要在子类中覆盖该属性
    """

    output_file_type = "csv"

    @property
    @abstractmethod
    def base_dir(self) -> Optional[pathlib.Path]:
        """
        返回当前项目根目录绝对路径。

        Returns:
            Optional[pathlib.Path]: 当前项目根目录绝对路径，如果未定义，则返回 `None`
        """
        return None

    @property
    @abstractmethod
    def data_dir(self) -> Optional[pathlib.Path]:
        """
        返回欲保存的数据目录的绝对路径。

        Returns:
            Optional[pathlib.Path]: 欲保存的数据目录的绝对路径，如果未定义，则返回 `None`
        """
        return None

    @property
    def environment(self) -> str:
        """
        返回环境字符串，需要改变则复写此方法
        :return: 环境字符串，比如development
        """
        return "development"

    def output_directory(self) -> Optional[pathlib.Path]:
        """
        有趣的机制，如果这里使用类方法，那么cls.__class__会指向元类。
        这是目前发现的唯一的一个类方法导致与直觉相反的情况。

        根据任务的信息，生成任务输出目录。
        如果当前对象为 TaskBase 类，则返回 None。

        Returns:
            Optional[pathlib.Path]: 任务输出目录的绝对路径，如果未定义，则返回 None
        """
        if not self.base_dir or not self.data_dir:
            raise ValueError("Please imply base_dir and data_dir")
        file_type_suffix_re = re.compile(r"\.[^.\\/]*?$")
        if self.__class__ == TaskBase:
            return None
        data_dir = self.data_dir
        current_path = sys.modules[self.__class__.__module__].__file__
        current_file_path = pathlib.Path(current_path).absolute()
        current_data_dir = data_dir / current_file_path.relative_to(self.base_dir)
        current_data_dir = pathlib.Path(
            file_type_suffix_re.sub("", str(current_data_dir))
        )
        current_data_dir.mkdir(parents=True, exist_ok=True)
        return current_data_dir

    def output(self):
        """
        根据任务名称和参数创建输出文件的名称，并返回一个 LocalTarget 对象。返回任务输出的 LocalTarget 对象。

        Returns:
            luigi.LocalTarget: 任务输出的 LocalTarget 对象
        """
        output_file_name = self.__class__.__name__
        for parameter_name, parameter_value in self.to_str_params().items():
            output_file_name += "(" + parameter_name + "_" + parameter_value + ")"
        output_file_name += (
            f"(environment_{self.environment})" + f".{self.output_file_type}"
        )
        return luigi.LocalTarget(self.output_directory() / output_file_name)

    @property
    def description_dir(self) -> pathlib.Path:
        """
        返回当前输出文件对应的描述文件目录的路径。
        该目录与输出文件的名称相同，但不包括文件后缀。

        Returns:
            pathlib.Path: 描述文件目录的绝对路径
        """
        file_path = pathlib.Path(self.output().path)
        description_dir = file_path.parent / file_path.name.rstrip(
            f".{self.output_file_type}"
        )
        description_dir.mkdir(exist_ok=True, parents=True)
        return description_dir
