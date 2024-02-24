from django.shortcuts import render
from Bank_database.models.Tranzakcio import Tranzakcio

def add_to_balance_success(request,id):
    actual_transaction = Tranzakcio.objects.get(id = id)
    print(actual_transaction.szamla_id)

    #THe problematic  binarry:
    #We need an If
    new_balance = actual_transaction.szamla_id.aktualis_osszeg + actual_transaction.osszeg
    new_balance.save()
    #Transaction change to active to inactive:
    context = {}
    return render(request,'add_to_balance_success.html',context)