import sys

#Entry point (orchestrator)

# read the passed output in bugsquancher.zsh
    # sys.argv --> metadata (command is sys.argv[1], exit code is sys.argv[2])
    # sys.stdin --> actual error output sys.stdin.read()
command = sys.argv[1]
exit_code = sys.argv[2]
output = sys.stdin.read()

# call the parser  (to clean and extract useful info from the raw output)

# call the matcher

# call the formatter

# print final result
