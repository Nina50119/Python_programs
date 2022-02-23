# program to concatenate two lists index wise
list1=["Ni","i","intere","i","pene","tes"]
list2=["na","s","sted","n","tration","ting"]
list3=[i+j for i,j in zip(list1,list2)]
print(list3)
