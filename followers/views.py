from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.shortcuts import get_object_or_404
from authentification.models import User
from . import models, forms


    
    
@login_required()
def user_follow(request):
    user_form = forms.UserFollowsForm()
    following = models.UserFollow.objects.filter(user__exact=request.user)
    followed_by = models.UserFollow.objects.filter(followed_user__exact=request.user)
    
    all_user = User.objects.all()

    if request.method == 'POST':
        user_form = forms.UserFollowsForm(request.POST)
        
        username = request.POST['username_follow']
        
        user = User.objects.get(username__exact=username)
        
        if user_form.is_valid() and user and user != request.user:
        
            models.UserFollow.objects.create(user=request.user, followed_user=user)
            return redirect('user_follow')
    return render(request, 'followers/user_follow_form.html',
        context = {'following': following, 'followed_by': followed_by, "form": user_form, "all_user": all_user}) 


@login_required
def delete_user_follows(request, followed_user_id=None):
    user = get_object_or_404(User, id=followed_user_id)
    follow = get_object_or_404(models.UserFollow, user=request.user, followed_user=user)

    if follow:
        follow.delete()
    return redirect('user_follow')
