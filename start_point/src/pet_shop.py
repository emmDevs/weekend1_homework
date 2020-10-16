def get_pet_shop_name(pet_shop_info):
    return pet_shop_info["name"]

def get_total_cash(pet_shop_info):
    return pet_shop_info["admin"]["total_cash"]

# def add_or_remove_cash(pet_shop_info, cash_to_add_or_remove):
#     new_total_cash = (pet_shop_info["admin"] ["total_cash"]) + cash_to_add_or_remove
#     return new_total_cash

def get_pets_sold(pet_shop_info):
    return pet_shop_info["admin"]["pets_sold"]