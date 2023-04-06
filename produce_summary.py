def watermelons(day, the_file):
    """Use the day and the text file that day uses
        to create delivery reports
    """

    print("Day:", day)

    delivery_data = open(the_file)


 # For loop over each line
    for line in delivery_data: 
        line = line.rstrip()  # Remove extra whitespace to the right of the line (REVIEW .rstrip()!!!)
        words = line.split('|')  # Creates list of strings
        
        # each item in list assigned to a variable
        melon = words[0]
        count = words[1]
        amount = words[2]

        # list unpacking (REVIEW)

        # Print/Console Log 
        print(f"Delivered {count} {melon}s for total of ${amount}")

watermelons(1, "um-deliveries-day-1.txt")
watermelons(2, "um-deliveries-day-2.txt")
watermelons(3, "um-deliveries-day-3.txt")