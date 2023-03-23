from xml.dom.minidom import parse
import xml.dom.minidom
import bpy

obj = bpy.context.active_object
print("Armature selected:",obj.name)
bpy.ops.cats_manual.start_pose_mode()

dom = xml.dom.minidom.parse("C:\\Users\\Led\\Desktop\\SubExport.xml")
root = dom.documentElement
root = root.getElementsByTagName('TheSubs')[0]
name = root.getElementsByTagName('NameString')
value = root.getElementsByTagName('Value')
length = len(name)
axis = ['x','y','z']
for x in range(length):
    n = name[x]
    print(n.firstChild.data)
    for y in range(3):
        v = value[3*x+y]
        vv = float(v.firstChild.data)
        a = axis[y]
        if n.firstChild.data in obj.data.bones:
            bpy.data.objects[obj.name].pose.bones[n.firstChild.data].scale[y] = vv
            print(a + 'scaled to' + v.firstChild.data)
        else:
            continue




