import bpy
from bpy.types import Operator
from .Landmarks_HelperFunctions import create_single_vert, unhide, delete_obj
    

class coordinates_takefromfile(Operator):
    """ """
    bl_label = "Import"
    bl_idname = "object.takefromfile"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        myfilepath = mytool.myfilepath
        with open (myfilepath, 'r') as myFile:
            for line in myFile:
                my_line = line.split()
                coord_x = float(my_line[-3])
                coord_y = float(my_line[-2])
                coord_z = float(my_line[-1])
                end = len(my_line) - 3

                if end == 0:
                    name = "my point"
                else:
                    name = "_".join(my_line[:end])
                    try:
                        unhide(bpy.data.objects[name])
                        delete_obj(bpy.data.objects[name])
                    except:
                        pass

                create_single_vert(coord_x, coord_y, coord_z, name)
        
        return {'FINISHED'}   