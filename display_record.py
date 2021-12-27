#	Option ‘2’: Display item(s)

# Module for functions on pathnames.
import os.path

#def DI():

# Main function for loading inventory file and display all record list.
def option_2():

    # Create a new / loading an existing inventory file.
    inventory_file = input("Please enter an inventory name: ")

    # Exists()in the os.path module  is used with if structure to test
    # whether a file exists or not.
    if os.path.exists(inventory_file):
        print(inventory_file, "exisits in the currect directory.\n")

    # Load readdata function.
    read_data(inventory_file)

# Readdata function for display all existing record details.
def read_data(inventory_file):

    # Open an inventory file.
    infile = open(inventory_file, "r")

    # Load field data record_number in the 1st record.
    record_number = infile.readline()

    # If a field was load, continue processing.
    while record_number != "":

        # Get each data(9) from the inventory.
        item_name = infile.readline()
        item_number = infile.readline()
        category = infile.readline()
        quantity = infile.readline()
        weight = infile.readline()
        recipient = infile.readline() 
        final_destination = infile.readline()
        delivery_status = infile.readline()
        new_Line = infile.readline()

        # Display record details.
        print("Record number:", record_number, end = "")
        print("Item name:", item_name, end = "")
        print("Item number:", item_number, end = "")
        print("Category:", category, end = "")
        print("Quantity:", quantity, end = "")
        print("Weight:", weight, end = "")
        print("Recipient:", recipient, end = "")
        print("Final destination:", final_destination, end = "")
        print("Delivery status:", delivery_status, end = "")
        print(new_Line, end = "")

        # Load the record_number field of next record.
        record_number = infile.readline()

    print("All record detail has been displaying.")
    # Close the file.
    infile.close()

