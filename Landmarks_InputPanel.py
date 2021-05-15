import bpy
from bpy.types import Panel

class coordinates_import(Panel):
    """ """
    bl_label = "Import coordinates"
    bl_idname = "coordinates_inputpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Coordinates"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        row.label(text= "Select the text file")
        row = layout.row()
        row.prop(mytool, 'myfilepath')
        row = layout.row()
        row.operator("object.takefromfile")
        
        
   