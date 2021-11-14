from os import error
from instagrapi import Client
from flask import Flask,jsonify
import json
import csv
import random


with open(f"Instagram Scraper Profiles - Instagram_Accounts (2).csv",'r',encoding="utf8") as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader, None)
        print("plz wit ....   while we are generaring session id's for peovided accountd\n will notify you as soon as the process complete")

        print()
        instagramProfiles=[]
        for i in csv_reader:
            USERNAME=i[2]
            PASSWORD=i[3]
            print(f'Getting Session id for this :-{USERNAME,PASSWORD}')
            print("")
            try:

                cl=Client()
                cl.login(USERNAME,PASSWORD)
                instagramProfiles.append(cl.get_settings())
            except:
                print("account not loggin")
print("we are done with the session id's now you  can proceed to submit button ")
print(f'{len(instagramProfiles)} no.  of session ids are there')
print((instagramProfiles))