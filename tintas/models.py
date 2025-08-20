from django.db import models

class Tinta(models.Model):
    class Meta:
        db_table = 'produtos'
        
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    tipo_parede = models.CharField(max_length=100)
    ambiente = models.CharField(max_length=100)
    acabamento = models.CharField(max_length=50)
    features = models.TextField()
    linha = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.cor} ({self.tipo_parede})"