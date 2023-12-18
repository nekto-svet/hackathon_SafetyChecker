from country import Country
from news import News

# This is a version of meny for console using


def first_menu():
    print (
        '''
            You can chek safety status of one contry (print '1')\n
            Or you can compare countries by their safety(print '2')\n
            For Exit (print 'E')
        '''
    )
def user_first_imput():
    user_first_answer = input(' ').capitalize().strip()
    return user_first_answer


def user_second_input():
    user_second_answer = input('Print a country here or print "E" for the Main Menu:   ')
    if user_second_answer.strip().capitalize() == 'E':
        print('            You are in the Main Menu.\n\n')
        main()
    else:
        country = user_second_answer.strip().lower().capitalize()
        return country


def user_third_input():
    user_third_answer = input('Print two countries here separated by comma or print "E" for the Main Menu:   ')
    if user_third_answer.capitalize().strip() == 'E':
        print('\n            You are in the Main Menu.\n')
        main()
    else:
        countries = user_third_answer.split(',')
        return countries

    
def second_menu():
    print (
        '''
            You can compare this country with another by their safety (print 'C')
            For Main Menu (print 'E')
        '''
    )
    user_fourth_answer = input(' ').capitalize().strip()
    return user_fourth_answer


def user_fifth_input():
    user_fifth_answer = input ('            With what contry do you want to compare?\n')
    return user_fifth_answer.capitalize().strip()    
    

def main():
    while True:
        # shows the first menu
        first_menu()
        # takes the first users input
        user_first_answer = user_first_imput()
        if user_first_answer == '1':
            # takes the second user input with one country
            user_second_answer = user_second_input()
            # takes information from Objects
            curr_country = Country(user_second_answer)
            news = News(curr_country)
            print('\n')
            print(curr_country.info())
            print(news.get_text())
            # askes if user whants to compare or return
            user_fourth_answer = second_menu()
            if user_fourth_answer == 'E':
                print('\n            You are in the Main Menu.\n')
                main()
            elif user_fourth_answer == 'C':       
                # askes with what user wants to compare
                user_fifth_answer = user_fifth_input()
                second_country = Country(user_fifth_answer)
                print('\n')
                print(curr_country.compare_threat(second_country))
                main()
            
        
        elif user_first_answer == '2':
            # takes a users input with two countries
            countries = user_third_input()
            country_one = countries[0].strip().lower().capitalize()
            country_two = countries[1].strip().lower().capitalize()
            # takes an information from the object Country
            country_obj1 = Country(country_one)
            country_obj2 = Country(country_two)
            print('\n')
            print(country_obj1.compare_threat(country_obj2))
            main()

        elif user_first_answer == 'E':
            break
        else:
            print('Not clear request, try again')

# Tis funktion works just one time to say hello
def action():
    print ('\n            Hello, traveler!')
    main()

action()


