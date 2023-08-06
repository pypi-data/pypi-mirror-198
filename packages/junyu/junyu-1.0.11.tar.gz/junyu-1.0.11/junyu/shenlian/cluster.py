import numpy as np


class Cluster:
    def __init__(self, pts):
        self.pts = pts
        self.occus = [0 for _ in self.pts]
        self.amount_threshold = 50
        self.connect_distance = 1500  # 相邻范围
        self.look_distance = 10000  # 查找范围
        self.kernel_bandwidth = 1000  # 高斯权重参数，sigma

    @staticmethod
    def euclid_distance(x, xi):
        """
        计算两点之间的欧式距离
        :param x:
        :param xi:
        :return:
        """
        return np.sqrt(np.sum((np.array(x, dtype=np.int64) - np.array(xi, dtype=np.int64)) ** 2))

    def neighbourhood_points(self, X, x_centroid, distance=5000):
        """
        查找个x_centroid距离小于distance的所有点的坐标
        :param X: 所有点集合
        :param x_centroid: 当前中心点坐标
        :param distance: 截止距离
        :return:
        """
        eligible_x = []
        for x in X:
            distance_between = self.euclid_distance(x, x_centroid)
            if distance_between < distance:
                eligible_x.append(x)
        return eligible_x

    @staticmethod
    def gaussian_kernal(distance, bandwidth):
        """
        计算高斯权重
        :param distance:
        :param bandwidth:
        :return:
        """
        return (1 / (bandwidth * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (distance / bandwidth) ** 2)

    def add(self, index):
        centroid = self.pts[index]
        for i in range(len(self.pts)):
            if self.occus[i] == 0 and self.euclid_distance(centroid, self.pts[i]) < self.connect_distance:
                self.occus[i] = self.occus[index]
                self.add(i)

    def cluster(self):
        """
        标记所有团簇在self.occus
        :return:
        """
        self.occus = [0 for _ in self.pts]
        v = 1
        while self.occus.count(0) > 0:
            index = self.occus.index(0)
            self.occus[index] = v
            # print(self.occus)
            self.add(index)
            v += 1

    def find_cut(self):
        """
        查找是否存在切片，判定条件：1.存在团簇数目>50，2.团簇边界宽度小于20000
        :return:
        """
        self.cluster()
        result = [0 for _ in self.pts]
        if len(self.pts) < self.amount_threshold:
            return result
        s = max(self.occus)
        for v in range(1, s+1):
            t = [(i, *pt) for i, (pt, occu) in enumerate(zip(self.pts, self.occus)) if occu == v]
            index, x, y = zip(*t)
            if len(t) > 50 and max(x) - min(x) < 20000 and max(y) - min(y) < 20000:
                for i in index:
                    result[i] = 1
        return result
