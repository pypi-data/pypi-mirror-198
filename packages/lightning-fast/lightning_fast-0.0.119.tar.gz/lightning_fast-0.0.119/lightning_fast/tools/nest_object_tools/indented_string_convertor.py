from __future__ import annotations
from typing import List, Optional, Tuple


class IndentNode:
    def __init__(self, value: str, children: Optional[List[IndentNode]] = None):
        """
        初始化一个IndentNode对象。

        Parameters
        ----------
        value : str
            当前节点的值。
        children : Optional[List[IndentNode]], optional
            当前节点的子节点列表，默认为None。
        """
        self.value = value
        self.children: List[IndentNode] = [] if children is None else children

    def __eq__(self, other: IndentNode):
        """
        判断当前节点是否与另一个节点相等。当前值与递归下边所有值都相同才是相。

        Parameters
        ----------
        other : IndentNode
            另一个节点。

        Returns
        -------
        bool
            如果当前节点与另一个节点相等则返回True，否则返回False。
        """
        if self.value != other.value:
            return False
        if len(self.children) != len(other.children):
            return False
        for i in range(len(self.children)):
            if self.children[i] != other.children[i]:
                return False
        return True

    def to_list(self) -> List[List[str]]:
        """
        将嵌套节点转换为二层列表。

        例如，将如下嵌套节点：

            1
                1.1
                1.2
                    1.3
            2
                2.1

        转换为如下二层列表：

            [['root', '1', '1.1'], ['root', '1', '1.2', '1.3'], ['root', '2', '2.1']]

        Returns
        -------
        List[List[str]]
            转换后的二层列表。
        """
        # 保存结果
        result: List[List[str]] = []
        # 用来中间组合字符串时用来分割字符串
        tmp_sep = "&&"
        # 遍历树结构时的栈
        stack: List[Tuple[IndentNode, str]] = [(self, self.value)]
        # 遍历栈
        while stack:
            # 拿出当前节点
            current_node_info = stack.pop()
            # 如果当前节点有子节点，则继续拼字符串
            if current_node_info[0].children:
                for child in current_node_info[0].children[::-1]:
                    stack.append((child, current_node_info[1] + tmp_sep + child.value))
            # 如果当前节点没有子节点，则将已经拼好的字符串加到结果中
            else:
                result.append(current_node_info[1].split(tmp_sep))
        return result


class IndentedStringConvertor:
    """
    这是一个将使用某种字符缩进（比如\t）作为等级区分的字符串转换为嵌套数据结构的类。

    比如字符串如::

        1
            1.1
            1.2
                1.3
        2
            2.1

    将转换为::

        [
            IndentNode(
                "1",
                children=[
                    IndentNode("1.1"),
                    IndentNode("1.2", children=[IndentNode("1.3")]),
                ],
            ),
            IndentNode("2", children=[IndentNode("2.1")]),
        ]

    Attributes:
        indent_char (str): 用来区分等级的缩进符号，只能是单个字符
        line_sep (str): 用来分割行的符号

    Raises:
        ValueError: 当缩进符号不是单个字符时，抛出异常
    """

    def __init__(self, indent_char="\t", line_sep="\n"):
        """
        初始化IndentedStringConvertor类

        Args:
            indent_char (str): 用来区分等级的缩进符号，只能是单个字符
            line_sep (str): 用来分割行的符号

        Raises:
            ValueError: 当缩进符号不是单个字符时，抛出异常
        """
        if len(indent_char) != 1:
            raise ValueError("indent_char must be char")
        self.indent_char = indent_char
        self.line_sep = line_sep

    def count_indent_str(self, line: str) -> int:
        """
        计算缩进的数量

        Args:
            line (str): 当前行

        Returns:
            int: 缩进的数量

        Raises:
            ValueError: 当整行字符全部等于缩进符号时，抛出异常
        """
        for i in range(len(line)):
            if line[i] != self.indent_char:
                return i
        raise ValueError("All character are equal to indent_char!")

    def convert(self, content: str) -> List[IndentNode]:
        """
        将字符串转换为嵌套数据结构，使用类似单调栈的方式（事实上没有使用弹出序列做事）构造。

        Args:
            content (str): 需要转换的文本

        Returns:
            List[IndentNode]: 转换后的嵌套数据结构
        """
        # 创建一个跟节点
        root_node = IndentNode("root")
        # 用来遍历的栈
        stack: List[Tuple[IndentNode, int]] = [(root_node, -1)]
        # 遍历每一行
        for line in content.split(self.line_sep):
            # 当前行如果是空行，则直接跳过
            if not line.strip():
                continue
            # 计算当前行的缩进数量
            level = self.count_indent_str(line)
            # 将所有等级大于等于当前行的节点全都弹出，因为输入的格式限制，所有缩进大于当前行的事实上应该都处理完了
            while stack[-1][1] >= level:
                stack.pop()
            # 生成当前节点
            current_node = IndentNode(line.lstrip(self.indent_char))
            # 将当前节点加到他的最近上层节点的children中
            stack[-1][0].children.append(current_node)
            # 将当前节点加入到栈中
            stack.append((current_node, level))
        return root_node.children
