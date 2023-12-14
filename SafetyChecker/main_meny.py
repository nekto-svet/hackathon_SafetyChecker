from country import Country


def first_menu():
    print (
        '''
            You can chek safety status of one contry (print '1')\n
            Or you can compare countries by their safety(print '2')\n
            For Exit (print 'E')
        '''
    )

def user_first_imput():
    user_first_answer = input(' ').strip()
    return user_first_answer

def second_menu():
    print (
        '''
            What country do you want to check?\n
        '''
    )

def user_second_input():
    user_second_answer = input('Print a country here or print "E" for exit:   ')
    if user_second_answer.strip().capitalize() == 'E':
        print('            You are in the main menu.\n\n')
        main()
    else:
        country = user_second_answer.strip().lower().capitalize()
        return country


def user_third_input():
    user_third_answer = input('Print two countries here separated by commaor print "E" for exit:   ')
    if user_third_answer.capitalize().strip() == 'E':
        print('\n            You are in the main menu.\n')
        main()
    else:
        countries = user_third_answer.split(',')
        return countries


def third_menu():
    pass

def main():
    while True:
        first_menu()
        user_first_answer = user_first_imput()
        if user_first_answer == '1':
            user_second_answer = user_second_input()
            curr_country = Country(user_second_answer)
            print('\n')
            curr_country()
            main()
            return curr_country
        
        elif user_first_answer == '2':
            countries = user_third_input()
            country_one = countries[0].strip().lower().capitalize()
            country_two = countries[1].strip().lower().capitalize()
            print (country_one, country_two)
            country_obj1 = Country(country_one)
            country_obj2 = Country(country_two)
            print('\n')
            main()

        elif user_first_answer == 'E':
            break
        else:
            print('Not clear request, try again')

def action():
    print ('\n            Hello, traveler!')
    main()

action()


