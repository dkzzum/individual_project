from AllClasses import *


def test_per(last_name: str, position: str, phon_number: int | str, email: str):
    performers = Performers(last_name, position, phon_number, email)

    print(performers.position)
    print(performers.email)
    print(performers.last_name)
    print(performers.phon_number)

    performers.position = 'owner'
    performers.email = 'fjldakg@gjkfds.fsda'
    performers.phon_number = '324567897654'
    performers.last_name = 'Petrov'

    print()

    print(performers.__str__())
    print()
    print()


def test_tasks(last_name: str, position: str, phon_number: int | str, email: str,
                code: str | int, task: str,
                deadline: datetime.date | datetime.datetime = datetime.datetime.now(),
                performers: Performers = None):

    task = Tasks(code, task, deadline, performers)
    performers1 = Performers(last_name, position, phon_number, email)
    print(task.deadline)
    print(task.code)
    print(task.performers)
    print(task.tasks)

    task.tasks = 'edit edit'
    task.code = '1234'
    task.deadline = '2024-02-19'
    task.performers = performers1

    print()

    print(task.__str__())
    print()
    print()


def test_dcor(department: str, position: str):

    cor = DomesticCorrespondent(department, position)

    print(cor.department)
    print(cor.position)

    cor.department = 'FuTu'
    cor.position = 'member'

    print()

    print(cor.__str__())
    print()
    print()


def test_external_cor(code: int | str, name_organization: str):

    cor = ExternalCorrespondents(code, name_organization)

    print(cor.name_organization)
    print(cor.code)

    cor.name_organization = 'FuTu'
    cor.code = '2134567423'

    print()

    print(cor.__str__())
    print()
    print()


def test_doc(p1: Performers, t1: Tasks, c1: ExternalCorrespondents | DomesticCorrespondent,
             number_doc: str | int, type_doc: str,
             correspondent: DomesticCorrespondent | ExternalCorrespondents = None,
             task: Tasks = None, performers: Performers = None,
             date_of_creation: datetime.datetime | datetime.date | str = datetime.datetime.now(),
             date_of_registration: datetime.datetime | datetime.date | str | None = None):

    document = Document(number_doc, type_doc, correspondent, task, performers, date_of_creation, date_of_registration)
    print(document.type_doc)
    print(document.number_doc)
    print(document.date_of_creation)
    print(document.tasks)
    print(document.performers)
    print(document.correspondent)

    document.type_doc = 'extremal'
    document.number_doc = '1234543234542132423'
    document.date_of_creation = '2024-02-19'
    document.correspondent = c1
    document.performers = p1
    document.tasks = t1
    document.date_of_registration = '2024-05-20'

    print()

    print(document.__str__())
    print()
    print()


def test_res(a1: Performers, commit: str, author: Performers = None,
                 date_of_creation: datetime.datetime | str = datetime.datetime.now()):

    res = Resolutions(commit, author, date_of_creation)
    print(res.date_of_creation)
    print(res.commit)
    print(res.author)

    res.date_of_creation = '2024-02-19'
    res.commit = 'git commit'
    res.author = a1

    print()

    print(res.__str__())
    print()
    print()


def test_ex(performers: Performers, p1: Performers):

    ex = ExecutionController(performers)
    print(ex.performers)

    ex.performers = p1
    print()

    print(ex.__str__())


if __name__ == '__main__':
    per = Performers(last_name='Ivanov', position='editor', phon_number='89052934700',
                     email='dddddd@gggg.ss')

    tasks = Tasks(code='12985342', task='edit text', deadline=datetime.date(2024, 3, 11),
                  performers=per)

    dcor = DomesticCorrespondent(department='Dkz INC', position='editor')

    external_cor = ExternalCorrespondents(code='123456', name_organization='YaMi')

    doc = Document(number_doc='1423536', type_doc='inside', correspondent=external_cor, task=tasks,
                   performers=per)

    resol = Resolutions(commit='commit -m "xnj nj"', author=per)

    ex_contr = ExecutionController(performers=per)

    ###### test ######
    test_per(last_name='Ivanov', position='editor', phon_number='89052934700',
                     email='dddddd@gggg.ss')
    test_tasks(last_name='Durov', position='owner', phon_number='1112223333',
                     email='docuch@mail.ru', code='12985342', task='edit text',
               deadline=datetime.date(2024, 3, 11), performers=per)
    test_dcor(department='Dkz INC', position='editor')
    test_external_cor(code='123456', name_organization='YaMi')

    p1 = Performers(last_name='Durov', position='owner', phon_number='1112223333',
                     email='docuch@mail.ru')
    t1 = Tasks('123432412', 'task*****', '2025-06-06', per)
    c1 = DomesticCorrespondent(department='MiMiMu', position='creator')
    test_doc(p1, t1, c1, '23423452', 'type_inside', dcor, tasks, per, '2020-02-02',
             '2020-03-03')
    test_res(p1, 'commit -m -d -t', per, '2020-08-12')
    test_ex(per, p1)
