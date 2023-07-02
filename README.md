# Enku Valut

![Logo](/src/assets/icon-128.png)

**NOTE : ENCRYPTION NOT IMPLEMENTED YET.**

Your secure, offline password manager. Keep all your passwords encrypted and stored locally. Organize, generate, and access passwords with ease. Protect your data and take control of your online security.

## Build the exe yourself (for Windows)

You can build the exe using below command :

```bash
> pyinstaller main.py --name EnkuVault --onefile --windowed --add-data "src/assets/;."
```

Another method is to run from the spec file:

```bash
> pyinstaller EnkuVault.spec
```
