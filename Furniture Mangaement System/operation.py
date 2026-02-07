import read
import write
import datetime
def show_furniture(dic):
    """ Display available furniture with proper alignment. """
    print("*" * 80)
    print("ID   Manufacturer                  Product                         Quantity     Price")
    print("-" * 80)
    for key, value in dic.items():
        # Format and display each line correctly
        print("{:<5} {:<30} {:<30} {:>10} {:>10}".format(key, value[0], value[1], value[2], value[3]))
    print("*" * 80)



def sell_furniture():
    dic = read.getFileContent()
    show_furniture(dic)
    
    transactions = []
    total_amount = 0
    while True:
        try:
            furniture_id = input("Enter the ID of the furniture you want to sell: ")
            if furniture_id in dic:
                quantity = int(input("Enter the quantity to sell: "))
                
                if quantity > 0 and quantity <= int(dic[furniture_id][2]):
                    # Update inventory
                    dic[furniture_id][2] = str(int(dic[furniture_id][2]) - quantity)
                    write.update_furniture(dic)
                    
                    # Calculate item total
                    item_total = float(dic[furniture_id][3].replace('$', '').replace(',', '')) * quantity
                    total_amount += item_total
                    
                    # Record transaction
                    transactions.append({
                        'id': furniture_id,
                        'quantity': quantity,
                        'item_total': item_total,
                        'details': dic[furniture_id]
                    })
                    
                    # Ask if more items to sell
                    more_items = input("Do you want to sell more items? (yes/no): ").lower()
                    if more_items != 'yes':
                        break
                else:
                    print("Invalid quantity. Please enter a quantity between 1 and available stock.")
            else:
                print("Invalid ID. Please enter a valid furniture ID.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")
    
    # Determine the type of transaction
    transaction_type = input("Is this purchase by an employee or customer? (employee/customer): ").lower()
    
    if transaction_type == 'employee':
        employee_name = input("Enter the name of the employee: ")
        
        # Generate invoice for each transaction
        for transaction in transactions:
            generate_employee_invoice(
                transaction['id'],
                transaction['quantity'],
                transaction['item_total'],
                transaction['details'],
                employee_name
            )
    elif transaction_type == 'customer':
        customer_name = input("Enter the name of the customer: ")
        
        # Ask for shipping cost and generate final invoice
        shipping_cost = float(input("Enter the shipping cost (0 if not applicable): "))
        vat = 0.13 * total_amount
        final_total = total_amount + vat + shipping_cost

        # Generate invoice for each transaction
        for transaction in transactions:
            generate_customer_invoice(
                transaction['id'],
                transaction['quantity'],
                transaction['details'][3],
                transaction['item_total'],
                transaction['details'],
                customer_name
            )

        # Generate final invoice
        generate_final_invoice(
            total_amount,
            shipping_cost,
            vat,
            final_total
        )
    else:
        print("Invalid transaction type. Please enter 'employee' or 'customer'.")

def generate_employee_invoice(furniture_id, quantity, item_total, details, employee_name):
    """ Generate invoice for an employee transaction. """
    invoice_filename = "Employee_Invoice_" + furniture_id + "_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    with open(invoice_filename, "w") as file:
        file.write("*" * 60 + "\n")
        file.write("Furniture Purchase Invoice (Employee)\n")
        file.write("*" * 60 + "\n")
        file.write("ID: " + furniture_id + "\n")
        file.write("Manufacturer: " + details[0] + "\n")
        file.write("Product: " + details[1] + "\n")
        file.write("Quantity Sold: " + str(quantity) + "\n")
        file.write("Price per Unit: " + details[3] + "\n")
        file.write("Total Price: $" + "{:.2f}".format(item_total) + "\n")
        file.write("Employee Name: " + employee_name + "\n")
        file.write("Date and Time: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
        file.write("Thank you for your purchase!\n")
    print("Employee Invoice generated: " + invoice_filename)

def generate_customer_invoice(furniture_id, quantity, price_per_unit, item_total, details, customer_name):
    """ Generate invoice for a customer transaction. """
    invoice_filename = "Customer_Invoice_" + furniture_id + "_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    with open(invoice_filename, "w") as file:
        file.write("*" * 60 + "\n")
        file.write("Furniture Purchase Invoice (Customer)\n")
        file.write("*" * 60 + "\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("ID: " + furniture_id + "\n")
        file.write("Manufacturer: " + details[0] + "\n")
        file.write("Product: " + details[1] + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Price per Unit: " + price_per_unit + "\n")
        file.write("Total Price (excluding shipping): $" + "{:.2f}".format(item_total) + "\n")
    print("Customer Invoice generated: " + invoice_filename)

def generate_final_invoice(total_amount, shipping_cost, vat, final_total):
    """ Generate the final invoice summarizing all transactions. """
    final_invoice_filename = "Final_Invoice_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    with open(final_invoice_filename, "w") as file:
        file.write("*" * 60 + "\n")
        file.write("Final Purchase Invoice\n")
        file.write("*" * 60 + "\n")
        file.write("Total Amount (before VAT and shipping): $" + "{:.2f}".format(total_amount) + "\n")
        file.write("Shipping Cost: $" + "{:.2f}".format(shipping_cost) + "\n")
        file.write("VAT (13%): $" + "{:.2f}".format(vat) + "\n")
        file.write("Total Amount to be Paid: $" + "{:.2f}".format(final_total) + "\n")
        file.write("Date and Time: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
        file.write("Thank you for your purchase!\n")
    print("Final Invoice generated: " + final_invoice_filename)

# Example usage
if __name__ == "__main__":
    sell_furniture()
