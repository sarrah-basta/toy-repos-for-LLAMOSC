Here is the pull request:

Issue Summary: Add support for custom internal links using double brackets.

Approach: In this pull request, I modified the `compiler/compiler.py` file to parse `[[LinkText|URL]]` into `<a href="URL">LinkText</a>`. This allows users to create custom internal links using double brackets, making it easier to navigate within the documentation. The change is designed to improve the overall user experience by providing a convenient and intuitive way to link to other parts of the documentation.