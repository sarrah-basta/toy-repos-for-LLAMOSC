Here is the requested pull request:

Issue Summary: Fixes issue with To-Do list losing data when process closes by adding persistence through JSON file.

Approach:

This pull request addresses the problem of losing task data when the Python process terminates. I added two new methods to `todo/todo.py`: `save_to_file` and `load_from_file`. The `save_to_file` method serializes the tasks list into a JSON file, allowing the data to be persisted even after the process closes. The `load_from_file` method deserializes the tasks from the JSON file and updates the internal state of the To-Do list with the loaded tasks and highest ID. This ensures that the task data is retained across process restarts.