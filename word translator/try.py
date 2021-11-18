import googletrans  # hi ek library ahet jyat goole translator mplemented ahe.
dict1 = googletrans.LANGUAGES  # return karel dictionary saglya supported languages chi
dict2 = {}
count = 0

for items in dict1.items():     # key ani value swap kele, i.e. key la value kel ani value la key of dict1
    if(items[0]=='hi'):         # hindi jaga sodhayla aplyala lagnare
        print(count)
    dict2[items[1]] = items[0]
    count+=1

print(dict1)
print(dict2)