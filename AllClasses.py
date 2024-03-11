from typing import Any
import datetime
import pickle
import io


class Performers:
    """ Исполнители """

    def __init__(self, last_name: str, position: str, phon_number: int | str, email: str):
        self.__last_name = last_name
        self.__position = position
        self.__phon_number = phon_number
        self.__email = email
        # self.__old_name = None

    def __str__(self, flag: bool = True):
        if flag:
            return (f'last name: {self.last_name}; position: {self.position}; '
                    f'phon number: {self.phon_number}; email: {self.email}')
        else:
            return self

    def __del__(self):
        # self.__serialize(self.__dict__.values())

        with io.open('activity_log/del_logs.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tlast name: {self.last_name}\n\tposition: {self.position}\n'
                      f'\tphon number: {self.phon_number}\n\t email: {self.email}')

    @classmethod
    def restore_class(cls):
        return cls(*Performers.__deserialize())

    # @classmethod
    # def serialize(*args) -> None:
    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/performers.pkl', 'wb') as pk:
            for data in args:
                pickle.dump(data, pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/performers.pkl', 'rb') as pk:
            lens = pickle.load(pk)
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        with io.open('activity_log/performers_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — last name edit: old - {self.__last_name}; '
                f'new - {last_name}\n')

        self.__last_name = last_name

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        with io.open('activity_log/performers_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — position edit: old - {self.__position}; '
                f'new - {position}\n')

        self.__position = position

    @property
    def phon_number(self) -> int | str:
        return self.__phon_number

    @phon_number.setter
    def phon_number(self, phon_number: int | str):
        with io.open('activity_log/performers_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — phon number edit: old - {self.__phon_number}; '
                f'new - {phon_number}\n')

        self.__phon_number = phon_number

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        with io.open('activity_log/performers_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — email edit: old - {self.__email}; '
                f'new - {email}\n')

        self.__email = email


class Tasks:
    """ Задачи """

    def __init__(self, code: str, task: str, performers: Performers = None,
                 deadline: datetime.date | datetime.datetime | str = datetime.datetime.now()):
        self.__code = code
        self.__tasks = task
        self.__performers = performers
        self.__deadline = deadline

    def __str__(self, flag: bool = True):
        if flag:
            return (f'code: {self.code}; task: {self.tasks}; '
                    f'performers: {self.performers.last_name}; deadline: {self.deadline}')
        else:
            return self

    def __del__(self):

        with io.open('activity_log/del_logs.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tcode: {self.code}\n\ttask: {self.tasks}\n'
                      f'\tperformers: {self.performers}\n'
                      f'\tdeadline: {self.deadline}\n\n')

    @classmethod
    def restore_class(cls):
        return cls(*Tasks.__deserialize())

    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/task.pkl', 'wb') as pk:
            for data in args:
                if isinstance(data, Performers):
                    pickle.dump(data.__str__(False), pk)
                else:
                    pickle.dump(str(data), pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/task.pkl', 'rb') as pk:
            lens = int(pickle.load(pk))
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def code(self) -> str | int:
        return self.__code

    @code.setter
    def code(self, code: str | int):
        with io.open('activity_log/tasks_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — code edit: old - {self.__code}; '
                f'new - {code}\n')

        self.__code = code

    @property
    def tasks(self) -> str:
        return self.__tasks

    @tasks.setter
    def tasks(self, task: str):
        with io.open('activity_log/tasks_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — task edit: old - {self.__tasks}; '
                f'new - {task}\n')

        self.__tasks = task

    @property
    def performers(self) -> Performers:
        return self.__performers

    @performers.setter
    def performers(self, performers: Performers):
        with io.open('activity_log/tasks_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — performers edit: old - ({self.__performers}); '
                f'new - ({performers})\n')

        self.__performers = performers

    @property
    def deadline(self) -> datetime.date:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: datetime.datetime | datetime.date | str):
        if isinstance(deadline, datetime.datetime):
            get_deadline = list(map(int, str(deadline)[:10].split('-')))
        else:
            get_deadline = list(map(int, str(deadline).split('-')))

        new_deadline = datetime.date(get_deadline[0], get_deadline[1], get_deadline[2])
        with io.open('activity_log/tasks_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — deadline edit: old - {self.__deadline}; '
                f'new - {new_deadline}\n')

        self.__deadline = new_deadline


class DomesticCorrespondent:
    """ Внутренние корреспонденты """

    def __init__(self, department: str, position: str):
        self.__department = department
        self.__position = position

    def __str__(self, flag: bool = True):
        if flag:
            return f'department: {self.department}; position: {self.position}'
        else:
            return self

    def __del__(self):

        with io.open('activity_log/del_logs.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tdepartment: {self.department}\n'
                      f'\tposition: {self.position}\n\n')

    @classmethod
    def restore_class(cls):
        return cls(*DomesticCorrespondent.__deserialize())

    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/domestic_correspondent.pkl', 'wb') as pk:
            for data in args:
                pickle.dump(data, pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/domestic_correspondent.pkl', 'rb') as pk:
            lens = pickle.load(pk)
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def department(self) -> str:
        return self.__department

    @department.setter
    def department(self, department: str):
        with io.open('activity_log/domestic_correspondent_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — department edit: old - {self.__department}; '
                f'new - {department}\n')

        self.__department = department

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        with io.open('activity_log/domestic_correspondent_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — position edit: old - {self.__position}; '
                f'new - {position}\n')

        self.__position = position


class ExternalCorrespondents:
    """ Внешние корреспонденты """

    def __init__(self, code: int | str, name_organization: str):
        self.__code = code
        self.__name_organization = name_organization

    def __str__(self, flag: bool = True):
        if flag:
            return f'code: {self.code}; name org: {self.name_organization}'
        else:
            return self

    def __del__(self):

        with io.open('activity_log/del_logs.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tcode: {self.code}\n'
                      f'\tname organization: {self.name_organization}\n\n')

    @classmethod
    def restore_class(cls):
        return cls(*ExternalCorrespondents.__deserialize())

    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/external_correspondents.pkl', 'wb') as pk:
            for data in args:
                pickle.dump(data, pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/external_correspondents.pkl', 'rb') as pk:
            lens = pickle.load(pk)
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def code(self) -> int | str:
        return self.__code

    @code.setter
    def code(self, code: int | str):
        with io.open('activity_log/external_correspondents_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — code correspondents edit: old - {self.__code}; '
                f'new - {code}\n')

        self.__code = code

    @property
    def name_organization(self) -> str:
        return self.__name_organization

    @name_organization.setter
    def name_organization(self, name_organization: str):
        with io.open('activity_log/external_correspondents_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — name organization edit: old - {self.__name_organization}; '
                f'new - {name_organization}\n')

        self.__name_organization = name_organization


class Document:
    """ Документы """

    def __init__(self, number_doc: str | int, type_doc: str,
                 correspondent: DomesticCorrespondent | ExternalCorrespondents = None,
                 task: Tasks = None, performers: Performers = None,
                 date_of_creation: datetime.datetime | datetime.date | str = datetime.datetime.now(),
                 date_of_registration: datetime.datetime | datetime.date | str | None = None):
        self.__number_doc = number_doc
        self.__type_doc = type_doc
        self.__correspondent = correspondent
        self.__tasks = task
        self.__performers = performers
        self.__date_of_creation = date_of_creation
        self.__date_of_registration = date_of_registration

    def __str__(self, flag: bool = True):
        if flag:
            return (f'number doc: {self.number_doc}; type doc: {self.type_doc};\n'
                    f'correspondent: ({self.correspondent});\ntasks: ({self.tasks});\n'
                    f'performers: ({self.performers});\ndata of creation: {str(self.date_of_creation)}')
        else:
            return self

    def __del__(self):

        with io.open('activity_log/del_logs.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tnumber doc: {self.number_doc}\n\ttype doc: {self.type_doc}\n'
                      f'\tcorrespondent: ({self.correspondent})\n\ttask: ({self.tasks})\n'
                      f'\tperformers: ({self.performers})\n'
                      f'\tdate of creation: {self.date_of_creation}\n'
                      f'\tdata of registration: {self.date_of_registration}\n\n')

    @classmethod
    def restore_class(cls):
        return cls(*Document.__deserialize())

    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/document.pkl', 'wb') as pk:
            for data in args:
                if isinstance(data, (DomesticCorrespondent, ExternalCorrespondents, Tasks, Performers)):
                    pickle.dump(data.__str__(False), pk)
                else:
                    pickle.dump(str(data), pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/document.pkl', 'rb') as pk:
            lens = int(pickle.load(pk))
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def type_doc(self) -> str:
        return self.__type_doc

    @type_doc.setter
    def type_doc(self, types: str):
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — type doc edit: old - {self.__type_doc}; '
                f'new - {types}\n')

        self.__type_doc = types

    @property
    def correspondent(self) -> ExternalCorrespondents | DomesticCorrespondent:
        return self.__correspondent

    @correspondent.setter
    def correspondent(self, correspondent: ExternalCorrespondents | DomesticCorrespondent):
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — correspondent edit: old - ({self.__correspondent}); '
                f'new - ({correspondent})\n')

        self.__correspondent = correspondent

    @property
    def tasks(self) -> Tasks:
        return self.__tasks

    @tasks.setter
    def tasks(self, task: Tasks):
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — task edit: old - ({self.__tasks}); '
                f'new - ({task.tasks})\n')

        self.__tasks = task

    @property
    def performers(self) -> Performers:
        return self.__performers

    @performers.setter
    def performers(self, performers: Performers):
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — performers edit: old - ({self.__performers}); '
                f'new - ({performers})\n')

        self.__performers = performers

    @property
    def date_of_creation(self) -> datetime.date:
        return self.__date_of_creation

    @date_of_creation.setter
    def date_of_creation(self, date_of_creation: datetime.datetime | datetime.date | str):
        if isinstance(date_of_creation, datetime.datetime):
            get_date = list(map(int, str(date_of_creation)[:10].split('-')))
        else:
            get_date = list(map(int, str(date_of_creation).split('-')))

        new_date = datetime.date(get_date[0], get_date[1], get_date[2])
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — date of creation edit: old - {self.__date_of_creation}; '
                f'new - {new_date}\n')

        self.__date_of_creation = new_date

    @property
    def number_doc(self) -> str | int:
        return self.__number_doc

    @number_doc.setter
    def number_doc(self, number_doc: str | int):
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(
                f'[{datetime.datetime.now()}] — number doc edit: old - {self.__number_doc}; '
                f'new - {number_doc}\n')

        self.__number_doc = number_doc

    @property
    def date_of_registration(self) -> datetime.date | None:
        return self.__date_of_registration

    @date_of_registration.setter
    def date_of_registration(self, date_of_registration: datetime.datetime | datetime.date | str | None):
        if date_of_registration is None:
            with io.open('activity_log/document_log.txt', 'a') as log:
                log.write(
                    f'[{datetime.datetime.now()}] — date of registration edit: old - {self.__date_of_registration}; '
                    f'new - {date_of_registration}\n')

            self.__date_of_registration = date_of_registration
            return
        elif isinstance(date_of_registration, datetime.datetime):
            get_date = list(map(int, str(date_of_registration)[:10].split('-')))
        else:
            get_date = list(map(int, str(date_of_registration).split('-')))

        new_date = datetime.date(get_date[0], get_date[1], get_date[2])
        with io.open('activity_log/document_log.txt', 'a') as log:
            log.write(f'[{datetime.datetime.now()}] — date of registration edit: old - {self.__date_of_registration}; '
                      f'new - {new_date}\n')

        self.__date_of_registration = new_date


