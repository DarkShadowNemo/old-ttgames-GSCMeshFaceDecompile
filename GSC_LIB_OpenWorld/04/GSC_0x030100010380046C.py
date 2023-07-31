from struct import unpack

faces=[]
#trainglestrips

def GSC_4_():
    global VertexCount2
    fa = -1
    fb = 0
    fc = 1
    faces = []
    for i in range(VertexCount2-2):
        if VertexCount2 == 4:
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
            
            
                
