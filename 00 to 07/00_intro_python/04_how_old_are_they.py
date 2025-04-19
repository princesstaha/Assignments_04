def main():
    sania : int = 21  # Sania's age is given as 21 years old
    sidra : int = 6 + sania  # Sidra is 6 years older than Sania, so add 6 to Sania's age to get Sidra's
    arbish : int = 20 + sidra  # Arbish is 20 years older than Sidra, so add 20 to Sidra's age to get Arbish's
    tanzeela  : int= arbish + sania  # Tanzeela is as old as Arbish's age plus Sania's age, so add them together
    unzeela : int = arbish  # Unzeela is the same age as Arbish, so set Unzeela's age equal to Arbish's

   # Print out all of the ages!
    print("Sania is " + str(sania))
    print("Sidra is " + str(sidra))
    print("Arbish is " + str(arbish))
    print("Tanzeela is " + str(tanzeela))
    print("Unzeela is " + str(unzeela))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()