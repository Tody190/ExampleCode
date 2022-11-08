# -*- coding: utf-8 -*-
# author:yangtao
# time: 2022/11/08

# 查看未知节点

import maya.cmds as cmds


transforms = cmds.ls()

unknown_nodes = set()
for tran in transforms:
    unknown_nodes.append(cmds.ls(tran, type='unknown'))

if unknown_nodes:
    raise ValueError("Unkown nodes found: {0}".format(unknown_nodes))