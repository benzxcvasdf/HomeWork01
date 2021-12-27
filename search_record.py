#	Option ‘3’: Search item information

# Main function for loading inventory file and search & display specific
# record list.
def option_3():

    # Module for functions on pathnames.
    import os.path

    # Create a new / loading an existing inventory file.
    inventory_file = input("Please enter an inventory name: ")

    # Exists()in the os.path module  is used with if structure to test
    # whether a file exists or not.
    if os.path.exists(inventory_file):
        print(inventory_file, "exisits in the currect directory.")
    print("")

    # Load readdata function.
    search_data(inventory_file)

# Readdata function for search & display specific and existing
# record details.
def search_data(inventory_file):

    # Again for add other new record.
    again = "y"

    while again == "y":

        # Open an inventory file.
        infile = open(inventory_file, "r")

        # Search for single word and list all match details.
        ##for line in infile:
        ##    if "r" in line:
        ##        print(line)
        ##infile.close()

        # Output all lines of record detail in search_details.
        search_details = infile.readlines()

        # Input key record detail.
        search_record_number = input("What record do you want to read? ")
        
        # If input nothing or space, request search another record.
        while search_record_number == "" or int(search_record_number) > 1050 or int(search_record_number) < 1001 :

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
            
            search_record_number = input("What record do you want to read? ")

        # The l means of line number, output 1 search_detail to line in
        # loop each time. 
        for l, line in enumerate(search_details):

            # If search_detail belong to Record number.
            if (l % 10 == 0): 

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l], end = "")
                    print("Item name:", search_details[l+1], end = "")
                    print("Item number:", search_details[l+2], end = "")
                    print("Category:", search_details[l+3], end = "")
                    print("Quantity:", search_details[l+4], end = "")
                    print("Weight:", search_details[l+5], end = "")
                    print("Recipient:", search_details[l+6], end = "")
                    print("Final destination:", search_details[l+7], end = "")
                    print("Delivery status:", search_details[l+8], end = "")
                    print(search_details[l+9], end = "")

            #If search_detail belong to Item name.
            elif (l % 10 == 1):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-1], end = "")
                    print("Item name:", search_details[l], end = "")
                    print("Item number:", search_details[l+1], end = "")
                    print("Category:", search_details[l+2], end = "")
                    print("Quantity:", search_details[l+3], end = "")
                    print("Weight:", search_details[l+4], end = "")
                    print("Recipient:", search_details[l+5], end = "")
                    print("Final destination:", search_details[l+6], end = "")
                    print("Delivery status:", search_details[l+7], end = "")
                    print(search_details[l+8], end = "")

            #If search_detail belong to Item number.
            elif (l % 10 == 2):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-2], end = "")
                    print("Item name:", search_details[l-1], end = "")
                    print("Item number:", search_details[l], end = "")
                    print("Category:", search_details[l+1], end = "")
                    print("Quantity:", search_details[l+2], end = "")
                    print("Weight:", search_details[l+3], end = "")
                    print("Recipient:", search_details[l+4], end = "")
                    print("Final destination:", search_details[l+5], end = "")
                    print("Delivery status:", search_details[l+6], end = "")
                    print(search_details[l+7], end = "")

            #If search_detail belong to Category.
            elif (l % 10 == 3):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-3], end = "")
                    print("Item name:", search_details[l-2], end = "")
                    print("Item number:", search_details[l-1], end = "")
                    print("Category:", search_details[l], end = "")
                    print("Quantity:", search_details[l+1], end = "")
                    print("Weight:", search_details[l+2], end = "")
                    print("Recipient:", search_details[l+3], end = "")
                    print("Final destination:", search_details[l+4], end = "")
                    print("Delivery status:", search_details[l+5], end = "")
                    print(search_details[l+6], end = "")

            #If search_detail belong to Quantity.
            elif (l % 10 == 4):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-4], end = "")
                    print("Item name:", search_details[l-3], end = "")
                    print("Item number:", search_details[l-2], end = "")
                    print("Category:", search_details[l-1], end = "")
                    print("Quantity:", search_details[l], end = "")
                    print("Weight:", search_details[l+1], end = "")
                    print("Recipient:", search_details[l+2], end = "")
                    print("Final destination:", search_details[l+3], end = "")
                    print("Delivery status:", search_details[l+4], end = "")
                    print(search_details[l+5], end = "")

            #If search_detail belong to Weight.
            elif (l % 10 == 5):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-5], end = "")
                    print("Item name:", search_details[l-4], end = "")
                    print("Item number:", search_details[l-3], end = "")
                    print("Category:", search_details[l-2], end = "")
                    print("Quantity:", search_details[l-1], end = "")
                    print("Weight:", search_details[l], end = "")
                    print("Recipient:", search_details[l+1], end = "")
                    print("Final destination:", search_details[l+2], end = "")
                    print("Delivery status:", search_details[l+3], end = "")
                    print(search_details[l+4], end = "")

            #If search_detail belong to Recipient.
            elif (l % 10 == 6):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-6], end = "")
                    print("Item name:", search_details[l-5], end = "")
                    print("Item number:", search_details[l-4], end = "")
                    print("Category:", search_details[l-3], end = "")
                    print("Quantity:", search_details[l-2], end = "")
                    print("Weight:", search_details[l-1], end = "")
                    print("Recipient:", search_details[l], end = "")
                    print("Final destination:", search_details[l+1], end = "")
                    print("Delivery status:", search_details[l+2], end = "")
                    print(search_details[l+3], end = "")

            #If search_detail belong to Final destination.
            elif (l % 10 == 7):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-7], end = "")
                    print("Item name:", search_details[l-6], end = "")
                    print("Item number:", search_details[l-5], end = "")
                    print("Category:", search_details[l-4], end = "")
                    print("Quantity:", search_details[l-3], end = "")
                    print("Weight:", search_details[l-2], end = "")
                    print("Recipient:", search_details[l-1], end = "")
                    print("Final destination:", search_details[l], end = "")
                    print("Delivery status:", search_details[l+1], end = "")
                    print(search_details[l+2], end = "")

            #If search_detail belong to Delivery status.
            elif (l % 10 == 8):

                # If the line of search_detail match with search_record_number.
                if search_record_number in line:

                    # Print 9 details and 1 space line
                    ##for record_detail in search_details[l:l+10]:
                    ##    print(record_detail, end = "")
                    print("\nRecord number:", search_details[l-8], end = "")
                    print("Item name:", search_details[l-7], end = "")
                    print("Item number:", search_details[l-6], end = "")
                    print("Category:", search_details[l-5], end = "")
                    print("Quantity:", search_details[l-4], end = "")
                    print("Weight:", search_details[l-3], end = "")
                    print("Recipient:", search_details[l-2], end = "")
                    print("Final destination:", search_details[l-1], end = "")
                    print("Delivery status:", search_details[l], end = "")
                    print(search_details[l+1], end = "")

            #If search_detail belong to space line.
            else:
                
                pass

        # Close the file.
        infile.close()

        # Again for search other new record.
        again = input("Do you want to search another item record? (y/n): ")
        print("")





