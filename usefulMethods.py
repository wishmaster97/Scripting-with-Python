from collections import Counter, defaultdict, OrderedDict

string = "Abhijeet Sawankumar Tedle"
string1 = Counter(string)


for x, y in string1.items():
    if y>=2:
        print(x)