# LuckyPorter, Experimental Python File-Transfer Utility

LuckyPorter is an experimental terminal-based Python utility intended to support sending and receiving files through temporary network tunnels and command-line transfer tools. The repository contains one main Python script, a dependency list, sample files, a logo, and screenshots.

The program presents a menu for sending or receiving files. Depending on the selected path, it uses ngrok to create a tunnel, interacts with shell processes through pexpect, and invokes external utilities such as a simple HTTP server, netcat, wget, or curl.

This project should be treated as a learning prototype. Its current implementation is not a hardened file-transfer service and should not be used to expose private files, transfer sensitive data, or operate on systems without explicit authorization.

> [!WARNING]
> **Security-sensitive behavior:** the script copies files into a web-server directory, starts public network tunnels, spawns shells, and constructs external commands from user input. These behaviors can expose data or execute unintended commands if inputs or environment assumptions are unsafe. Run only in a disposable, controlled environment with files you own and never with elevated privileges.

## Features visible in the current source

- Interactive terminal menu with send, receive, and exit options.
- File selection using terminal input and path completion.
- Tunnel creation through the ngrok Python package.
- A send path that copies selected files into `/var/www/html` and displays a download command.
- Receive paths that offer netcat, wget, or curl-related workflows.
- Terminal color helper functions.
- Shell process interaction through pexpect.

These are descriptions of code paths, not guarantees that every path works on every operating system or current version of its external tools.

## Technology and environment

| Component | Role |
|---|---|
| Python 3 | Main program |
| pyngrok | Create and manage ngrok tunnels |
| pexpect | Spawn and interact with child processes |
| keyboard | Keyboard interaction dependency |
| readline / glob | Terminal path completion |
| Bash | Shell expected by parts of the script |
| netcat | One of the receive transfer options |
| wget / curl | Command-line transfer tools |
| SimpleHTTPServer invocation | Legacy Python HTTP serving command in current source |

The script is Linux-oriented. It uses paths and commands that are not portable to every operating system. In particular, the current source invokes `python -m SimpleHTTPServer`, which is a Python 2-era module name and is not available as written in standard Python 3. A modern Python 3 environment normally uses `http.server`, but changing the implementation is a source-code task and is not silently applied here.

## Repository layout

```text
.
├── luckyporter.py
├── requirements.txt
├── assets/
│   ├── logo/
│   └── Screenshots/
└── testing_files/
```

## Requirements

- Python 3.
- Linux-like shell environment for the paths and commands currently used.
- Network access for tunnel creation.
- ngrok account and authentication token when the selected workflow requires it.
- System utilities required by the chosen transfer path.
- A disposable directory containing non-sensitive sample files.

Review the script and its dependencies before installing or running it.

## Installation

Create an isolated Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Python package installation does not install every system utility used by the script. Confirm that the required shell and transfer tools are installed separately. Do not install dependencies globally or run the program as root.

## Run

```bash
python3 luckyporter.py
```

The program clears the terminal and displays an interactive menu. Choose a send or receive workflow only after reviewing the exact source path that will execute. Use a temporary test directory and synthetic files.

## Operational model

The send workflow asks for a port and selected filenames, creates a tunnel, copies files into a web-root directory, and displays a remote download command. This can make the copied files publicly reachable through the tunnel.

The receive workflow asks for a transfer method and destination filename. Depending on the selection, it can start a local listener or download from a remote address. These operations involve shell commands and external network endpoints.

See [operations guide](docs/OPERATIONS.md) for the current flow and [security review](docs/SECURITY.md) for the risks and containment requirements.

## Security requirements for safe experimentation

1. Use only a disposable virtual machine or isolated test environment.
2. Use sample files with no personal or confidential information.
3. Never run as root or with administrator privileges.
4. Never expose a production web root.
5. Never paste tokens into public issues, source files, shell history, or screenshots.
6. Confirm every file path and remote endpoint before starting a transfer.
7. Stop the tunnel and child processes after the test.
8. Remove temporary copies and verify the files are no longer reachable.
9. Do not use the tool against systems or networks without authorization.

## Known implementation limitations

- Shell commands are built using user-provided values in several code paths.
- File copies use a fixed web-root location.
- Public tunnel URLs can expose copied content to anyone who obtains the URL.
- The current HTTP server command uses a legacy Python module name.
- Transfer completion and file integrity are not comprehensively verified.
- Cleanup of temporary files, tunnels, and child processes is not consistently guaranteed.
- Platform assumptions are not abstracted.
- There is no automated transfer integration test suite.
- The dependency list and imported modules should be reviewed for compatibility and necessity.

## Validation

The CI workflow runs Python bytecode compilation:

```bash
python -m py_compile luckyporter.py
```

This catches syntax errors. It does not start tunnels, run shell commands, open ports, or transfer files. Do not add public network operations to CI merely to make the workflow appear more comprehensive.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Operations and transfer flow](docs/OPERATIONS.md)
- [Security review](docs/SECURITY.md)
- [Development guide](docs/DEVELOPMENT.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Security policy](SECURITY.md)
- [Contribution guide](CONTRIBUTING.md)

Last updated: 2026-11-14 07:23 UTC
