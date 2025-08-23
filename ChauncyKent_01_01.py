# Defines the set_message function and its arguments.
def set_message(tickets):
    """Takes in the number of tickets as an argument and returns the 
    appropriate message for the next customer.

    args:
    tickets = An integer representing the number of tickets remaining.
    """
    # Initializes the message variable with an empty string.
    message = ''
    # Evaluates the number of tickets remaining. If 4 or more remain, 
    # The first message is used, otherwise the second is used.
    if tickets >= 4:
        message = 'How many tickets would you like? You may purchase up to 4. '
    else:
        message = f'How many tickets would you like? You may purchase up to {tickets}. '

    # Returns the designated message as a string.
    return message
# Defines the set_max_ticks function and its arguments.
def set_max_ticks(tickets):
    """Takes in the number of tickets as an argument and returns the
    appropriate maximum number of tickets the next customer may buy.

    args:
    tickets = An integer representing the number of tickets remaining.
    """
    # Initializes the max_tickets variable and sets its value to 4.
    max_tickets = 4
    # Evaluates the number of remaining tickets and sets max_tickets to 
    # the remaining value if it is lower than 4.
    if tickets < 4:
        max_tickets = tickets

    # Returns max_tickets as an integer.
    return max_tickets

# Defines the buy_ticks function and its arguments.
def buy_ticks(tickets):
    """Takes in the number of tickets as an argument and returns the 
    number of tickets purchased by the customer.

    args:
    tickets = An integer representing the number of tickets remaining.
    """
    # Calls the set_message function to set an appropriate message for 
    # the next customer.
    message = set_message(tickets)
    # Calls the set_max_ticks function to set an appropriate value for 
    # the maximum number of tickets each customer may purchase.
    max_ticks = set_max_ticks(tickets)
    
    # Starts an input validation loop.
    while True:
        # Takes initial input from the customer.
        order = input(message)
        # Attempts to convert the customer's input to an integer. If 
        # there is an error, prints a message and restarts the loop.
        try:
            int(order)
        except:
            print('Please enter a number')
            continue

        # Evaluates the customer input to see if it's within the 
        # allowable range. If not prints a message and restarts the 
        # loop. Otherwise returns the value of order.
        if int(order) > max_ticks or int(order) < 1:
            print(f'Please enter a number between 1 and {max_ticks}.')
            continue
        else:
            return int(order)
        
# Defines the main function.
def main():
    """The main function where initial variable values are established 
    and helper functions are called.
    """
    # Initializes the tickets variable with a value of 20.
    tickets = 20
    # Initializes the customers variable with a value of 0.
    customers = 0

    # Starts a loop that runs until there are no more tickets.
    while tickets > 0:
        # On each loop, subtracts the number of tickets bought from 
        # the total.
        tickets -= buy_ticks(tickets)
        # On each loop, adds 1 to the number of customers.
        customers += 1
    
    # Displays the total number of customers.
    print(f'Total number of customers: {customers}')
        
if __name__ == '__main__':
    main()
