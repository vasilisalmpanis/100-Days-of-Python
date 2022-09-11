##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

templates = ["letter_templates/letter_1.txt", "letter_templates/letter_3.txt"]
now = dt.datetime.now()
todayday = now.day
todaymonth = now.month
data = pandas.read_csv('birthdays.csv')
dict = data.to_dict(orient="records")
for i in dict:
    if todayday == i["day"] and todaymonth == i["month"]:
        template = random.choice(templates)
        with open(template, "r") as text:
            mlk = text.read()
            x = mlk.replace("[NAME]", i["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="vasilisalmpanis@gmail.com", password="6980691434")
            connection.sendmail(from_addr="vasilisalmpanis@gmail.com", to_addrs=i["email"], msg=f"Subject: Happy Birthday"     
                                                                                                f"\n\n{text}")









