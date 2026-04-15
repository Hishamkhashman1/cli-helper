from __future__ import annotations

import argparse
import sys
from importlib import resources
from pathlib import Path

try:
    from .formatter import format_hint
    from .matcher import match_pattern
    from .parser import parse_output
except ImportError:  # pragma: no cover - compatibility for direct file execution
    from formatter import format_hint
    from matcher import match_pattern
    from parser import parse_output


CONFIG_DIR = Path.home() / ".config" / "bugsquancher"
CONFIG_SHELL_PATH = CONFIG_DIR / "bugsquancher.zsh"
ZSHRC_PATH = Path.home() / ".zshrc"
ZSHRC_BEGIN = "# >>> bugsquancher >>>"
ZSHRC_END = "# <<< bugsquancher <<<"


def run_pipeline(command: str, exit_code: str | int, output: str) -> str | None:
    parsed = parse_output(output)
    matched_pattern = match_pattern(parsed)
    return format_hint(command, exit_code, matched_pattern)


def run_from_stdin(command: str, exit_code: str | int) -> int:
    hint = run_pipeline(command, exit_code, sys.stdin.read())
    if hint:
        print(hint)
    return 0


def _shell_template_text() -> str:
    shell_path = resources.files("bugsquancher").joinpath("shell/bugsquancher.zsh")
    return shell_path.read_text(encoding="utf-8")


def _rewrite_zshrc(source_line: str, remove: bool = False) -> None:
    if not ZSHRC_PATH.exists():
        if remove:
            return
        ZSHRC_PATH.write_text("", encoding="utf-8")

    current = ZSHRC_PATH.read_text(encoding="utf-8")
    block = f"{ZSHRC_BEGIN}\n{source_line}\n{ZSHRC_END}\n"

    if remove:
        if ZSHRC_BEGIN not in current:
            return
        lines = current.splitlines()
        rebuilt: list[str] = []
        skipping = False
        for line in lines:
            if line.strip() == ZSHRC_BEGIN:
                skipping = True
                continue
            if line.strip() == ZSHRC_END:
                skipping = False
                continue
            if not skipping:
                rebuilt.append(line)
        ZSHRC_PATH.write_text("\n".join(rebuilt).rstrip() + ("\n" if rebuilt else ""), encoding="utf-8")
        return

    if ZSHRC_BEGIN in current and source_line in current:
        return

    with ZSHRC_PATH.open("a", encoding="utf-8") as handle:
        if current and not current.endswith("\n"):
            handle.write("\n")
        handle.write(block)


def install_zsh_hook() -> Path:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_SHELL_PATH.write_text(_shell_template_text(), encoding="utf-8")
    _rewrite_zshrc(f"source {CONFIG_SHELL_PATH}")
    return CONFIG_SHELL_PATH


def uninstall_zsh_hook() -> None:
    if CONFIG_SHELL_PATH.exists():
        CONFIG_SHELL_PATH.unlink()
    _rewrite_zshrc(f"source {CONFIG_SHELL_PATH}", remove=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bugsquancher", description="Append human-readable hints to terminal errors.")
    subparsers = parser.add_subparsers(dest="subcommand")

    run_parser = subparsers.add_parser("run", help="Format captured command output.")
    run_parser.add_argument("input_command")
    run_parser.add_argument("exit_code")

    init_parser = subparsers.add_parser("init", help="Install a shell hook.")
    init_parser.add_argument("shell", choices=["zsh"])

    uninstall_parser = subparsers.add_parser("uninstall", help="Remove a shell hook.")
    uninstall_parser.add_argument("shell", choices=["zsh"])

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.subcommand == "run":
        return run_from_stdin(args.input_command, args.exit_code)

    if args.subcommand == "init":
        path = install_zsh_hook()
        print(f"Installed zsh hook at {path}")
        print(f"Add this to your shell startup once if needed: source {path}")
        return 0

    if args.subcommand == "uninstall":
        uninstall_zsh_hook()
        print("Removed Bugsquancher zsh hook")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
