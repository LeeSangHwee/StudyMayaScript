# 마야 cmds import
import maya.cmds as cmds
# ramdom import
import random

# 오브젝트 생성 함수 - 매개변수는 오브젝트 종류 명과 생성 할 갯수
def cObj(mode, num):
    objList = []
    for i in range(num):
        if   mode == "Cube"  :obj = cmds.polyCube()   # Cube 생성
        elif mode == "Cone"  :obj = cmds.polyCone()   # Cone 생성
        elif mode == "Sphere":obj = cmds.polySphere() # Sphere 생성
        else:cmds.error("I don't know Type")          # 예외처리 코드
        objList.append(obj[0]) # 오브젝트 생성시 List 에 추가

    return objList # List 를 return

# 오브젝트 랜덤으로 생성하는 함수 - 매개변수는 오브젝트 List와 랜덤 값의 최대, 최솟값
def randObj(objList, minP=-20, maxP=20):
    for obj in objList:#리스트 내의 모든 오브젝트의 x, y, z 값을 랜덤으로 변경
        cmds.setAttr(obj+".tx", random.randint(minP, maxP))
        cmds.setAttr(obj+".ty", random.randint(minP, maxP))
        cmds.setAttr(obj+".tz", random.randint(minP, maxP))                

# 오브젝트 명과 생성 할 오브젝트의 갯수 입력
ObjType, ObjNum = raw_input().split()
# 오브젝트 랜덤 좌표로 이동하는 함수 호출
randObj(cObj(ObjType, int(ObjNum)))
