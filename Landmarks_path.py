import bpy

class MyProperties(bpy.types.PropertyGroup):

    myfilepath : bpy.props.StringProperty(name= 'File path', maxlen = 1000, subtype='FILE_PATH')
    myfiledir : bpy.props.StringProperty(name= "File Directory", maxlen = 1000, subtype='DIR_PATH') 
    myfilename : bpy.props.StringProperty(name= "File name", maxlen = 1000, subtype= 'FILE_NAME') 
