# Development

Create an isolated environment and install the packages listed in `requirements.txt`. Review the required operating-system commands separately; Python package installation alone does not provide Bash, netcat, wget, or an ngrok account.

Run a syntax check:

```bash
python -m py_compile luckyporter.py
```

Do not test with private files or public systems. Use a temporary directory, synthetic sample data, and a tunnel configured for a controlled test. Add unit tests for input validation and command construction before changing transfer behavior.
