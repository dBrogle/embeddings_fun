# Project Title

Compare any phrase (or list of phrases) you want to states on a graph

You need an OpenAI api key for the embeddings. It saves all phrases'
embeddings so that it's both faster and doesn't burn unnecessary tokens.

Requirements:
OPENAI_API_KEY. You can search for it (Vscode: CMD+SHIFT+F) for "openai_api_key"
This should be in your environment. If you have this everything should run after
the setup instructions.
---

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Clone the repository

```bash
git clone git@github.com:dBrogle/embeddings_fun.git
cd embeddings_fun
```

*(If you prefer HTTPS instead of SSH:)*

```bash
git clone https://github.com/dBrogle/embeddings_fun.git
cd embeddings_fun
```

---

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

> **On Windows:**
> ```bash
> venv\Scripts\activate
> ```

---

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the project

```bash
python main.py
```

---

## Notes

- Make sure you're using **Python 3.8+** (or your project's required version).
- All required packages are listed in `requirements.txt`.
- If you encounter any issues, ensure your virtual environment is activated and that you have the correct Python version.
