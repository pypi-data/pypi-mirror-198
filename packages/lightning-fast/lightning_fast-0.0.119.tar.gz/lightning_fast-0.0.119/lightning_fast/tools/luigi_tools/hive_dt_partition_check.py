import luigi
from luigi.contrib.hive import HivePartitionTarget


class HiveDtPartitionCheck(luigi.Task):
    """
    检查某个hive的某个partition(dt)是否存在

    Attributes:
        hive_path (str): Hive 表的路径。
        partition (str): 待检查的分区。
    """

    hive_path = luigi.Parameter()
    partition = luigi.Parameter()

    def run(self):
        """运行任务，检查指定的分区是否存在。

        Raises:
            ValueError: 如果分区不存在。

        """
        existed = HivePartitionTarget(
            str(self.hive_path), partition={"dt": self.partition}
        ).exists()
        if existed:
            with self.output().open("w") as f:
                f.write(f"Got f{self.partition} of {self.hive_path}。")
        else:
            raise ValueError(f"Got no f{self.partition} of {self.hive_path}。")
