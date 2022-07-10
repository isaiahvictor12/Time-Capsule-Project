from datetime import datetime
from Time import Time

class Capsule:
    def __init__(self, date_unlocked, label, note) -> None:
        now_time = datetime.now()
        self.now = Time(now_time.month, now_time.day, now_time.year)
        self.date_written = self.now
        self.date_unlocked = date_unlocked
        self.label = label
        self.note = note
        self.previous = None
        self.next = None
        pass

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
    
    def print_note(self):
        if self.is_before(self.now):
            print(f'\nDate Written: {self.date_written.month}-{self.date_written.day}-{self.date_written.year}')
            print(f'Date Unlocked: {self.date_unlocked.month}-{self.date_unlocked.day}-{self.date_unlocked.year}')
            print(self.label + '\n')
            print(self.note + '\n')


    def print_label(self):
        print(f'\nDate Written: {self.date_written.month}-{self.date_written.day}-{self.date_written.year}')
        print(f'Date Unlocked: {self.date_unlocked.month}-{self.date_unlocked.day}-{self.date_unlocked.year}')
        print(self.label + '\n')