Issue Summary:

Modified `server/server.py` to handle HTTP POST requests by reading the Content-Length header, extracting the request body, and passing it to the route handler.

Approach:

Solved the issue by modifying the `server.py` file to include the necessary changes to handle HTTP POST requests. The modification involves reading the Content-Length header, extracting the request body, and storing it in a variable. This variable is then passed to the route handler for processing. The changes also include updates to the server's handling of request bodies for POST requests. The modifications ensure that the server can now properly handle and process request bodies for POST requests. The changes are reflected in the updated `server.py` file.