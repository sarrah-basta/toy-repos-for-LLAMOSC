Here is the template for the pull request:

Issue Summary:
Implement Dynamic Regex Routing

Approach:
Modifies the `handle_client` function to first check for exact matching routes in `self.routes`, and if no match is found, iterates through `self.regex_routes` using `re.match` to find regex pattern matches. If a regex match is found, passes regex capture groups as arguments to the `handler` function.

Changes:
- Updated `handle_client` function to handle regex routes
- Improved routing logic for dynamic regex routing
- Enhanced code readability and maintainability

PR Title: Implement Dynamic Regex Routing Feature

PR Description: This pull request implements the dynamic regex routing feature, allowing the server to use regex routes in addition to exact matching routes. The updated `handle_client` function now checks for regex pattern matches in `self.regex_routes` when no exact match is found in `self.routes`.