def mul_table(num):
    """
    Function prints the multiplication table of the passed number
    :param num: number whose table is to be generated
    :return: None
    """

    print("Entered number : ", num)

    # table from 1 -> 10, syntax of range (<start>, <end>, <step>)
    for i in range(1, 11, 1):
        print("{0} * {1} = {2}".format(num, i, num*i))



print("Hello from import")
print(__name__)

if __name__ == '__main__':
    num = input("Enter a number >> ")
    print(type(num))  # to get data type of the variable, it is a string

    # cast string to int and pass to function
    num_int = int(num)

    # pass the integer to the function
    mul_table(num_int)



