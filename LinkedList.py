from Capsule import Capsule

class LinkedList:
    def __init__(self) -> None:
        self.list = []
        self.head = None
        self.current = None


    def add_capsule(self, new_cap):
        if self.head is None:  # when list is empty
            self.head = new_cap
        elif new_cap.is_before(self.head.date_unlocked):  # when it should replace the head
            new_cap.next = self.head
            self.head.next = None
            self.head = new_cap
        else: # regular middle placement
            self.current = self.head
            while self.current.next is not None:
                if new_cap.is_before(self.current.date_unlocked):  # when at last node before new one
                    new_cap.next = self.current.next  # new node points to node that was bigger
                    self.current.next = new_cap  # current node points to new node
                    break
                self.current = self.current.next  # move to next node
            if self.current.next is None:  # when it is the last node
                    self.current.next = new_cap


    def remove_capsule():
        pass


    def find_capsule_by_name():
        pass


    def find_capsule_by_date():
        pass

    def show_all_notes(self):
        self.current = self.head
        while self.current is not None:
            self.current.print_note()
            self.current = self.current.next

    def show_all_labels(self):
        self.current = self.head
        while self.current is not None:
            if not self.current.is_before(self.current.now): 
                self.current.print_label()
            self.current = self.current.next