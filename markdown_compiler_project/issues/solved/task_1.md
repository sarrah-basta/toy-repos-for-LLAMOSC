The current markdown compiler supports `**bold**` and `*italic*`, but it breaks when they are combined into `***nested***`.
Please modify `compiler/compiler.py` to support `***text***` and compile it into `<strong><em>text</em></strong>`.
