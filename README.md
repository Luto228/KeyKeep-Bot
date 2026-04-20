# 🔐 KeyKeep-Bot

**KeyKeep-Bot** is a simple and lightweight Telegram bot designed to keep your passwords organized. It allows you to safely store account data (service, password, login) and retrieve it instantly.

## 🚀 Features
- **Local Storage**: All data is saved in a local SQLite database.
- **Quick Access**: Get your credentials by service name in a single command.
- **Minimalistic**: No fluff, just your passwords when you need them.

## 🛠 Commands
- `/start` — View the welcome message and basic instructions.
- `/add [service] [password] [login]` — Add a new entry.
- `/get [service]` — Retrieve all accounts for a specific service.

> [!NOTE]
> **Multiple Accounts Support**:
> You can now save multiple accounts for the same service (e.g., several Steam accounts). When you use `/get [service]`, the bot will return all accounts associated with that service.

## 🔜 Upcoming Features
In the next update, you will be able to delete accounts using the following commands:
- `/del [Service]` — Delete **ALL** accounts associated with that service.
- `/del [Service] [login]` — Delete a **specific** account from that service.


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