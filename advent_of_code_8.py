pass_min = 136818
pass_max = 685979
valid_pass = []

def check_duplicates(lst):
    if ((lst[0] == lst[1] and lst[0] != lst[2]) or
        (lst[1] == lst[2] and lst[1] != lst[3] and lst[1] != lst[0]) or
        (lst[2] == lst[3] and lst[2] != lst[4] and lst[2] != lst[1]) or
        (lst[3] == lst[4] and lst[3] != lst[5] and lst[3] != lst[2]) or
        (lst[4] == lst[5] and lst[4] != lst[3])): 
        return True

for num in range(pass_min, pass_max):
    # convertimos el numero en una lista de integers
    lst_pass = [int(x) for x in str(num)]
    duplicate_just_once = False
    for i in range(len(lst_pass)-1):
        # comprobamos si los digitos no decrecen
        if lst_pass[i] <= lst_pass[i+1]:
            increasing = True
        else:
            increasing = False
            break
        # comprobamos si hay duplicados seguidos
        duplicate_just_once = check_duplicates(lst_pass)
    if increasing and duplicate_just_once: valid_pass.append(num)
        
print(len(valid_pass))
#print(valid_pass)
