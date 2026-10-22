# Basic Energy cost calculator
def billing_period():
    billing_p = input("What is your billing period: Monthly (m), Annual (a) or Specific (s): ")
    if billing_p == "s":
        billing_d =float(input("How many days is your billing period? "))
    elif billing_p == "m":
        billing_d = 30.0
    else:
        billing_d = 365.0
    return billing_d,billing_p

def electric_calc(billing_d):
    e_energy_u = float(input("What is your electric energy usage? in KWh: "))
    e_unit_rate = float(input("What is your electric unit rate? in pence: "))
    e_standing_c = float(input("What is your electric standing charge? in pence : "))
    e_total_c = (e_energy_u * (e_unit_rate / 100)) + ((e_standing_c / 100) * billing_d)
    print("Your monthly electric energy costs are: £" + str(e_total_c))
    return e_total_c

def gas_calc(billing_d):
    g_energy_u = float(input("\nWhat is your gas energy usage? in KWh: "))
    g_unit_rate = float(input("What is your gas unit rate? in pence: "))
    g_standing_c = float(input("What is your gas standing charge? in pence : "))
    g_total_c = (g_energy_u * (g_unit_rate / 100)) + ((g_standing_c / 100) * billing_d)
    print("Your monthly gas energy costs are: £" + str(g_total_c))
    return g_total_c

def energy_calc(e_total_c,g_total_c):
    total_c = e_total_c + g_total_c
    print("\nYour monthly energy costs are: £" + str(total_c))
    return total_c
#bill comparer
def compare_b(total_c):
    new_bill = int(input("What is the cost of your new bill?: "))
    bill_difference = new_bill - total_c
    percent_difference = bill_difference / total_c * 100
    print("\nThe difference in your bills is: " + str(bill_difference) +
          "\nThat is a" + str(percent_difference) + "% difference.")
    return percent_difference, bill_difference

# x = True
# while x:
#     billing_d, billing_p =billing_period()
#     e_total_c = electric_calc(billing_d)
#     g_total_c = gas_calc(billing_d)
