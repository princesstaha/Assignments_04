def print_multiples(num: int):
    print("Here are the multiples of", num)
    for i in range(1,num+1):
       print(i*2)

def main():
    num = int(input("Enter a number: "))

    print_multiples(num)
   


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()