import numpy as np
from RNN.ulils import softmax
# 单个cell的前向传播过程
# 两个输入:x_t（输入序列）,s_prev（上一个S）, 其他参数parameters

def run_cell_forward(x_t, s_prev, parameters):
    """
    单个cell的前向传播的过程
    :param x_t:当前T时刻的序列输入
    :param s_prev: 上一个cell的隐层状态输入
    :param parameters: cell中的参数
    :return:隐藏层输出，s_next,out_pred,cache
    """
    # 取出参数
    u = parameters['u']
    w = parameters['w']
    v = parameters['v']
    ba = parameters['ba']
    by = parameters['by']

    #根据公式计算
    # 计算隐藏层输出 s_next
    s_next = np.tanh(np.dot(u, x_t) + np.dot(w, s_prev) + ba)

    # 计算cell的输出out_pred
    out_pred = softmax(np.dot(v, s_next) + by)

    # 记录每一层的值，用于反向传播计算使用
    cache = (s_next, s_prev, x_t, parameters)

    return  s_next, out_pred, cache
