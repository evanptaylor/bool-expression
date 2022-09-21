# Kmap solver using Quine-McClusky Algorithm

# dec_to_bin converts each int in an array to their 4-bit decimal values
num_vars = 4
minterms = [0,1,4,6,8,9,14,15]

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
        if str1[i] == "-" or str2[i] == "-":
            return str1
        if str1[i] != str2[i]:
            off_by+=1
    if off_by != 1:
        return str1
    else:
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                temp_str+= "-"
            else:
                temp_str+=str1[i]
        return temp_str

# replace_nums replaces the alike digits in the dictionary
def replace_nums(arr):
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            arr[i] = off_by_one(arr[i],arr[j])
                



print(dec_to_bin(minterms))

#print(group_ones(minterms))

print(minterms)
print(replace_nums(minterms))
print(minterms)


