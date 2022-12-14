import maya.cmds as cmds
# import sys
# sys.path.insert(0, r"D:\Fork\Maya Learn\Maya python\scripts\Learn002")
#import create_cube as cb
#import delete_all_cube as dac
import random
from datetime import datetime
##
def create_cube_insta():
    random_seed = int(datetime.now().minute*60 + datetime.now().second)
    random.seed(random_seed)

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

def delete_all_cubes():
    cubeList = cmds.ls( "myCube*" )
    if len( cubeList )>0:
        cmds.delete( cubeList )

def store_item(txt):
    selections = cmds.ls(sl=True)
    if len(selections)>0:
        cmds.textField(txt,edit=True,text=selections[0])
    else:
        cmds.textField(txt,edit=True,text="")

def select_item(txt):
    txtt = cmds.textField(txt,query=True,text=True)
    print txtt
    cmds.select(txtt,replace=True)

# def press_button_button(name,*args ):
#     namename = cmds.textFieldGrp(name,query=True,text=True)
#     print("Debug: Button pressed." + str ( namename ))

class StartWindow:
    def __init__(self):
        pass

    def start_window(self):
        window = cmds.window(title="Long Name", iconName='Short Name', widthHeight=(400, 350))
        master_layout = cmds.columnLayout ( adjustableColumn=True )
        cmds.text ( "Box Distribute" )
        cmds.separator ( 20 )

        cmds.rowLayout(adj=1,nc=4)
        cmds.button ( label='Create' , command=lambda x:create_cube_insta())
        cmds.button ( label='Delete',command="delete_all_cubes()")          #command = delete_all_cubes,btw method must has (_) for temp argument
        cmds.button ( label='Close' , command=('cmds.deleteUI(\"' + window + '\", window=True)') )
        cmds.setParent(master_layout)

        cmds.text("Selector")

        for i in range(3):
            name = "store_obj"+str(i)
            cmds.rowLayout ( adj=1 , nc=2 )
            store_obj1 = cmds.textField(editable=False)
            cmds.button(label="Store Item",command=lambda x:store_item(store_obj1))
            cmds.setParent ( master_layout )
            cmds.button(label="Selection",command = lambda x:select_item(store_obj1))
            cmds.separator(20)


        cmds.text ( "Box Creator" )
        self.textTest = cmds.textFieldGrp(label='Name:',text="myCube")                #,editable=False
        self.size = cmds.floatFieldGrp(nf = 3 ,label = "Size(x,y,z):",v1=1,v2=1,v3=1)
        self.subdivision = cmds.intSliderGrp(field=True ,label="Slider",min=1,max=20,v=10)
        self.pressButton = cmds.button ( label="Create Cube" , command=self.press_button )
        cmds.setParent ( master_layout )

        cmds.showWindow ( window )

    def press_button(self,*args ):
        name = cmds.textFieldGrp ( self.textTest , query=True , text=True )
        width = cmds.floatFieldGrp(self.size,query=True,v1=True)
        height = cmds.floatFieldGrp(self.size,query=True,v2=True)
        depth = cmds.floatFieldGrp(self.size,query=True,v3=True)
        subdivs = cmds.intSliderGrp(self.subdivision,query=True,v=True)

        if name =="":
            name = "empty"
        cmds.polyCube(name=name+"#",width=width,height=height,depth=depth,sw=subdivs,sh=subdivs,sd=subdivs)

        print("Debug: Button pressed." + str ( width ))


my_window = StartWindow().start_window()
