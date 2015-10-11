from django.shortcuts import render, redirect
from lists.models import Item

def homepage(request):
   if request.method == 'POST':
       text = request.POST.get('item_text', '')
       item = Item.objects.create(text=text)
       return redirect('/')
   items = Item.objects.all()
   return render(request, 'home.html', {'items':items})

