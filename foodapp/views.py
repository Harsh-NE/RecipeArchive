from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from foodapp.models import Dish
from foodapp.forms import DishForm
from django.shortcuts import render, get_object_or_404,redirect
# Create your views here.
def index(request):
    dish_list=Dish.objects.all()
    template='foodapp/index.html'
    context={'dish_list':dish_list,}
    return render(request,template,context)

def add_item(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('foodapp:index')  # Corrected redirect syntax
    else:
        form = DishForm()
    return render(request, 'foodapp/dish_form.html', {'form': form})

from django.http import HttpResponseNotAllowed

def removerecipe(request, id):
    if request.method == "POST":
        obj = get_object_or_404(Dish, id=id)
        obj.delete()
        return redirect('foodapp:index')
    else:
        return HttpResponseNotAllowed(["POST"])

def dishdetails(request,id):
    obj=get_object_or_404(Dish,id=id)
    return render(request,'foodapp/details.html',{'object':obj})


def updaterecipe(request, id):
    obj = Dish.objects.get(id=id)
    form = DishForm(instance=obj)
    if(request.method=='POST'):
        form = DishForm(request.POST or request.FILES, instance=obj)
        print(form.is_valid())
        if form.is_valid():
                form.save()
                return redirect('foodapp:index')
        else:
            form = DishForm(instance=obj)
    return render(request, "foodapp/dish_form.html", {"form": form})
