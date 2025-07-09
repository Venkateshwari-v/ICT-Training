with open("example.txt",'r')as file:
 lines=file.readlines()
 print(f"Entire file data:{lines}")
 for line in lines:
   print(line.strip())

 
with open("example.txt","w+")as file:
 file.write('Writing new example.\n')
 file.seek(0)
 content = file.read()
 print(content)

import copy
original_list=[[1,2,3],[4,5,6]]
shallow_copy=copy.copy(original_list)
original_list[0][0]=100
print(original_list)
print(shallow_copy)

import copy
original_list=[[1,2,3],[4,5,6]]
deep_copy=copy.deepcopy(original_list)
original_list[0][0]=100
print(original_list)
print(deep_copy)