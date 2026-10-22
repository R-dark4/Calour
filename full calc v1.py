import time
# Basic Energy cost calculator
def billing_period():
    while True:
        billing_p = input("\nWhat is your billing period: Monthly (m), Annual (a) or Specific (s): ")
        if billing_p == "s":

            billing_d =float(input("How many days is your billing period? "))
            if billing_d < 1:
                print("\nInvalid billing period, please enter a positive number.")
                billing_d = float(input("How many days is your billing period? "))

            return billing_d,billing_p
        elif billing_p == "m":
            billing_d = 30.0
            return billing_d,billing_p
        elif billing_p == "a":
            billing_d = 365.0
            return billing_d,billing_p
        else:
            print("Please enter a valid billing period, by entering m, a or s.")
        #print(billing_p, billing_d)

def electric_calc(billing_d, e_energy_u,e_unit_rate, e_standing_c):
    e_total_c = (e_energy_u * (e_unit_rate / 100)) + ((e_standing_c / 100) * billing_d)
    print("Your monthly electric energy costs are: £" + str(e_total_c) + "\n")
    return e_total_c


def gas_calc(billing_d, g_energy_u,g_unit_rate, g_standing_c):
    g_total_c = (g_energy_u * (g_unit_rate / 100)) + ((g_standing_c / 100) * billing_d)
    print("Your monthly gas energy costs are: £" + str(g_total_c) + "\n")
    return g_total_c


def energy_calc(e_total_c,g_total_c):
    total_c = e_total_c + g_total_c
    print("\nYour monthly energy costs are: £" + str(total_c))
    return total_c

def compare_b(total_c):
    new_bill = int(input("What is the cost of your new bill?: "))
    bill_difference = new_bill - total_c
    percent_difference = bill_difference / total_c * 100
    print("\nThe difference in your bills is: " + str(bill_difference) +
          "\nThat is a" + str(percent_difference) + "% difference.")
    return percent_difference, bill_difference

def annual_estimate_e(ed_energy_u,e_unit_rate,e_standing_c ):
    a_total_c = ed_energy_u * ((e_unit_rate / 100) * 365)
    print("NOTE: THIS IS ONLY AN ESTIMATE, NOT A GUARANTEE!!")
    print("Your annual energy costs are: £" + str(a_total_c) + "\n")
    return a_total_c

def annual_estimate():
    a_total_c = a_energy_u * ((a_unit_rate / 100) * 365)
    print("NOTE: THIS IS ONLY AN ESTIMATE, NOT A GUARANTEE!!")
    print("Your annual energy costs are: £" + str(a_total_c) + "\n")
    return a_total_c

while True:
    print("----------Calor----------")
    print("\nOptions:")
    print("1. Calculate electricity bill")
    print("2. Calculate gas bill")
    print("3. Compare bills")
    print("5. Estimate yearly energy cost")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        billing_d,billing_p = billing_period()
        e_energy_u = float(input("\nWhat is your electric energy usage? in KWh: "))
        e_unit_rate = float(input("What is your electric unit rate? in pence: "))
        e_standing_c = float(input("What is your electric standing charge? in pence : "))
        electric_calc(billing_d, e_energy_u, e_unit_rate, e_standing_c)

    elif choice == "2":
        billing_d,billing_p = billing_period()
        g_energy_u = float(input("\nWhat is your gas energy usage? in KWh: "))
        g_unit_rate = float(input("What is your gas unit rate? in pence: "))
        g_standing_c = float(input("What is your gas standing charge? in pence : "))
        gas_calc(billing_d, g_energy_u, g_unit_rate, g_standing_c)

    elif choice == "3":
        break

    elif choice == "4":
        a_energy_u = float(input("\nWhat is your daily electric average energy usage? in KWh: "))
        a_unit_rate = float(input("What is your electric unit rate? in pence: "))
        a_standing_c = float(input("What is your electric standing charge? in pence : "))
        annual_estimate_e(a_energy_u, a_unit_rate, a_standing_c)

    elif choice == "5":
        print("Thank you for using this program")
        break

    else:
        print("Please enter a valid choice, by entering 1, 2, 3 or 4")