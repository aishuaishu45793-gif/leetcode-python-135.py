try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) >= 2:
        print("Second largest number:", unique_numbers[-2])
    else:
        print("There is no second largest distinct number.")

except ValueError:
    print("Invalid input! Please enter integers only.")