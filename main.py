import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "ENTER EMAIL HERE"
email_smtp = "ENTER SMTP HERE"
password = "ENTER PASSWORD HERE"
addressee = "ENTER ADDRESSEE EMAIL HERE"

today = dt.datetime.now()
today = (today.month, today.day)


df = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_text = letter_file.read()
        new_letter = letter_text.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(email_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=addressee, msg=f"Subject:Happy Birthday\n\n "
                                                                                       f"{new_letter}")


