from django.shortcuts import render, redirect
from apps.products.models import ProductImages, Product,Kind,Category
from apps.users.models import User
from apps.host.models import Host
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel
from apps.base.models import Settings

# Create your views here.
def create_product(request):
    index_host = Host.objects.latest('id')
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if not request.user.is_authenticated or request.user.user_role != 'chef':
        return redirect('becomehost')
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
        calendar_availability_date = request.FILES.getlist('calendar_availability_date')
        product = Product.objects.create(
            title=title,
            image=image,
            description=description,
            price=price,
            delivery_price=delivery_price,
            category_id=category,
            kind_id=kind,
            user=request.user,
            delivery_type=delivery_type,
            calendar_availability_date=calendar_availability_date
        )
        if images:
            for image in images:
                ProductImages.objects.create(image=image, product=product)
        product.save()
        return redirect('profile', request.user.username)
    
    kinds = Kind.objects.all()
    categories = Category.objects.all()
    return render(request, 'host/create_product.html', locals())


def all_products(request,username):
    user = User.objects.get(username = username)
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    user_shop = user.shop_user
    return render(request, 'shop/all_products.html', locals())

def product_detail(request, id):
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    product_detail = True
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', locals())