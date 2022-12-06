from django.db import models

class Pessoa(models.Model):
	cliente = models.CharField(max_length=100)
	numero_conteiner = models.CharField(max_length=100)
	tipo = models.CharField(max_length=100)
	status = models.CharField(max_length=100)
	categoria = models.CharField(max_length=100)
	movimentacao = models.CharField(max_length=100)
	data_inicial = models.DateField()
	data_final = models.DateField()
	
	

	def __str__(self):
		return self.cliente
