import maya.cmds as cmds
import maya.mel as mel
import os.path


# def exporter():
#     selected = cmds.ls(selection=True)
#     # mel.eval("doGroup")
#     cmds.group(selected,name="Export_Temp_Group")
#     cmds.select(clear=True)
#     tempSelect = cmds.ls("Export_Temp_Group")
#     cmds.xform(tempSelect,worldSpace=True,absolute=True,scalePivot=(0,0,0),rotatePivot=(0,0,0))
#     cmds.select(tempSelect)
#     return (tempSelect)
#
#     # print selected
#     # print tempSelect

def fbxExport():
    ff = "Maya ASCII (*.ma);; Autodesk FBX (*.fbx);; Wavefront OBJ (*.obj);; All Files (*.*)"
    ff2 ="Autodesk FBX (*.fbx)"
    saveAsFile = cmds.fileDialog2 ( caption="Export to..." , dialogStyle=2 , fileMode=0 , fileFilter=ff2 ,
                                      returnFilter=True )

    # Find the last character '\' and remove everything from that point and before, returning only the file name
    purSaveAsFile = str ( saveAsFile[ 0 ] ).rindex ( "/" ) + 1
    fileNameToSaveAs = str ( saveAsFile[ 0 ] )[ purSaveAsFile: ]
    manualExportFilePath = str ( saveAsFile[ 0 ] )

    # Find the last character '\' and remove everything from that point onwards, only returning the folder path we saved to
    # This is for texture exporting
    textureManualExportPath = str ( saveAsFile[ 0 ] )[ :purSaveAsFile ]

    # File path to explore to
    exploreFilePath = str ( saveAsFile[ 0 ] )[ :purSaveAsFile ]



    # Our File Type to save as
    if manualExportFilePath.endswith ( ".fbx" ):
        manualExportFileType = "FBX export"

    if manualExportFilePath.endswith ( ".obj" ):
        manualExportFileType = "OBJexport"

    if manualExportFilePath.endswith ( ".ma" ):
        manualExportFileType = "mayaAscii"


    # Finally export our file
    cmds.file ( str ( manualExportFilePath ) , type=manualExportFileType , exportSelected=True )

def desktopExport():
    desktopPath = os.path.expanduser ( "~/Desktop" )
    print"Debug(DeskTop):" + desktopPath
    expCmd = 'ExportSelection -f "{}" -s;'.format ( desktopPath )
    mel.eval ( expCmd )

def toBlender():
    #Group and Rotate
    mel.eval ( "doGroup 1 1 1" )
    tempSelect = cmds.ls(selection=True)
    cmds.rotate(worldSpace=True,rotateXYZ=True,orientAxes=(0,90,0))
    # cmds.makeIdentity(tempSelect,apply=True,t=True,r=True,s=True)
    mel.eval ( "ungroup" )
    print ("Debug: Y rotate 90,and Ungroup.")

    #ExportFbx
    desktopExport()

    #Group and Unrotate
    mel.eval ( "doGroup 1 1 1" )
    tempSelect = cmds.ls ( selection=True )
    cmds.rotate ( worldSpace=True , rotateXYZ=True , orientAxes=(0 , -90 , 0) )
    # cmds.makeIdentity ( tempSelect , apply=True , t=True , r=True , s=True )
    mel.eval ( "ungroup" )
    print ("Debug: Y rotate -90,and Ungroup.")

def toUnity():
    #Group and Rotate
    mel.eval ( "doGroup 1 1 1" )
    tempSelect = cmds.ls(selection=True)
    cmds.rotate(worldSpace=True,rotateXYZ=True,orientAxes=(0,-90,0))
    # cmds.makeIdentity(tempSelect,apply=True,t=True,r=True,s=True)
    mel.eval ( "ungroup" )
    print ("Debug: Y rotate -90,and Ungroup.")
    # cmds.fileDialog2()    return the file path
    # https: // github.com / krausekai / maya - scripts / blob / master / Maya2UnityExporter / Maya2UnityExporter.py
    #ExportFbx
    desktopExport()

    #Group and Unrotate
    mel.eval ( "doGroup 1 1 1" )
    tempSelect = cmds.ls ( selection=True )
    cmds.rotate ( worldSpace=True , rotateXYZ=True , orientAxes=(0 , 90 , 0) )
    # cmds.makeIdentity ( tempSelect , apply=True , t=True , r=True , s=True )
    mel.eval ( "ungroup" )
    print ("Debug: Y rotate 90,and Ungroup.")



class StartWindow:
    def __init__(self):
        pass

    def start_window(self):
        window = cmds.window(title="Fbx Exporter", iconName='Short Name', widthHeight=(400, 350))
        master_layout = cmds.columnLayout ( adjustableColumn=True )
        cmds.text ( "Fbx Exporter" )
        cmds.separator ( 20 )

        # cmds.rowLayout(adj=1,nc=4)
        cmds.button(label="Blender",command="toBlender()")
        cmds.button ( label="Max",command="toBlender()")
        cmds.button ( label="Unity",command="toUnity()" )
        # cmds.button ( label='Create' , command=lambda x:create_cube_insta())
        # cmds.button ( label='Delete',command="delete_all_cubes()")          #command = delete_all_cubes,btw method must has (_) for temp argument
        # cmds.button ( label='Close' , command=('cmds.deleteUI(\"' + window + '\", window=True)') )
        cmds.setParent(master_layout)


        cmds.showWindow ( window )

my_window=StartWindow().start_window()
