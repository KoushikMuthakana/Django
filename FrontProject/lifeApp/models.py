from django.db import models

class Topic(models.Model):
    topic_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.topic_name

        
class WebPage(models.Model):
    web_name=models.CharField(max_length=40,unique=True)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.web_name +"   " + str(self.url)
    
class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date )+" ," +str(self.name.url)



