## Quick Start on macOS: Running `server.py` with Flask & Flask-CORS

### 1. Check Python & pip
```bash
# Verify Python is installed
python3 --version

# Ensure pip is installed/upgraded
python3 -m ensurepip --upgrade
```
> If `python3` is not recognized, install it via [python.org](https://www.python.org/downloads/) or Homebrew (`brew install python`).

---

### 2. Navigate to Your Project Folder
```bash
cd HotBeansWeb
```

---

### 3. Create a Virtual Environment
```bash
python3 -m venv venv
```
This creates a `venv` folder that isolates your project’s packages.

---

### 4. Activate the Virtual Environment
```bash
source venv/bin/activate
```
Your terminal prompt should now show `(venv)` at the beginning.

---

### 5. Install Flask & Flask-CORS
```bash
pip install flask flask-cors
```
> If pip doesn’t work, try:
> ```bash
> python3 -m pip install flask flask-cors
> ```

---

### 6. Run Your Server
```bash
python server.py
```
You should see:
```
 * Serving Flask app 'server'
 * Running on http://127.0.0.1:5000
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to test.

---

### 7. Stop & Deactivate
- **Stop the server**: Press `Ctrl + C` in the terminal
- **Deactivate** the virtual environment:
  ```bash
  deactivate
  ```

That’s all! Your Flask server (with Flask-CORS) is now up and running on macOS.
