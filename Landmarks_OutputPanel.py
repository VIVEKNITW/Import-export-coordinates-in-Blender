import bpy
from bpy.types import Panel

class coordinates_export(Panel):
    """ """
    bl_label = "Export coordinates"
    bl_idname = "coordinates_outputpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Coordinates"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        row.prop(mytool, "myfilename")
        row = layout.row()
        row.prop(mytool, "myfiledir")
        row = layout.row()
        row.operator("object.savetofile")
   