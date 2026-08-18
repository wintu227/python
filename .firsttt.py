[print("hello world!")
student_name = "wintana mengsteab"
age=19
education_level = "freshman student"

print("my name is " + student_name) 
print ("iam " + education_level) 
print(" iam " + str(age) + " years  old" )
print (f"my name is {student_name} and i am {age} years old")
print(len(student_name))
print(student_name.upper())
print(student_name.strip())
print("a" in student_name)
ask_name = input("what is your name?")
print("hello " + ask_name)
a = 2
b = 4 
print(a!=b)
if "a" in student_name:print("no")
elif "B" in student_name:print("yes")
else:print("not")
if age > 18:
  if student_name == "wintana mengsteab":
      print("pass")
  else:print("not found")
else:print("not pass")
fruits = [ "apple","banana","mango"]
for name in fruits:
   print(f"i love {name}")
print(len(fruits))
customer_name = [("almaz",1500),("dawiT",700),("tigist",200)]
for name ,balance in customer_name: 
    if balance >= 1500:
       tier = "premium "
    elif balance >= 700 and balance <1500 :
       tier = "standard"
    elif balance >= 200 and  balance < 700 :
       tier = "basic"
    print(f"{name}: {tier} ({balance}ETB)")]




   





