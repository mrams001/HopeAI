class GroupFunctions:
    subFields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing" ,"Natural Language Processing" ]
    
    def displaySubFields(self):
        print("Sub-fields in AI are: ")
        for var in self.subFields:
            print(var)


    def checkEvenNum(self):
        val=int(input("Enter a Number: "))
        if val % 2 == 0:
            print(str(val) + " is Even number")
        else:
            print(str(val) + " is Odd number")

    def checkMarriageEligibility(self):
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))

        if gender == 'Male' and age >= 21:            
            print("ELIGIBLE")
        elif (gender == 'Female') and (age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def findPercentage(self):
        total =0
        for i in range(1,6):
            val=int(input("Subject"+ str(i)  +"= " ))
            total=total+val
        print("Total : "+ str(total))
        percentage = (total/500)*100
        print("Percentage : "+ str(percentage))

    def findArea(self):
         ht=int(input("Height : "))
         bdh=int(input("Breadth : ")) 
         area=ht*bdh/2
         print("Area formula: (Height*Breadth)/2")
         print("Area of Triangle:" + str(area))


    def findPerimeter(self):
         ht1=int(input("Height1 : "))
         ht2=int(input("Height2 : "))
         bdh=int(input("Breadth : ")) 
         pmeter=ht1+ht2+bdh
         print("Perimeter formula: Height1+Height2+Breadth")
         print("Perimeter of Triangle:" + str(pmeter))



