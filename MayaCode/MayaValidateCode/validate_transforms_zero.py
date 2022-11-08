# -*- coding: utf-8 -*-
# author:yangtao
# time: 2022/11/03


import maya.cmds as cmds

# 当物体无缩放，位移，旋转信息时，他的矩阵应为下面的样式
__identity = [1.0, 0.0, 0.0, 0.0,
              0.0, 1.0, 0.0, 0.0,
              0.0, 0.0, 1.0, 0.0,
              0.0, 0.0, 0.0, 1.0]

# 这是浮点数在内存中的表示方式
# 此值是python的微小值 1e-3 为 0.001（三个0），1e-30 就是30个0
__tolerance = 1e-30


# 获取选中的 transform 节点
transforms = cmds.ls(sl=True, type="transform")

invalid = []  # 此项保存旋转移动缩放“清零”的物体
for tan in transforms:
    # 查看对象变换的矩阵值
    mat = cmds.xform(tan, q=1, matrix=True, objectSpace=True)
    # zip 将当前变换节点的值和需要对比的“零点值”一一对应组成元组
    # abs（x-y） 将两个值相减并取绝对值
    # 当他们的差值小于__tolerance（1e-30），则判断此项已经归零
    # all() 判断此迭代器里的参数是否都是True
    if not all(abs(x - y) < __tolerance
               for x, y in zip(__identity, mat)):
        # 将值未清零的实体保存到列表
        invalid.append(tan)

if invalid:
        raise ValueError("Nodes found with transform "
                         "values: {0}".format(invalid))