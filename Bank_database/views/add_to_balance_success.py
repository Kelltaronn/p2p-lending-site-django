from django.shortcuts import render
from Bank_database.models.Tranzakcio import Tranzakcio

def add_to_balance_success(request,id):
    actual_transaction = Tranzakcio.objects.get(id = id)

    if actual_transaction.activated == True:
        new_balance = actual_transaction.szamla_id.aktualis_osszeg + actual_transaction.osszeg
        actual_transaction.szamla_id.aktualis_osszeg = new_balance
        actual_transaction.szamla_id.save()
         #szamla id objektum:
        actual_transaction.activated = False
        #Transaction change to active to inactive:
        actual_transaction.save()
        context = {}
        
        return render(request,'add_to_balance_success.html',context)
    else:
        context = {}
        return render(request,'add_to_balance_unsuccess.html',context)
