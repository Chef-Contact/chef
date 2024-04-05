from django.shortcuts import render, redirect
from django.http import Http404

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
    # user = User.objects.get(id = product.user.id)
    # print(user.username)
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


def all_products_edit(request,username):
    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    user = User.objects.get(username = username)
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    user_shop = user.shop_user
    return render(request, 'host/user_foods.html', locals())


def edit_product(request, id):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    product = Product.objects.get(id=id)
    user = User.objects.get(id = product.user.id)
    kinds = Kind.objects.all()
    categories = Category.objects.all()

    if request.user.username != user.username:
        raise Http404("Нет доступа к данному профилю")
    
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_image = request.FILES.get('image')
        new_price = request.POST.get('price')
        new_price_per = request.POST.get('price_per')
        new_delivery_price = request.POST.get('delivery_price')
        new_delivery_price_per = request.POST.get('delivery_price_per')
        new_category = request.POST.get('category')
        new_kind = request.POST.get('kind')
        new_images = request.FILES.getlist('images')
        new_delivery_type = request.POST.get('delivery_type')
        new_calendar_availability_date = request.POST.get('calendar_availability_date')
        new_location_product = request.POST.get('location_product')
        new_diet = request.POST.get('diet')
        new_allergens = request.POST.get('allergens')
        print(f"\n\n\n\n\n\n\n\n\n\n{new_title}\n{new_price_per}\n{new_location_product}\n\n\n\n\n\n\n\n")
        
        try:
            product.title = new_title
            product.description = new_description
            product.image = new_image
            product.price = new_price
            product.price_per = new_price_per
            product.delivery_price = new_delivery_price
            product.delivery_price_per = new_delivery_price_per
            product.category = new_category
            product.kind = new_kind
            product.images = new_images
            product.delivery_type = new_delivery_type
            product.calendar_availability_date = new_calendar_availability_date
            product.location_product = new_location_product
            product.diet = new_diet
            product.allergens = new_allergens

            product.save()
            return redirect('all_products_edit', user.username)
        except Exception as e:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(f"Error saving user: {e}")
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return redirect('profile', user.username)
    
    return render(request, 'host/edit_product.html', locals())