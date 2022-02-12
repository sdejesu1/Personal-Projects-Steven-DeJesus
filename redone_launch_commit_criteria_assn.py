# redone launch commit criteria assn
# define some constants for criteria
WIND_SPEED_CRITERIA = 35
VISIBILITY_CRITERIA = 4
CLOUD_CRITERIA = 4500
THUNDERSTORM_CRITERIA = 10
# Time import used for "real time" launch countdown import time
import time
# define main():
def main():
    # call display title
    display_title()
    # prompt users for information
    # wind speed
    wind_speed = float(input('Enter the current wind speed (mph): '))
    while wind_speed < 0:
        print('Wind speed cannot be negative.')
        wind_speed = float(input('Enter the current wind speed (mph): '))
    # visibility
    visibility = float(input('Enter current visibility (miles): '))
    while visibility < 0:
        print('Visibility cannot be negative.')
        visibility = float(input('Enter current visibility (miles): '))
    # cloud layer thickness
    cloud_thick = float(input('Enter maximum thickness of any current freezing cloud layer (ft): '))
    while cloud_thick < 0:
        print('Cloud thickness cannot be negative.')
        cloud_thick = float(input('Enter maximum thickness of any current freezing cloud layer (ft): '))
    # thunderstorm
    thunderstorm = float(input('Enter distance of the nearest thunderstorm, or a zero if no current storms (miles): '))
    while thunderstorm < 0:
        print('Thunderstorm distance cannot be negative.')   
        thunderstorm = float(input('Enter distance of the nearest thunderstorm, or a zero if no current storms (miles): '))
    # call process_criteria and pass user inputs
    process_criteria(wind_speed, visibility, cloud_thick, thunderstorm)

# define display_title():
def display_title():
    print('---------------------------------')
    print('Launch Commit Criteria - Falcon 9')
    print('---------------------------------')
# define process_criteria():
def process_criteria(wind_speed, visibility, cloud_thick, thunderstorm):
    if wind_speed > WIND_SPEED_CRITERIA:
        abort_message()
    elif visibility < VISIBILITY_CRITERIA:
        abort_message()
    elif cloud_thick > CLOUD_CRITERIA:
        abort_message()
    elif thunderstorm < THUNDERSTORM_CRITERIA and thunderstorm != 0:
        abort_message()
    else:
        success_message()
#  def abort_message():
def abort_message():
    print('\nLaunch Commit Criteria not satisfied. Aborting launch...')
# def success_message():
def success_message():
    for i in range(10, 0, -1):
        print(f't-minus: {i}')
        time.sleep(1)
    print('*** LIFTOFF ***')



# call main
if __name__ == '__main__':
    main()