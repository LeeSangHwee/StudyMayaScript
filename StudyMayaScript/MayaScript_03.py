from maya import cmds
import random # 랜덤 함수를 쓰기위해 import

i = 0
while i < 10: # Cube 10개 생성
    obj = cmds.polyCube()
    i = i+1

    # 오브젝트 생성시 x, y, z 랜덤 좌표로 이동
    cmds.setAttr(obj[0]+".tx", random.randint(0, 20)) #int로 랜덤
    cmds.setAttr(obj[0]+".ty", random.randint(0, 20)) #float 로 하려면 randfloat
    cmds.setAttr(obj[0]+".tz", random.randint(0, 20))
    print(obj[0]) #오브젝트 명 출력
