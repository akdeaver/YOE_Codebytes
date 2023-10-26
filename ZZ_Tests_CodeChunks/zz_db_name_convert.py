
entry_data = "db_1687829425_1687790678_46_98011A77-5970-40A4-A8E9-B29D8A7A6330"

name = entry_data.split('_')

'''
for parts in name:
    n = len(parts)
    if n == 10:
        print(parts)
'''

for count, parts in enumerate(name):
    n = len(parts)
    if n == 10 and count == 1:
        print('stop_time ' + parts)
    elif n == 10 and count == 2:
        print('stop_time ' + parts)