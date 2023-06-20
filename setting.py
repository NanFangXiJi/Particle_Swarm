"""
这是一些全局设置
"""
PARTICLE_COUNT = 1000  # 粒子数目

ARGUMENT_COUNT = 5  # 自变量的数目

RANGE = [(-32, 32) for i in range(5)]  # 每个自变量的取值范围

SPEED_BASE = 0.8  # 速度基准值

BAN_THE_OUTRANGE = True  # 是否禁止粒子出界。如果禁止，会在出界后对出界方向分速度反向

TIME_ATTRACT_CHANGE_WHEN_MIN_CHANGE = False  # 是否在找到新的最小值时使吸引力步长更改
TIME_ATTRACT_CHANGE_INDEX = 1.05

TIME_RANGE_CHANGE_WHEN_MIN_CHANGE = False  # 是否在找到新的最小值时使随机行动步长更改
TIME_RANGE_CHANGE_INDEX = 0.75

RANGE_CHANGE_INDEX = 0.8  # 随机加上、减去速度基准值的倍数

ATTRACT_CHANGE_INDEX = 0.05  # 被找到的点对粒子的吸引能力

MAX_ITERATION = 2000
