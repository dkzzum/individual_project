# from LinkedList import LinkedList, Node
from AllClasses import *


class DocumentManager:
    """ Менеджер документов """
    def __init__(self):
        self.documents: dict[str, DocumentType] = {}
        self.performers: dict[str, Performers] = {}
        self.tasks: dict[str, Tasks] = {}
        self.resolutions: dict[str, Resolutions] = {}
        self.correspondents: dict[str, ExternalCorrespondents | DomesticCorrespondent] = {}

    def add_document(self, code: str, *args):
        self.documents[code] = DocumentType(*args)

    def add_performers(self, code: str, *args):
        self.performers[code] = Performers(*args)

    def add_task(self, code, *args):
        self.tasks[code] = Tasks(*args)

    def add_resolutions(self, code, *args):
        self.resolutions[code] = Resolutions(*args)

    def add_external_correspondents(self, code, *args):
        self.correspondents[code] = ExternalCorrespondents(*args)

    def add_domestic_correspondent(self, code, *args):
        self.correspondents[code] = DomesticCorrespondent(*args)

    @staticmethod
    def serialize(document: DocumentType, resolution: Resolutions,
                  execution_controller: ExecutionController) -> None:

        document.serialize()
        resolution.serialize()
        execution_controller.serialize()

    @staticmethod
    def deserialize() -> [Performers, Tasks, DomesticCorrespondent | ExternalCorrespondents,
                          DocumentType, ExecutionController, Resolutions]:

        doc = DocumentType.restore_class()
        resol = Resolutions.restore_class()
        cont = ExecutionController.restore_class()
        # print(document.__dict__)
        perf = doc.performers
        task = doc.tasks
        corr = doc.correspondent

        # Настраиваем новую связь между исполнителем,
        # контролером и резолюциями
        cont.performers = perf
        resol.author = perf
        return [perf, task, corr, doc, cont, resol]


if __name__ == '__main__':
    doc_manager = DocumentManager()

    performers = Performers(last_name='Petrov', position='editor', phon_number='89052934700', email='dddddd@gggg.ss')

    tasks = Tasks(code='1285342', task='edit text',
                  deadline=datetime.date(2024, 6, 20), performers=performers)

    dcor = DomesticCorrespondent(department='Dkz INC', position='owner')

    external_cor = ExternalCorrespondents(code='123456', name_organization='YaMi')

    resolution = Resolutions(commit='commit -m "xnj nj"', author=performers)

    ex_contr = ExecutionController(performers=performers)

    document = DocumentType(number_doc='1423536', type_doc='inside',
                            correspondent=dcor, task=tasks, performers=performers)

    doc_manager.serialize(document, resolution, ex_contr)
    del performers, tasks, dcor, external_cor, resolution, ex_contr, document

    lst = doc_manager.deserialize()
    performer: Performers = lst[0]
    task: Tasks = lst[1]
    correspondent: ExternalCorrespondents | DomesticCorrespondent = lst[2]
    documents: DocumentType = lst[3]
    controller: ExecutionController = lst[4]
    resolutions: Resolutions = lst[5]
    performer.last_name = 'Ivanov'
    print()
