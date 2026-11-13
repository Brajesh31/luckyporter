# Security Review and Hardening Plan

## 1. Security posture

LuckyPorter should be considered an experimental, high-risk local utility. It combines filesystem access, shell execution, public tunnel creation, and network file transfer. The current implementation does not establish a strong trust boundary between user input, filesystem paths, shell commands, and remote endpoints.

Do not use it with sensitive information or on production systems.

## 2. Shell command construction

The script sends command strings to a spawned Bash process. User-controlled filenames, ports, and remote addresses are incorporated into those strings in several places. Shell interprets special characters, substitutions, pipes, redirections, and command separators.

A malicious or malformed value can therefore alter the command that executes. Interactive prompts do not make shell input safe.

### Safer implementation direction

- Prefer Python APIs for filesystem operations.
- Use `subprocess.run([...], shell=False)` for unavoidable external commands.
- Pass each argument separately.
- Validate values against strict formats.
- Do not interpolate arbitrary strings into shell scripts.
- Set timeouts and check exit codes.
- Capture output safely and redact secrets.

## 3. File path and web-root exposure

The send path copies selected files into `/var/www/html`. This is a broad exposure surface. A path may refer to a file outside the intended workspace, and a copied file may remain accessible after the transfer.

Recommended controls:
- Resolve paths and require them to remain beneath a dedicated transfer directory.
- Reject symbolic links unless their behavior is explicitly designed.
- Restrict file types and sizes where appropriate.
- Use a unique temporary directory for each transfer.
- Avoid a shared production web root.
- Remove temporary files on success, failure, and cancellation.
- Verify the web server cannot serve files outside the intended directory.

## 4. Public tunnel risk

A tunnel endpoint is externally reachable. Treat its URL as a temporary public access path, not as a secret authentication system. URLs can be copied, logged, or shared unintentionally.

Recommended controls:
- Require explicit confirmation before creating a tunnel.
- Limit tunnel lifetime.
- Bind the local server only to the required interface.
- Use an authenticated transfer service where access control is needed.
- Close tunnels in a guaranteed cleanup path.
- Do not expose directory listings or unrelated files.

## 5. Receive-side integrity

A downloaded or received file is untrusted input. The current implementation does not document a complete sender identity, checksum, file-size, or content validation policy.

Recommended controls:
- Receive only into a dedicated quarantine directory.
- Enforce a maximum file size.
- Compute and compare a trusted checksum.
- Do not execute received files.
- Avoid overwriting existing files by default.
- Record transfer metadata without logging sensitive content.

## 6. Credential handling

Tunnel authentication tokens must not be committed or embedded in source code. Avoid shell arguments and environment dumps that can reveal credentials. Use a secret manager or protected environment variable where appropriate, and rotate any token that may have been exposed.

## 7. Privilege and platform boundaries

Do not run the script as root. Avoid broad filesystem permissions. The current script assumes Linux paths and tools, so execution on other platforms may fail or behave differently. Platform differences should be handled explicitly rather than by weakening security controls.

## 8. Dependency and supply-chain review

Review each third-party dependency for:
- Maintainer and package provenance.
- Supported Python versions.
- Known vulnerabilities.
- Whether it is actually used.
- Whether it can be removed in favor of standard-library functionality.

Pinning dependencies and running a vulnerability scan are useful, but they do not replace code review of shell and filesystem behavior.

## 9. Safe testing

Use synthetic files in an isolated environment. Do not test against public systems without permission. Do not add live tunnel creation or file transfer to CI. Unit tests should mock tunnel and subprocess boundaries.

## 10. Priority hardening plan

1. Remove shell string interpolation.
2. Confine all file operations to a validated workspace.
3. Replace the legacy HTTP server command with a supported Python 3 implementation.
4. Add explicit tunnel creation confirmation and guaranteed teardown.
5. Add transfer size and checksum validation.
6. Add safe destination naming and no-overwrite behavior.
7. Add timeouts and child-process cleanup.
8. Add tests for malicious filenames, cancellation, and process failures.
9. Review dependencies and document supported platforms.
