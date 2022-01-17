n = int(input())

regular_list = set()
vip_list = set()

for _ in range(n):
    res_number = input()
    if res_number[0].isdigit():
        vip_list.add(res_number)
    else:
        regular_list.add(res_number)

guest = input()
while guest != 'END':
    if guest[0].isdigit():
        vip_list.remove(guest)
    else:
        regular_list.remove(guest)
    guest = input()

print(len(regular_list) + len(vip_list))
if vip_list:
    print('\n'.join(sorted(vip_list)))
if regular_list:
    print('\n'.join(sorted(regular_list)))


