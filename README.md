# Enku Valut

![Logo](/src/assets/icon-128.png)

**NOTE : ENCRYPTION NOT IMPLEMENTED YET.**

Your secure, offline password manager. Keep all your passwords encrypted and stored locally. Organize, generate, and access passwords with ease. Protect your data and take control of your online security.

## Setup for Development

1. Create a python virtual env and activate

```bash
> python -m venv venv
> venv\Scripts\activate
```

2. Install necessary packages

```bash
> pip install -r requirements.txt
```

3. Run the app

```bash
> python main.py
```

## Build the exe yourself (for Windows)

You can build the exe using below command :

```bash
> pyinstaller main.py --name EnkuVault --onefile --windowed --add-data "src/assets/;."
```

Another method is to run from the spec file:

```bash
> pyinstaller EnkuVault.spec
```
