from utils.scraper import get_product_price
from utils.notifier import send_email_notification

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

title, price = get_product_price(url)
subject = f"Price Alert: {title}"
body = f"The product '{title}' is currently priced at {price}."

print("[INFO] Sending email notification...")
if send_email_notification(subject, body):
    print("[SUCCESS] Email sent!")
else:
    print("[ERROR] Failed to send email.")
