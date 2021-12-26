from types import new_class
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.db.models import CharField, Value
from itertools import chain


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
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('posts')
            if 'delete_ticket' in request.POST:
                delete_form = forms.DeleteTicketForm(request.POST)
                if delete_form.is_valid():
                    ticket.delete()
                    return redirect('posts')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'flux/edit_ticket.html', context=context)

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    ticket.delete()
    return redirect('posts')
    




@login_required
def review(request, ticket_id=None):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)    
    review_form = forms.ReviewForm()
    review = None
    if request.method == 'POST':       
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            ticket.starred = True
            ticket.save()
            return redirect('home')   
    return render(request, 'flux/create_review_post.html', context={'review_form': review_form, 'ticket' : ticket})
            
@login_required
def ticket_and_review(request):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.starred = True
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'flux/create_ticket_and_review_post.html', context=context) 

@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
    )
    context = {'posts': posts}
    
    return render(request, 'flux/posts.html', context=context) 


@login_required
def home(request):
    
    reviews = models.Review.objects.all()
    tickets = models.Ticket.objects.all()

    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    # posts = chain(reviews, tickets)
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
            )

    return render(request, 'flux/home.html', context={'posts':posts})


