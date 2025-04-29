from django.shortcuts import render, redirect
from .ChefBot import chat
from django.urls import reverse



def blog_list(request):
    return render(request, "blog_list.html")

def base(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        return redirect(f"{reverse('result')}?input={user_input}")
    return render(request, "new_page.html")


def result(request):
    user_input = request.GET.get("input", "No input provided")
    response = chat(user_input)  # Assuming this returns a generator or iterable of message objects

    if hasattr(response, "__iter__") and not isinstance(response, str):
        response_text = "".join(str(chunk.message.content) for chunk in response)
    else:
        response_text = str(response)

    lines = response_text.split("\n")  # Split by new lines
    title = None
    ingredients = []
    instructions = []
    calories = []
    section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        if not title and line:  
            title = line  # Assume first non-empty line is the title

        if line.lower().startswith("ingredients"):
            section = "ingredients"
        elif line.lower().startswith("instructions") or line.lower().startswith("steps"):
            section = "instructions"
        elif section == "ingredients" and line.startswith("- "):  # Ingredients list
            ingredients.append(line.replace("- ", ""))
        elif section == "instructions" and (line[0].isdigit() and line[1] == "."):  # Numbered steps
            instructions.append(line)

        elif line.lower().startswith("calories"):
            section = "calories"

    context = {
        "title": title if title else "Untitled Recipe",
        "ingredients": ingredients,
        "instructions": instructions,
        "calories": calories,
    }

    return render(request, "display.html", context)
