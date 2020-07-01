from django.db import models

# Create your models here.
CATEGORIES = (
    ('Food Nutrition', 'FoodNutrition'),
    ('Food Safety', 'FoodSafety'),
    ('Other Analysis', 'OtherAnalysis'),
)

Analysis_Types = [
    ('Unknown','Unknown'),
    ('Sample Milling','Sample Milling'),
    ('Protein','Protein'),
    ('Aflatoxin','Aflatoxin'),
    ('Multimycotoxin','Multimycotoxin'),
    ('Primary Amino Acids','Primary Amino Acids'),
    ('Water soluble vitamin','Water soluble vitamin'),
    ('Fat soluble vitamins','Fat soluble vitamins'),
    ('Tannins','Tannins'),
    ('DM content','DM content'),
    ('Total free phenolics','Total free phenolics'),
    ('phytic acid','phytic acid'),
    ('total oxalate','total oxalate'),
    ('Crude fat','Crude fat'),
    ('Crude fiber','Crude fiber'),
    ('Mineral analysis (Fe, Zn, Mg, Ca, Mn, Co, Al, K, Na)','Mineral analysis (Fe, Zn, Mg, Ca, Mn, Co, Al, K, Na)'),
]

class AddProductModel(models.Model):
    product_category = models.CharField(max_length=200, choices=CATEGORIES, default='OtherAnalysis')
    product_name = models.CharField(max_length=200, choices=Analysis_Types)
    product_description = models.CharField(max_length=100)
    product_price = models.IntegerField()


STATUS = [
		('Ordered','Ordered'),
		('Accepted',"Accepted"),
		('Recieved',"Recieved"),
		('Extracted',"Extracted"),
		('QCd',"QCd"),
		('Complete',"Complete"),
	]

class PlaceOrderModel(models.Model):
    order_by = models.CharField(max_length=20, null=True)
    product_name = models.CharField(max_length=50, null=True)
    product_quantity = models.IntegerField(default=1)
    product_price = models.IntegerField(null=True)
    product_status = models.CharField(max_length=100, null=True, choices=STATUS, default='Ordered')
