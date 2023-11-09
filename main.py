#### COS
## mr yusuf

print("MR YUSUF AND SONS")
print("Enter the required information to calculate simple and compound interest respectively")
initial_principal = float(input("Enter your initial principal:   "))
interest_rate = float(input("Enter your initial rate:   "))
number_of_times_interests_per_time_period = float(input("Enter number of times interests per time period:   "))
number_of_time_period_elapsed = float(input("Enter number of time period elapsed:   "))

simple_interest = initial_principal *(1+interest_rate*number_of_times_interests_per_time_period)
compound_interest = initial_principal *(1+(interest_rate/number_of_time_period_elapsed))**number_of_time_period_elapsed*number_of_times_interests_per_time_period

print("YUSUF AND SONS COMPANY")
print(f'Simple interest : {simple_interest}')
print(f'Compound interest : {compound_interest}')