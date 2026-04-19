# 🔐 KeyKeep-Bot

**KeyKeep-Bot** is a simple and lightweight Telegram bot designed to keep your passwords organized. It allows you to safely store account data (service, password, login) and retrieve it instantly.

## 🚀 Features
- **Local Storage**: All data is saved in a local SQLite database.
- **Quick Access**: Get your credentials by service name in a single command.
- **Minimalistic**: No fluff, just your passwords when you need them.

## 🛠 Commands
- `/start` — View the welcome message and basic instructions.
- `/add [service] [password] [login]` — Add a new entry.
- `/get [service]` — Retrieve data for a specific service.

> [!WARNING]
> **Important Limitation:**
> Currently, the bot does not support saving two different passwords for the same service name. If you want to save multiple accounts for the same service (e.g., Steam), use unique identifiers.

### Example (Current Workaround):
```text
/add steam_first 1234 Alex
/add steam_two 12345 LoveChairs
```

**This is a temporary limitation and will be fixed in an upcoming update!**

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Luto228/KeyKeep-Bot.git
   ```
2. **Install dependencies:**
   ```bash
   pip install aiogram
   ```
3. **Configure the bot:**
   - Locate the file `config.py.example`.
   - Rename it to `Config.py` (remove the `.example` extension).
   - Open `Config.py` and replace `"YOUR_TOKEN_BOT"` with your actual Telegram Bot Token.
4. **Run the bot:**
   ```bash
   python bot.py
   ```

---
*Built with ❤️ and code.*