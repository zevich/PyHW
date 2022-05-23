def amount_payment(payment):
    sum = 0
    for i in payment:
        if i > 0:
            sum = sum + i
    return (sum)