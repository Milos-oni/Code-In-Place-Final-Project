# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    years = float(input("Enter an age in calendar years: "))
    dog_age = years * DOG_YRS_MULTIPLIER
    print(f"That's {round(dog_age)} in dog years!")
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()