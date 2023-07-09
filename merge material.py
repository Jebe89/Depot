import bpy

mat_list = bpy.data.materials

for o in bpy.data.objects:
    for s in o.material_slots:
        if s.material.name[-3:].isnumeric():
            # the last 3 characters are numbers
            if s.material.name[:-4] in mat_list:
                # there is a material without the numeric extension so use it
                s.material = mat_list[s.material.name[:-4]]