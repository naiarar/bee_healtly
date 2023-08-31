from django.shortcuts import render

def imc(self):
    height_m = self.height / 100
    imc = self.weight / (height_m ** 2)
    return imc