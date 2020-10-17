def get_pet_shop_name(pet_shop_info):
    return pet_shop_info["name"]

def get_total_cash(pet_shop_info):
    return pet_shop_info["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_info, cash_to_add_or_remove):
    pet_shop_info["admin"]["total_cash"] += cash_to_add_or_remove
    

def get_pets_sold(pet_shop_info):
    return pet_shop_info["admin"]["pets_sold"]

def increase_pets_sold(pet_shop_info, number_pets_sold):
    pet_shop_info["admin"]["pets_sold"] += number_pets_sold

def get_stock_count(pet_shop_info):
    stock = len(pet_shop_info["pets"])
    return stock 

def get_pets_by_breed(pet_shop_info, breed_type):
    breed_list = []
    for pet in pet_shop_info["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list

def find_pet_by_name(pet_shop_info, pet_name):
    for pet in pet_shop_info["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop_info, pet_name):
    for pet in pet_shop_info["pets"]:
        if pet["name"] == pet_name:
            pet_shop_info["pets"].remove(pet)
       
def add_pet_to_stock(pet_shop_info, new_pet):
    pet_shop_info["pets"].append(new_pet)

def get_customer_cash(customers):
    for customer in customers:
        return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash
    
