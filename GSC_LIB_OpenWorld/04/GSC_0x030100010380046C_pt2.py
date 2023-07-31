from struct import unpack

faces=[]
#trainglestrips

def GSC_4_():
    global VertexCount2_pt2
    fa = -1
    fb = 0
    fc = 1
    for i in range(VertexCount2_pt2-vertexCount2_pt2+1):
        if VertexCount2_pt2 == 4:
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
            
            
                
