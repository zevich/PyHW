def game(terra, power):
    for small_list in terra:
        for i in small_list:
            if power >= i:
                power = power+i
            else:
                break
    return (power)