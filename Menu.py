from ast import arg
from datetime import datetime
from Capsule import Capsule
from Time import Time
from LinkedList import LinkedList

class Menu:
    def __init__(self) -> None:
        self.capsule_list = LinkedList()
        now_time = datetime.now()
        self.now = Time(now_time.month, now_time.day, now_time.year)



    def check_if_int(self, var):
        try:
            int(var)  # see if year can be cast to int
            return var
        except ValueError:  # if it cant, set year to 0 and print error message 
            print('You must enter a valid integer')
            return '0'


    def create_capsule(self):
        print('You will now enter the date you wish for the capsule to be unlocked.\n')
        year = month = day = '0'

        while(len(year) != 4 or int(year) < 2022 or int(year) > 2300):  # check that input is 4 digits and between 2022 and 2300
            year = input('Enter a year up to 2300 (4 digits)\n')
            year = self.check_if_int(year)

        while(len(month) != 2 or int(month) < 1 or int(month) > 12):  # check that input is 2 digits and between 1 and 12
            month = input('Enter month (2 digits)\n')
            month = self.check_if_int(month)

        while(len(day) != 2 or int(day) < 1 or int(day) > 31):  # check that input is 2 digits and between 1 and 31 
            day = input('Enter day (2 digits)\n')
            day = self.check_if_int(day)

        label = ''
        while len(label) < 1 or len(label) > 25:
            label = input('Enter label between 1-25 characters\n')

        note = input('Enter note\n')

        t = Time(month, day, year)
        c = Capsule(t, note, label, self.now)
        self.capsule_list.add_capsule(c, self.now)


    def view_unlocked_capsules(self):
        print('These are all of the unlocked capsules:`')
        self.capsule_list.show_all_notes(self.now)

    
    def view_locked_capsules(self):
        print('These are the locked capsules:\n')
        self.capsule_list.show_all_labels(self.now)


    def find_capsule(self):
        choice = '0'
        while int(choice) < 1 or int(choice) > 3:
            choice = input('How would you like to search?\n\
                            1: Search by label\n\
                            2: Search by date\n\
                            3: Cancel search\n')
            choice = self.check_if_int(choice)
        if int(choice) == 1:
            self.capsule_list.label_search(self.now)
        elif int(choice) == 2:
            pass
        else:
            print('Returning to main menu...')


    def close_program(self):
        print('Closing Program...')


    def choice_not_found(self):
        print('\nUser input did not correspond to any choices given')


    def main(self):
        user_input = '0'
        while(int(user_input) != 10):
            user_input = input('Please select one of the following:\n\
            1: Create time capsule message\n\
            2: View unlocked messages\n\
            3: View locked capsules\n\
            4: Find capsule\n\
            10: Close Program\n')

            user_input = self.check_if_int(user_input)  # check if user input is an int

            # create options for functions users can call
            
            options = {
                1: self.create_capsule,
                2: self.view_unlocked_capsules,
                3: self.view_locked_capsules,
                4: self.find_capsule,
                10: self.close_program,
            }
            options.get(int(user_input), self.choice_not_found)()

m = Menu()
m.main()
