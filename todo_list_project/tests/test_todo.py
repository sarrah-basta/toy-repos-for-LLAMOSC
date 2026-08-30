import unittest
from todo.todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        task = self.todo.add_task("Test task")
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Test task")
        self.assertEqual(len(self.todo.tasks), 1)

    def test_list_tasks(self):
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        tasks = self.todo.list_tasks()
        self.assertEqual(len(tasks), 2)

if __name__ == "__main__":
    unittest.main()
