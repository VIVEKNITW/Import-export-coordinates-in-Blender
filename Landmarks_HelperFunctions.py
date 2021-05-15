import bpy

def deselect():
    bpy.ops.object.select_all(action='DESELECT')
   
   
def select_activate(object):
    object.select_set(True)
    bpy.context.view_layer.objects.active = object
    
   
def origin_to_gem(item):
    deselect()
    select_activate(item)
    bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY', center='MEDIAN')  


def create_single_vert(coord_x, coord_y, coord_z, name):
    bpy.ops.mesh.primitive_vert_add()
    bpy.ops.object.editmode_toggle()
    bpy.context.object.name = name
    bpy.data.objects[name].location = (coord_x, coord_y, coord_z)


def delete_obj(obj):
    deselect()
    select_activate(obj)
    bpy.ops.object.delete(use_global=False, confirm=False)


def unhide(obj):
    deselect()
    bpy.context.view_layer.objects.active = obj
    bpy.context.object.hide_set(False)

