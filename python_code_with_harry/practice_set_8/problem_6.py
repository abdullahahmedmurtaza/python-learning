def inches_to_cms(inches):
    if(inches ==0):
        return 0
    return inches * 2.54

print(f'Given length in cms is : {round(inches_to_cms(12),2)}')