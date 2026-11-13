# Contributing

- Work only in an authorized test environment with files you own.
- Explain any changes to transfer commands, tunnel lifecycle, file paths, or permissions.
- Avoid shell command construction from untrusted input.
- Add tests for path validation, cancellation, failures, cleanup, and transfer integrity.
- Never include tokens, private files, or real network endpoints in commits or issue reports.
- Run Python syntax validation before submitting changes.

Security-sensitive changes require careful review. Do not add stealth, persistence, credential collection, or unauthorized access functionality.
