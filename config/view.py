import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

restaurants = [
    {'name': 'Sonny\'s BBQ', 'category': 'BBQ', 'budget_ranges': ['16$-25$', '25$-35$'], 'menu_url': 'https://sonnysbbq.com/menu', 'rating': '4.5', 'address': '123 BBQ St, City, State'},
    {'name': 'Sweet Baby Ray\'s BBQ', 'category': 'BBQ', 'budget_ranges': ['16$-25$', 'Above'], 'menu_url': 'https://sweetbabyrays.com/menu', 'rating': '4.7', 'address': '456 BBQ Ave, City, State'},
    {'name': 'Famous Dave\'s', 'category': 'BBQ', 'budget_ranges': ['16$-25$', '1$-15$'], 'menu_url': 'https://famousdaves.com/menu', 'rating': '4.2', 'address': '789 BBQ Blvd, City, State'},
    {'name': 'Shane\'s Rib Shack', 'category': 'BBQ', 'budget_ranges': ['1$-15$', '16$-25$'], 'menu_url': 'https://shanesribshack.com/menu', 'rating': '4.0', 'address': '101 BBQ Rd, City, State'},
    {'name': 'Dickey\'s Barbecue Pit', 'category': 'BBQ', 'budget_ranges': ['1$-15$', '16$-25$'], 'menu_url': 'https://dickeys.com/menu', 'rating': '3.9', 'address': '202 BBQ Ln, City, State'},
    {'name': 'ZAAPs', 'category': 'Hibachi', 'budget_ranges': ['16$-25$', '25$-35$'], 'menu_url': 'https://zaapthai.com/menu', 'rating': '4.6', 'address': '303 Hibachi Rd, City, State'},
    {'name': 'China Express', 'category': 'Hibachi', 'budget_ranges': ['16$-25$', '1$-15$'], 'menu_url': 'https://chinaexpress.com/menu', 'rating': '4.3', 'address': '404 Hibachi Dr, City, State'},
    {'name': 'Sakura', 'category': 'Hibachi', 'budget_ranges': ['16$-25$', 'Above'], 'menu_url': 'https://sakurasteakhouse.com/menu', 'rating': '4.7', 'address': '505 Hibachi Ave, City, State'},
    {'name': 'Kobe Japanese Steakhouse', 'category': 'Hibachi', 'budget_ranges': ['25$-35$', 'Above'], 'menu_url': 'https://kobe-steakhouse.com/menu', 'rating': '4.8', 'address': '606 Hibachi Blvd, City, State'},
    {'name': 'Benihana', 'category': 'Hibachi', 'budget_ranges': ['Above', '16$-25$'], 'menu_url': 'https://benihana.com/menu', 'rating': '4.5', 'address': '707 Hibachi Ln, City, State'},
    {'name': 'Buffalo Wild Wings', 'category': 'Wings', 'budget_ranges': ['16$-25$', '25$-35$'], 'menu_url': 'https://buffalowildwings.com/menu', 'rating': '4.1', 'address': '808 Wings Rd, City, State'},
    {'name': 'Zaxby\'s', 'category': 'Wings', 'budget_ranges': ['1$-15$', '16$-25$'], 'menu_url': 'https://zaxbys.com/menu', 'rating': '3.8', 'address': '909 Wings St, City, State'},
    {'name': 'Wingstop', 'category': 'Wings', 'budget_ranges': ['16$-25$', '1$-15$'], 'menu_url': 'https://wingstop.com/menu', 'rating': '4.0', 'address': '1010 Wings Blvd, City, State'},
    {'name': 'Pluckers Wing Bar', 'category': 'Wings', 'budget_ranges': ['25$-35$', 'Above'], 'menu_url': 'https://pluckers.com/menu', 'rating': '4.3', 'address': '1111 Wings Rd, City, State'},
    {'name': 'Hooters', 'category': 'Wings', 'budget_ranges': ['1$-15$', '16$-25$'], 'menu_url': 'https://hooters.com/menu', 'rating': '3.9', 'address': '1212 Wings Ave, City, State'},
    {'name': 'Amici\'s', 'category': 'Italian', 'budget_ranges': ['1$-15$', '16$-25$'], 'menu_url': 'https://amicisrestaurant.com/menu', 'rating': '4.4', 'address': '1313 Italian St, City, State'},
    {'name': 'Olive Garden', 'category': 'Italian', 'budget_ranges': ['16$-25$', '25$-35$'], 'menu_url': 'https://olivegarden.com/menu', 'rating': '4.2', 'address': '1414 Italian Rd, City, State'},
    {'name': 'Carrabba\'s Italian Grill', 'category': 'Italian', 'budget_ranges': ['16$-25$', '1$-15$'], 'menu_url': 'https://carrabbas.com/menu', 'rating': '4.0', 'address': '1515 Italian Ln, City, State'},
    {'name': 'Maggiano\'s Little Italy', 'category': 'Italian', 'budget_ranges': ['25$-35$', 'Above'], 'menu_url': 'https://maggianos.com/menu', 'rating': '4.6', 'address': '1616 Italian Blvd, City, State'},
    {'name': 'The Olive Tree', 'category': 'Italian', 'budget_ranges': ['Above', '16$-25$'], 'menu_url': 'https://theolivetree.com/menu', 'rating': '4.4', 'address': '1717 Italian Ave, City, State'},
    {'name': 'El Jasico\'s', 'category': 'Mexican', 'budget_ranges': ['1$-15$', '16$-25$'], 'menu_url': 'https://eljasicos.com/menu', 'rating': '4.0', 'address': '1818 Mexican Rd, City, State'},
    {'name': 'Chipotle', 'category': 'Mexican', 'budget_ranges': ['16$-25$', '1$-15$'], 'menu_url': 'https://chipotle.com/menu', 'rating': '4.3', 'address': '1919 Mexican Blvd, City, State'},
    {'name': 'Taco Bell', 'category': 'Mexican', 'budget_ranges': ['1$-15$', 'Above'], 'menu_url': 'https://tacobell.com/menu', 'rating': '3.7', 'address': '2020 Mexican Ave, City, State'},
    {'name': 'Moe\'s Southwest Grill', 'category': 'Mexican', 'budget_ranges': ['16$-25$', '25$-35$'], 'menu_url': 'https://moes.com/menu', 'rating': '4.1', 'address': '2121 Mexican St, City, State'},
    {'name': 'La Fiesta', 'category': 'Mexican', 'budget_ranges': ['25$-35$', 'Above'], 'menu_url': 'https://lafiestamex.com/menu', 'rating': '4.6', 'address': '2222 Mexican Rd, City, State'},
    {'name': 'Third on Cherry', 'category': 'Seafood', 'budget_ranges': ['25$-35$', 'Above'], 'menu_url': 'https://thirdoncherry.com/menu', 'rating': '4.7', 'address': '2323 Seafood Ave, City, State'},
    {'name': 'Red Lobster', 'category': 'Seafood', 'budget_ranges': ['Above', '25$-35$'], 'menu_url': 'https://redlobster.com/menu', 'rating': '4.2', 'address': '2424 Seafood St, City, State'},
    {'name': 'The Crab Shack', 'category': 'Seafood', 'budget_ranges': ['25$-35$', '16$-25$'], 'menu_url': 'https://crabshack.com/menu', 'rating': '4.1', 'address': '2525 Seafood Blvd, City, State'},
    {'name': 'Joe\'s Crab Shack', 'category': 'Seafood', 'budget_ranges': ['16$-25$', '1$-15$'], 'menu_url': 'https://joescrabshack.com/menu', 'rating': '3.9', 'address': '2626 Seafood Ln, City, State'},
    {'name': 'Bonefish Grill', 'category': 'Seafood', 'budget_ranges': ['16$-25$', 'Above'], 'menu_url': 'https://bonefishgrill.com/menu', 'rating': '4.5', 'address': '2727 Seafood Dr, City, State'}
]

