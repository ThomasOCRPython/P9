from types import new_class
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render


from . import forms, models

@login_required
def ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'flux/create_ticket_post.html', context={'ticket_form': ticket_form})

@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'flux/view_ticket.html', {'ticket': ticket})




@login_required
def review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)    
    review_form = forms.ReviewForm(instance=ticket)
    if request.method == 'POST':       
        review_form = forms.ReviewForm(request.POST, instance=ticket)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('home')   
    return render(request, 'flux/create_review_post.html', context={'review_form': review_form})
            
            


@login_required
def home(request):
    
    reviews = models.Review.objects.all()
    tickets = models.Ticket.objects.all()
    context = {
        'reviews': reviews,
        'tickets': tickets,
    }
    return render(request, 'flux/home.html', context=context)


