def print_multiplys(num: int):
    print("Here are the multiplys of", num)
    for i in range(num):
        curr_multiply = i + 1
        if num % curr_multiply == 0:
            print(curr_multiply)

def main():
    num = int(input("Enter a number: "))
    print_multiplys(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()