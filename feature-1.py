samans_str = input()
samans_str = samans_str.lower()
don_use = ''
use_num = ''
for i in range(0, len(samans_str)):
    if samans_str[i] == 'a' or samans_str[i] == 'e' or samans_str[i] == 'o' or samans_str[i] == 'i' or samans_str[i] == 'u':
        don_use += samans_str[i]
    else:
        use_num += '.' + samans_str[i]
print (use_num)