# BugSquancher
![logo](image.png)
## Overview
BugSquancher appends short, human-readable hints to terminal errors without changing how users run commands.

## Why It Exists
Terminal errors are loud and often unhelpful. BugSquancher adds a brief, structured hint block so you can decide what to try next without digging through long logs.

## What It Does
- Keeps the original output intact
- Appends a concise hint block at the end
- Avoids certainty and never auto-runs commands

## Output (Example)
```
before Bugsquancher

ModuleNotFoundError: No module named 'does_not_exist'

after Bugsquancher




Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'does_not_exist'
🛸 Bugsquancher detected a squanch
━━━━━━━━━━━━━━━━━━━━━━━
Command: python3 -c "import does_not_exist"

Exit Code: 1
Type: modulenotfounderror

Cause
A required Python package or local module could not be found.

Fix
Install the missing package or check your import path/module name.

Try
pip install <package_name>

Context
Run in your active virtual environment or fix the import statement.


```

## Install
```bash
pip install bugsquancher
bugsquancher init zsh
source ~/.zshrc
```

## Styles
- Default output is a clean diagnostic block.
- Set `BUGSQUANCHER_STYLE=2` for the squanchier Rick-and-Morty style.

## Notes
The shell hook is zsh-first right now.
