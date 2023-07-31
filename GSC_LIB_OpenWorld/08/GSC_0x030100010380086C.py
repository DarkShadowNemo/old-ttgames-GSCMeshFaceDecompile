from struct import unpack

faces=[]
#trianglestrips
#duplicated  vertices 8 todo subtract by 4
#seek by 64 again

def GSC_8_():
    global VertexCount6
    fa=-1
    fb=0
    fc=1
    for i in range(VertexCount6-6):
        if VertexCount6 == 8:
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
        
