f=open("py.txt")
print(f.read())


f=open("py.txt","w")
data="Hello students,we are learning file handling in python"
f.write(data)

file=open("content.txt","r")
content=file.read()
print(content)

f=open("py.txt")
print(f.read(5))

with open("content.txt","rb")as file:
  content=file.read()
print(content)

with open("content.txt","r")as file:
  file.seek(5)
  content = file.read(32)
  print(content)


  with open("content.txt",'r')as file:
   line=file.readline()
while line:
 print(line.strip())
line=file.readline()



