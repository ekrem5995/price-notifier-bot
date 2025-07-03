# 📦 Price Notifier Bot

A simple Python automation script that scrapes a product price from a website and sends an email alert.

---

## 🔧 Features

- Web scraping with `BeautifulSoup`
- Clean and modular codebase
- Secure credential handling with `.env`
- Sends price alert via Gmail SMTP

---

## 📸 Demo

```
Product: A Light in the Attic  
Price: £51.77  
Email sent successfully ✅
```

---

## ⚙️ Tech Stack

- Python 3
- BeautifulSoup
- requests
- python-dotenv
- smtplib (Gmail SMTP)

---

## 🛠 Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/price-notifier-bot.git
cd price-notifier-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your_app_password_here
TO_EMAIL=youremail@gmail.com
```

### 5. Run the bot

```bash
python main.py
```

---

## 📍 Example Site Used

- http://books.toscrape.com

---

## 🔒 Note

To use Gmail:
- Enable 2-Step Verification
- Create an App Password here: https://myaccount.google.com/apppasswords

---

## 📬 Output Example

```
Subject: Price Alert: A Light in the Attic  
Body: The product 'A Light in the Attic' is currently priced at £51.77.
```

---

## 📚 Folder Structure

```
price_notifier_bot/
├── utils/
│   ├── scraper.py
│   └── notifier.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 👤 Author

Built by Ekrem Bahadır KEF feel free to reach out on Upwork or GitHub.
