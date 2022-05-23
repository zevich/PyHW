def cost_delivery(quantity:int, *_, discount=0):
    """Функция возвращает общую сумму доставки.

    Первый параметр quantity  количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0.
    """ 
    result = (5 + 2 * (quantity-1))*(1-discount)
    return result