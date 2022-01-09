"""Single Responsibility Principel SRP - Separation of concerns""" 

class Journal:

    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # PRINCIPLE VIOLATION:
    # Adding another reponsibility
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def  load(self, filename):
    #     pass

    # def load_from_web(self):
    #     pass

class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(Journal))
        file.close()



j = Journal()
j.add_entry('Entry 1')
j.add_entry('Entry 2')
print(f'Journal entries: \n{j}')

file = r'data/journal.txt'
PersistenceManager.save_to_file(j, file)