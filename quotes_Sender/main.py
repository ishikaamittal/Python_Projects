import random
import smtplib
import datetime as dt


my_mail = "ivannamacbeth01@gmail.com"
password = "@18"

current_day = dt.datetime.now()
weekday = current_day.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        any_quote = random.choice(quotes_list)
        print(any_quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs="arya@gmail.com ",
                                msg=f"Subject:\n\n{any_quote}")
