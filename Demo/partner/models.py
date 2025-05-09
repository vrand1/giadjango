from django.db import models
from django.db.models import Sum, Count


# Create your models here.
class PartnerType(models.Model):
    ID = models.IntegerField(primary_key=True, db_column='Код')
    Name = models.CharField(max_length=255, null=True, db_column="Наименование")

    class Meta:
        managed = False
        db_table = 'Типы_партнеров'


class Partner(models.Model):
    ID = models.AutoField(primary_key=True, db_column='Код')  # РК
    Partner_type = models.ForeignKey(PartnerType, on_delete=models.PROTECT, db_column="Тип_партнера")
    Name = models.CharField(max_length=255, null=True, db_column='Наименование')
    Director = models.CharField(max_length=255, null=True, db_column='Директор')
    Email = models.CharField(max_length=255, null=True, db_column='Электронная_почта')
    PhoneNumber = models.CharField(max_length=50, null=True, db_column='Телефон')
    LegalAddress = models.CharField(max_length=500, null=True, db_column='Юридический_адрес')
    Rating = models.IntegerField(null=True, db_column='Рейтинг')
    INN = models.CharField(max_length=20, null=True, db_column='ИНН')
    def discount(self):
        try:
            total = Sale.objects.filter(PartnerID=self.ID).aggregate(total_count=Sum("Count"))["total_count"] or 0
            print(total)
            if(total > 10000):
                if(total > 50000):
                    if(total > 300000):
                        return 15
                    return 10
                return 5
            return 0
        except: return 0

    class Meta:
        managed = False  # Django не будет управлять таблицей
        db_table = 'Партнеры'


class Production(models.Model):
    ID = models.IntegerField(primary_key=True, db_column='Код')  # РК
    Name = models.CharField(max_length=255, null=True, db_column='Наименование')

    class Meta:
        managed = False
        db_table = 'Продукция'


class Sale(models.Model):
    ID = models.IntegerField(primary_key=True, db_column='Код')  # РК
    Date = models.DateField(null=True, db_column='Дата')
    ProductionType = models.ForeignKey(Production, on_delete=models.PROTECT, db_column='Продукция')
    PartnerID = models.ForeignKey(Partner, on_delete=models.PROTECT, db_column='Партнер')
    Count = models.IntegerField(db_column='Количество')  # РК

    class Meta:
        managed = False
        db_table = 'Продажи'
