import maya.cmds as cmds

def rename():
    selected = cmds.ls(selection =True,dag=True,long=True)

    selected.sort(key=len,reverse = True)


    for i in selected:
        shortNmae = i.split("|")[-1]
        children = cmds.listRelatives(i,children=True,fullPath=True)or[]
        if len(children)==1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(i)

        # print "Children:" + str(children)
    print "Selected"+ str(selected)

    # cmds.rename()