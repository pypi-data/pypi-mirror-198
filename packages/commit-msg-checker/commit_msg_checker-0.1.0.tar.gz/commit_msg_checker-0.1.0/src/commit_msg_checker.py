import argparse
import re
import pathlib
import sys


REDMINE_TICKET_REGEX = re.compile(r"^\[\bREDMINE\b-\d+\]")
PASS = 0
FAIL = 1

TAGS = ["[FIX]", "[FEATURE]", "[REFACTOR]", "[DOCS]", "[INIT]", "[TEST]", "[ADD]", "[MERGE]"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    commit_msg = pathlib.Path(args.filename).read_text()

    print(commit_msg)

    if "[MERGE]" in commit_msg:
        return sys.exit(PASS)

    if not REDMINE_TICKET_REGEX.match(commit_msg):
        print("❌ [Aborted] The commit message should start with the redmine ticket number.")
        print("Example - [REDMINE-000][FIX] commit msg")

        return sys.exit(FAIL)

    result = None
    for tag in TAGS:

        if tag in commit_msg:
            result = tag

    if not result:
        print("❌ [Aborted] Commit tag must be the same as the example.")
        print(f"Example - {', '.join(TAGS)}")

        return sys.exit(FAIL)

    print(f"Commit Message : {commit_msg} ✅")
    return sys.exit(PASS)


if __name__ == "__main__":
    main()
