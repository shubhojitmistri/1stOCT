import bpy

obj = bpy.context.object
mesh = obj.data


file1 = open("C:\\Users\\Johno\\Desktop\\txtFiles\\vertices.txt", 'a')
for vert in mesh.vertices:
   xyz = vert.co.xyz
   print(f"{xyz[0]}, {xyz[1]}, {xyz[2]}")
   file1.write(f"({xyz[0]}, {xyz[1]}, {xyz[2]}),\n")





for face in mesh.polygons:
   print(f"{face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}")
   file2 = open("C:\\Users\\Johno\\Desktop\\txtFiles\\faces.txt", 'a')
   file2.write(f"({face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}),\n")
