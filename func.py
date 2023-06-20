import math


def func_1(argument: list):
    """
    x**2+y**2
    """
    return argument[0] ** 2 + argument[1] ** 2


def func_2(argument: list):
    """
    -sigma<x_1,x_2,……,x_n>(x_i*sin(sqrt(x_i)))
    """
    out = 0
    for x in argument:
        out += x * math.sin(math.sqrt(abs(x)))
    return out


def func_3(argument: list):
    """
    max{|x_i|}
    """
    lst = [abs(x) for x in argument]
    return max(lst)


def func_4(argument: list):
    """
    -20*exp(-0.2*sqrt(1/n*sigma<x_1,x_2,……,x_n>(x_i**2)))-exp(1/n*sigma<x_1,x_2,……,x_n>cos(2*pi*x_i))+20+e
    """
    l = len(argument)
    sigma_1 = 0
    sigma_2 = 0
    for x in argument:
        sigma_1 += x**2
        sigma_2 += math.cos(2*math.pi*x)
    return -20*math.exp(-0.2*math.sqrt(1/l*sigma_1))-math.exp(1/l*sigma_2)+20+math.e


func = func_4
