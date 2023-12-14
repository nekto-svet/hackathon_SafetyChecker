


def first_menu():
    print (
        '''
            Hello, traveler!\n
            You can chek safety status of one contry (print '1')\n
            Or you can compare countries by their safety(print '2')
        '''
    )

def user_first_imput():
    user_first_answer = input(' ').strip()
    return user_first_answer

def second_menu():
    print (
        '''
            What country do you want to check?\n
            Now you can check USA, Franse, Russia, Yemen
        '''
    )

def user_second_input():
    user_second_answer = input('Print a country here:    ')
    country = user_second_answer.lower().capitalize().strip()
    return country


def main():
    first_menu()
    user_first_answer = user_first_imput()
    if user_first_answer == '1':
        user_second_answer = second_menu()
        show_one_coutry(user_second_answer)
    elif user_first_answer == '2':
        show_all_countries()
