from django.shortcuts import render, redirect
from apps.products.models import ProductImages, Product,Kind,Category, ProductRequest
from apps.users.models import User
from apps.host.models import Host
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel
from apps.base.models import Settings

# Create your views here.
def create_product(request):
    settings = Settings.objects.latest('id')
    index_host = Host.objects.latest('id')
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if not request.user.is_authenticated or request.user.user_role != 'chef':
        return redirect('becomeahost')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        price_per = request.POST.get('price_per')
        delivery_price = request.POST.get('delivery_price')
        delivery_price_per = request.POST.get('delivery_price_per')
        category = request.POST.get('category')
        kind = request.POST.get('kind')
        images = request.FILES.getlist('images')
        delivery_type = request.POST.get('delivery_type')
        calendar_availability_date = request.POST.get('calendar_availability_date')
        location_product = request.POST.get('location_product')
        diet = request.POST.get('diet')
        allergens = request.POST.get('allergens')
        print(f"\n\n\n\n\n\n\n\n\n\n{diet}\n{allergens}\n{calendar_availability_date}\n\n\n\n\n\n\n\n")
        product = Product.objects.create(
            title=title,
            image=image,
            description=description,
            price=price,
            price_per=price_per,
            delivery_price=delivery_price,
            delivery_price_per=delivery_price_per,
            category_id=category,
            kind_id=kind,
            user=request.user,
            delivery_type=delivery_type,
            calendar_availability_date=calendar_availability_date,
            location=location_product
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
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    product_detail = True
    product = Product.objects.get(id=id)
    user = User.objects.get(id = product.user.id)
    print(user.username)
    if request.method == 'POST':
        if 'product_request' in request.POST:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            number = request.POST.get('number')

            color = request.POST.get('color')
            add_service = request.POST.get('add_service')
            comment = request.POST.get('comment')
            ProductRequest.objects.create(
                chef=product.user,
                customer=request.user,
                product=product,

                full_name=full_name,
                email=email,
                number=number,

                color=color,
                add_service=add_service,
                comment=comment,
            )
        return redirect('product_detail', product.id)
    return render(request, 'shop/product_detail.html', locals())