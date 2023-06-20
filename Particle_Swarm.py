import setting
import Particle
from func import func


class Particle_Swarm:
    """
    粒子群
    """
    Particle_list: list[Particle.Particle]  # 粒子群的粒子列表
    answer_list: list  # 获取到的值
    pos_list: list  # 获取值对应的自变量
    min_answer = 2**64 - 1  # 获取到的最小值
    min_pos: list  # 获取到最小值对应位置
    iteration_time = 0  # 迭代次数

    def __init__(self):
        self.Particle_list = list()
        self.answer_list = list()
        self.pos_list = list()
        self.min_pos = list()

        # 创建对应数量的粒子
        for i in range(setting.PARTICLE_COUNT):
            self.Particle_list.append(Particle.Particle())
            self.answer_list.append(0)
            self.pos_list.append(list())

    # 处理发现点对个粒子的吸引
    def attract(self):
        for par in self.Particle_list:
            for i in range(setting.ARGUMENT_COUNT):
                dim = -self.min_pos[i]+par.pos[i]
                if dim != 0:
                    par.speed[i] += setting.ATTRACT_CHANGE_INDEX/(dim*abs(dim))

    def compute_once(self):
        for i in range(setting.PARTICLE_COUNT):
            self.pos_list[i] = self.Particle_list[i].pos.copy()
            self.answer_list[i] = func(self.Particle_list[i].pos)
            self.Particle_list[i].motion()
            self.Particle_list[i].range_change()

        # 出界管理
        if setting.BAN_THE_OUTRANGE:
            for par in self.Particle_list:
                par.outrange_process()

        # 最小值管理
        for i in range(setting.ARGUMENT_COUNT):
            if self.answer_list[i] <= self.min_answer:
                self.min_answer = self.answer_list[i]
                self.min_pos = self.pos_list[i]
                if setting.TIME_ATTRACT_CHANGE_WHEN_MIN_CHANGE:
                    setting.ATTRACT_CHANGE_INDEX *= setting.TIME_ATTRACT_CHANGE_INDEX
                if setting.TIME_RANGE_CHANGE_WHEN_MIN_CHANGE:
                    setting.RANGE_CHANGE_INDEX *= setting.TIME_RANGE_CHANGE_INDEX

        # 吸引
        self.attract()

        self.iteration_time += 1

        print("这是第{}次迭代，找到的最小值为{}，其自变量为{}".format(self.iteration_time, self.min_answer, self.min_pos))