# Home view
def home(request):
    return render(request, 'restaurant/home.html')

# Guest View
def guest(request):
    return render(request, 'restaurant/guest.html', {})

# Register View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('guest')  # Redirect to budget selection page after registration
    else:
        form = UserCreationForm()
    return render(request, 'restaurant/register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('choose_budget')  # Redirect to budget selection page after login
    else:
        form = AuthenticationForm()
    return render(request, 'restaurant/login.html', {'form': form})

# Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# Choose Budget View - Allow guest and logged-in users to select a budget
def choose_budget(request):
    return render(request, 'restaurant/choose_budget.html')

# Choose Category View - Allow users to select multiple categories
def choose_category(request):
    # Get budget_range from the GET parameter
    budget_range = request.GET.get('budget_range')  # Query parameter passed as ?budget_range=1$-15$

    if budget_range:
        # Store the selected budget range in the session
        request.session['budget_range'] = budget_range

    # Get all categories
    categories = set(r['category'] for r in restaurants)

    return render(request, 'restaurant/choose_category.html', {'categories': categories, 'budget_range': budget_range})


def show_restaurants(request):
    # Get the budget and categories from the request
    budget_range = request.GET.get('budget_range')
    categories = request.GET.get('categories', '')
    categories = categories.split(',') if categories else []

    # Filter restaurants based on selected budget and categories
    filtered_restaurants = [r for r in restaurants if budget_range in r['budget_ranges'] and r['category'] in categories]

    # If fewer than 3 restaurants are available, show all of them
    selected_restaurants = random.sample(filtered_restaurants, min(3, len(filtered_restaurants)))

    # Store selected restaurants in session
    request.session['selected_restaurants'] = selected_restaurants

    return render(request, 'restaurant/show_restaurants.html', {
        'selected_restaurants': selected_restaurants,
        'budget_range': budget_range,
        'categories': categories,
    })

def eliminate_or_new_round(request):
    selected_restaurants = request.session.get('selected_restaurants', [])

    # Handle the "Start a New Round" action
    if 'new_round' in request.GET:
        request.session['selected_restaurants'] = []  # Clear selected restaurants
        return redirect('choose_category')  # Redirect to category selection for a new round

    # Handle the "Eliminate" action
    if 'eliminate' in request.GET:
        restaurant_to_eliminate = request.GET['eliminate']
        # Filter out the eliminated restaurant
        selected_restaurants = [r for r in selected_restaurants if r['name'] != restaurant_to_eliminate]
        request.session['selected_restaurants'] = selected_restaurants

        # If only two restaurants remain, pick one randomly as the final choice
        if len(selected_restaurants) == 2:
            final_restaurant = random.choice(selected_restaurants)  # Randomly pick one of the two
            request.session['final_restaurant'] = final_restaurant  # Store final choice in session
            return redirect('final_choice')  # Redirect to final choice page

        # If only one restaurant remains, go to the final choice page
        if len(selected_restaurants) == 1:
            final_restaurant = selected_restaurants[0]
            request.session['final_restaurant'] = final_restaurant
            return redirect('final_choice')

    # If no "new_round" or "eliminate" parameter, just go back to the show_restaurants page
    return redirect('show_restaurants')


from django.shortcuts import render, redirect

def final_choice(request):
    # Get the final restaurant choice from the session
    final_restaurant = request.session.get('final_restaurant')

    # If no final restaurant is selected, redirect back to the category selection
    if not final_restaurant:
        return redirect('choose_category')

    # Define the mapping of shorthand to full category names
    category_map = {
        'BBQ': 'Barbecue',
        'Hibachi': 'Japanese Hibachi',
        'Wings': 'Wing Restaurant',
        'Italian': 'Italian Cuisine',
        'Mexican': 'Mexican Cuisine',
        'Seafood': 'Seafood Restaurant'
    }

    # Get the category from the final restaurant and replace it if needed
    category = final_restaurant.get('category', '')
    if category in category_map:
        final_restaurant['category'] = category_map.get(category, category)

    return render(request, 'restaurant/final_choice.html', {'final_restaurant': final_restaurant})

from django.shortcuts import redirect

# Start Over View - Clear the session and redirect to home
def start_over(request):
    # Clear the session data
    request.session.flush()  # This will clear all session data
    
    # Redirect to the home page to restart the process
    return redirect('home')



