
def createline(Lenght:int):
    line = []
    for i in range(Lenght):
        line.append('*' if i % 2 == 0 else '-')
        maxline = ''.join(line)
    
    print(maxline)

input_length = input("Please enter line length:")


createline(int(input_length))