from django.db import models



class status(models.Model):
    status=models.CharField(max_length=10,default="Demo",null=True,blank=True)
    def __str__(self):
        return self.status
    


class video(models.Model):
    video_title=models.CharField(max_length=500,default="",null=True)
    chapter_name=models.CharField(max_length=500,default="")
    video=models.FileField(upload_to="Media")
    status=models.ForeignKey("status", on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.video_title
    
class short_video(models.Model):
    video_title=models.CharField(max_length=500,default="",null=True)
    chapter_name=models.CharField(max_length=500,default="")
    video=models.FileField(upload_to="Media")
    status=models.ForeignKey("status", on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.video_title
    
class pdf(models.Model):
    pdf_title=models.CharField(max_length=500,default="",null=True)
    chapter_name=models.CharField(max_length=500,default="")
    pdf=models.FileField(upload_to="Media")
    status=models.ForeignKey("status", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.pdf_title
    
class eleventh(models.Model):
    Sno=models.CharField(max_length=50)
    chapter_name=models.CharField(max_length=500)
    pdfs=models.ManyToManyField(pdf,null=True,blank=True)
    videos=models.ManyToManyField(video,null=True,blank=True)
    def __str__(self):
        return self.chapter_name
    
class twelveth(models.Model):
    Sno=models.CharField(max_length=50)
    chapter_name=models.CharField(max_length=500)
    pdfs=models.ManyToManyField(pdf,null=True,blank=True)
    videos=models.ManyToManyField(video,null=True,blank=True)
    def __str__(self):
        return self.chapter_name

class order(models.Model):
    chapter=models.CharField(max_length=500,null=True)
    order_id=models.CharField(max_length=500,null=True)
    flag=models.CharField(max_length=500,default="False")
    

class mycart(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    eleven=models.ManyToManyField("eleventh",null=True)
    twelve=models.ManyToManyField("twelveth",null=True)

class ouruser(models.Model):
    username=models.CharField(null=True, max_length=50)  
    password=models.CharField(null=True,max_length=50)
    counter=models.IntegerField(null=True,default=0)
    eleven=models.ManyToManyField("eleventh", null=True,blank=True)
    twelve=models.ManyToManyField("twelveth",null=True,blank=True)
    userorder=models.ManyToManyField("order",null=True,blank=True)
    razorpay_payment_id=models.CharField(max_length=500,default="" ,null=True,blank=True)
    razorpay_order_id=models.CharField(max_length=500,default="" ,null=True,blank=True)
    razorpay_signature=models.CharField(max_length=500,default="", null=True,blank=True)




 





# Create your models here.
