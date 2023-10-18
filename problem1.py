def get_instructions(filename):

    with open(filename) as file:

        print(file.read())

get_instructions("input1.txt")
