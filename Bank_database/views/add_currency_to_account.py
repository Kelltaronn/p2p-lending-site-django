from Bank_database.views.main import main
from Bank_database.models.Szamla import Szamla
from Bank_database.form import  TransactionForm
from django.shortcuts import render ,redirect
import stripe
import os
from dotenv import load_dotenv
#Stripe connection setting up:
stripe.api_key = os.getenv('STRIPE_API_KEY') or os.environ.get('STRIPE_API_KEY')
domain_host= os.getenv('DJANGO_DOMAIN') or os.environ.get('DJANGO_DOMAIN')




def add_currency_to_account(request):
    active_user = request.user
    user_account = Szamla.objects.get(szamla_tulajdonos = active_user)
    if request.method == "GET":
        currency_form = TransactionForm(initial={"szamla_id" : user_account, "tranzakcio_fajta":"Befizetés"})
        field1 = currency_form.fields["szamla_id"]
        field3 = currency_form.fields["tranzakcio_fajta"]

        field1.widget = field1.hidden_widget()
        field3.widget = field3.hidden_widget()

        context = {"added_currency": currency_form}
        return render(request,"add_to_balance.html",context)
    
    '''
    if request.method == "POST":
        user = request.user.id
        transaction = TransactionForm(request.POST)
        transaction.save()

        account_data = Szamla.objects.get(szamla_tulajdonos = user)
        actual_balance = account_data.aktualis_osszeg
        account_data.aktualis_osszeg = int(request.POST["osszeg"]) + int(actual_balance) #The new actual balance
        account_data.save()
        context = {}
        return main(request)
    '''
    #This will be directed to Stripe:
    if request.method == 'POST':
        df = stripe.Price.create(
                    currency="EUR",
                    unit_amount= (100 * int(request.POST['osszeg'])), #The price is multiplied by 100.
                    product='prod_Pa0CGCrydM2nkn')
        transaction = TransactionForm(request.POST)
        new_transaction = transaction.save()
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': df['id'],
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= '{1}add_to_balance_success/{0}/'.format(new_transaction.id,domain_host),
            cancel_url= '{0}add_to_balance_unsuccess/'.format(domain_host),
        )
        return redirect(checkout_session.url)

    
        
        
