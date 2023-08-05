import numpy as np
import pandas as pd

"""
1.输入:
    1)一组数据
    2)真值(可选)
    3)置信度(可选)    
    4)是否排除异常值(可选)
    5)Q法/Grubbs法(可选),置信度(可选)
2.处理过程:
    1)排序
    2)排除异常值
    3)检验系统误差;误差,偏差,平均偏差,标准偏差,重复性
3.输出:
    1)置信区间
    2)整理后的数据
    3)数据的统计结果
4.其他功能:
    保存历史数据
    多组(同一实验室或不同实验室)
    多组数据--再现性,两组平均值比较
"""
# 测试用例
a1 = [0.2862, 0.2859, 0.2851, 0.2848, 0.2852, 0.2863]

# Q表,G表,t表
Q_table = [[3, 0.94, 0.98, 0.99],
           [4, 0.76, 0.85, 0.93],
           [5, 0.64, 0.73, 0.82],
           [6, 0.56, 0.64, 0.74],
           [7, 0.51, 0.59, 0.68],
           [8, 0.47, 0.54, 0.63],
           [9, 0.44, 0.51, 0.60],
           [10, 0.41, 0.48, 0.57]]

G_table = [[3, 1.15, 1.15, 1.15],
           [4, 1.46, 1.48, 1.49],
           [5, 1.67, 1.71, 1.75],
           [6, 1.82, 1.89, 1.94],
           [7, 1.94, 2.02, 2.1],
           [8, 2.03, 2.13, 2.22],
           [9, 2.11, 2.21, 2.32],
           [10, 2.18, 2.29, 2.41],
           [11, 2.23, 2.36, 2.48],
           [12, 2.29, 2.41, 2.55],
           [13, 2.33, 2.46, 2.61],
           [14, 2.37, 2.51, 2.66],
           [15, 2.41, 2.55, 2.71]]

t_table = [[2, 6.314, 12.706, 63.657],
           [3, 2.92, 4.303, 9.925],
           [4, 2.353, 3.182, 5.841],
           [5, 2.132, 2.776, 4.604],
           [6, 2.015, 2.571, 4.032],
           [7, 1.943, 2.447, 3.707],
           [8, 1.895, 2.365, 3.499],
           [9, 1.86, 2.306, 3.355],
           [10, 1.833, 2.262, 3.25],
           [11, 1.812, 2.228, 3.169]]


