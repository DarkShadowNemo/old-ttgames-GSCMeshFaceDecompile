from struct import unpack

faces=[]
#unknown

def GSC_5_():
    global VertexCount3_pt2
    fa = -1
    fb = 0
    fc = 1
    for i in range(VertexCount3_pt2-VertexCount3_pt2+1):
        if VertexCount3_pt2 == 5:
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
            
            
                
