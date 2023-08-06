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
# ��ʵ����ϵx, y, z��λ1
_xUnit = 0.16
_yUnit = 0.08
_zUnit = 0.1
# big_element��������
_xAmend = 0.04
### end define ###

# ��Ԫ������ϵת��Ϊ��ʵ֧�ֵ�����ϵ
def xyzTranslate(x: Union[int, float], y: Union[int, float], z: Union[int, float], isBigElement = False):
    x *= _xUnit
    y *= _yUnit
    z *= _zUnit
    if isBigElement:
        y += _xAmend
    return x, y, z

# ����ʵ֧�ֵ�����ϵת��ΪԪ������ϵ
def translateXYZ(x: Union[int, float], y: Union[int, float], z: Union[int, float], isBigElement = False):
    x /= _xUnit
    y /= _yUnit
    z /= _zUnit
    if isBigElement:
        y -= _xAmend
    return x, y, z

def set_elementXYZ(boolen: bool):
    global elementXYZ
    elementXYZ = bool(boolen)