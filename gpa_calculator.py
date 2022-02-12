# author: Steven De Jesus


# program description: This program is designed to
# calculate a semester's gpa by prompting users for their course, 
# credits, and letter grade by using dictionaries, strings 
# and string methods, loops, and functions, all within the same program.

# dictionary of grades
QUALITY_VALUES = {"A+": 4.00,
                  "A": 4.00,
                  "A-": 3.67,
                  "B+": 3.33,
                  "B": 3.00,
                  "B-": 2.67,
                  "C+": 2.33,
                  "C": 2.00,
                  "C-": 1.67,
                  "D+": 1.33,
                  "D": 1.00,
                  "D-": 0.67,
                  "F": 0.00}

# define main
def main():
    # call functions
    display_title()
    course_dictionary = get_courses()
    final_gpa = calculate_gpa(course_dictionary)
    display_grades(course_dictionary, final_gpa)
    print('Thank you for using My GPA Calculator!')

# function to display title
def display_title():
    print("----------------")
    print(" GPA Calculator ")
    print("----------------")

# function to get courses and return dictionary
def get_courses():
    course_info = {}

    # loop to get multiple inputs from user
    while True:
        # prompt user for inputs
        print('Submit your course Information below: ')
        course_id = input('Enter the course ID (e.g. CS021): ')
        course_id = course_id.upper()

        try:
            course_credits = float(input(f'How many credits is {course_id}?: '))
        except ValueError:
            print('Enter a number for your credits.')
            course_credits = float(input(f'How many credits is {course_id}?: '))

        try:
            course_grade = str(input(f'What letter grade did you get in {course_id}?: '))
            course_grade = course_grade.upper()
        except ValueError:
            print('Enter a letter for your grade.')
            course_grade = str(input(f'What letter grade did you get in {course_id}?: '))
            course_grade = course_grade.upper()
            

        # if course is not valid then ask for other input
        if course_grade not in QUALITY_VALUES:
            print("\nInvalid result grade")
            course_grade = input(f'What letter grade did you get in {course_id}?: ')

        try:
            # ask user if he wants to enter new course
            choice = input('\nWould you like to add new course?(y/n): ')
            choice = choice.lower()
        except ValueError:
            print('Wrong Value.\n')
            choice = input('Would you like to add new course?(y/n): ')
            choice = choice.lower()
            
        # add to the dictionary
        course_info[course_id] = (course_credits, course_grade)
        if choice == 'n':
            return course_info


# calculate credits and values for quality points
def calculate_quality_points(course_credits, letter_grade):
    return course_credits * QUALITY_VALUES[letter_grade]


# function to calculate GPA
def calculate_gpa(course_dictionary):
    total_credits = 0
    total_quality_points = 0
    # loop to go through dictionary
    for course in course_dictionary:
        # increment total credits
        total_credits += course_dictionary[course][0]
        # calculate quality points and increment total quality points
        total_quality_points += calculate_quality_points(course_dictionary[course][0], course_dictionary[course][1])
    # calculate GPA and return it
    GPA = total_quality_points/total_credits
    return GPA


# program to print display transcript
def display_grades(course_dictionary, GPA):
    print("-" * 30)
    # print grades
    print('\nFor the following courses: ')
    print('Course\t', 'Credits\t', 'Grade')
    print("-" * 30)

    # loop to print the courses
    for course in course_dictionary:
        print(f'{course}\t {course_dictionary[course][0]}\t {course_dictionary[course][1]}')
    print("-" * 30)
    # print GPA
    print(f'Your GPA is {GPA:.2f}.')


# call main function
if __name__ == '__main__':
    main()
