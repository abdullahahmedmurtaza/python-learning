from typing import List
def print_table_list(n : int) -> List:
    l_tables : List = [n*i for i in range(1,11)] 
    return l_tables

table : List = print_table_list(4)
print(table)


with open ('tables.txt', 'w') as f:
    f.write(str(table))