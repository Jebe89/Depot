# By Eleanor

for i in range(0,105):
    bpy.context.scene.frame_current = i*5
    bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier='Armature',report=True)

bpy.context.scene.frame_current = 1