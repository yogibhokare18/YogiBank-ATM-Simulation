# 🏦 YogiBank ATM Simulation

A simple and interactive **ATM Simulation System using Python** with a colorful terminal interface powered by the Rich library.

This project simulates basic ATM operations such as checking account balance, withdrawing money, depositing money, and changing the ATM PIN.

## ✨ Features

* 🔐 **PIN Authentication** — Login using an ATM PIN.
* 💰 **Check Balance** — Display the current account balance.
* 📤 **Withdraw Money** — Withdraw money with balance validation.
* 📥 **Deposit Money** — Deposit money and update the balance.
* 🔑 **Change PIN** — Change the existing PIN.
* ❌ **Invalid Input Handling** — Handle invalid menu choices and transaction amounts.
* 🎨 **Colorful Terminal UI** — Styled tables, panels, colors, and icons using Rich.
* 🚪 **Exit Option** — Exit the ATM simulation safely.

## 🛠️ Technologies Used

* Python
* Rich Library
* Command-Line Interface (CLI)

## 📂 Project Structure

```text
ATM-Simulation/
│
├── atm.py
└── README.md
```

## ⚙️ Installation

### Step 1: Install Python

Install Python if it is not already installed on your computer.

Check the Python version:

```bash
python --version
```

### Step 2: Clone the Repository

If this project is uploaded to GitHub, clone it using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the project and open its folder in VS Code.

### Step 3: Install Required Library

Open the terminal and run:

```bash
pip install rich
```

## ▶️ How to Run

Navigate to the project folder and execute:

```bash
python atm.py
```

## 🔑 Default Login Details

| Field           | Value   |
| --------------- | ------- |
| Initial PIN     | `1122`  |
| Initial Balance | ₹10,000 |

**Note:** These are demo values for testing and learning purposes.

## 📋 ATM Menu

| Option | Operation      |
| ------ | -------------- |
| 1      | Check Balance  |
| 2      | Withdraw Money |
| 3      | Deposit Money  |
| 4      | Change PIN     |
| 5      | Exit           |

## 💻 Sample Output

```text
╭──────────────────────────────╮
│       🏦 YOGIBANK ATM 🏦     │
│      SMART BANKING SYSTEM    │
╰──────────────────────────────╯

Enter your ATM PIN: 1122

✔ Login Successful!

          💳 ATM SERVICES
╭────────┬─────────────────────╮
│ Option │ Service             │
├────────┼─────────────────────┤
│   1    │ 💰 Check Balance    │
│   2    │ 📤 Withdraw Money   │
│   3    │ 📥 Deposit Money    │
│   4    │ 🔐 Change PIN       │
│   5    │ 🚪 Exit             │
╰────────┴─────────────────────╯
```

*The actual appearance depends on your terminal and Rich library rendering.*

## 📚 Learning Outcomes

By building this project, you can practice:

* Python variables and data types
* Conditional statements (`if`, `elif`, `else`)
* Loops (`while`)
* User input and output
* Arithmetic operations
* Functions and library imports
* Input validation
* Building a styled command-line interface

## ⚠️ Limitations

* The account balance and PIN are stored in program memory.
* Data resets when the program restarts.
* This project is intended for learning and demonstration, not real banking.
* It does not use a database or secure banking authentication.

## 🚀 Future Improvements

* Add transaction history.
* Store account information in MySQL or SQLite.
* Add multiple user accounts.
* Add secure PIN storage.
* Generate transaction receipts.
* Add a graphical user interface.

## 👨‍💻 Author

**Yoginand Bhokare**

GitHub: [@yogibhokare18](https://github.com/yogibhokare18)

Instagram: [@codewithyogi_2005](https://www.instagram.com/codewithyogi_2005/)

---

⭐ If you find this project useful, consider giving the repository a star!

**Made with ❤️ using Python**
