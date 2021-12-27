# Module for functions on pathnames.
import os.path

def option_5():
# input the file name
    inventory_file = input("Please enter an inventory name: ")
# confirm file presence
    if os.path.exists(inventory_file):
        print(inventory_file, "exisits in the currect directory.")
    print("")
    
    delete_record (inventory_file)

def delete_record (inventory_file):
    
    again = "y"
      
    while again == "y":
        
        infile = open(inventory_file, "r+")
#       Load field data delete_details
        delete_details = infile.readlines()
        
#        input delete item number.
        delete_number = input("What record do you want to delete? ")
        
#       confirm delete item number is correct.
        
        while delete_number == "" or int(delete_number) > 1050 or int(delete_number) < 1001 :
                
                    print ("Wrong input, please try again.")
                    delete_number = input("What record do you want to read? ")
#       find the delete item record.
        for X, data in enumerate(delete_details):
            
            if delete_number in data:
                print("\nRecord number:", delete_details[X], end = "")
                print("Item name:", delete_details[X+1], end = "")
                print("Item number:", delete_details[X+2], end = "")
                print("Category:", delete_details[X+3], end = "")
                print("Quantity:", delete_details[X+4], end = "")
                print("Weight:", delete_details[X+5], end = "")
                print("Recipient:", delete_details[X+6], end = "")
                print("Final destination:", delete_details[X+7], end = "")
                print("Delivery status:", delete_details[X+8], end = "")
                print(delete_details[X+9], end = "")
                
                confirm = input("Please confirm this information (y/n)")
                
#               confirm delete item record yes/no.
                if confirm == "y" or confirm == "Y":
                
#               delete item record
                    delete_details[X] = " "
                    delete_details[X+1] = " "
                    delete_details[X+2] = " "
                    delete_details[X+3] = " "
                    delete_details[X+4] = " "
                    delete_details[X+5] = " "
                    delete_details[X+6] = " "
                    delete_details[X+7] = " "
                    delete_details[X+8] = " "
                    delete_details[X+9] = " "
                    infile.seek(0,0)
                    infile.writelines(delete_details)
                        
#       Close the file.
        infile.close()
#       confirm delete another item record yes/no.
        again = input("Do you want to delete another item record? (y/n): ")
        print("")
