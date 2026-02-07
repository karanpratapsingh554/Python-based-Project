def update_furniture(data_dict):
    """ Update the furniture data in the file. """
    try:
        with open('furniture.txt', 'w') as file:
            for key, value in data_dict.items():
                # Format: ID, Manufacturer, Product, Quantity, Price
                line = key + "," + value[0] + "," + value[1] + "," + str(value[2]) + "," + value[3] + "\n"
                file.write(line)
        print("Furniture data updated successfully.")
    except Exception as e:
        print("An error occurred while updating the furniture data: " + str(e))

def append_furniture(id, manufacturer, product, quantity, price):
    """ Append new furniture data to the file. """
    try:
        with open('furniture.txt', 'a') as file:
            # Format: ID, Manufacturer, Product, Quantity, Price
            line = id + "," + manufacturer + "," + product + "," + str(quantity) + "," + price + "\n"
            file.write(line)
        print("New furniture data added successfully.")
    except Exception as e:
        print("An error occurred while appending the furniture data: " + str(e))

def remove_furniture(id):
    """ Remove furniture data from the file. """
    try:
        # Read all lines from the file
        with open('furniture.txt', 'r') as file:
            lines = file.readlines()
        
        # Write back all lines except the one to be removed
        with open('furniture.txt', 'w') as file:
            for line in lines:
                if not line.startswith(id + ","):
                    file.write(line)
        print("Furniture with ID " + id + " removed successfully.")
    except Exception as e:
        print("An error occurred while removing the furniture data: " + str(e))
