Add support for basic static file serving.
Modify `server/server.py` so that if a route is not found in `self.routes` or regex routes, it checks if a corresponding file exists in the current directory and returns its content.
