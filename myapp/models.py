from django.db import models

class clothes(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='clothes_image/')

    def __str__(self) :
        return self.name
    
class shoe(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='shoe_image/')

    def __str__(self) :
        return self.name
    
class wristwatch(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='wristwatch_image/')

    def __str__(self) :
        return self.name
    
class bag(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='bag_image/')

    def __str__(self) :
        return self.name
    
class sunglas(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='sunglas_image/')

    def __str__(self) :
        return self.name
    
class accessory(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='accessory_image/')

    def __str__(self) :
        return self.name
    

class global_brand(models.Model):
    name = models.CharField(max_length=30)
    brand_name = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='accessory_image/')

    def __str__(self) :
        return self.name