# 处理单组数据
class AnaChem(object):
    # 初始化
    def __init__(self, data, true_value=None, confidence_level_interval=None, discard_suspicious=False,
                 discard_method="Grubbs", confidence_discard=None):
        """

        :param data:
        :param true_value:
        :param confidence_level_interval:
        :param discard_suspicious:
        :param discard_method:
        :param confidence_discard:
        """
        # 将数据转换为ndarray,排序
        if type(data) != np.ndarray:
            self.data = np.sort(np.array(data))
        else:
            self.data = np.sort(data)

        # 生成数据副本
        self.data_copy = self.data

        # 参数
        self.true_value = true_value
        self.confidence_level_interval = confidence_level_interval

        self.discard_suspicious = discard_suspicious
        self.discard_method = discard_method
        self.confidence_discard = confidence_discard

        # 统计结果
        self.num = None
        self.determinate_error = None
        self.mean = None
        self.stds = None
        self.confidence_interval = None
        self.relative_stds = None
        self.deviation = None
        self.relative_deviation = None
        self.average_deviation = None
        self.relative_average_deviation = None
        self.repeatability = None
        self.error = None
        self.relative_error = None
        self.t = None

    # 舍去离群数据
    def discard(self, discard_method="Grubbs", confidence_discard=None):
        self.num = self.data.size
        discard_data = np.array([])

        # Grubbs法
        if discard_method == "Grubbs":
            # 计算G计算
            self.mean = np.mean(self.data)
            self.stds = np.std(self.data, ddof=1)
            grubbs1 = np.divide(np.subtract(self.mean, np.min(self.data)), self.stds)
            grubbs2 = np.divide(np.subtract(np.max(self.data), self.mean), self.stds)

            # 获取G表
            if confidence_discard is None:
                self.confidence_discard = 0.95
                row = 1  # 0.95
            if confidence_discard == 0.95:
                row = 1
            elif confidence_discard == 0.975:
                row = 2
            elif confidence_discard == 0.99:
                row = 3
            else:
                row = 1

            g_t = G_table[self.num - 3][row]

            # G计算与G表比较
            if grubbs1 > g_t:
                np.append(discard_data, self.data[0])
                self.data = self.data[1:]
            if grubbs2 > g_t:
                np.append(discard_data, self.data[-1])
                self.data = self.data[:-1]

        # Q法
        elif discard_method == "Q":
            # 计算Q计算
            rang = np.max(self.data) - np.min(self.data)
            q1 = np.divide(np.subtract(self.data[1], self.data[0]), rang)
            q2 = np.divide(np.subtract(self.data[-1], self.data[-2]), rang)

            # 获取Q表
            if confidence_discard is None:
                self.confidence_discard = 0.90
                row = 1  # 0.90
            if confidence_discard == 0.90:
                row = 1  # 0.90
            elif confidence_discard == 0.95:
                row = 2  # 0.95
            elif confidence_discard == 0.99:
                row = 3  # 0.95
            else:
                row = 1

            q_t = Q_table[self.num - 3][row]

            # Q计算与Q表比较
            if q1 > q_t:
                np.append(discard_data, self.data[0])
                self.data = self.data[1:]
            if q2 > q_t:
                np.append(discard_data, self.data[-1])
                self.data = self.data[:-1]

        return discard_data

    # 计算置信区间
    def confidence_interval_i(self, confidence_level_interval=None):
        # 获取t表
        self.num = self.data.size

        if confidence_level_interval is None:
            self.confidence_level_interval = 0.95
            row = 2  # 0.95
        elif confidence_level_interval == 0.90:
            row = 1
        elif confidence_level_interval == 0.95:
            row = 2
        elif confidence_level_interval == 0.99:
            row = 3
        else:
            row = 2

        t_t = t_table[self.num - 2][row]

        # 计算置信区间
        self.mean = np.mean(self.data)
        self.stds = np.std(self.data, ddof=1)
        uncertainty = np.divide(np.multiply(t_t, self.stds), np.sqrt(self.num))
        self.confidence_interval = (self.mean, uncertainty)

    # 其他统计量及打印输出
    def describe(self):
        print("-" * 100)
        print("原始数据:", "\n", self.data_copy)

        # 如果选择舍去离群数据
        if self.discard_suspicious is True:
            discard_data = self.discard(discard_method=self.discard_method, confidence_discard=self.confidence_discard)
            print("用{}法,置信度取{}%,处理后的数据:".format(self.discard_method, self.confidence_discard * 100), "\n",
                  self.data)
            if discard_data.size > 0:
                print("舍去的数据:", "\n", discard_data)
            else:
                print("(没有数据被舍弃)")
        print("-" * 100)

        # 计算统计量
        self.confidence_interval_i(confidence_level_interval=self.confidence_level_interval)
        self.num = self.data.size
        self.mean = np.mean(self.data)
        self.stds = np.std(self.data, ddof=1)
        self.relative_stds = np.divide(self.stds, self.mean)
        self.deviation = np.subtract(self.data, self.mean)
        self.relative_deviation = np.divide(self.deviation, self.mean)
        self.average_deviation = np.mean(np.absolute(self.deviation))
        self.relative_average_deviation = np.divide(self.average_deviation, self.mean)
        self.repeatability = np.multiply(2 * np.sqrt(2), self.stds)

        # 输出统计量
        print("置信度{}%对应置信区间:{}±{}"
              .format(self.confidence_level_interval * 100, self.confidence_interval[0], self.confidence_interval[1]))
        print("平均值:\t{}\n平均偏差:\t{}\n相对平均偏差:\t{}\n样本标准偏差:\t{}\n相对标准偏差:\t{}\n复现性:\t{}"
              .format(self.mean, self.average_deviation, self.relative_average_deviation, self.stds, self.relative_stds,
                      self.repeatability, ))

        # 如果提供了真值
        if self.true_value is not None:
            self.error = np.subtract(self.data, self.true_value)
            self.relative_error = np.divide(self.error, self.true_value)

            self.t = np.divide(np.absolute(np.subtract(np.mean(self.data), self.true_value)), self.stds)
            print("t值:\t{}".format(self.t), end="\t")

            if self.confidence_level_interval is None:
                row = 2  # 0.95
            elif self.confidence_level_interval == 0.90:
                row = 1
            elif self.confidence_level_interval == 0.95:
                row = 2
            elif self.confidence_level_interval == 0.99:
                row = 3
            else:
                row = 2

            t_t = t_table[self.num - 2][row]

            if self.t > t_t:
                self.determinate_error = True
                print("存在系统误差")
            else:
                self.determinate_error = False
                print("不存在系统误差")

        # 输出统计量
        print("-" * 100)
        DF = pd.DataFrame(
            {"数据": self.data, "误差": self.error, "相对误差": self.relative_error, "偏差": self.deviation,
             "相对偏差": self.relative_deviation})
        print(DF)


if __name__ == "__main__":
    test1 = AnaChem(a1, discard_suspicious=True, true_value=12)
    test1.describe()


