from django.shortcuts import redirect
from django.http import Http404
from Bank_database.models.Szamla import Szamla

def is_lender(func):
    def wrapper(*args,**kwargs):
        if str(args[0].user) != 'AnonymousUser':
            active_user = args[0].user
            user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
            if user_account.szamla_tipus == "Lender":
                return func(*args,**kwargs)
            else:
                raise Http404("You are not a Lender")
        else:
            return redirect("login/")
    return wrapper
        

def is_investor(func):
    def wrapper(*args,**kwargs):
        if str(args[0].user) != 'AnonymousUser':
            active_user = args[0].user
            user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
            if user_account.szamla_tipus == "Investor":
                return func(*args,**kwargs)
            else:
                raise Http404("You are not an Investor")
        else:
            return redirect("login/")
    return wrapper
