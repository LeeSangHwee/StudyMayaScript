from maya import cmds

for i in range(4):
    obj = cmds.polyCylinder(name = "pCy1")# 오브젝트 명 지정 해주면서 생성
    cmds.setAttr(obj[0]+".s", 3, 0.2, 3)
    cmds.setAttr(obj[0]+".rx", 90)

# 해당 오브젝트 x, y, z 값 변경
cmds.setAttr("pCy2.t", -10, 0, 0)
cmds.setAttr("pCy3.t", -10, 0, 5)
cmds.setAttr("pCy4.t", 0, 0, 5)

cmds.polyCube(name = "Cube")
cmds.setAttr("Cube.s", 10, 0.5, 5)
cmds.setAttr("Cube.t", -5, 0, 2.5)

cmds.polyCone(name = "Cone")
cmds.setAttr("Cone.scale", 1, 3, 1)
cmds.setAttr("Cone.t", -1, 3, 2.5)
cmds.setAttr("Cone.rz", -30)
