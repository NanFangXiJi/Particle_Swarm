import random

import setting


class Particle:
    """
    粒子类
    """
    pos: list  # 位置
    speed: list  # 速度

    def __init__(self):
        self.pos = list()
        self.speed = list()
        for i in range(setting.ARGUMENT_COUNT):
            self.pos.append(random.uniform(setting.RANGE[i][0], setting.RANGE[i][1]))  # 初始化位置
            self.speed.append(random.uniform(-setting.SPEED_BASE, setting.SPEED_BASE))  # 初始化速度

    def motion(self):
        """
        粒子一帧的移动行为
        """
        for i in range(setting.ARGUMENT_COUNT):
            self.pos[i] += self.speed[i]

    def outrange_process(self):
        """
        出界处理
        """
        for i in range(setting.ARGUMENT_COUNT):
            if setting.RANGE[i][0] > self.pos[i]:
                self.speed[i] *= -1
                self.pos[i] = setting.RANGE[i][0]
            elif setting.RANGE[i][1] < self.pos[i]:
                self.speed[i] *= -1
                self.pos[i] = setting.RANGE[i][1]

    def range_change(self):
        """
        粒子随机改变一点方向
        """
        for i in range(setting.ARGUMENT_COUNT):
            self.speed[i] += random.choices([-1, 0, 1])[0] * setting.SPEED_BASE

