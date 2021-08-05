import random
import smtplib
import datetime as dt

import pandas


my_mail = "ivannamacbeth1801@gmail.com"
password = "ishika@18"
#
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_mail, password=password)
#    connection.sendmail(from_addr=my_mail, to_addrs="mittallishika18@gmail.com", msg="PARVI vaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#
current_day = dt.datetime.now()
weekday = current_day.weekday()
if weekday == 2:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        any_quote = random.choice(quotes_list)
        print(any_quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs="arya.mayank2001@gmail.com ",
                                msg=f"Subject: motivate hojao bkl\n\n{any_quote}")
