Our To-Do list currently loses all data when the Python process closes because it's only stored in memory.

We need persistence. Modify `todo/todo.py` to add two new methods:
1. `save_to_file(self, filename="data.json")`: This should save the `self.tasks` list to a JSON file.
2. `load_from_file(self, filename="data.json")`: This should load tasks from the JSON file and restore the `self.tasks` list, as well as correctly update `self.next_id` based on the highest loaded ID.

Remember to import the `json` module.
