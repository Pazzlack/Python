def create_array(arr_length:int)->list:
    my_array = []
    for i in range (arr_length):
        my_line = i*'*'
        my_array.append(my_line)
    return my_array

def print_array(arr:list):
    for line in (arr):
        print(line)
input_length = input("Please enter array length:")
arr_length = int(input_length) 

my_array = create_array(arr_length)
print_array(my_array)