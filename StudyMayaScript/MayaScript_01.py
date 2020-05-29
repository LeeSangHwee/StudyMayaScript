from maya import cmds
import random
#from maya import cmds    : Maya 로부터 cmds import
#import maya.cmds as cmds : 위와 같은 의미
 
'''
- 오브젝트 생성
  cmds.polyCube, cmds.polyCylinder, cmds.polySphere, cmd.polyCone

- setAttr : Maya 에서 Attribute 부분을 받는 함수
  매개 변수는 오브젝트명 그리고 xyz 값
  이미 생성된 오브젝트의 값을 변경 할 수도 있지만
  생성 되있지 않다면 초기화하면서 생성
  
  cmds.setAttr("pCube1.translate", 2, 4, 6) 약어 t, tx, ty, tz
  cmds.setAttr("pCube1.rotate", 20, 30, 10) 약어 r, rx, ry, rz
  cmds.setAttr("pCube1.scale", 1, 2, 1)  약어 s, sx, sy, sz
  
- 에러 출력 : 예외 처리문에 쓰면 좋은 디버그용 에러 출력 함수
  cmds.error(문자열)
'''

num = 5
mode = "Cone"

for i in range(num):
    if mode == "Cube":obj = cmds.polyCube()
    elif mode == "Sphere":obj = cmds.polySphere()
    elif mode == "Cone":obj = cmds.polyCone()
    elif mode == "Cylinder":obj = cmds.polyCylinder()
    else:cmds.error("I don't know")
    
    cmds.setAttr(obj[0]+".translateX", random.randint(0, 20))
    cmds.setAttr(obj[0]+".translateY", random.randint(0, 20))
    cmds.setAttr(obj[0]+".translateZ", random.randint(0, 20))
