import os
import json
from array import array
import UnityPy
import struct
import lz4.block

src = 'actor-shader.unity3d'
env = UnityPy.load(src)

for obj in env.objects:
    if obj.type.name == 'Shader':
        tree = obj.read_typetree()
        if tree['m_ParsedForm']['m_Name'] == "Campus/Actor/Default":
            print(tree['m_ParsedForm']['m_Name'])
            decompressL_tree = tree['decompressedLengths'][0]
            compressedL_tree = tree['compressedLengths'][0]
            data = tree['compressedBlob']
            count = -1
            byte_accumulate = 0
            temp_compressL = 0
            temp_byte_array = []
            for a in decompressL_tree:
                bytedata = b''
                count += 1
                temp_compressL = compressedL_tree[count]
                temp_decompressL = decompressL_tree[count]
                temp_byte_array = data[byte_accumulate:byte_accumulate+temp_compressL]
                byte_accumulate += temp_compressL
                for b in temp_byte_array:
                    bytedata += struct.pack('B', b)
                    #print(bytedata)
                output = lz4.block.decompress(bytedata, uncompressed_size=temp_decompressL)
                outputtxt_string = 'output' + str(count) + '.txt'
                with open(outputtxt_string, 'wb+') as f:
                    f.write(output)
                    print(count)





            




