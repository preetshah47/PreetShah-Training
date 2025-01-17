# 7. Write a python program to determine if the switch is on or off,
#     - use the given truth table for checking values and showing results.
# --------------------------------------------
# main_input    input1    input2    result
# --------------------------------------------
# 0           	0            0           0
# 0           	0            1           0
# 0           	1            0           0
# 0           	1            1           0
# 1           	0            0           0
# 1           	0            1           1
# 1           	1            0           1
# 1           	1            1           1

def switch(main_input,input1,input2):
    if main_input == 0:
        return main_input
    else:
        if input1 == 0 and input2 == 0:
            return input1
        else:
            return main_input

main_input,input1,input2 = list(map(int, input("Enter multiple numbers separated by space: ").split()))
result = switch(main_input,input1,input2)
print (result)