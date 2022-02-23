# remove all occurrences of a specific value
list=[4,6,0,6,7,8,10]
def remove_value(sample_list,value):
 return [i for i in sample_list if i!=value]
res=remove_value(list,6)
print(res)


