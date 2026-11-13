# Troubleshooting

## Python package import fails

Activate the project virtual environment and install the requirements:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

If a package is unavailable, check the supported Python version and package name. Do not install unrelated similarly named packages without verifying their provenance.

## `SimpleHTTPServer` module is missing

The current source invokes `python -m SimpleHTTPServer`, which is associated with Python 2. Standard Python 3 uses the `http.server` module. This is a known source compatibility issue. A source-code change is needed; documentation does not patch the running command.

## Permission denied copying to web root

The send path uses `/var/www/html`. Do not run the entire application as root to bypass the error. Use an isolated test web root with permissions restricted to the test user, or change the implementation to use a dedicated safe workspace.

## Tunnel creation fails

Check network connectivity, ngrok account configuration, authentication token validity, and whether the selected port is available. Do not publish the token or tunnel URL in logs or issue reports.

## Download URL cannot be reached

Confirm the local server started, the selected port is correct, the tunnel is active, and the copied sample file exists in the expected web root. Remember that a tunnel exposes the service externally. Stop it after testing.

## Netcat command is unavailable

Install a trusted netcat implementation for the test environment if that path is required. Different distributions provide different variants and command flags. Confirm compatibility before relying on a particular invocation.

## File transfer is incomplete

Check both process exit status and received file size. The current implementation does not provide comprehensive transfer verification. Use checksums on synthetic files and do not trust a success message alone.

## File already exists

Use a fresh test filename and directory. The current implementation does not guarantee safe no-overwrite behavior. Do not risk overwriting user files.

## Program behaves differently outside Linux

The script uses Linux-specific paths and shell commands. It is not documented as cross-platform. Use a supported Linux environment or refactor platform-specific behavior behind explicit adapters.

## Process or tunnel remains running

Inspect active child processes and tunnel sessions, then stop only the processes created for your test. Check the web root and remove temporary sample files. Current cleanup is not guaranteed on every exit path.

## CI passes but a transfer fails

CI only runs Python syntax compilation. It does not install every system utility, start tunnels, open network ports, or test file transfer. A passing syntax check is not evidence of operational correctness.
