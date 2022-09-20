# 2x2 Kmap solver

class Kmap(object):
    
    def __init__(self):
        self.kmap = [0]*4
        self.size = 4

    def get_true(self):
        true_vals = 0
        for i in self.kmap:
            if i==1:
                true_vals+=1
        return true_vals
    # fill out entire map with 0 or 1 based on input
    def fill(self, function):
        self.kmap = [0]*self.size
        for i in range(0, self.size):
            if i in function:
                self.kmap[i] = 1
        return self.kmap

    def split(self): 
        arr = []
        sub_arr = []
        arr.append(self.kmap)
        for i in range(0,len(self.kmap)-1):
            sub_arr.append(self.kmap[i])
            sub_arr.append(self.kmap[i+1])
            arr.append(sub_arr)
            sub_arr.clear()
        return arr


        



myfunction = [0,1]
kmap = Kmap()
print(kmap.fill(myfunction))
print(kmap.get_true())
print(kmap.split())


