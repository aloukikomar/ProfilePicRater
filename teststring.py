i="pass"
j = 5
k= [12,34,5,56]
if i=="pass" :
 for i in range(1,200,5):
    print("hello {0} {1}".format(i,"."))
 if j==5:
  print("exact") 
  if j in k:
   print("duplicate") 
 elif j>1:
    print(j)
  
elif i=="failed":
    print("the attempt was {0}".format(i))
    
else:      
  db={
    'server':'localhost',
    'user':'test',
    'pass':'aloukik'
   }
  print(db.keys())
  print(db.values())
  print(db.items())