from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Link

class LinkListView(ListView):
    model = Link
    template_name = 'link_list.html'


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")
    # template model_form -> link_form.html


class LinkUpdateView(UpdateView):
    model = Link
    fields = ['name', "url"]
    success_url = reverse_lazy('link-list')
    # template model_form -> link_form.html


class LinkDeleteView(DeleteView):
    # take in the id/pk of an object
    # query to db for that object
    # check if it exists  -> delete the object
    # retur some template or forward to user to some url
    model = Link
    success_url = reverse_lazy('link-list')
    # form to submit to delete the item
    # expecpt a template name model model_confirm_delete.html





class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'


class ProfileCreateView(CreateView):
    model = Profile
    # success_url = reverse_lazy()
    fields = "__all__"
    success_url = reverse_lazy('profile-list')


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug = profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }
    return render(request, 'link_tree/profile.html', context=context)

