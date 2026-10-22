# Basic Energy cost calculator
billing_p = input("What is your billing period: Monthly (m), Annual (a) or Specific (s): ")
if billing_p == "s":
    billing_d =float(input("How many days is your billing period? "))
elif billing_p == "m":
    billing_d = 30.0
else:
    billing_d = 365.0

e_energy_u = float(input("What is your electric energy usage? in KWh: "))
e_unit_rate = float(input("What is your electric unit rate? in pence: "))
e_standing_c = float(input("What is your electric standing charge? in pence : "))
e_total_c = (e_energy_u* (e_unit_rate/100)) + ((e_standing_c/100) * billing_d)
print("Your monthly electric energy costs are: £" + str(e_total_c))


g_energy_u = float(input("\nWhat is your gas energy usage? in KWh: "))
g_unit_rate = float(input("What is your gas unit rate? in pence: "))
g_standing_c = float(input("What is your gas standing charge? in pence : "))
g_total_c = (g_energy_u* (g_unit_rate/100)) + ((g_standing_c/100) * billing_d)
print("Your monthly gas energy costs are: £" + str(g_total_c))

total_c = e_total_c + g_total_c
print("\nYour monthly energy costs are: £" + str(total_c))