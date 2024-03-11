import unittest
import datetime
from AllClasses import (DomesticCorrespondent, ExternalCorrespondents,
                        Performers, Resolutions, ExecutionController, Tasks, Document)


class TestClasses(unittest.TestCase):

    def test_domestic_correspondent(self):
        domestic_correspondent = DomesticCorrespondent(department="Finance", position="Manager")
        self.assertEqual(domestic_correspondent.department, "Finance")
        self.assertEqual(domestic_correspondent.position, "Manager")

    def test_external_correspondents(self):
        external_correspondent = ExternalCorrespondents(code="123456", name_organization="XYZ Corp")
        self.assertEqual(external_correspondent.code, "123456")
        self.assertEqual(external_correspondent.name_organization, "XYZ Corp")

    def test_performers(self):
        performers = Performers(last_name="Smith", position="Analyst", phon_number="123456789",
                                email="smith@example.com")
        self.assertEqual(performers.last_name, "Smith")
        self.assertEqual(performers.position, "Analyst")
        self.assertEqual(performers.phon_number, "123456789")
        self.assertEqual(performers.email, "smith@example.com")

    def test_resolutions(self):
        author = Performers(last_name="Johnson", position="Manager", phon_number="987654321",
                            email="johnson@example.com")
        resolutions = Resolutions(commit="Approved", author=author, date_of_creation=datetime.datetime.now())
        self.assertEqual(resolutions.commit, "Approved")
        self.assertEqual(resolutions.author, author)

    def test_execution_controller(self):
        performer = Performers(last_name="Brown", position="Developer", phon_number="555555555",
                               email="brown@example.com")
        execution_controller = ExecutionController(performers=performer)
        self.assertEqual(execution_controller.performers, performer)

    def test_tasks(self):
        performer = Performers(last_name="Clark", position="Designer", phon_number="999999999",
                               email="clark@example.com")
        tasks = Tasks(code="123", task="Design UI", deadline=datetime.datetime.now(), performers=performer)
        self.assertEqual(tasks.code, "123")
        self.assertEqual(tasks.tasks, "Design UI")
        self.assertEqual(tasks.performers, performer)

    def test_document(self):
        performer = Performers(last_name="Williams", position="Engineer", phon_number="777777777",
                               email="williams@example.com")
        external_correspondent = ExternalCorrespondents(code="654321", name_organization="ABC Ltd")
        document = Document(number_doc="987", type_doc="Internal", correspondent=external_correspondent,
                            task=None, performers=performer, date_of_creation=datetime.datetime.now())
        self.assertEqual(document.number_doc, "987")
        self.assertEqual(document.type_doc, "Internal")
        self.assertEqual(document.correspondent, external_correspondent)
        self.assertEqual(document.performers, performer)

    def test_document_task_assignment(self):
        performer = Performers(last_name="Jones", position="Manager", phon_number="333333333",
                               email="jones@example.com")
        document = Document(number_doc="123", type_doc="External")
        task = Tasks(code="456", task="Review document", deadline=datetime.datetime.now(), performers=performer)
        document.tasks = task
        self.assertEqual(document.tasks, task)

    def test_document_resolution_assignment(self):
        author = Performers(last_name="Davis", position="Coordinator", phon_number="444444444",
                            email="davis@example.com")
        resolution = Resolutions(commit="Reviewed and approved", author=author,
                                 date_of_creation=datetime.datetime.now())
        document = Document(number_doc="789", type_doc="Internal")
        document.resolutions = resolution
        self.assertEqual(document.resolutions, resolution)

    def test_document_creation_date(self):
        document = Document(number_doc="123", type_doc="Internal")
        self.assertIsInstance(document.date_of_creation, datetime.date)

    def test_document_task_deadline(self):
        performer = Performers(last_name="Smith", position="Analyst", phon_number="123456789",
                               email="smith@example.com")
        task = Tasks(code="456", task="Analyze data", deadline=datetime.date(2024, 12, 31),
                     performers=performer)
        self.assertIsInstance(task.deadline, datetime.date)
        self.assertLess(datetime.date(2024, 12, 30), task.deadline)

    def test_execution_controller_invalid_performers(self):
        with self.assertRaises(TypeError):
            execution_controller = ExecutionController(performers="invalid")

    def test_resolutions_invalid_author(self):
        with self.assertRaises(TypeError):
            resolution = Resolutions(commit="Approved", author="invalid", date_of_creation=datetime.datetime.now())

    def test_domestic_correspondent_department_change(self):
        domestic_correspondent = DomesticCorrespondent(department="HR", position="Assistant")
        domestic_correspondent.department = "Finance"
        self.assertEqual(domestic_correspondent.department, "Finance")

    def test_external_correspondents_code_change(self):
        external_correspondent = ExternalCorrespondents(code="654321", name_organization="ABC Ltd")
        external_correspondent.code = "123456"
        self.assertEqual(external_correspondent.code, "123456")

    def test_performers_email_change(self):
        performers = Performers(last_name="Brown", position="Developer", phon_number="555555555",
                                email="brown@example.com")
        performers.email = "brown2@example.com"
        self.assertEqual(performers.email, "brown2@example.com")

    def test_resolutions_commit_change(self):
        author = Performers(last_name="Johnson", position="Manager", phon_number="987654321",
                            email="johnson@example.com")
        resolutions = Resolutions(commit="Reviewed", author=author, date_of_creation=datetime.datetime.now())
        resolutions.commit = "Approved"
        self.assertEqual(resolutions.commit, "Approved")

    def test_execution_controller_set_performers(self):
        performer = Performers(last_name="Clark", position="Designer", phon_number="999999999",
                               email="clark@example.com")
        execution_controller = ExecutionController()
        execution_controller.performers = performer
        self.assertEqual(execution_controller.performers, performer)

    def test_tasks_code_change(self):
        performer = Performers(last_name="Smith", position="Analyst", phon_number="123456789",
                               email="smith@example.com")
        tasks = Tasks(code="123", task="Analyze data", deadline=datetime.datetime.now(), performers=performer)
        tasks.code = "456"
        self.assertEqual(tasks.code, "456")

    def test_document_number_doc_change(self):
        performer = Performers(last_name="Williams", position="Engineer", phon_number="777777777",
                               email="williams@example.com")
        external_correspondent = ExternalCorrespondents(code="654321", name_organization="ABC Ltd")
        document = Document(number_doc="987", type_doc="Internal", correspondent=external_correspondent,
                            task=None, performers=performer, date_of_creation=datetime.datetime.now())
        document.number_doc = "123"
        self.assertEqual(document.number_doc, "123")

    def test_document_type_doc_change(self):
        document = Document(number_doc="123", type_doc="External")
        document.type_doc = "Internal"
        self.assertEqual(document.type_doc, "Internal")

    def test_document_task_assignment_none(self):
        document = Document(number_doc="123", type_doc="External")
        document.tasks = None
        self.assertIsNone(document.tasks)

    def test_document_resolution_assignment_none(self):
        document = Document(number_doc="123", type_doc="Internal")
        document.resolutions = None
        self.assertIsNone(document.resolutions)

    def test_domestic_correspondent_position_change(self):
        domestic_correspondent = DomesticCorrespondent(department="HR", position="Assistant")
        domestic_correspondent.position = "Manager"
        self.assertEqual(domestic_correspondent.position, "Manager")

    def test_external_correspondents_name_organization_change(self):
        external_correspondent = ExternalCorrespondents(code="654321", name_organization="ABC Ltd")
        external_correspondent.name_organization = "XYZ Corp"
        self.assertEqual(external_correspondent.name_organization, "XYZ Corp")

    def test_performers_phon_number_change(self):
        performers = Performers(last_name="Brown", position="Developer", phon_number="555555555",
                                email="brown@example.com")
        performers.phon_number = "123456789"
        self.assertEqual(performers.phon_number, "123456789")

    def test_resolutions_author_change(self):
        author = Performers(last_name="Johnson", position="Manager", phon_number="987654321",
                            email="johnson@example.com")
        new_author = Performers(last_name="Smith", position="Analyst", phon_number="123456789",
                                email="smith@example.com")
        resolutions = Resolutions(commit="Reviewed", author=author, date_of_creation=datetime.datetime.now())
        resolutions.author = new_author
        self.assertEqual(resolutions.author, new_author)

    def test_execution_controller_set_performers_none(self):
        execution_controller = ExecutionController()
        execution_controller.performers = None
        self.assertIsNone(execution_controller.performers)

    def test_tasks_task_change(self):
        performer = Performers(last_name="Smith", position="Analyst", phon_number="123456789",
                               email="smith@example.com")
        tasks = Tasks(code="123", task="Analyze data", deadline=datetime.datetime.now(), performers=performer)
        tasks.task = "Review report"
        self.assertEqual(tasks.task, "Review report")

    def test_document_creation_date_type(self):
        document = Document(number_doc="123", type_doc="Internal")
        self.assertIsInstance(document.date_of_creation, datetime.date)

    def test_document_correspondent_none(self):
        document = Document(number_doc="123", type_doc="Internal")
        document.correspondent = None
        self.assertIsNone(document.correspondent)

    def test_document_performers_none(self):
        document = Document(number_doc="123", type_doc="Internal")
        document.performers = None
        self.assertIsNone(document.performers)

    def test_document_task_deadline_type(self):
        performer = Performers(last_name="Smith", position="Analyst", phon_number="123456789",
                               email="smith@example.com")
        tasks = Tasks(code="123", task="Analyze data", deadline=datetime.datetime.now(), performers=performer)
        self.assertIsInstance(tasks.deadline, datetime.date)


if __name__ == '__main__':
    unittest.main()
