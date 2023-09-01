import bpy
import json
import os

collname = "Office Prop"
mesh_dir = r'F:/UE4/starlitseason_archive/StarlitSeason/Content/Prop/Priv01/Mesh/'
lib_dir = r'F:/UE4/starlitseason_archive/'

coll = bpy.data.collections.get(collname)
for obj in coll.objects:
    #print(obj.name)

    meshfile = open(mesh_dir + obj.name + '.json')
    meshdata = json.load(meshfile)

    for i in meshdata:
        meshtype = i['Type']

        if meshtype == 'StaticMesh':
            mat = i['Properties']['StaticMaterials']

            for u in mat:
                matname = str(u['MaterialInterface']['ObjectName']).replace("MaterialInstanceConstant'","").replace("'","")
                matdir = str(u['MaterialInterface']['ObjectPath']).replace(".0",".json")
                #print(matname)
                #print(matdir)

                for bmat in bpy.data.materials:
                    if matname == bmat.name:

                        bmat.use_nodes = True
                        matfile = open(lib_dir + matdir)
                        matdata = json.load(matfile)
                        matdata = matdata[0]['Properties']

                        if matdata.get('TextureParameterValues') != None:
                            matdata = matdata['TextureParameterValues']
                            #print(matdata)

                            for o in matdata:

                                if o['ParameterInfo']['Name'] == 'defTex' or o['ParameterInfo']['Name'] == 'DefTex':

                                    deftex_path = str(o['ParameterValue']['ObjectPath']).replace(".0",".tga")
                                    deftex = bpy.data.images.load(lib_dir + deftex_path)
                                    deftex.alpha_mode = 'NONE'

                                    principled_BSDF = bmat.node_tree.nodes['Principled BSDF']
                                    deftex_node = bmat.node_tree.nodes.new('ShaderNodeTexImage')
                                    deftex_node.image = deftex
                                    bmat.node_tree.links.new(deftex_node.outputs[0], principled_BSDF.inputs[0])

                                    print(matname)

                                if o['ParameterInfo']['Name'] == 'emiTex' or o['ParameterInfo']['Name'] == 'EmiTex':

                                    emitex_path = str(o['ParameterValue']['ObjectPath']).replace(".0",".tga")
                                    emitex = bpy.data.images.load(lib_dir + emitex_path)
                                    emitex.alpha_mode = 'NONE'

                                    principled_BSDF = bmat.node_tree.nodes['Principled BSDF']
                                    emitex_node = bmat.node_tree.nodes.new('ShaderNodeTexImage')
                                    emitex_node.image = emitex
                                    bmat.node_tree.links.new(emitex_node.outputs[0], principled_BSDF.inputs[19])


