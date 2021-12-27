# Main function for loading inventory file and create record list.

# Module for functions on pathnames.
import os.path

#    Option ‘1’: Add new item record(s)
def option_1():
    
    # Create a new / loading an existing inventory file.
    inventory_file = input("Please enter an inventory name: ")

    # Exists()in the os.path module  is used with if structure to test
    # whether a file exists or not.
    if os.path.exists(inventory_file):
        print(inventory_file, "exisits in the currect directory")

    # Load writedata function.
    write_data(inventory_file)

# Writedata function for input record details.
def write_data(inventory_file):

    # Set a constant data of 9.
    # Record_number(0), item_name(1), item_number(2), category(3),
    # quantity(4), weight(5), recipient(6), final_destination(7),
    # delivery_status(8).
    ##data = 9

    # Create a list for each data(9).
    ##record = [0] * data

    # Create a variable to hold an index.
    ##index = 0

    # Get each data(9) to the list.
    # Again for add other new record.
    again = "y"

    while again == "y":

        # Open an inventory file.
        outfile = open(inventory_file, "a")

        # Input data by user.
        record_number = int(input("Please enter New Record Number: "
                              +"(1001-1050)\n"))

        # If input nothing or space or out of range (1001-1050),
        # request search another record detail.
        while record_number == "" or record_number > 1050 or record_number < 1001:

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
                
            record_number = int(input("Please enter New Record Number: "
                              +"(1001-1050)\n"))
                              
        # Write the record of details to the file.
        outfile.write(str(record_number) + "\n")

        item_name = input("Please enter New Item Name: "
                              +"(Maximum Numbers of Characters = 40)\n")
        # If input nothing or space or more than 40 characters,
        # request search another record detail.
        while item_name == "" or item_name[0] == " " or len(item_name) > 40:

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
                
            item_name = input("Please enter New Item Name: "
                              +"(Maximum Numbers of Characters = 40)\n")

        outfile.write(str(item_name) + "\n")
               
        item_number = int(input("Please enter New Item Number: "))
        outfile.write(str(item_number) + "\n")
               
        category = input("Please enter New Category: ")
        outfile.write(str(category) + "\n")

        quantity = int(input("Please enter New Quantity: "))
        outfile.write(str(quantity) + "\n")

        weight = float(input("Please enter New Weight: "))
        outfile.write(str(weight) + " kg\n")

        recipient = input("Please enter New Recipient: "
                              +"(Maximum Numbers of Characters = 40)\n")

        # If input nothing or space or more than 40 characters,
        # request search another record detail.
        while recipient == "" or recipient[0] == " " or len(recipient) > 40:

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
                
            recipient = input("Please enter New Recipient: "
                              +"(Maximum Numbers of Characters = 40)\n")

        outfile.write(str(recipient) + "\n")

        final_destination = input("Please enter New Final Destination: "
                              +"(Maximum Numbers of Characters = 40)\n")

        # If input nothing or space or more than 40 characters,
        # request search another record detail.
        while final_destination == "" or final_destination[0] == " " or len(final_destination) > 40:

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
                
            final_destination = input("Please enter New Final Destination: "
                              +"(Maximum Numbers of Characters = 40)\n")

        outfile.write(str(final_destination) + "\n")

        delivery_status = input("Please enter New Delivery Status: "
                              +"(Maximum Numbers of Characters = 40)\n")

        # If input nothing or space or more than 40 characters,
        # request search another record detail.
        while delivery_status == "" or delivery_status[0] == " " or len(delivery_status) > 40:

            print("Wrong input, please try again.")
            #"Sorry, no any relevent record in this inventory."
                
            delivery_status = input("Please enter New Delivery Status: "
                              +"(Maximum Numbers of Characters = 40)\n")
        
        outfile.write(str(delivery_status) + "\n\n")

        # Close the file.
        outfile.close()

        # Again for add other new record.
        again = input("Do you want to add another new item record? (y/n): ")
