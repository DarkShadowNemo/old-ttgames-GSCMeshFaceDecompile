from struct import unpack

faces=[]
#unknown

def GSC_5_():
    global VertexCount3
    fa = -1
    fb = 0
    fc = 1
    for i in range(VertexCount3-2):
        if VertexCount3 == 5:
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
            
            
                
