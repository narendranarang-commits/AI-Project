# Mistral AI Bot

Simple chatbot using the `mistralai` Python client.

Files:

- `mistral_bot.py` - Basic interactive chat client
- `advanced_mistral_bot.py` - Advanced chat client with commands
- `requirements.txt` - Python dependencies

Setup (Windows PowerShell):

```powershell
python -m venv venv
& ".\venv\Scripts\Activate.ps1"
pip install -r requirements.txt
```

Run:

```powershell
python mistral_bot.py
```

Security:

- Do not commit your API key. Instead set `MISTRAL_API_KEY` as an environment variable before running.
