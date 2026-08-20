
shopping = ["bread","milk","eggs"]
shopping.append("coffee")
shopping.insert(1,"sugar")
shopping.remove("milk")
shopping.sort()
print(shopping)


numbers =  [1,2,2,3,4,4,5,5]
unique =set(numbers)
print(unique)
hana_fav_food  = { "shiro","doro","tibis","burger"}
eyuel_fav_food  = { "burger","pizza","tibis","kolo"}
all_fav_food = hana_fav_food.union(eyuel_fav_food)
print(all_fav_food) 
common_fav_food = hana_fav_food.intersection(eyuel_fav_food)
print(common_fav_food)
difference1 = hana_fav_food.difference(eyuel_fav_food)
print(difference1)


