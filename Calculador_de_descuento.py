def calculate_discount(price, discount_percentage):
    
    discount_amount = price * discount_percentage / 100
    result = price - discount_amount
    final_price = round(result, 2)
    return final_price
