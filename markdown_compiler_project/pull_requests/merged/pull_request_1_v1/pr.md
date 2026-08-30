Here is the pull request:

Issue Summary: Fixed issue with nested markdown syntax, allowing for the compilation of `***nested***` into `<strong><em>text</em></strong>`.

Approach: Modified the `compiler/compiler.py` file to extend the existing markdown syntax to support nested bold and italic text. This was achieved by updating the regular expression patterns used to identify and parse the markdown syntax, allowing for the correct compilation of `***text***` into the desired HTML output.