filename = input("Input the Filename: ")
for i in range(len(filename)):
  if filename[i] =='.':
    x=i
print ("The extension of the file is : " +filename[x+1:])