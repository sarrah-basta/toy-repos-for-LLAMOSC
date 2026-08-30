The current WebServer stores normal routes in `self.routes` and regex routes in `self.regex_routes`.

Now we need to make the server actually use the regex routes when serving requests!

Please modify `server/server.py` to update the `handle_client` function:
1. When checking for a matching route, first check if `path` is in `self.routes`.
2. If the exact path doesn't exist in `self.routes`, you must iterate through `self.regex_routes` and use `re.match` to see if the requested path matches any of the stored regex patterns.
3. If a regex match is found, pass any regex capture groups (like `(.*)`) as arguments to the `handler` function. 

This will complete our Dynamic Regex Routing feature!
