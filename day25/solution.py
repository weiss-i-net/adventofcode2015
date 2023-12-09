first_box = 20151125

i = 2978 - 1 # zero indexed
j = 3083 - 1

base = 252533
mod = 33554393

power = (i+j) * (i+j+1) // 2 + j # cantor pairing function

def mod_power(i):
    if i == 0:
        return 1
    return mod_power(i//2)**2 * base**(i%2) % mod

print(first_box * mod_power(power) % mod)
