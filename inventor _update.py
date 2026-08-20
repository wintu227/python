def update_inventory(filename):
    inventory  = {}
    try:
        with open(filename,"r") as file:
           for line in file:
               product, quantity =line.strip().split(",")
               inventory[product] = int(quantity)
        print("current inventory:")
        for product, quantity in inventory.items():
            print(product,":",quantity)
        product = input("\nEnter the product you want to update: ")
        if product not in inventory:
            print("product does not exist.")
            return 
        try:
            new_quantity = int(input("Enter the new quantity: "))
            if new_quantity < 0 : 
                print("quantity cannot be negative.")
                return 
        except ValueError : 
            print("Invalid quantity.please enter a number.")
            return     
        inventory[product] = new_quantity
        with open("inventory_update.txt", "w")as file : 
            for product ,quanity in inventory.items():
              file.write(f"{product},{quantity}\n")
        print("Inventory updated successfully!")
    except FileNotFoundError:
         print("The inventory file was not found.")
update_inventory("inventory.txt")
                 

            