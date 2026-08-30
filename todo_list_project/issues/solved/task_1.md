We need the ability to delete tasks from our To-Do list.

Please modify `todo/todo.py` to add a new method `remove_task(self, task_id)`.
This method should take an integer `task_id` and remove the task with that corresponding ID from the `self.tasks` list.
If no task exists with that ID, it should do nothing or return False. If successful, return True.

Also, please add a simple test case for this in `tests/test_todo.py`.
