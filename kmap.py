# 2x2 Kmap solver

# fill out entire map with 0 or 1 based on input

def fill(indexes):
    kmap = [0]*4
    for i in range(0, 4):
        if i in indexes:
            kmap[i] = 1
    return kmap
        

mykmap = [0,1]

print(fill(mykmap))