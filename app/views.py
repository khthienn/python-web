from django.shortcuts import render
from django.http import HttpResponse
from app.models import Contact, Item, ItemList, AboutUs, Feedback
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def home(request):
    items = Item.objects.all()
    lists= ItemList.objects.all()
    feedback= Feedback.objects.all()
    
    return render(request, 'home.html', {'items': items, 'list': lists, 'feedback': feedback})

def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Vui lòng điền đầy đủ tên đăng nhập và mật khẩu!", extra_tags="danger")
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Đăng nhập thành công!")  
            return redirect('home')
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!", extra_tags="danger")  
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
                messages.error(request, "Mật khẩu nhập lại không khớp!")
                return redirect('register')

        if User.objects.filter(username=username).exists():
                messages.error(request, "Tên người dùng đã tồn tại!")
                return redirect('register')

        if User.objects.filter(email=email).exists():
                messages.error(request, "Email đã được sử dụng!")
                return redirect('register')
        customer = User.objects.create_user(username, email, pass1)
        customer.save()
        messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
        return redirect('register')
    return render(request, 'register.html')

def user_logout (request):
 logout(request)

 return redirect('home')

# def auth_view(request):
#     if request.method == "POST":
#         if "login" in request.POST:  # Nếu form đăng nhập được submit
#             email = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(email=email, password=password)  # Xác thực user
#             if user is not None:
#                 auth_login(request, user)
#                 messages.success(request, "Đăng nhập thành công!")  # Thông báo thành công
#                 return redirect('home')  # Chuyển hướng về trang chủ
#             else:
#                 messages.error(request, "Sai email hoặc mật khẩu!")  # Thông báo lỗi
        
#         elif "register" in request.POST:  # Nếu form đăng ký được submit
#             username = request.POST.get('username')
#             email = request.POST.get('email')
#             pass1 = request.POST.get('pass1')
#             pass2 = request.POST.get('pass2')

#             if pass1 != pass2:
#                 messages.error(request, "Mật khẩu nhập lại không khớp!")
#                 return redirect('auth_view')

#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Tên người dùng đã tồn tại!")
#                 return redirect('auth_view')

#             if User.objects.filter(email=email).exists():
#                 messages.error(request, "Email đã được sử dụng!")
#                 return redirect('auth_view')

#             customer = User.objects.create_user(username=username, email=email, password=pass1)
#             customer.save()
#             messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")  # Thông báo thành công
#             return redirect('auth_view')  # Điều hướng về trang login sau khi đăng ký thành công

#     return render(request, 'login.html')  # Hiển thị trang đăng nhập/đăng ký

def cart(request):
    
    return render(request, 'Cart/cart_detail.html')

def order(request):
    return render(request, 'order.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

       # Kiểm tra các trường
        if all([name, email, phone, message]):
            try:
                # Lưu thông tin liên hệ
                c = Contact(name=name, email=email, phone=phone, message=message)
                c.save()
                messages.success(request, 'Cảm ơn bạn đã liên hệ với chúng tôi!')
            except Exception as e:
                messages.error(request, f'Đã xảy ra lỗi: {e}')
        else:
            messages.warning(request, 'Vui lòng điền đầy đủ thông tin!')

    return render(request, 'contact.html')

def menu(request):
    items = Item.objects.all()
    lists= ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': lists})


def cart_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    
    messages.success(request, f"Đã thêm sản phẩm vào giỏ hàng!")
    # Kiểm tra nếu request có 'HTTP_REFERER' (trang trước đó)
    referer = request.META.get('HTTP_REFERER', '')

    # Nếu trang trước có chứa 'menu', quay lại trang menu, nếu không thì về home
    if 'menu' in referer:
        return HttpResponseRedirect(referer)
    return redirect("home")

def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product, quantity=1)  # Thêm 1 sản phẩm
    return redirect("cart_detail")

def item_decrement(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.decrement(product)  # Giảm 1 sản phẩm
    return redirect("cart_detail")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def checkout(request):
  if request.method == "POST":
       uid = request.session.get('_auth_user_id')
       user = User.objects.get(id=uid) if uid else None
       cart = request.session.get('cart', {})
       name =  request.POST.get('name')
       phone = request.POST.get('phone')
       province = request.POST.get('province')
       district = request.POST.get('district')
       address = request.POST.get('address')
       note = request.POST.get('note')
       payment_method = request.POST.get("payment_method", "cash")  # Lấy giá trị được chọn
       
       order = Order(
           user = user,
           name = name,
           phone =  phone,  
           province = province,
           district = district,
           address = address,
           note = note,
           payment_method = payment_method
                   
        )
       order.save()
       
       for i in cart: 
           a = cart[i]['price']
           b = cart[i]['quantity']
           total = int(a) * int(b)
           item = OrderItem(
               order = order,
               product = cart[i]['name'],
               image = cart[i]['image'],
               quantity = cart[i]['quantity'],
               price = cart[i]['price'],
               total = total
           )
           item.save()
       cart = Cart(request)
       cart.clear()
       messages.success(request, "Đặt hàng thành công! Cảm ơn bạn đã mua sắm.")

       return redirect("cart_detail")  # Chuyển hướng về trang giỏ hàng sau khi đặt hàng thành công
  return render(request, 'cart/cart_detail.html')