class Resolutions:
    """ Резолюции """

    def __init__(self, commit: str, author: Performers,
                 date_of_creation: datetime.datetime | datetime.date | str = datetime.datetime.now()):
        self.__commit = commit

        if isinstance(author, Performers):
            self.__author = author
        else:
            raise TypeError('performers must be an instance of Performers')

        self.__date_of_creation = date_of_creation

    def __str__(self, flag: bool = True):
        if flag:
            return (f'author: {self.author.last_name}; commit: {self.commit};'
                    f'date of creation: {self.date_of_creation}')
        else:
            return self

    def __del__(self):

        with io.open('activity_log/resolutions.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tcommit: {self.commit}\n\tauthor: ({self.author})\n'
                      f'\tdate of creation: {self.date_of_creation}\n\n')

    @classmethod
    def restore_class(cls):
        return cls(*Resolutions.__deserialize())

    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/resolutions.pkl', 'wb') as pk:
            for data in args:
                if isinstance(data, Performers):
                    pickle.dump(data.__str__(False), pk)
                else:
                    pickle.dump(data, pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/resolutions.pkl', 'rb') as pk:
            lens = int(pickle.load(pk))
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def author(self) -> Performers:
        return self.__author

    @author.setter
    def author(self, author: Performers):
        with io.open('activity_log/resolutions_log.txt', 'a') as log:
            log.write(f'[{datetime.datetime.now()}] — author edit: old - ({self.__author}); '
                      f'new - ({author})\n')

        self.__author = author

    @property
    def commit(self) -> str:
        return self.__commit

    @commit.setter
    def commit(self, commit: str):
        with io.open('activity_log/resolutions_log.txt', 'a') as log:
            log.write(f'[{datetime.datetime.now()}] — commit edit: old - {self.__commit}; '
                      f'new - {commit}\n')

        self.__commit = commit

    @property
    def date_of_creation(self) -> datetime.date:
        return self.__date_of_creation

    @date_of_creation.setter
    def date_of_creation(self, date_of_creation: datetime.datetime | datetime.date | str):
        if isinstance(date_of_creation, datetime.datetime):
            get_date = list(map(int, str(date_of_creation)[:10].split('-')))
        else:
            get_date = list(map(int, str(date_of_creation).split('-')))

        new_date = datetime.date(get_date[0], get_date[1], get_date[2])

        with io.open('activity_log/resolutions_log.txt', 'a') as log:
            log.write(f'[{datetime.datetime.now()}] — date of creation edit: old - {self.__date_of_creation}; '
                      f'new - {str(new_date)}\n')

        self.__date_of_creation = new_date


class ExecutionController:
    """ Контролер исполнения """

    def __init__(self, performers: Performers = None):
        if isinstance(performers, Performers) or performers is None:
            self.__performers = performers
        else:
            raise TypeError("performers must be an instance of Performers")

    def __str__(self, flag: bool = True):
        if flag:
            return f'performers: {self.performers.last_name}'
        else:
            return self

    def __del__(self):

        with io.open('activity_log/del_logs.txt', 'a') as log:
            log.write(f'Delete object: {type(self)}\n'
                      f'\tperformers: ({self.performers})\n\n')

    @classmethod
    def restore_class(cls):
        return cls(*ExecutionController.__deserialize())

    def serialize(self) -> None:
        args = list(self.__dict__.values())
        args.insert(0, len(args))

        with io.open('serialize_file/execution_controller.pkl', 'wb') as pk:
            for data in args:
                if isinstance(data, Performers):
                    pickle.dump(data.__str__(False), pk)
                else:
                    pickle.dump(data, pk)

    @staticmethod
    def __deserialize() -> list[str | int]:
        data = []
        with io.open('serialize_file/execution_controller.pkl', 'rb') as pk:
            lens = pickle.load(pk)
            for i in range(lens):
                data.append(pickle.load(pk))

        return data

    @property
    def performers(self) -> Performers:
        return self.__performers

    @performers.setter
    def performers(self, performers: Performers):
        if isinstance(performers, Performers) or performers is None:
            with io.open('activity_log/execution_controller_log.txt', 'a') as log:
                log.write(f'[{datetime.datetime.now()}] — performers edit: old - ({self.__performers});'
                          f' new - ({performers})\n')

            self.__performers = performers
        else:
            raise TypeError("performers must be an instance of Performers")


if __name__ == '__main__':
    per = Performers(last_name='Petrov', position='editor', phon_number='89052934700', email='dddddd@gggg.ss')
    per.serialize()
    del per
    per = Performers.restore_class()

    tasks = Tasks(code='1285342', task='edit text',
                  deadline=datetime.date(2024, 6, 20), performers=per)
    tasks.serialize()
    del tasks
    tasks = Tasks.restore_class()

    dcor = DomesticCorrespondent(department='Dkz INC', position='owner')
    dcor.serialize()
    del dcor
    dcor = DomesticCorrespondent.restore_class()

    external_cor = ExternalCorrespondents(code='123456', name_organization='YaMi')
    external_cor.serialize()
    del external_cor
    external_cor = ExternalCorrespondents.restore_class()

    doc = Document(number_doc='1423536', type_doc='inside', correspondent=dcor, task=tasks, performers=per)
    doc.serialize()
    del doc
    doc = Document.restore_class()

    resol = Resolutions(commit='commit -m "xnj nj"', author=per)
    resol.serialize()
    del resol
    resol = Resolutions.restore_class()

    ex_contr = ExecutionController(performers=per)
    ex_contr.serialize()
    del ex_contr
    ex_contr = ExecutionController.restore_class()
    print()
