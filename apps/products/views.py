from django.shortcuts import render, redirect
from apps.products.models import ProductImages, Product,Kind,Category
# Create your views here.
def create_product(request):
    if request.user.user_role != 'chef':
        return redirect('index')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        delivery_price = request.POST.get('delivery_price')
        category = request.POST.get('category')
        kind = request.POST.get('kind')
        images = request.FILES.getlist('images')
        try:
            product = Product.objects.create(
                title=title,
                image=image,
                description=description,
                price=price,
                delivery_price=delivery_price,
                category=category,
                kind=kind,
                user=request.user
            )
            if images:
                for image in images:
                    ProductImages.objects.create(image=image, product=product)
            product.save()
            return redirect('shop', request.user.username)
        except:
            return redirect('create_product')
    kinds = Kind.objects.all()
    categories = Category.objects.all()
    return render(request, 'host/create_product.html', locals())
