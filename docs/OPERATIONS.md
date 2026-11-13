# Operations and Transfer Workflow

## 1. Operational warning

This tool can copy files into a web server directory, open network tunnels, spawn shell processes, and receive data from remote endpoints. Only use it on systems you own or are explicitly authorized to administer. Never use it to access or transfer files from third-party systems without permission.

## 2. Prepare an isolated environment

Before running:
1. Use a disposable virtual machine or container with the required network capabilities.
2. Create a dedicated temporary directory for sample files.
3. Populate it only with synthetic data.
4. Confirm the web-root path and listener ports are not used by another service.
5. Confirm that the tunnel account and endpoint belong to you.
6. Review the current script path that will execute for the selected menu option.

Do not run the script with elevated privileges. The current fixed path under `/var/www/html` may require permissions that should not be solved by running the whole program as root.

## 3. Send workflow as implemented

The current send branch asks for a port, requests an ngrok HTTP tunnel, configures tab completion, and prompts for one or more filenames. It then copies those files into `/var/www/html` and prints a command that a recipient can use to download the file.

### Exposure implications

- The copy operation places data in a web-served directory.
- The tunnel may make the web server reachable from outside the local machine.
- Anyone who obtains the URL may be able to download exposed files.
- A copied file may remain in the web root after the session.
- The script does not provide a complete access-control or expiry policy for each file.

Only use a temporary web root containing synthetic files. After the test, stop the tunnel and server, remove copied test files, and verify that the URL no longer works.

## 4. Receive workflow as implemented

The receive branch asks the user to select netcat, wget, or curl. It then collects a filename and additional connection information. Depending on the selection, it can start a local listener or invoke a download command.

### Receive-side risks

- A remote sender may provide unexpected content.
- Destination paths may overwrite existing files if not validated.
- A listener can accept data from an unintended source if exposed.
- The script does not comprehensively verify the sender, content type, size, or checksum.
- A transfer can be interrupted while leaving a partial file.

Use an empty temporary directory and unique test filenames. Do not receive executable files from untrusted sources.

## 5. Port selection

Use a port that is not occupied by another process. Do not assume a port is reachable through local or external firewalls. The current script does not provide a complete port availability check or a robust retry strategy.

## 6. Tunnel credentials

If a tunnel authentication token is required, enter it only through the intended private interactive prompt. Do not paste it into a public issue, commit, shell command stored in history, screenshot, or log. Rotate the token if it is accidentally disclosed.

## 7. Process lifecycle

Track all processes started by the workflow:
- Local HTTP server.
- Netcat listener.
- Spawned Bash process.
- ngrok tunnel process.

Stop them after the transfer. Confirm no listener remains active and no public tunnel remains connected. The current script's cleanup behavior is not sufficiently comprehensive to assume this happens automatically.

## 8. Post-transfer cleanup

1. Stop the transfer process.
2. Close the tunnel.
3. Stop the HTTP server or netcat listener.
4. Remove temporary copied and received files.
5. Inspect the web root for leftovers.
6. Verify the public URL is no longer accessible.
7. Rotate credentials if they were exposed.
8. Record only sanitized operational details.

## 9. Operational acceptance criteria

A controlled test is complete only when the expected sample file arrives, its checksum matches, the service is stopped, the tunnel is closed, and temporary files are removed. The current application does not automate all of these checks.
