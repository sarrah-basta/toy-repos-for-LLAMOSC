We want to introduce priority levels to our tasks to help users sort their work.

Please modify `todo/todo.py` to:
1. Update `add_task` to accept an optional `priority` argument (string). This should default to "Low" if not provided. Valid options are "High", "Medium", "Low". 
2. Modify `list_tasks` to return the tasks sorted by priority (High first, then Medium, then Low). If tasks have the same priority, sort them by ID.
