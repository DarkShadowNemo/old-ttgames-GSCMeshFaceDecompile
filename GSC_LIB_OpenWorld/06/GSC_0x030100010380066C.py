from struct import unpack

faces=[]
#triangles

def GSC_6_():
    global VertexCount4
    fa = -3
    fb = -2
    fc = -1
    for i in range(VertexCount4//2-1):
        if VertexCount4 == 6:
            fa+=1*3
            fb+=1*3
            fc+=1*3
            faces.append([fa,fb,fc])
            
            
                
