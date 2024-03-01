from django.shortcuts import render, redirect
from apps.products.models import ProductImages, Product,Kind,Category
from apps.host.models import Host
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel


# Create your views here.
def create_product(request):
    index_host = Host.objects.latest('id')
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
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
        delivery_type = request.FILES.getlist('delivery_type')
        # try:
        product = Product.objects.create(
            title=title,
            image=image,
            description=description,
            price=price,
            delivery_price=delivery_price,
            category_id=category,
            kind_id=kind,
            user=request.user,
            delivery_type=delivery_type
        )
        if images:
            for image in images:
                ProductImages.objects.create(image=image, product=product)
        product.save()
        return redirect('profile', request.user.username)
        # except:
            
        #     return redirect('create_product')
    kinds = Kind.objects.all()
    categories = Category.objects.all()
    return render(request, 'host/create_product.html', locals())
