def non_unique_elements():
    f=input('please input the numbers:')
    f=f.split(' ')      
    list1=[int(f[i]) for i in range(len(f))]  #这里转换时要加上[]才行哦^-^
    set1=set(list1.copy())    
    for i in set1:
        if list1.count(i) ==1:
            list1.remove(i)
    
        print("the %d has found %d" %(i,list1.count(i)))
    return list1

print(non_unique_elements())
                
                
                

#一行代码秒杀.....
def checkio(data):
        return [i for i in data if data.count(i) > 1]
