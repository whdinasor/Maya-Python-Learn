import maya.cmds as cmds
import random

def create_cube_insta():
    random.seed(556876)

    parentCube = cmds.polyCube( w=1 , h=1 , d=1 , n ="myCube#" )
    # print("(Debug)Result:" + str( parentCube ))

    transformName = parentCube[0]
    insGroupName = cmds.group(em=True,n = transformName + "_instance_Grp#")

    for i in range(0,50):
        instanceResult = cmds.instance ( transformName , n=transformName + "_instance#")
        cmds.parent(instanceResult,insGroupName)

        x = random.uniform( -10 , 10 )
        y = random.uniform ( -10 , 10 )
        z = random.uniform ( -10 , 10 )

        rotX = random.uniform(0,360)
        rotY = random.uniform ( 0 , 360 )
        rotZ = random.uniform ( 0 , 360 )

        scaleRandom = random.uniform(0.3,1.5)

        cmds.move(x , y , z , instanceResult )
        cmds.rotate(rotX,rotY,rotZ,instanceResult)
        cmds.scale(scaleRandom,scaleRandom,scaleRandom,instanceResult)

    # print("(Debug) Instances built." )

    cmds.hide(transformName)
    cmds.xform(insGroupName,cp=True)