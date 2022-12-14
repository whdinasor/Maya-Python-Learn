import maya.cmds as cmds


def delete_all_cubes():
    cubeList = cmds.ls( "myCube*" )
    if len( cubeList )>0:    cmds.delete( cubeList )