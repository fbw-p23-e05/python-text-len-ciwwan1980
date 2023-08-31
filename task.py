# ## Task
# Write a program that detects if a string has an even/odd number of characters and prints "even" or "odd" accordingly.


# ## Input --> Output
# ```
# "hello world"     -->    "odd"  
# "hello planet"    -->    "even"  
# ""                -->    "even"  
# ```


# input_string = input("Enter the string you want: ")

# if len(input_string) % 2 == 0:
#     print(f'"{input_string}" length is even')
# else:
#     print(f'"{input_string}" length is odd')


while True:
    letter = input("Enter the character you want: ")

    if len(letter) % 2 == 0:
        print(letter, "length is even")
    else:
        print(letter, "length is odd")

    break  # This break statement should be inside the loop if you want to exit after one iteration
