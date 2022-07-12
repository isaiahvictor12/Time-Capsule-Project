from datetime import datetime
from Time import Time

class Capsule:
    def __init__(self, date_unlocked, label, note, now) -> None:
        self.date_written = now
        self.date_unlocked = date_unlocked
        self.label = label
        self.note = note
        self.next = None

        # returns true when capsule has unlock date before the time given
    def is_before(self, other_time):
        return self.date_unlocked.total_time <= other_time.total_time
        # if(now.year > unlock.year):
        #     return True
        # elif(now.year < unlock.year):
        #     return False
        # else:
        #     if(now.month > unlock.month):
        #         return True
        #     elif(now.month < unlock.month):
        #         return False
        #     else:
        #         if(now.day >= unlock.day):
        #             return True
        #         else:
        #             return False
    
    def print_note(self, now):
        if self.is_before(now):
            print(f'\nDate Written: {self.date_written.month}-{self.date_written.day}-{self.date_written.year}')
            print(f'Date Unlocked: {self.date_unlocked.month}-{self.date_unlocked.day}-{self.date_unlocked.year}')
            print('Label:' + self.label + '\n')
            print(self.note + '\n')


    def print_label(self):
        print(f'\nDate Written: {self.date_written.month}-{self.date_written.day}-{self.date_written.year}')
        print(f'Date Unlocked: {self.date_unlocked.month}-{self.date_unlocked.day}-{self.date_unlocked.year}')
        print(self.label + '\n')