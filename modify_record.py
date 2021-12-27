#	Option ‘4’: Modify item record(s)

# Main function for loading inventory file and search & modify specific
# record list.
def option_4():

    # Module for functions on pathnames.
    import os.path

    # Create a new / loading an existing inventory file.
    inventory_file = input("Please enter an inventory name: ")

    # Exists()in the os.path module  is used with if structure to test
    # whether a file exists or not.
    if os.path.exists(inventory_file):
        print(inventory_file, "exisits in the currect directory.")
    print("")

    # Load modify_data function.
    modify_data(inventory_file)

# Readdata function for search & modify specific and existing
# record details.
def modify_data(inventory_file):

    # Again for add other new record.
    again = "y"

    while again == "y":

        # Open an inventory file.
        overfile = open(inventory_file, "r")

        # Search for single word and list all match details.
        ##for line in overfile:
        ##    if "r" in line:
        ##        print(line)
        ##overfile.close()

        # Output all lines of record detail in search_details.
        search_details = overfile.readlines()

        # Input key record detail.
        search_record_number = input("Which record do you want to modify?"
                                     + " (only accept record number)\n")

        # If input nothing or space, request search another record detail.
        while search_record_number == "" or search_record_number[0] == " ":

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
            
            search_record_number = input("Which record do you want to modify?"
                                     + " (only accept record number)\n")

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
                    s_l = l

            #If search_detail belong to others.
            else:
                
                pass

        # Close the file.
        overfile.close()


        # Continue for modify other record details in the same record.
        modify_continue = "y"

        while modify_continue == "y":

            # Input key record detail.
            modify_record_detail = input("Which record detail do you want to modify?"
                                         + " (accept other without record number)\n")

            # If input nothing or space, request modify another record detail.
            while modify_record_detail == "" or modify_record_detail[0] == " ":

                print("Wrong input, please try again.")
                #"Sorry, no any relevent record detail in this record."
                    
                modify_record_detail = input("Which record detail do you want to modify?"
                                             + " (accept other without record number)\n")

            # If need to modify item name.
            if modify_record_detail.lower() == "item name":

                # Input new data in old relevant line of detail.
                search_details[s_l+1] = input("Please enter Item name: "
                              +"(Maximum Numbers of Characters = 40)\n")
                search_details[s_l+1] = str(search_details[s_l+1]) + "\n"
                
                # If input nothing or space or more than 40 characters,
                # request search another record detail.
                while search_details[s_l+1] == "" or search_details[s_l+1][0] == " " or len(search_details[s_l+1]) > 40:

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+1] = input("Please enter Item name: "
                              +"(Maximum Numbers of Characters = 40)\n")
                    search_details[s_l+1] = str(search_details[s_l+1]) + "\n"

            # If need to modify item number.
            elif modify_record_detail.lower() == "item number":

                # Input new data in old relevant line of detail.
                search_details[s_l+2] = int(input("Please enter Item number: "))
                search_details[s_l+2] = str(search_details[s_l+2]) + "\n"
                
                # If input nothing or space, request modify another record detail.
                while search_details[s_l+2] == "" or search_details[s_l+2][0] == " ":

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+2] = int(input("Please enter Item number: "))
                    search_details[s_l+2] = str(search_details[s_l+2]) + "\n"

            # If need to modify category.
            elif modify_record_detail.lower() == "category":

                # Input new data in old relevant line of detail.
                search_details[s_l+3] = input("Please enter Category: ")
                search_details[s_l+3] = str(search_details[s_l+3]) + "\n"
                
                # If input nothing or space, request modify another record detail.
                while search_details[s_l+3] == "" or search_details[s_l+3][0] == " ":

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+3] = input("Please enter Category: ")
                    search_details[s_l+3] = str(search_details[s_l+3]) + "\n"

            # If need to modify quantity.
            elif modify_record_detail.lower() == "quantity":

                # Input new data in old relevant line of detail.
                search_details[s_l+4] = input("Please enter Quantity: ")
                search_details[s_l+4] = str(search_details[s_l+4]) + "\n"
                
                # If input nothing or space, request modify another record detail.
                while search_details[s_l+4] == "" or search_details[s_l+4][0] == " ":

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+4] = input("Please enter Quantity: ")
                    search_details[s_l+4] = str(search_details[s_l+4]) + "\n"

            # If need to modify weight.
            elif modify_record_detail.lower() == "weight":

                # Input new data in old relevant line of detail.
                search_details[s_l+5] = float(input("Please enter Weight: "))
                search_details[s_l+5] = str(search_details[s_l+5]) + " kg\n"
                
                # If input nothing or space, request modify another record detail.
                while search_details[s_l+5] == "" or search_details[s_l+5][0] == " ":

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+5] = float(input("Please enter Weight: "))
                    search_details[s_l+5] = str(search_details[s_l+5]) + " kg\n"

            # If need to modify recipient.
            elif modify_record_detail.lower() == "recipient":

                # Input new data in old relevant line of detail.
                search_details[s_l+6] = input("Please enter Recipient: "
                              +"(Maximum Numbers of Characters = 40)\n")
                search_details[s_l+6] = str(search_details[s_l+6]) + "\n"
                
                # If input nothing or space or more than 40 characters,
                # request search another record detail.
                while search_details[s_l+6] == "" or search_details[s_l+6][0] == " " or len(search_details[s_l+6]) > 40:

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+6] = input("Please enter Recipient: "
                              +"(Maximum Numbers of Characters = 40)\n")
                    search_details[s_l+6] = str(search_details[s_l+6]) + "\n"

            # If need to modify final destination.
            elif modify_record_detail.lower() == "final destination":

                # Input new data in old relevant line of detail.
                search_details[s_l+7] = input("Please enter Final destination: "
                              +"(Maximum Numbers of Characters = 40)\n")
                search_details[s_l+7] = str(search_details[s_l+7]) + "\n"
                
                # If input nothing or space or more than 40 characters,
                # request search another record detail.
                while search_details[s_l+7] == "" or search_details[s_l+7][0] == " " or len(search_details[s_l+7]) > 40:

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+7] = input("Please enter Final destination: "
                              +"(Maximum Numbers of Characters = 40)\n")
                    search_details[s_l+7] = str(search_details[s_l+7]) + "\n"

            # If need to modify delivery status.
            elif modify_record_detail.lower() == "delivery status":

                # Input new data in old relevant line of detail.
                search_details[s_l+8] = input("Please enter Delivery status: "
                              +"(Maximum Numbers of Characters = 40)\n")
                search_details[s_l+8] = str(search_details[s_l+8]) + "\n"
                
                # If input nothing or space or more than 40 characters,
                # request search another record detail.
                while search_details[s_l+8] == "" or search_details[s_l+8][0] == " " or len(search_details[s_l+8]) > 40:

                    print("Wrong input, please try again.")
                    #"Sorry, no any relevent record in this inventory."
                    
                    search_details[s_l+8] = input("Please enter Delivery status: "
                              +"(Maximum Numbers of Characters = 40)\n")
                    search_details[s_l+8] = str(search_details[s_l+8]) + "\n"

            #If get error??
            else:

                pass

            # Open an inventory file.
            overfile = open(inventory_file, "w")

            # Rewrite all lines of record detail from search_details.
            overfile.writelines(search_details)

            # Close the file.
            overfile.close()

            # Continue for modify other record details in the same record.
            modify_continue = input("Do you want to modify another detail in this record? (y/n): ")
            print("")

        # Again for search other new record.
        again = input("Do you want to search another item record? (y/n): ")
        print("")
