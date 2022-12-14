import sys
import maya.api.OpenMaya as api


def maya_useNewAPI():
    pass

class HelloWorldCmd(api.MPxCommand):
    KCmdName = "helloWorld"

    def __init__(self):
        api.MPxCommand.__init__(self)


    @staticmethod
    def creator():
        return HelloWorldCmd()

    def doIt(self, arg_list):
        print "Hello,world~"


def initializePlugin(mobject):
    fn_plugin = api.MFnPlugin(mobject)
    try:
        fn_plugin.registerCommand(HelloWorldCmd.KCmdName, HelloWorldCmd.creator)
    except:
        sys.stderr.write("Fail to regist command"+HelloWorldCmd.KCmdName)


def uninitializePlugin(mobject):
    fn_plugin = api.MFnPlugin(mobject)
    try:
        fn_plugin.deregisterCommand(HelloWorldCmd.KCmdName)
    except:
        sys.stderr.write("Fail to uninitialize command"+HelloWorldCmd.KCmdName)