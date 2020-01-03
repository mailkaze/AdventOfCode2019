pass_min = 136818
pass_max = 685979
valid_pass = []

for num in range(pass_min, pass_max):
    # convertimos el numero en una lista de integers
    lst_pass = [int(x) for x in str(num)]
    duplicate = False
    for i in range(len(lst_pass)-1):
        # comprobamos si los digitos no decrecen
        if lst_pass[i] <= lst_pass[i+1]:
            increasing = True
        else:
            increasing = False
            break
        # comprobamos si hay duplicados seguidos
        if lst_pass[i] == lst_pass[i+1]:
            duplicate = True
    if increasing and duplicate: valid_pass.append(num)
        
print(len(valid_pass))
