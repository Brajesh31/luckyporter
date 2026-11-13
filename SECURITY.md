# Security Policy

## Reporting

Report vulnerabilities privately through GitHub's security reporting feature where available. Do not publish live tunnel addresses, access tokens, private files, or exploit steps against third-party systems.

## Risk profile

The current script can spawn shells, copy files into a web root, launch network tunnels, and invoke utilities such as netcat and wget. It interpolates user-controlled values into shell commands in several places. This creates command-injection and unintended file exposure risks.

## Safe operation

- Run only on systems you own or are authorized to test.
- Use a disposable directory and non-sensitive sample files.
- Never run as root.
- Do not expose `/var/www/html` or a tunnel containing private files.
- Keep ngrok credentials out of source code, shell history, logs, and screenshots.
- Stop tunnels and child processes after each transfer.
