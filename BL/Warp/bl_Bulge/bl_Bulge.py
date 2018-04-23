# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named bl_BulgeExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from bl_BulgeExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.bl_Bulge"

def getLabel():
    return "bl_Bulge"

def getVersion():
    return 1.0

def getIconPath():
    return "bl_Bulge.png"

def getGrouping():
    return "Community/BL/Warp"

def getPluginDescription():
    return "The Bulge function is a copy of the Bulge inside AfterEffect.Some operators in production ask me for that tool.This PyPlug is basicaly creating a drop/buble effect on a picture."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.3333, 0.702, 0.3451)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createIntParam("NoOp1value", "Value : ")
    param.setMinimum(-100, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(-100, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.NoOp1value = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("NoOp1softness", "Softness : ")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.NoOp1softness = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createDouble2DParam("NoOp1scale", "Scale : ")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(0.5, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(2, 1)
    param.setDefaultValue(0.5, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setCanAutoFoldDimensions(True)
    lastNode.NoOp1scale = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createDouble2DParam("NoOp1center", "Center : ")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(100, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(100, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setUsePointInteract(True)
    lastNode.NoOp1center = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "bl_Bulge v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "Version NATRON du Gizmo Nuke développés par Bertrand Lempereur")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("ENG", "NATRON version of Nuke Gizmo developed by Bertrand Lempereur")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.ENG = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep111", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep111 = param
    del param

    param = lastNode.createStringParam("sep112", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep112 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(4140, 5733)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(4140, 4072)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Multiply3"
    lastNode = app.createNode("net.sf.openfx.MultiplyPlugin", 2, group)
    lastNode.setScriptName("Multiply3")
    lastNode.setLabel("Multiply3")
    lastNode.setPosition(4431, 4343)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupMultiply3 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("value")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Multiply3"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4173, 4352)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Radial4"
    lastNode = app.createNode("net.sf.openfx.Radial", 2, group)
    lastNode.setScriptName("Radial4")
    lastNode.setLabel("Radial4")
    lastNode.setPosition(4431, 4561)
    lastNode.setSize(80, 32)
    lastNode.setColor(1, 1, 1)
    groupRadial4 = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(512, 0)
        param.setValue(512, 1)
        del param

    param = lastNode.getParam("interactive")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Radial4"

    # Start of node "ColorLookup2"
    lastNode = app.createNode("net.sf.openfx.ColorLookupPlugin", 1, group)
    lastNode.setScriptName("ColorLookup2")
    lastNode.setLabel("ColorLookup2")
    lastNode.setPosition(4431, 4655)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupColorLookup2 = lastNode

    param = lastNode.getParam("hasBackgroundInteract")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("lookupTable")
    if param is not None:
        param.setCurveColor(0, 0.9, 0.9, 0.9)
        param.deleteAllControlPoints(0)
        param.addControlPoint(0, 0, 0, 2.5, 2.5, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeFree)
        param.addControlPoint(0, 1, 1, 0.06, 0.06, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeFree)
        param.setCurveColor(1, 0.7115, 0.1645, 0.1645)
        param.deleteAllControlPoints(1)
        param.addControlPoint(1, 0, 0, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.addControlPoint(1, 1, 1, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.setCurveColor(2, 0, 0.547, 0)
        param.deleteAllControlPoints(2)
        param.addControlPoint(2, 0, 0, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.addControlPoint(2, 1, 1, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.setCurveColor(3, 0.2885, 0.2885, 0.8355)
        param.deleteAllControlPoints(3)
        param.addControlPoint(3, 0, 0, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.addControlPoint(3, 1, 1, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.setCurveColor(4, 0.399, 0.399, 0.399)
        param.deleteAllControlPoints(4)
        param.addControlPoint(4, 0, 0, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        param.addControlPoint(4, 1, 1, 1, 1, NatronEngine.Natron.KeyframeTypeEnum.eKeyframeTypeCubic)
        del param

    param = lastNode.getParam("backgroundDisplay")
    if param is not None:
        param.set("none")
        del param

    del lastNode
    # End of node "ColorLookup2"

    # Start of node "Reformat1"
    lastNode = app.createNode("net.sf.openfx.Reformat", 1, group)
    lastNode.setScriptName("Reformat1")
    lastNode.setLabel("Reformat3")
    lastNode.setPosition(4431, 4418)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.651, 0.4863, 1)
    groupReformat1 = lastNode

    param = lastNode.getParam("reformatType")
    if param is not None:
        param.set("box")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("boxSize")
    if param is not None:
        param.setValue(512, 0)
        param.setValue(512, 1)
        del param

    param = lastNode.getParam("boxFixed")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Reformat1"

    # Start of node "NoOp1"
    lastNode = app.createNode("net.sf.openfx.NoOpPlugin", 2, group)
    lastNode.setScriptName("NoOp1")
    lastNode.setLabel("NoOp1")
    lastNode.setPosition(3856, 4988)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupNoOp1 = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param


    # Create the user parameters
    lastNode.user = lastNode.createPageParam("user", "user")
    param = lastNode.createIntParam("value", "value")
    param.setMinimum(-100, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(-100, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.user.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setEnabled(False, 0)
    lastNode.value = param
    del param

    param = lastNode.createDoubleParam("softness", "softness")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.user.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setEnabled(False, 0)
    lastNode.softness = param
    del param

    param = lastNode.createDouble2DParam("scale", "scale")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0.5, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(0.5, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.user.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setEnabled(False, 0)
    param.setEnabled(False, 1)
    lastNode.scale = param
    del param

    param = lastNode.createDouble2DParam("center", "center")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0.5, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)
    param.setDefaultValue(0.5, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.user.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(100, 0)
    param.setValue(100, 1)
    param.setEnabled(False, 0)
    param.setEnabled(False, 1)
    lastNode.center = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['user', 'Controls', 'Node', 'Info'])
    lastNode.refreshUserParamsGUI()
    del lastNode
    # End of node "NoOp1"

    # Start of node "Ramp1"
    lastNode = app.createNode("net.sf.openfx.Ramp", 2, group)
    lastNode.setScriptName("Ramp1")
    lastNode.setLabel("Ramp1")
    lastNode.setPosition(4727, 4655)
    lastNode.setSize(80, 32)
    lastNode.setColor(1, 1, 1)
    groupRamp1 = lastNode

    param = lastNode.getParam("point0")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("point1")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(514, 1)
        del param

    del lastNode
    # End of node "Ramp1"

    # Start of node "black"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("black")
    lastNode.setLabel("black")
    lastNode.setPosition(4577, 4655)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupblack = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("0")
        del param

    del lastNode
    # End of node "black"

    # Start of node "R_to_A"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("R_to_A")
    lastNode.setLabel("R_to A")
    lastNode.setPosition(4727, 4742)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupR_to_A = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    del lastNode
    # End of node "R_to_A"

    # Start of node "Multiply4"
    lastNode = app.createNode("net.sf.openfx.MultiplyPlugin", 2, group)
    lastNode.setScriptName("Multiply4")
    lastNode.setLabel("Multiply4")
    lastNode.setPosition(4727, 4834)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupMultiply4 = lastNode

    param = lastNode.getParam("value")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        param.setValue(2, 2)
        param.setValue(2, 3)
        del param

    del lastNode
    # End of node "Multiply4"

    # Start of node "Add2"
    lastNode = app.createNode("net.sf.openfx.AddPlugin", 2, group)
    lastNode.setScriptName("Add2")
    lastNode.setLabel("Add2")
    lastNode.setPosition(4727, 4918)
    lastNode.setSize(80, 32)
    lastNode.setColor(1, 1, 1)
    groupAdd2 = lastNode

    param = lastNode.getParam("value")
    if param is not None:
        param.setValue(-1, 0)
        param.setValue(-1, 1)
        param.setValue(-1, 2)
        param.setValue(-1, 3)
        del param

    del lastNode
    # End of node "Add2"

    # Start of node "Reformat4"
    lastNode = app.createNode("net.sf.openfx.Reformat", 1, group)
    lastNode.setScriptName("Reformat4")
    lastNode.setLabel("Reformat4")
    lastNode.setPosition(4727, 4997)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.651, 0.4863, 1)
    groupReformat4 = lastNode

    param = lastNode.getParam("useRoD")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("reformatType")
    if param is not None:
        param.set("scale")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("boxSize")
    if param is not None:
        param.setValue(514, 0)
        param.setValue(514, 1)
        del param

    param = lastNode.getParam("boxFixed")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("resize")
    if param is not None:
        param.set("distort")
        del param

    param = lastNode.getParam("reformatCentered")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("flip")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("turn")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Reformat4"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(4501, 4985)
    lastNode.setSize(80, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("b")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(4378, 4987)
    lastNode.setSize(80, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("b")
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Shuffle2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle2")
    lastNode.setLabel("Shuffle2")
    lastNode.setPosition(4430, 5118)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle2 = lastNode

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    del lastNode
    # End of node "Shuffle2"

    # Start of node "Transform1"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform1")
    lastNode.setLabel("Transform1")
    lastNode.setPosition(4430, 5206)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.651, 0.4863, 1)
    groupTransform1 = lastNode

    param = lastNode.getParam("translate")
    if param is not None:
        param.setValue(-157, 0)
        param.setValue(-157, 1)
        del param

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(0.5, 0)
        param.setValue(0.5, 1)
        del param

    param = lastNode.getParam("center")
    if param is not None:
        param.setValue(257, 0)
        param.setValue(257, 1)
        del param

    param = lastNode.getParam("transformCenterChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Transform1"

    # Start of node "IDistort1"
    lastNode = app.createNode("net.sf.openfx.IDistort", 2, group)
    lastNode.setScriptName("IDistort1")
    lastNode.setLabel("IDistort1")
    lastNode.setPosition(4140, 5265)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.651, 0.4863, 1)
    groupIDistort1 = lastNode

    param = lastNode.getParam("uvScale")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "IDistort1"

    # Start of node "Shuffle3"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle3")
    lastNode.setLabel("Shuffle3")
    lastNode.setPosition(4301, 5265)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle3 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("1")
        del param

    del lastNode
    # End of node "Shuffle3"

    # Start of node "Crop1"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop1")
    lastNode.setLabel("Crop1")
    lastNode.setPosition(4430, 5265)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.651, 0.4863, 1)
    groupCrop1 = lastNode

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(750, 0)
        param.setValue(500, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("blackOutside")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupIDistort1)
    groupMultiply3.connectInput(0, groupDot1)
    groupDot1.connectInput(0, groupInput1)
    groupRadial4.connectInput(0, groupReformat1)
    groupColorLookup2.connectInput(0, groupRadial4)
    groupReformat1.connectInput(0, groupMultiply3)
    groupRamp1.connectInput(0, groupblack)
    groupblack.connectInput(0, groupColorLookup2)
    groupR_to_A.connectInput(0, groupRamp1)
    groupMultiply4.connectInput(0, groupR_to_A)
    groupAdd2.connectInput(0, groupMultiply4)
    groupReformat4.connectInput(0, groupAdd2)
    groupMerge1.connectInput(0, groupColorLookup2)
    groupMerge1.connectInput(1, groupReformat4)
    groupMerge2.connectInput(0, groupAdd2)
    groupMerge2.connectInput(1, groupColorLookup2)
    groupShuffle2.connectInput(0, groupMerge1)
    groupShuffle2.connectInput(1, groupMerge2)
    groupTransform1.connectInput(0, groupShuffle2)
    groupIDistort1.connectInput(0, groupDot1)
    groupIDistort1.connectInput(1, groupShuffle3)
    groupShuffle3.connectInput(0, groupDot1)
    groupShuffle3.connectInput(1, groupCrop1)
    groupCrop1.connectInput(0, groupTransform1)

    param = groupRadial4.getParam("softness")
    param.slaveTo(groupNoOp1.getParam("softness"), 0, 0)
    del param
    param = groupNoOp1.getParam("value")
    group.getParam("NoOp1value").setAsAlias(param)
    del param
    param = groupNoOp1.getParam("softness")
    group.getParam("NoOp1softness").setAsAlias(param)
    del param
    param = groupNoOp1.getParam("scale")
    group.getParam("NoOp1scale").setAsAlias(param)
    del param
    param = groupNoOp1.getParam("center")
    group.getParam("NoOp1center").setAsAlias(param)
    del param
    param = groupRamp1.getParam("point1")
    param.setExpression("rod = black.getRegionOfDefinition(frame,view)\nret = rod.height()", True, 1)
    del param
    param = groupTransform1.getParam("translate")
    param.setExpression("rod = black.getRegionOfDefinition(frame,view)\nval1 = rod.width()/2\nret = NoOp1.center.get()[0]-val1", True, 0)
    param.setExpression("rod = black.getRegionOfDefinition(frame,view)\nval1 = rod.height()/2\nret = NoOp1.center.get()[1]-val1", True, 1)
    del param
    param = groupTransform1.getParam("scale")
    param.slaveTo(groupNoOp1.getParam("scale"), 0, 0)
    param.slaveTo(groupNoOp1.getParam("scale"), 1, 1)
    del param
    param = groupTransform1.getParam("center")
    param.setExpression("rod = black.getRegionOfDefinition(frame,view)\nret = rod.width()/2", True, 0)
    param.setExpression("rod = black.getRegionOfDefinition(frame,view)\nret = rod.height()/2", True, 1)
    del param
    param = groupIDistort1.getParam("uvScale")
    param.setExpression("NoOp1.value.get()", False, 0)
    param.setExpression("NoOp1.value.get()", False, 1)
    del param
    param = groupCrop1.getParam("size")
    param.setExpression("rod = Multiply3.getRegionOfDefinition(frame,view)\nret = rod.width()", True, 0)
    param.setExpression("rod = Multiply3.getRegionOfDefinition(frame,view)\nret = rod.height()", True, 1)
    del param

    try:
        extModule = sys.modules["bl_BulgeExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
