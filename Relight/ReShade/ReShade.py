# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ReShadeExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ReShadeExt import *
except ImportError:
    pass

def getPluginID():
    return "CommunityPyplug.Reshade"

def getLabel():
    return "ReShade"

def getVersion():
    return 1

def getIconPath():
    return "ReShade.png"

def getGrouping():
    return "Community/Relight"

def getPluginDescription():
    return "Normal Based Relighting based on a ShaderToy node.\nYou can set Diffuse , Specular (Phong) and Ambiant color separately.\n\nNote that you need to have an Alpha Channel for ambiant color to work properly.\n\nThanks to Alessandro Dalla Fontana for the initial SeExpr code. "

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createDouble2DParam("LightXY", "Light Position")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(300, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1000, 1)
    param.setDefaultValue(200, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(300, 0)
    param.setValue(500, 1)
    param.setUsePointInteract(True)
    lastNode.LightXY = param
    del param

    param = lastNode.createDoubleParam("posZ", "z")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-1, 0)
    param.setDisplayMaximum(1, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    param.setValue(-0.14, 0)
    lastNode.posZ = param
    del param

    param = lastNode.createSeparatorParam("sepa", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepa = param
    del param

    param = lastNode.createColorParam("ambcol", "Ambiant Color", False)
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setDefaultValue(0.05, 1)
    param.restoreDefaultValue(1)
    param.setMinimum(-2147483648, 2)
    param.setMaximum(2147483647, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)
    param.setDefaultValue(0.1, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.009134056999999999, 0)
    param.setValue(0.012983031, 1)
    param.setValue(0.015996292, 2)
    lastNode.ambcol = param
    del param

    param = lastNode.createColorParam("difcol", "Diffuse Color", False)
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.5, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setDefaultValue(0.5, 1)
    param.restoreDefaultValue(1)
    param.setMinimum(-2147483648, 2)
    param.setMaximum(2147483647, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)
    param.setDefaultValue(0.5, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.43415371, 0)
    param.setValue(0.21952623, 1)
    param.setValue(0.017641952, 2)
    lastNode.difcol = param
    del param

    param = lastNode.createColorParam("specol", "Specular Color", False)
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.5, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setDefaultValue(0.5, 1)
    param.restoreDefaultValue(1)
    param.setMinimum(-2147483648, 2)
    param.setMaximum(2147483647, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)
    param.setDefaultValue(0.5, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    param.setValue(1, 1)
    param.setValue(0.30946895, 2)
    lastNode.specol = param
    del param

    param = lastNode.createSeparatorParam("sepb", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepb = param
    del param

    param = lastNode.createIntParam("rough", "Specular Hardness")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(50, 0)
    param.setDefaultValue(7, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(3, 0)
    lastNode.rough = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Node', 'Settings', 'Info'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(782, 606)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Normal"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Normal")
    lastNode.setLabel("Normal")
    lastNode.setPosition(782, 129)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "ReshadeShader"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("ReshadeShader")
    lastNode.setLabel("ReshadeShader")
    lastNode.setPosition(794, 309)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupReshadeShader = lastNode

    param = lastNode.getParam("mousePosition")
    if param is not None:
        param.setValue(709, 0)
        param.setValue(1918, 1)
        del param

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(14, 0)
        del param

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(-0.14, 0)
        del param

    param = lastNode.getParam("paramValueVec31")
    if param is not None:
        param.setValue(0.009134056999999999, 0)
        param.setValue(0.012983031, 1)
        param.setValue(0.015996292, 2)
        del param

    param = lastNode.getParam("paramValueVec32")
    if param is not None:
        param.setValue(0.43415371, 0)
        param.setValue(0.21952623, 1)
        param.setValue(0.017641952, 2)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramValueVec34")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(0.30946895, 2)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("uniform float Z = -0.5 ; // Z light position\nuniform\tvec3 difcol=vec3(0.5,0.5,0.5);\nuniform\tvec3 specol=vec3(0.5,0.5,0.5);\nuniform\tvec3 ambcol=vec3(0,0.05,0.1);\nuniform int rough = 7 ; // specular roughness / hardness\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec4 nor = texture2D(iChannel0, fragCoord.xy / iResolution.xy).rgba;\n\tvec3 pos=vec3(Z,-(iMouse.xy/iResolution.xy)+0.5);\n\tvec3 light=normalize(pos);\n\n\tvec2 col=vec2(0,0);\n\tvec3 h =(-light+-nor.rgb)/length(light+nor.rgb); \n\tcol.x=dot(light.x,nor.r)+dot(light.y,nor.g)+dot(light.z,nor.b); // diffuse\n\tcol.y=pow(-(dot(h.x,nor.r)+dot(h.y,nor.g)+dot(h.z,nor.b)),rough*10); //specular\n\n\tcol=clamp(col,0,1);\n\tfragColor = vec4((difcol*col.x)+specol*col.y+(ambcol*nor.a),nor.a);\n}\n")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("Z")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Z light position")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(-0.5, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("ambcol")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("ambcol")
        del param

    param = lastNode.getParam("paramDefaultVec31")
    if param is not None:
        param.setValue(0.05000000074505806, 1)
        param.setValue(0.1000000014901161, 2)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("difcol")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("difcol")
        del param

    param = lastNode.getParam("paramDefaultVec32")
    if param is not None:
        param.setValue(0.5, 0)
        param.setValue(0.5, 1)
        param.setValue(0.5, 2)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("rough")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("specular roughness / hardness")
        del param

    param = lastNode.getParam("paramDefaultInt3")
    if param is not None:
        param.setValue(7, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("specol")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("specol")
        del param

    param = lastNode.getParam("paramDefaultVec34")
    if param is not None:
        param.setValue(0.5, 0)
        param.setValue(0.5, 1)
        param.setValue(0.5, 2)
        del param

    del lastNode
    # End of node "ReshadeShader"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupReshadeShader)
    groupReshadeShader.connectInput(0, groupInput1)

    param = groupReshadeShader.getParam("mousePosition")
    param.setExpression("thisGroup.LightXY.get()[0]", False, 0)
    param.setExpression("thisGroup.LightXY.get()[1]", False, 1)
    del param
    param = groupReshadeShader.getParam("paramValueFloat0")
    param.setExpression("thisGroup.posZ.get()", False, 0)
    del param
    param = groupReshadeShader.getParam("paramValueVec31")
    param.setExpression("thisGroup.ambcol.get()[0]", False, 0)
    param.setExpression("thisGroup.ambcol.get()[1]", False, 1)
    param.setExpression("thisGroup.ambcol.get()[2]", False, 2)
    del param
    param = groupReshadeShader.getParam("paramValueVec32")
    param.setExpression("thisGroup.difcol.get()[0]", False, 0)
    param.setExpression("thisGroup.difcol.get()[1]", False, 1)
    param.setExpression("thisGroup.difcol.get()[2]", False, 2)
    del param
    param = groupReshadeShader.getParam("paramValueInt3")
    param.setExpression("thisGroup.rough.get()", False, 0)
    del param
    param = groupReshadeShader.getParam("paramValueVec34")
    param.setExpression("thisGroup.specol.get()[0]", False, 0)
    param.setExpression("thisGroup.specol.get()[1]", False, 1)
    param.setExpression("thisGroup.specol.get()[2]", False, 2)
    del param

    try:
        extModule = sys.modules["ReShadeExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)