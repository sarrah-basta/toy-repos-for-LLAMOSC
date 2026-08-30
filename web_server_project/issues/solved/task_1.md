The current WebServer only supports exact string matches for routes (e.g. `self.routes[path]`).

We want to support Dynamic Regex Routing, but we'll do it in steps. For this issue, please modify `server/server.py` to prepare the `add_route` function:

1. Import the `re` module.
2. In `__init__`, add a new list or dictionary called `self.regex_routes` to store regex patterns.
3. Modify `add_route(path, handler)`: check if the `path` contains the exact string `<regex:`. If it does, store the path and handler in `self.regex_routes`. If it doesn't, store it in `self.routes` as it currently does.

Do NOT modify `handle_client` yet. Just ensure `add_route` correctly separates normal routes from regex routes.
