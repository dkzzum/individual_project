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

    @staticmethod
    def serialize(document: DocumentType, resolution: Resolutions,
                  execution_controller: ExecutionController) -> None:

        document.serialize()
        resolution.serialize()
        execution_controller.serialize()

    @staticmethod
    def deserialize() -> [Performers, Tasks, DomesticCorrespondent | ExternalCorrespondents,
                          DocumentType, ExecutionController, Resolutions]:

        document = DocumentType.restore_class()
        resolutions = Resolutions.restore_class()
        controller = ExecutionController.restore_class()
        print(document.__dict__)
        performer = document.performers
        task = document.tasks
        correspondent = document.correspondent

        # Настраиваем новую связь между исполнителем,
        # контролером и резолюциями
        controller.performers = performer
        resolutions.author = performer
        return [performer, task, correspondent, document, controller, resolutions]


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
