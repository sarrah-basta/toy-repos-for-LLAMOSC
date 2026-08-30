Here is the pull request based on the provided diff file:

Issue Summary: We need support for blockquotes.

Approach:
In this pull request, I have modified the `compiler/compiler.py` file to support blockquotes. Specifically, I have updated the code to wrap any line starting with `> ` in `<blockquote>...</blockquote>` instead of `<p>...</p>`. This change allows for proper rendering of blockquotes in our compiler.