# Allows user to input the arrows dimensions and assigns the value to the associated variables
print ('Enter arrow base height: ')
arrow_base_height = int(input())
   
print ('Enter arrow base width: ')
arrow_base_width = int(input())
   
print ('Enter arrow head width: ')
arrow_head_width = int(input())

""" If the user input for the arrows head is less then the arrows base then prompts 
the user to reneter the head width and runs until proper operand is entered """
while arrow_head_width <= arrow_base_width:
    print('Enter arrow head width: ')
    arrow_head_width = int(input())
    
""" Iteration starts with the variable l being assigned a value by the range function tied to the 
variable arrow_base_height, l is further processed by appending the existing value with the string '*', multiplied by the variable 
arrow_base_width to it's current value and then prints l forming the arrows shaft height and width """
for l in range (arrow_base_height):
    l = ('*' * arrow_base_width)
    print(l)

""" Iteration starts with the variable m being assigned a value by the range function tied to the 
variable arrow_head_width, m is further processed by appending the existing value with the string * multiplied by the variable 
arrow_head_width to it's current value and then prints m forming the arrows head first then with each range iteration forms the rest 
of the body followed by the arrows tip"""
for m in range(arrow_head_width):
    m = '*' * arrow_head_width
    print (m)
    arrow_head_width = arrow_head_width - 1
