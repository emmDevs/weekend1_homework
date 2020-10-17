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

# def get_pets_by_breed(pet_shop_info, breed_type):
#     pets = []
#     for pet in pet_shop_info:
#         for breed in pet:
#             if pets[2] == breed_type:
#                 pets.append((pet_shop_info["pets"]["name"]))
#     return pets
