from django.shortcuts import render, redirect, get_object_or_404
from .models import CalorieEntry
from .forms import CalorieEntryForm
import calendar
from datetime import date

def home(request):
    return render(request, 'caltrack/home.html')

def add_entry(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caltrack:dashboard')  # <-- corrected
    else:
        form = CalorieEntryForm()
    return render(request, 'caltrack/add_entry.html', {'form': form})

def dashboard(request):
    entries = CalorieEntry.objects.all().order_by('-date')
    return render(request, 'caltrack/dashboard.html', {'entries': entries})

def edit_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, pk=entry_id)
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('caltrack:dashboard')  # <-- corrected
    else:
        form = CalorieEntryForm(instance=entry)
    return render(request, 'caltrack/edit_entry.html', {'form': form, 'entry': entry})

def delete_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, pk=entry_id)
    entry.delete()
    return redirect('caltrack:dashboard')  # <-- corrected

def progress_report(request):
    entries = CalorieEntry.objects.all().order_by('date')

    # Prepare data for Chart.js
    dates = [entry.date.strftime('%Y-%m-%d') for entry in entries]
    calories = [entry.calories for entry in entries]

    return render(request, 'caltrack/progress_report.html', {
        'entries': entries,
        'dates': dates,
        'calories': calories,
    })


def calendar_view(request):
    today = date.today()
    year = today.year
    month = today.month

    cal = calendar.Calendar(firstweekday=6)  # Sunday start
    month_days = cal.monthdatescalendar(year, month)

    entries = CalorieEntry.objects.filter(date__year=year, date__month=month)

    # Map entries per date
    entry_map = {}
    for entry in entries:
        if entry.date not in entry_map:
            entry_map[entry.date] = []
        entry_map[entry.date].append(f"{entry.meal} ({entry.calories} cal)")

    context = {
        'calendar': month_days,
        'entry_map': entry_map,
        'month': today.strftime('%B'),
        'year': year,
        'today': today,
    }
    return render(request, 'caltrack/calendar_view.html', context)
