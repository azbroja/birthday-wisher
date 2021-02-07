import smtplib
import random
import pandas as pd
import datetime as dt

now = dt.datetime.now()
today_month = now.month
today_day = now.day

my_email = "email@gmail.com"
password = "password"

birthdays_dict = {}
with open("birthdays.csv") as data:
    dict_data = pd.read_csv(data)
    birthdays_dict = {(row.month, row.day): row for (
        index, row) in dict_data.iterrows()}

if (today_month, today_day) in birthdays_dict:
    name = str(birthdays_dict[(today_month, today_day)]["name"])
    email = str(birthdays_dict[(today_month, today_day)]["email"])

    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_tmp = letter.read()
        letter_tmp = letter_tmp.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email, msg=f"Subject:Happy Birthday :)\n\n{letter_tmp}.")
