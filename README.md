# LuckyPorter

LuckyPorter is a Python terminal utility intended to send and receive files using temporary network tunnels and command-line transfer tools. The repository includes a Python script, dependency list, logo, and example screenshots.

## Intended environment

The script is written for a Linux-style shell and expects tools and paths such as Bash, `/var/www/html`, `nc`, `wget`, and ngrok. It is not a portable desktop file-transfer application.

## Installation

Use an isolated Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The script also relies on system utilities. Review the source and dependency requirements before installing or running it.

## Run

```bash
python3 luckyporter.py
```

The workflow asks whether to send or receive files and may create a public tunnel. Only use it with files and systems you own or are explicitly authorized to administer.

## Security warning

This tool can copy files into a web server directory, open network tunnels, spawn shell processes, and invoke external transfer commands. The current implementation builds shell commands from interactive input and uses broad system-level operations. Do not run it with sensitive files, elevated privileges, or on an untrusted network. Review and harden path handling, command execution, authentication, transfer integrity, and cleanup before any real use.

See [architecture](docs/ARCHITECTURE.md), [operations](docs/OPERATIONS.md), [security](docs/SECURITY.md), and [development](docs/DEVELOPMENT.md).
