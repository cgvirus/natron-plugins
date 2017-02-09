# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named SharpenPlusExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from SharpenPlusExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.SharpenPlus"

def getLabel():
    return "SharpenPlus"

def getVersion():
    return 1

def getGrouping():
    return "Filter"

def getPluginDescription():
    return "Image sharper."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("separator01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator01 = param
    del param

    param = lastNode.createStringParam("separator02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator02 = param
    del param

    param = lastNode.createSeparatorParam("SharpenPlus", "SharpenPlus")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SharpenPlus = param
    del param

    param = lastNode.createStringParam("separator03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator03 = param
    del param

    param = lastNode.createStringParam("separator04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator04 = param
    del param

    param = lastNode.createSeparatorParam("line01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line01 = param
    del param

    param = lastNode.createDoubleParam("Amount", "Amount")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Amount = param
    del param

    param = lastNode.createDoubleParam("Size", "Size")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Size = param
    del param

    param = lastNode.createStringParam("separator06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator06 = param
    del param

    param = lastNode.createSeparatorParam("line05", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line05 = param
    del param

    param = lastNode.createDoubleParam("White", "White")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.White = param
    del param

    param = lastNode.createDoubleParam("Black", "Black")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Black = param
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

    param = lastNode.createSeparatorParam("line08", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line08 = param
    del param

    param = lastNode.createBooleanParam("Use_mask", "Use alpha mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Use_mask = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line02", "EdgeMatteDetect")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
    del param

    param = lastNode.createSeparatorParam("line03", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2016)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4148, 3920)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Log2Lin1"
    lastNode = app.createNode("net.sf.openfx.Log2Lin", 1, group)
    lastNode.setScriptName("Log2Lin1")
    lastNode.setLabel("Log2Lin1")
    lastNode.setPosition(4387, 1818)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupLog2Lin1 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("Lin to Log")
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Log2Lin1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4420, 1651)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(4193, 1651)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Blur2"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur2")
    lastNode.setLabel("Blur2")
    lastNode.setPosition(4565, 1924)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur2 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        del param

    del lastNode
    # End of node "Blur2"

    # Start of node "Dot3_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3_2")
    lastNode.setLabel("Dot3_2")
    lastNode.setPosition(4610, 1832)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3_2 = lastNode

    del lastNode
    # End of node "Dot3_2"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(4375, 2027)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("minus")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("minus")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("BChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("OutputChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("aChannelsChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("bChannelsChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Dot4_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4_2")
    lastNode.setLabel("Dot4_2")
    lastNode.setPosition(4610, 2053)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4_2 = lastNode

    del lastNode
    # End of node "Dot4_2"

    # Start of node "Grade_Bandpass"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade_Bandpass")
    lastNode.setLabel("Grade_Bandpass")
    lastNode.setPosition(4375, 2179)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade_Bandpass = lastNode

    param = lastNode.getParam("white")
    if param is not None:
        param.setValue(3, 0)
        param.setValue(3, 1)
        param.setValue(3, 2)
        param.setValue(3, 3)
        del param

    param = lastNode.getParam("offset")
    if param is not None:
        param.setValue(0.5, 0)
        param.setValue(0.5, 1)
        param.setValue(0.5, 2)
        param.setValue(0.5, 3)
        del param

    param = lastNode.getParam("clampWhite")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade_Bandpass"

    # Start of node "Saturation1"
    lastNode = app.createNode("net.sf.openfx.SaturationPlugin", 2, group)
    lastNode.setScriptName("Saturation1")
    lastNode.setLabel("Saturation1")
    lastNode.setPosition(4375, 2290)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupSaturation1 = lastNode

    param = lastNode.getParam("saturation")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Saturation1"

    # Start of node "MergeMask"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("MergeMask")
    lastNode.setLabel("MergeMask")
    lastNode.setPosition(4697, 2443)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMergeMask = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("overlay")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("overlay")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "MergeMask"

    # Start of node "Dot5_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5_2")
    lastNode.setLabel("Dot5_2")
    lastNode.setPosition(4418, 2469)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5_2 = lastNode

    del lastNode
    # End of node "Dot5_2"

    # Start of node "Dot6_2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6_2")
    lastNode.setLabel("Dot6_2")
    lastNode.setPosition(4744, 1651)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6_2 = lastNode

    del lastNode
    # End of node "Dot6_2"

    # Start of node "Merge_Negative_Value"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge_Negative_Value")
    lastNode.setLabel("Merge_Negative_Value")
    lastNode.setPosition(4699, 2589)
    lastNode.setSize(104, 88)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge_Negative_Value = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("plus")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("plus")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "Merge_Negative_Value"

    # Start of node "Clamp_NEG"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp_NEG")
    lastNode.setLabel("Clamp_NEG")
    lastNode.setPosition(4924, 2612)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp_NEG = lastNode

    param = lastNode.getParam("minimum")
    if param is not None:
        param.setValue(-150, 0)
        param.setValue(-150, 1)
        param.setValue(-150, 2)
        param.setValue(-150, 3)
        del param

    param = lastNode.getParam("maximum")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Clamp_NEG"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(5185, 1649)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "Dot8"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot8")
    lastNode.setLabel("Dot8")
    lastNode.setPosition(5185, 2626)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot8 = lastNode

    del lastNode
    # End of node "Dot8"

    # Start of node "Clamp_POS"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp_POS")
    lastNode.setLabel("Clamp_POS")
    lastNode.setPosition(4926, 2711)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp_POS = lastNode

    param = lastNode.getParam("minimum")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    param = lastNode.getParam("maximum")
    if param is not None:
        param.setValue(1500, 0)
        param.setValue(1500, 1)
        param.setValue(1500, 2)
        param.setValue(1500, 3)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Clamp_POS"

    # Start of node "Dot9"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot9")
    lastNode.setLabel("Dot9")
    lastNode.setPosition(5185, 2725)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot9 = lastNode

    del lastNode
    # End of node "Dot9"

    # Start of node "Merge_Positive_Value"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge_Positive_Value")
    lastNode.setLabel("Merge_Positive_Value")
    lastNode.setPosition(4699, 2771)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge_Positive_Value = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("plus")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("plus")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    del lastNode
    # End of node "Merge_Positive_Value"

    # Start of node "Grade_Offset"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade_Offset")
    lastNode.setLabel("Grade_Offset")
    lastNode.setPosition(4926, 2783)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade_Offset = lastNode

    param = lastNode.getParam("offset")
    if param is not None:
        param.setValue(-1, 0)
        param.setValue(-1, 1)
        param.setValue(-1, 2)
        param.setValue(-1, 3)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade_Offset"

    # Start of node "Dissolve1"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("Dissolve1")
    lastNode.setLabel("Dissolve1")
    lastNode.setPosition(4148, 3273)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupDissolve1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Dissolve1"

    # Start of node "Dot10"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot10")
    lastNode.setLabel("Dot10")
    lastNode.setPosition(5185, 3287)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot10 = lastNode

    del lastNode
    # End of node "Dot10"

    # Start of node "Merge_Black"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge_Black")
    lastNode.setLabel("Merge_Black")
    lastNode.setPosition(4148, 2941)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge_Black = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("min")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("min")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Merge_Black"

    # Start of node "Merge_White"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge_White")
    lastNode.setLabel("Merge_White")
    lastNode.setPosition(4148, 3096)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge_White = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("max")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("max")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Merge_White"

    # Start of node "Dot11"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot11")
    lastNode.setLabel("Dot11")
    lastNode.setPosition(4744, 2967)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot11 = lastNode

    del lastNode
    # End of node "Dot11"

    # Start of node "Dot12"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot12")
    lastNode.setLabel("Dot12")
    lastNode.setPosition(4743, 3122)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot12 = lastNode

    del lastNode
    # End of node "Dot12"

    # Start of node "Alpha_copy1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Alpha_copy1")
    lastNode.setLabel("Alpha_copy1")
    lastNode.setPosition(4141, 3605)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupAlpha_copy1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("B.a")
        del param

    del lastNode
    # End of node "Alpha_copy1"

    # Start of node "Dot13"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot13")
    lastNode.setLabel("Dot13")
    lastNode.setPosition(5191, 3619)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot13 = lastNode

    del lastNode
    # End of node "Dot13"

    # Start of node "rgb"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("rgb")
    lastNode.setLabel("rgb")
    lastNode.setPosition(4148, 1429)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    grouprgb = lastNode

    del lastNode
    # End of node "rgb"

    # Start of node "Switch_Mask"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch_Mask")
    lastNode.setLabel("Switch_Mask")
    lastNode.setPosition(4146, 3487)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch_Mask = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch_Mask"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(3677, 3261)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("matte")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("matte")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("B")
        del param

    param = lastNode.getParam("BChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(3923, 2830)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    del lastNode
    # End of node "Mask"

    # Start of node "Alpha_copy1_2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Alpha_copy1_2")
    lastNode.setLabel("Alpha_copy1_2")
    lastNode.setPosition(3923, 3273)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupAlpha_copy1_2 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("B.a")
        del param

    del lastNode
    # End of node "Alpha_copy1_2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(3722, 1651)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(3718, 3503)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupAlpha_copy1)
    groupLog2Lin1.connectInput(0, groupDot1)
    groupDot1.connectInput(0, groupDot2)
    groupDot2.connectInput(0, grouprgb)
    groupBlur2.connectInput(0, groupDot3_2)
    groupDot3_2.connectInput(0, groupLog2Lin1)
    groupMerge1.connectInput(0, groupDot4_2)
    groupMerge1.connectInput(1, groupLog2Lin1)
    groupDot4_2.connectInput(0, groupBlur2)
    groupGrade_Bandpass.connectInput(0, groupMerge1)
    groupSaturation1.connectInput(0, groupGrade_Bandpass)
    groupMergeMask.connectInput(0, groupDot6_2)
    groupMergeMask.connectInput(1, groupDot5_2)
    groupDot5_2.connectInput(0, groupSaturation1)
    groupDot6_2.connectInput(0, groupDot1)
    groupMerge_Negative_Value.connectInput(0, groupMergeMask)
    groupMerge_Negative_Value.connectInput(1, groupClamp_NEG)
    groupClamp_NEG.connectInput(0, groupDot8)
    groupDot7.connectInput(0, groupDot6_2)
    groupDot8.connectInput(0, groupDot7)
    groupClamp_POS.connectInput(0, groupDot9)
    groupDot9.connectInput(0, groupDot8)
    groupMerge_Positive_Value.connectInput(0, groupMerge_Negative_Value)
    groupMerge_Positive_Value.connectInput(1, groupGrade_Offset)
    groupGrade_Offset.connectInput(0, groupClamp_POS)
    groupDissolve1.connectInput(0, groupDot10)
    groupDissolve1.connectInput(1, groupMerge_White)
    groupDot10.connectInput(0, groupDot9)
    groupMerge_Black.connectInput(0, groupDot2)
    groupMerge_Black.connectInput(1, groupDot11)
    groupMerge_White.connectInput(0, groupMerge_Black)
    groupMerge_White.connectInput(1, groupDot12)
    groupDot11.connectInput(0, groupMerge_Positive_Value)
    groupDot12.connectInput(0, groupDot11)
    groupAlpha_copy1.connectInput(0, groupDot13)
    groupAlpha_copy1.connectInput(1, groupSwitch_Mask)
    groupDot13.connectInput(0, groupDot10)
    groupSwitch_Mask.connectInput(0, groupDissolve1)
    groupSwitch_Mask.connectInput(1, groupDot4)
    groupMerge2.connectInput(0, groupDot3)
    groupMerge2.connectInput(1, groupAlpha_copy1_2)
    groupAlpha_copy1_2.connectInput(0, groupMask)
    groupAlpha_copy1_2.connectInput(1, groupDissolve1)
    groupDot3.connectInput(0, groupDot2)
    groupDot4.connectInput(0, groupMerge2)

    param = groupBlur2.getParam("size")
    param.setExpression("thisGroup.Size.get()", False, 0)
    param.setExpression("thisGroup.Size.get()", False, 1)
    del param
    param = groupGrade_Bandpass.getParam("white")
    param.setExpression("thisGroup.Amount.get()", False, 0)
    param.setExpression("thisGroup.Amount.get()", False, 1)
    param.setExpression("thisGroup.Amount.get()", False, 2)
    param.setExpression("thisGroup.Amount.get()", False, 3)
    del param
    param = groupMerge_Black.getParam("mix")
    param.setExpression("thisGroup.Black.get()", False, 0)
    del param
    param = groupMerge_White.getParam("mix")
    param.setExpression("thisGroup.White.get()", False, 0)
    del param
    param = groupSwitch_Mask.getParam("which")
    param.setExpression("thisGroup.Use_mask.get()", False, 0)
    del param

    try:
        extModule = sys.modules["SharpenPlusExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
