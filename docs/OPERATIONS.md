# Operations

This project should be treated as an experimental local utility.

1. Use a disposable Linux environment.
2. Review the full script before execution.
3. Install only the required packages from a trusted source.
4. Prepare a dedicated temporary directory containing non-sensitive sample files.
5. Confirm the selected transfer destination and tunnel exposure before proceeding.
6. Monitor spawned child processes and terminate them after use.
7. Remove temporary copies and verify that public web roots do not retain transferred files.

The script references `/var/www/html` and invokes shell commands. Do not point it at a production web root or a directory containing private data.
