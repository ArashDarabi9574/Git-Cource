import hashlib
import csv
from collections import OrderedDict
with open('/home/adn/Documents/git-Cource/a.csv') as reader:
    reader = csv.reader(reader)
    mydict = OrderedDict()
    dict_res = OrderedDict()
    for i in range(9999):
        hashlib_result = hashlib.sha256(str(i).encode())
        mydict [hashlib_result.hexdigest()] = i
    for j in reader:
        our_name = j[0]
        our_hashlib = j[1]
        short_cut = mydict.keys()
        for key in short_cut:
            if our_hashlib == key:
                dict_res[our_name] = mydict.get(key)
with open('/home/adn/Documents/git-cource/1.csv', 'w') as result:
        this_counter = 0
        for i in dict_res:
            this_counter += 1
            if this_counter == 1:
                result.write(i + ',' + str(dict_res.get(i)))
            else:
                result.write('\n' + i + ',' + str(dict_res.get(i)))