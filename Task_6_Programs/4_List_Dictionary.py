
# Add a dictionaries from user in such a way to get below output.Merge keys of dictionary and manage values accordingly
# Lst =[
# {52: {'march': 1, 'may': 2, 'june': 3, 'july': 1, 'feb': 0, 'aug': 2, 'jan': 0, 'april': 5, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {52: {'march': 0, 'may': 0, 'june': 0, 'july': 0, 'feb': 0, 'aug': 0, 'jan': 0, 'april': 0, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {51: {'march': 0, 'may': 1, 'june': 0, 'july': 0, 'feb': 8, 'aug': 0, 'jan': 0, 'april': 2, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {48: {'march': 0, 'may': 0, 'june': 4, 'july': 0, 'feb': 0, 'aug': 0, 'jan': 0, 'april': 3, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {48: {'march': 0, 'may': 0, 'june': 0, 'july': 0, 'feb': 4, 'aug': 0, 'jan': 1, 'april': 0, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}}]

# Result :
# Use this list of dictionaries to get below output.

# Result =[
# {52: {'march': 1, 'may': 2, 'june': 3, 'july': 1, 'feb': 0, 'aug': 2, 'jan': 0, 'april': 5, 'November': 2, 'dec': 0, 'sept': 0, 'oct': 0}},
# {51: {'march': 0, 'may': 1, 'june': 0, 'july': 0, 'feb': 8, 'aug': 0, 'jan': 0, 'april': 2, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
# {48: {'march': 0, 'may': 0, 'june': 4, 'july': 0, 'feb': 4, 'aug': 0, 'jan': 1, 'april': 3, 'November': 2, 'dec': 0, 'sept': 0, 'oct': 0}},
# }]

# Add the value of each month and create group by 52,51,48
lst = []
months = ['january','febrary','march','april','may','june','july','august','September','October','November','December']

while True:

    key = input("Enter the key:- ")
    if not key:
        break

    value = {}

    for month in months:
        value1 = int(input(f"Enter the value for {month}:- "))
        value[month] = int(value1)

    lst.append({int(key): value})

print("Origingal list of dictionaries:- ",lst)
    
merged_dict = {}

for item in lst:
    for key,value in item.items():
        if key not in merged_dict:
            merged_dict[key] = value
        else:
            for month in value:
                merged_dict[key][month] += value[month]

merged_lst = [{k : v} for k,v in merged_dict.items()]

print("Merged list is :- ", merged_lst)
    
