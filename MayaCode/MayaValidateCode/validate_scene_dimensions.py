# -*- coding: utf-8 -*-
# author:yangtao
# time: 2022/11/08

# 此脚本用来检查物体是否过于巨大，或者距离坐标中心太远

import maya.cmds as cmds


# 获取选中的 transform 节点
transforms = cmds.ls(sl=True, type="transform")
# 不能超过的最大值，100000
__far = 1e5


invalid = []
for tran in transforms:
    # 获取世界坐标下物体位置的最大最小值
    # boundingBox 的返回的值按以下顺序排列：xmin ymin zmin xmax ymax zmax
    bounding_box = cmds.xform(tran, q=1, worldSpace=True, boundingBox=True)
    # 最小值小于 -1e5 或者 最大值大于 1e5 为无效物体
    if any(x < -__far for x in bounding_box[:3]) \
            or any(x > __far for x in bounding_box[3:]):
        invalid.append(tran)

if invalid:
    raise ValueError("Nodes found far away or of big size ('{far}'): {0}".format(invalid, far=__far))