from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ProfileRegistrationForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
                  
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form=ProfileRegistrationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            p_user = profile_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            p_user.user=new_user
            # Create the user profile
            #Profile.objects.create(user=new_user,)
            p_user.save()
            return render(request,
                          'shop/account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
    return render(request,
                  'shop/account/register.html',
                  {'user_form': user_form,
                  'profile_form': profile_form})



def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'shop/account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
