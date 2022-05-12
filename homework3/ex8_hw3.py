def cost_delivery(quantity:int, *_, discount=0):
    #if quantity>1:
    sum = (5+(quantity-1)*2)*(1-discount)
    return(sum)