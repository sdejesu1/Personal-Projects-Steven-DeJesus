# author: steven De Jesus
# assignment: solar farms (practice)
# also practice functions as well
# cs021 green

# constants
PROFIT_RATE = 0.19

# define main function which calls other functions
def main():
    continue_var = True
    while continue_var == True:
        display_intro()
        
        main_280_watts, main_320_watts, main_sun_hours, main_num_weeks = take_inputs()
        
        total_kwh, total_profit = calculate_kwh_per(main_280_watts, main_320_watts, main_sun_hours, main_num_weeks)
        
        display_data(total_kwh, total_profit, main_num_weeks)
        
        continue_var = run_again()

# define display_intro
def display_intro():
    print('***********************')
    print('Solar Farm Power Output')
    print('***********************', '\n')
    
    
# define take_inputs
def take_inputs():
    # 280 watts input
    watts_280 = int(input('Enter the number of 280 watt solar panels: '))
    while watts_280 < 0:
        print('Enter a valid number (positive!)')
        watts_280 = int(input('Enter the number of 280 watt solar panels: '))

    # 320 watts input
    watts_320 = int(input('Enter the number of 320 watt solar panels: '))
    while watts_320 < 0:
        print('Enter a valid number (positive!)')
        watts_320 = int(input('Enter the number of 320 watt solar panels: '))

    # sunlight hours input
    sun_hours = float(input('Enter the number of hours of sunlight the panels receive per day: '))
    while sun_hours < 0 or sun_hours > 24:
        print('Invalid value, hours must be between 0 and 24')
        sun_hours = float(input('Enter the number of hours of sunlight the panels receive per day: '))

    # number of weeks input
    num_weeks = int(input('Enter the number of weeks to calculate the total power output: '))
    while num_weeks <= 0:
        print('Invalid value. Number of weeks must be above zero to be considered.')
        num_weeks = int(input('Enter the number of weeks to calculate the total power output: '))

    return watts_280, watts_320, sun_hours, num_weeks

# define calculate_kwh_per
def calculate_kwh_per(calc_watts_280, calc_watts_320, calc_sun_hours, calc_num_weeks):
    kwh_per_week_280 = ((calc_watts_280 * 280 * calc_sun_hours) / 1000) * 7

    kwh_per_week_320 = ((calc_watts_320 * 320 * calc_sun_hours) / 1000) * 7

    total_kwh_per_week = kwh_per_week_280 + kwh_per_week_320
    total_profit = PROFIT_RATE * total_kwh_per_week * calc_num_weeks
    
    return total_kwh_per_week, total_profit


# define dislay_data
def display_data(total_kwh, total_profit, data_num_weeks):
    i = 1
    print('\n')
    print('Week\tRunning Total')
    print('=====================')
    while i <= data_num_weeks:
        print(f'{i}\t{total_kwh * i:,.0f} kWh')
        i += 1
    print('\n')
    print(f'Total profit over {data_num_weeks} weeks: ${total_profit:,.2f}')

# define run_again
def run_again():
    continue_scenario = input('Would you like to run another scenario? (y/n): ')
    while continue_scenario != 'y' and continue_scenario != 'n':
        print('Wrong answer, choose y or n')
        continue_scenario = input('Would you like to run another scenario? (y/n): ')
    if continue_scenario == 'y':
        return True
    elif continue_scenario == 'n':
        return False

# run main
if __name__ == '__main__':
    main()