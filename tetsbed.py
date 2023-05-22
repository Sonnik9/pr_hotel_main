beds = "1 twin bed and 1 queen bed and 3 litle big"
count_beds = 0
flagOr = False

try:
    bedOr = beds.split(' ')

    for orr in bedOr:
        if orr == 'or':
            orFind = beds.split('or')[1]
            flagOr = True
            break
    if flagOr == True:
        for fnd in orFind:
            try:
                count_beds += int(fnd)
            except:
                continue
    else:
        for orr in bedOr:
            try:
               count_beds += int(orr)
            except:
                continue
except:
    pass

