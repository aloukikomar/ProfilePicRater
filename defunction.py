def name(a,*d):
    if a==1 and d=="a" and g=="pass":
     return g
    else:
     return a 
def call(**args):
    for i in args:
        print(i)

    
a=call(name='aloukik',passd='a',pas='s')
if a==1:
    print("accepted")
else:
    print(a)    