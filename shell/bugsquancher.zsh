# Capture Output of terminal (commands, output and exit status) detect failure and pass data to Python


# hook into zsh lifecycle

  # detect failed command
  preexec() {
    LAST_COMMAND="$1" # $1 is the command about to be executed
  }
  # capture output
  precmd() {
    EXIT_CODE=$?
    if ((EXIT_CODE >0)); then
      # call python with variables
      python3 /path/to/bugsquancher.py "$LAST_COMMAND" "$EXIT_CODE"
      fi
  }


# print appended output
