def getFileContent():
    """ Read the furniture data from the file and return as a dictionary. """
    furniture_dict = {}
    try:
        with open('furniture.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Remove trailing newline and split by comma
                parts = line[:-1].split(',') if line.endswith('\n') else line.split(',')
                if len(parts) == 5:
                    id, manufacturer, product, quantity, price = parts
                    furniture_dict[id] = [manufacturer, product, quantity, price]
    except FileNotFoundError:
        print("The furniture data file is missing.")
    return furniture_dict
