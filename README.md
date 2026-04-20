# 🔐 KeyKeep-Bot

**KeyKeep-Bot** is a simple and lightweight Telegram bot designed to keep your passwords organized. It allows you to safely store account data (service, login, password) and retrieve it instantly.

## 🚀 Features
- **Local Storage**: All data is saved in a local SQLite database.
- **Quick Access**: Get your credentials by service name in a single command.
- **Multi-Account Support**: Store multiple accounts for the same service.
- **Easy Management**: Delete specific accounts or entire services with ease.

## 🛠 Commands
- `/start` — View the welcome message and basic instructions.
- `/add [service] [login] [password]` — Add a new entry.
- `/get [service]` — Retrieve all accounts for a specific service.
- `/del [service]` — Delete **ALL** accounts associated with that service.
- `/del [service] [login]` — Delete a **specific** account from that service.

> [!IMPORTANT]
> **New Update:**
> Please note that the order of arguments for the `/add` command has changed. Now you should enter:
> `/add [Service] [Login] [Password]`

> [!TIP]
> **Multiple Accounts Support**:
> You can save multiple accounts for the same service (e.g., several Steam accounts). When you use `/get [service]`, the bot will return all found records.

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
   - Rename it to `Config.py`.
   - Open `Config.py` and replace `"YOUR_TOKEN_BOT"` with your actual Telegram Bot Token.
4. **Run the bot:**
   ```bash
   python bot.py
   ```

---
*Built with ❤️ and code.*