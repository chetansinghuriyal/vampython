#conditonal statement will check the conditon is true
# to cheeck the conditon we use if else 

# wap to check user eligible for voting 
userage=int(input("enter your age"))

#note the default input fucntion return 
# for vote usage must be greater than 18 
if userage>18:
    print("your are eligible for voting ")
else :
    print("your are not eligible for voting ")

    # to check the user is male or female 
usergender=input("enter your gender")
if usergender=="male":
        print("you cannot sit in first compartment")
elif usergender=="female":
        print("you can sit in first compartment")
else:
        print("you can sit in any compartment")
        #wap if gender is female and age is greater than 18-> govt job apply 
        #e
        #else male age greater than 18-> private job only 
if userage > 18:
        if usergender=="male":
            print("you can apply for private job")
        elif usergender=="female":
            print("you can apply for govt jobb")
        else:
            print("you are not eligible")  
else:
      print("you are under age ")              