# 🛸 BugSquancher

Terminal errors suck.
You get 50 lines of noise… and still have to Google the fix.

**BugSquancher adds a short, human-readable explanation directly in your terminal.**

---

## Example

### Before

```
ModuleNotFoundError: No module named 'does_not_exist'
```

### After

```
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

---
![logo](image.png)
##  What it does

* Keeps your original terminal output intact
* Appends a **clean, structured hint block**
* Gives:

  * Cause
  * Fix
  * Try (command)
  * Context
* No guessing, no AI hallucination, no auto-execution

---

## 🧱 How it works

* Hooks into your shell (`zsh`)
* Detects failed commands (exit code > 0)
* Captures:

  * command
  * output
  * exit code
* Passes everything to a Python analyzer
* Matches known patterns
* Prints a **human-readable summary at the end**

---

## 📦 Install

```
pipx install git+https://github.com/Hishamkhashman1/bug-squancher
bugsquancher init zsh
source ~/.zshrc

```

---

## 🎨 Styles

Default = clean diagnostic output

Optional:

```
export BUGSQUANCHER_STYLE=2
```

👉 enables a more “squanchy” / themed output

---

## ⚠️ Notes

* Currently **zsh-first**
* Pattern-based (no AI dependency)
* Designed to be:

  * fast
  * predictable
  * useful under pressure

---

## 🧠 Philosophy

This is not meant to replace debugging.

It’s meant to answer:

> “What should I try next?”

without leaving your terminal.

---

## 🛠 Roadmap

* More error patterns (Python, Node, DBs)
* Smarter matching (confidence scoring)
* Optional AI fallback
* Bash / Fish support

---

## 💬 Contributing

Found an error pattern worth adding?

Open an issue or PR — patterns are simple and easy to extend.

---

## 🔥 Status

Actively being built and tested.

Early feedback is very welcome.
