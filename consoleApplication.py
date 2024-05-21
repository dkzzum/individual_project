from AllClasses import *
import datetime


class DocumentManagementSystem:
    def __init__(self):
        self.performers = []
        self.tasks = []
        self.documents = []

    def print_menu(self):
        print("\nВыберите действие:")
        print("1 - Добавить исполнителя")
        print("2 - Удалить исполнителя")
        print("3 - Добавить задачу")
        print("4 - Удалить задачу")
        print("5 - Создать документ")
        print("6 - Удалить документ")
        print("7 - Вывести информацию о всех документах")
        print("8 - Выход")

    def add_performer(self):
        last_name = input("Введите фамилию: ")
        position = input("Введите должность: ")
        phon_number = input("Введите номер телефона: ")
        email = input("Введите email: ")
        performer = Performers(last_name, position, phon_number, email)
        self.performers.append(performer)
        print("Исполнитель добавлен!")

    def delete_performer(self):
        last_name = input("Введите фамилию исполнителя для удаления: ")
        found = [p for p in self.performers if p.last_name == last_name]
        if found:
            self.performers.remove(found[0])
            print("Исполнитель удален.")
        else:
            print("Исполнитель не найден.")

    def add_task(self):
        code = input("Введите код задачи: ")
        description = input("Введите описание задачи: ")
        last_name = input("Введите фамилию исполнителя для задачи: ")
        performer = next((p for p in self.performers if p.last_name == last_name), None)
        if performer:
            deadline = input("Введите срок сдачи (YYYY-MM-DD): ")
            deadline_date = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
            task = Tasks(code, description, performer, deadline_date)
            self.tasks.append(task)
            print("Задача добавлена!")
        else:
            print("Исполнитель не найден.")

    def delete_task(self):
        code = input("Введите код задачи для удаления: ")
        found = [t for t in self.tasks if t.code == code]
        if found:
            self.tasks.remove(found[0])
            print("Задача удалена.")
        else:
            print("Задача не найдена.")

    def create_document(self):
        number_doc = input("Введите номер документа: ")
        task_code = input("Введите код задачи для документа: ")
        task = next((t for t in self.tasks if t.code == task_code), None)
        if task:
            document = Document(number_doc, task=task, performers=task.performers)
            self.documents.append(document)
            print("Документ создан.")
        else:
            print("Задача не найдена.")

    def delete_document(self):
        number_doc = input("Введите номер документа для удаления: ")
        found = [d for d in self.documents if d.number_doc == number_doc]
        if found:
            self.documents.remove(found[0])
            print("Документ удален.")
        else:
            print("Документ не найден.")

    def show_documents(self):
        for doc in self.documents:
            print(doc)

    def run(self):
        while True:
            self.print_menu()
            choice = input("Ваш выбор: ")
            if choice == '1':
                self.add_performer()
            elif choice == '2':
                self.delete_performer()
            elif choice == '3':
                self.add_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.create_document()
            elif choice == '6':
                self.delete_document()
            elif choice == '7':
                self.show_documents()
            elif choice == '8':
                print("Выход из программы")
                break
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")


app = DocumentManagementSystem()
app.run()
