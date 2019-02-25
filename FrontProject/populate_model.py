import os
# Changes the environ to project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FrontProject.settings')
import django
django.setup()
# It will setup the environ settings 

import random
from faker import Faker
from lifeApp.models import Topic,WebPage,AccessRecord

fakgen=Faker()
topics=['Admin','Social','blog','Network','Forum']

def add_topic():
    top=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    top.save()
    return top


def populate(n=5):
    for i in range(n):
        top=add_topic()
        fake_webname=fakgen.company()
        fake_url=fakgen.url()
        fake_date=fakgen.date()

        web_page=WebPage.objects.get_or_create(web_name=fake_webname,topic=top,url=fake_url)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=web_page,date=fake_date)
    

if __name__=='__main__':
    print("populating the data")
    populate(15)
    print("Completed..!!")





