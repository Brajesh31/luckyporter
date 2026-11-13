# Architecture

The application is a single interactive Python script.

- `luckyporter.py`: terminal menus, file selection, tunnel setup, shell spawning, and transfer command orchestration.
- `requirements.txt`: Python package requirements.
- `assets/`: logo and screenshots.
- `testing_files/`: sample transfer inputs.

The implementation integrates with ngrok for public tunnel creation, uses pexpect to spawn shell processes, and relies on system tools for serving or transferring files. The script expects Linux-specific paths and commands. There is no documented client/server protocol, persistent service, or automated transfer verification layer.
