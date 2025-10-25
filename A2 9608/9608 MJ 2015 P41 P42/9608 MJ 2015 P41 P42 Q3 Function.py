def CalculateDiscount(GoodsTotal, HasDiscountCard):
    if GoodsTotal > 100 and HasDiscountCard:
        return 10
    elif GoodsTotal > 100:
        return 5
    elif GoodsTotal > 20 and HasDiscountCard:
        return 5
    else:
        return 0
GoodsTotal = 110 #INTEGER
HasDiscountCard = True  #BOOLEAN
print("The discount on your purchase is", CalculateDiscount(GoodsTotal, HasDiscountCard))