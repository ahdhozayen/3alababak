from django.shortcuts import render, redirect
from orders.forms import PurchaseOrderCreationForm, purchase_transaction_formset
from orders.models import PurchaseOder


# Create your views here.
def create_purchaseOrder_view(request):
    po_form = PurchaseOrderCreationForm()
    po_transaction_inlineformset = purchase_transaction_formset()
    if request.method == 'POST':
        po_form = PurchaseOrderCreationForm(request.POST)
        po_transaction_inlineformset = purchase_transaction_formset(request.POST)
        if po_form.is_valid() and po_transaction_inlineformset.is_valid():
            po_obj = po_form.save(commit=False)
            po_obj.created_by = request.user
            po_instance = po_obj.save()
            po_transaction_inlineformset = purchase_transaction_formset(request.POST, instance=po_instance)
            for form in po_transaction_inlineformset:
                if form.is_valid():
                    po_transaction_obj = form.save(commit=False)
                    po_transaction_obj.created_by = request.user
                    po_transaction_obj.save()

            return redirect('home:homepage')
        else:
            print("Order not place")
    subcontext = {
        'po_form': po_form,
        'po_transaction_inlineformset': po_transaction_inlineformset
    }
    return render(request, 'create-po.html', context=subcontext)


def list_purchaseOrder_view(request):
    purchase_orders = PurchaseOder.objects.all()
    subcontext = {
        'purchase_orders_list': purchase_orders
    }
    return render(request, 'list-purchase_orders.html', context=subcontext)


def update_purchaseOrder_view(request, id):
    order = PurchaseOder.objects.get(pk=id)
    purchase_order_form = PurchaseOrderCreationForm(instance=order)
    po_transaction_inlineformset = purchase_transaction_formset(instance=order)
    if request.method == 'POST':
        purchase_order_form = PurchaseOrderCreationForm(request.POST, instance=order)
        po_transaction_inlineformset = purchase_transaction_formset(request.POST, instance=order)
        if purchase_order_form.is_valid() and po_transaction_inlineformset.is_valid():
            po_obj = purchase_order_form.save(commit=False)
            po_obj.last_updated_by = request.user
            po_instance = po_obj.save()
            po_transaction_inlineformset = purchase_transaction_formset(request.POST, instance=po_instance)
            for form in po_transaction_inlineformset:
                if form.is_valid():
                    po_transaction_obj = form.save(commit=False)
                    po_transaction_obj.last_updated_by = request.user
                    po_transaction_obj.save()
            return redirect('orders:list-po')
        else:
            print(purchase_order_form.errors)

    supContext = {
        'po_form': purchase_order_form,
        'po_transaction_inlineformset': po_transaction_inlineformset
    }
    return render(request, 'create-po.html', supContext)
