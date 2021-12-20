from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.shortcuts import get_object_or_404

from . import models, forms

@login_required()
def user_follow(request):
    user_form = forms.UserFollowsForm()
    following = models.UserFollow.objects.filter(user__exact=request.user)
    followed_by = models.UserFollow.objects.filter(followed_user__exact=request.user)
    
    
    
    if request.method == 'POST':
        user_form = forms.UserFollowsForm(request.POST)
        if user_form.is_valid():
            user_form.user = request.user
            user_form.followed_by = followed_by
            user_form.save()
            return redirect('home')
    # following = models.UserFollows.objects.filter(user__exact=request.user)
    # followed_by = models.UserFollows.objects.filter(followed_user__exact=request.user)
    return render(request, 'followers/user_follow_form.html', context = {'following': following, 'followed_by': followed_by})   


    