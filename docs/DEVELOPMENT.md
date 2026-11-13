# Development Guide

## 1. Supported development approach

The current script is designed around a Linux-like shell environment. Use an isolated Linux VM for development and testing. The source references `/var/www/html`, Bash, and common command-line transfer utilities. These assumptions are not portable to all operating systems.

## 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Do not install project dependencies globally. Review the dependency list and package provenance before installation.

## 3. System tools

The script expects system tools in addition to Python packages. Verify which transfer paths are needed in the current environment and install only the tools required for controlled testing. Do not run the program with elevated privileges to work around permissions.

## 4. Syntax validation

```bash
python -m py_compile luckyporter.py
```

This command compiles the source to bytecode without executing its network or filesystem behavior. It is the check used by CI.

## 5. Safe local testing

Use a disposable directory and synthetic text files. Do not point the program at a home directory, production web root, shared drive, or directory containing secrets. Before testing a path, inspect the exact copy and shell commands in the selected code branch.

Do not start public tunnels during routine unit tests. Mock the tunnel API and child-process boundary.

## 6. Editing command execution

When changing command execution:
- Avoid `os.system` and shell command interpolation.
- Prefer Python filesystem APIs or subprocess argument arrays.
- Validate ports as integers in the permitted range.
- Resolve and constrain file paths.
- Check process exit codes.
- Add timeouts.
- Capture and sanitize output.
- Guarantee cleanup on exceptions and cancellation.

## 7. Testing strategy

Unit-test path validation, command argument construction, transfer state transitions, and cleanup behavior. Mock ngrok and pexpect in unit tests. Integration tests should run only in a private, controlled environment with synthetic files and no public exposure.

## 8. Dependency management

Keep `requirements.txt` synchronized with actual imports. Remove unused dependencies only after verifying their use across all branches. Use version constraints that are tested against the supported Python version. Do not blindly upgrade dependencies in the same change as security-sensitive process refactoring.

## 9. Pull request expectations

Every change should describe:
- Which send/receive path is affected.
- Which operating systems and tool versions were used.
- How command execution and paths were validated.
- How processes and tunnels are cleaned up.
- Whether any network or filesystem exposure changes.
- Which tests were run.

Never include tunnel tokens, public endpoints, or private file contents in pull requests.
