Here is the modified `todo/todo.py` file:

```
index 634bfb2..f03683e 100644
--- a/todo/todo.py
+++ b/todo/todo.py
@@ -19,6 +19,13 @@ class TodoList:
         tasks = sorted(self.tasks, key=lambda x: ("High", "Medium", "Low").index(x["priority"]))
         return tasks
 
+    def remove_task(self, task_id):
+        if task_id in [task["id"] for task in self.tasks]:
+            self.tasks = [task for task in self.tasks if task["id"] != task_id]
+            return True
+        else:
+            return False
+
```

Here is the pull request:

Issue Summary: This PR adds a new method `remove_task` to the TodoList class, allowing users to delete tasks from their to-do list.

Approach: The `remove_task` method takes an integer task ID as input and removes the corresponding task from the `self.tasks` list if it exists. If no task with the given ID is found, the method returns False.