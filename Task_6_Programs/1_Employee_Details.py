# Write a python program to manage multiple employee details.
# Enter employee detail like name, mobile, email, birthdate, position, city
# Enter all that detail into dictionary and store that dictionary into a list until nothing is added.
# Example : [{‘name’:’Bhaskar’, ’mobile’:’987’},{}]
# Keep adding dictionary into list with new employee data.
# Print the employee detail into a tabular format given below.

employee = []
while True:
    name = input("\nEnter the name of the employee:- ")
    if not name:
        break

    mobile = input(f"Enter the mobile number of {name}:- ")
    email = input(f"Enter the email of {name}:- ")
    birthdate = input(f"Enter the birthdate of {name}:- ")
    position = input(f"Enter the position of {name}:- ")
    city = input(f"Enter the city of {name}:- ")
    dct = {
        'name' :  name,
        'mobile' :  mobile,
        'email' :  email,
        'birthdate' : birthdate,
        'position' :  position,
        'city' :  city 
        }
    employee.append(dct)

print(f"\n{'Name':<15}{'Mobile':<15}{'Email':<25}{'Birthdate':<20}{'Position':<15}{'City':<15}")
print("-"*100)

for emp in employee:
    print(f"{emp['name']:<15}{emp['mobile']:<15}{emp['email']:<25}{emp['birthdate']:<20}{emp['position']:<15}{emp['city']:<15}")
