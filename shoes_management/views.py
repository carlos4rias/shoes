from django.shortcuts import render
from .models import Bill, BillItem

# Create your views here.
def solds(req):
    bills = Bill.objects.all()
    return render(req, 'ventas.html', context={'bills': bills})

def soldItems(req, pk):
    bill = Bill.objects.get(id=pk)
    items = BillItem.objects.filter(bill_id=pk)

    print (items)
    context={'id': pk}
    context['date'] = bill.sold_date
    context['items'] = items
    return render(req, 'ventas-detail.html', context)
