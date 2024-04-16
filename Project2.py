def main():
    customer_code = input("Enter customer code (R, C, or I): ").upper()
    if customer_code not in ['R', 'C', 'I']:
        print("Invalid input (customer code)")
        print_summary(customer_code, 0, 0, 0, 0)
        return
    begin_reading = int(input("Beginning meter reading (between 0 and 999999999): "))
    end_reading = int(input("Ending meter reading (between 0 and 999999999): "))
    if not (0 <= begin_reading <= 999999999 and 0 <= end_reading <= 999999999):
        print("Invalid input (beginning or ending reading value is out of the range)")
        print_summary(customer_code, begin_reading, end_reading, 0, 0)
        return
    gallons_used = compute_gallons(begin_reading, end_reading)
    amount_billed = compute_amount_billed(customer_code, gallons_used)
    print_summary(customer_code, begin_reading, end_reading, gallons_used, amount_billed)

def compute_gallons(begin_reading, end_reading):
    gallons_used = (end_reading - begin_reading) / 10.0
    return gallons_used

def compute_amount_billed(customer_code, gallons_used):
    if customer_code == 'R':
        amount_billed = 5.00 + (0.0005 * gallons_used)
    elif customer_code == 'C':
        if gallons_used <= 4000000:
            amount_billed = 1000.00
        else:
            additional_gallons = gallons_used - 4000000
            amount_billed = 1000.00 + (0.00025 * additional_gallons)
    elif customer_code == 'I':
        if gallons_used <= 4000000:
            amount_billed = 1000.00
        elif gallons_used <= 10000000:
            amount_billed = 2000.00
        else:
            additional_gallons = gallons_used - 10000000
            amount_billed = 2000.00 + (0.00025 * additional_gallons)
    return round(amount_billed, 2)


def print_summary(customer_code, begin_reading, end_reading, gallons_used, amount_billed):
    print("Customer code:", customer_code)
    print("Beginning meter reading:", "{:0>9}".format(begin_reading))
    print("Ending meter reading:", "{:0>9}".format(end_reading))
    print("Gallons of water used:", gallons_used)
    print("Amount billed:", "${:.2f}".format(amount_billed))


if __name__ == "__main__":
    main()
