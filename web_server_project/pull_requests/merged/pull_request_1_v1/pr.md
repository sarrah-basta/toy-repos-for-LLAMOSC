Here's a brief description of the changes made:

Issue Summary: 
Enhanced server.py to support dynamic regex routing.

Approach: 
Modified the `add_route` function to distinguish between exact string matches and regex patterns by checking for the presence of `<regex:` in the route path. This separation enables the server to store regex routes in `self.regex_routes` for future processing. The existing `self.routes` list remains unchanged for exact string matches. The modified `add_route` function has been successfully implemented and stored in the diff file.