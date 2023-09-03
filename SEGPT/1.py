res=[]
dic={1:"name1",2:"name2"}
for i in dic.keys():
    res.append({"id":i,"name":dic[i]})
print(res)