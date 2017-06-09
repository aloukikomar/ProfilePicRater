name = input("please enter your name\n")
print("hello {0}".format(name))
check=True
while check:
    try:
       age = int(input("input your age-"))
    except ValueError:
         print("enter a digit")
         continue
    if age>=10:
          print("proceed")
    elif age==0:
        print("exiting")
        check=False
    else:  
          print("re try after {0} years".format(10-age))
