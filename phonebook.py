class Phonebook:

    def __init__(self):
        self.book = []

    def __str__(self):
        list_of_contacts = []
        for i in self.book:
            list_of_contacts.append(i.__str__())
        return list_of_contacts

    def add_contact(self):
        name = input('enter name: ')
        number = input('enter number: ')
        new = Contact(name, number)
        self.book.append(new)
        print('contact has been added')

    def remove_contact(self):
        dump = self.search_contact()
        if dump in self.book:
            self.book.remove(dump)
        else:
            return 0
        #print(self.book.__str__())

    def search_contact(self):
        by = input('search by name or num: ')
        if by.lower() == 'name':
            wanted = input('enter name: ')
            for item in self.book:
                if type(item) == Contact:
                    if item.name == wanted:
                        print(item.__str__())
                        return item
            else:
                print('not found')
                return 0

        else:
            wanted = input('enter nunber: ')
            for item in self.book:
                if type(item) == Contact:
                    if item.num == wanted:
                        #print(item.__str__())
                        return item
            else:
                print('not found')
                return 0


class Contact:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __str__(self):
        return self.name, self.num

    def change_name(self):
        new_name = input('new name: ')
        self.name = new_name
        return new_name

    def change_num(self):
        new_num = input('enter new num: ')
        self.num = new_num
        return new_num


