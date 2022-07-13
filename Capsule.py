from datetime import datetime
from Time import Time

class Capsule:
    def __init__(self, date_unlocked,  note, label, now) -> None:
        self.date_written = now
        self.date_unlocked = date_unlocked
        self.label = label
        self.note = note
        self.next = None
        self.id = None

        # returns true when capsule has unlock date before the time given
    def is_before(self, other_time):
        return self.date_unlocked.total_time <= other_time.total_time

    
    def print_note(self, now):
        if self.is_before(now):
            print(f'\nCapsule ID: {self.id}')
            print(f'Date Written: {self.date_written.month}-{self.date_written.day}-{self.date_written.year}')
            print(f'Date Unlocked: {self.date_unlocked.month}-{self.date_unlocked.day}-{self.date_unlocked.year}')
            print('Label:' + self.label + '\n')
            print(self.note + '\n')


    def print_label(self):
        print(f'\nCapsule ID: {self.id}')
        print(f'Date Written: {self.date_written.month}-{self.date_written.day}-{self.date_written.year}')
        print(f'Date Unlocked: {self.date_unlocked.month}-{self.date_unlocked.day}-{self.date_unlocked.year}')
        print('Label: ' + self.label + '\n')