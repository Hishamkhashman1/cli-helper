# Capture output of terminal commands and pass failures to BugSquancher.

if command -v bugsquancher >/dev/null 2>&1; then
  BUGSQUANCHER_CMD=(bugsquancher run)
else
  BUGSQUANCHER_CMD=(python3 -m bugsquancher.cli run)
fi

OUTPUT_FILE=$(mktemp)

preexec() {
  LAST_COMMAND="$1"
  : > "$OUTPUT_FILE"
  exec {BUGSQUANCHER_STDOUT}>&1 {BUGSQUANCHER_STDERR}>&2
  exec > >(tee -a "$OUTPUT_FILE") 2>&1
}

precmd() {
  EXIT_CODE=$?

  if [[ -n ${BUGSQUANCHER_STDOUT:-} ]]; then
    exec >&$BUGSQUANCHER_STDOUT 2>&$BUGSQUANCHER_STDERR
    exec {BUGSQUANCHER_STDOUT}>&- {BUGSQUANCHER_STDERR}>&-
    unset BUGSQUANCHER_STDOUT BUGSQUANCHER_STDERR
  fi

  if (( EXIT_CODE > 0 )) && [[ -n ${LAST_COMMAND:-} ]]; then
    OUTPUT=$(<"$OUTPUT_FILE")
    printf '%s' "$OUTPUT" | "${BUGSQUANCHER_CMD[@]}" "$LAST_COMMAND" "$EXIT_CODE"
  fi
}

trap 'rm -f "$OUTPUT_FILE"' EXIT
