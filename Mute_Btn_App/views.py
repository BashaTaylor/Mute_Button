from django.shortcuts import render

def index(request):
    result = None  # Default value for result
    if request.method == 'POST':
        # Get the button text (you can adjust as needed for your buttons)
        button_value = request.POST.get('button_value')
        
        # Set the result based on the button pressed
        if button_value:
            result = button_value  # Update result to show which button was clicked

    return render(request, 'index.html', {'result': result})
