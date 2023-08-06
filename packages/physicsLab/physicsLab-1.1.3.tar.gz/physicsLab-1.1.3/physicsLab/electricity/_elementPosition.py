# Ԫ������ϵ
# һ�����ŵĳ�Ϊ0.15����Ϊ0.075
# һ�����ŵĳ�����ΪԪ������ϵ��x, y�ĵ�λ����
# z��ĵ�λ������ԭ����ϵ��0.1
#
# ���λ�˷�������Ԫ����λ�ñ��뾭����������ʹԪ����������
# x, z�᲻������
# y�������Ϊ +0.045

# _elementClassHead���element_Init_HEAD�в��ִ���Ԫ������ϵ�Ĵ���
# crt_ExperimentҲ�в��ִ���

from typing import Union

### define ###
elementXYZ = False
### end define ###

# ��Ԫ������ϵת��Ϊ��ʵ֧�ֵ�����ϵ
def translate(x: Union[int, float], y: Union[int, float], z: Union[int, float], isBigElement = False):
    x *= 0.15
    y *= 0.075
    z *= 0.1
    if isBigElement:
        y += 0.045
    return x, y, z

# ����ʵ֧�ֵ�����ϵת��ΪԪ������ϵ
def change(x: Union[int, float], y: Union[int, float], z: Union[int, float], isBigElement = False):
    x /= 0.15
    y /= 0.075
    z /= 0.1
    if isBigElement:
        y -= 0.045
    return x, y, z

def set_elementXYZ(boolen: bool):
    global elementXYZ
    elementXYZ = bool(boolen)