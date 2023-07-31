from struct import unpack

faces=[]

def GSC_3_():
    global VertexCount
    fa = -3
    fb = -2
    fc = -1
    faces=[]
    for i in range(VertexCount):
        if VertexCount == 3:
            fa+=1*3
            fb+=1*3
            fc+=1*3
            faces.append([fa,fb,fc])
            
            
                
