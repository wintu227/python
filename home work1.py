print("hello world!")
total_bill = float( input("enter the total bill amount(ETB): " ))
people_count = int ( input("enter the number of people splitting the bill: " ))
def split_bill(total,people,tip_rate= 0.10):
    total_with_tip = total *(1 + tip_rate)
    share_per_person  = total_with_tip / people
    return share_per_person
indivisual_share = split_bill(total_bill, people_count) 
friends  =  [ "liya","abenzer","fiker","eleshaday"]
for name in friends:
    print (f"{name}:{indivisual_share}ETB")
