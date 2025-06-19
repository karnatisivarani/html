# list = ["abhinaya","shivarani","jyothi"]
# count=0
# for i in list:
#     for j in i:
#         count+=1
#         print(count)

# list = ["abhinaya","shivarani","jyothi"]
# dict={}
# count=0
# for i in list:
#     for j in i:
#         count+=1
#     dict[i]=count    
        
# print(dict)

# dict={'1':'mahesh',3:'dhanush',4:'rajendra'}
# dict.pop('1')
# print(dict)


# dict={'1':'mahesh',3:'dhanush',4:'rajendra'}
# update_dict={'5':'mohan babu sir',6:'surya'}
# dict.update(update_dict)
# print(dict)

# setdefault
# dict={"user_name":"sivarani","password":"upasana"
#       }
# print(dict.get("next-movie","pedhi"))
# print(dict)
# print(dict.setdefault("user_name","pedhi"))
# print(dict.setdefault("user_movie","pedhi"))
# print(dict)

# zip
# list=['k1','k2','k1','k4','k5']
# list1=['v1','v2','v3','v4','k5']
# dict=dict(zip(list,list1))
# print(dict)

list1=[1,2,3,4,5,6]
list2=['a','b','c','d','e']
dict={}
for i in range(len(list1)):
    dict[list1[i]]=list2[i]
    print(dict)

a="sivarani"
b={}
for ch in a:
    if ch in b:
        b[ch]+=1
    else:
        b[ch]=3
        print(b)




