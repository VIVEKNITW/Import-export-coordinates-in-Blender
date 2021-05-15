import bpy
from bpy.types import Operator
from .Landmarks_HelperFunctions import origin_to_gem

class coordinates_savefile(Operator):
    """ """
    bl_label = "Save to file"
    bl_idname = "object.savetofile"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filedir = mytool.myfiledir
        filename = mytool.myfilename
        
        outputFile = filedir+'/'+filename+'.txt'
        verts = bpy.context.selected_objects
        
        for v in verts:
            origin_to_gem(v)
            
        textLines = [str(v.name) + "  " + str(v.location[0]) + "  " + str(v.location[1]) + "  " + str(v.location[2]) + "\n" for v in verts ]

        f = open( outputFile, 'w' )
        f.writelines( textLines )
        f.close()
        
        return {'FINISHED'}   