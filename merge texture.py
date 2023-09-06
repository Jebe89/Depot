import bpy

for mat in bpy.data.materials:
    if mat.node_tree:
        for n in mat.node_tree.nodes:
            if n.type == 'TEX_IMAGE':
                if n.image is None:
                    print(mat.name,'has an image node with no image')
                elif n.image.name[-3:].isdigit():
                    name = n.image.name[:-4]
                    exists = False
                    for img in bpy.data.images:
                        if img.name in name:
                            exists = True
                    if exists:
                        n.image = bpy.data.images[name]
                    else:
                        n.image.name = name


                    