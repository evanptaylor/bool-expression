# Kmap solver using Quine-McClusky Algorithm

num_vars = 4
minterms = [4,8,9,10,11,12,14,15]
minterms_ind = [4,8,9,10,11,12,14,15]
# dec_to_bin converts each int in an array to their 4-bit decimal values

def dec_to_bin(list):
    for i in range(0, len(list)):
        list[i] = bin(list[i])[2:]
        list[i] = list[i].zfill(num_vars)
    return list

# count_ones counts the number places who's value is 1 in a given number
def count_ones(str):
    count = 0
    
    for char in str:
        if char == "1":
            count+=1
    return count 

# group_ones returns a dictionary (k,v) => (binary digit, occurances of '1')
def group_ones(arr):
    temp_arr = []
    for i in arr:
        temp_arr.append(count_ones(i))
    
    return(dict(zip(arr, temp_arr)))

def off_by_one(str1, str2):
    off_by = 0
    temp_str = ""
    for i in range(0, len(str1)):
        if str1[i]=="*" or str2[i]=="*":
            return str1
        if str1[i] != str2[i]:
            off_by+=1
    if off_by != 1:
        return str1+"*"
    else:
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                temp_str+= "-"
            else:
                temp_str+=str1[i]
        return temp_str

# replace_nums replaces the alike digits 
def replace_nums(arr):
    replaced_arr = []
    replaced_indexes = []
    temp_str = ""
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            temp_str = off_by_one(arr[i],arr[j])
            if "-" in temp_str:
                replaced_arr.append(temp_str)
                replaced_indexes.append((minterms_ind[i],minterms_ind[j]))
    return replaced_indexes, replaced_arr

def size4_imp(arr):
    size4 = []
    size4_idx = []
    count = 0
    for i in range(0,len(arr)):
        if arr[i].count("-") == 2:
            size4.append(arr[i])
            size4_idx.append(size2_implicants_idx)
    return size4, size4_idx




dec_to_bin(minterms)

#print(group_ones(minterms))

size2_implicants = replace_nums(minterms)

size2_implicants_idx = size2_implicants[0]
size2_implicants_val = size2_implicants[1]
minterms_ind = size2_implicants[0]


#print(size2_implicants_idx)
#print(size2_implicants_val)

size4_implicants = replace_nums(size2_implicants_val)
print(size4_implicants[1])
print(size4_imp(size4_implicants[1]))

#print(minterms)
#print(minterms_ind)


