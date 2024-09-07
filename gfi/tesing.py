from django.views.generic import ListView
import json
from rest_framework import get_labels


class ListApiView(ListView):
    template_name = 'list.html'
    template_engine  = 'django.template.engine'
    queryset = ListView.objects.all()
    context_object_name = 'list'


    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels'] = get_labels()
        return context
    
    def get_queryset(self):
        return get_repos()
    
    def get_labels(self):
        # Fetch labels from your API
        # Here, we are assuming that labels are fetched from a static JSON file
        with open('labels.json', 'r') as file:
            return json.load(file)['labels']
        
    
    def post_labels(labels):
        # Fetch labels from your API
        # Here, we are assuming that labels are fetched from a static JSON file
        with open('labels.json', 'r') as file:
            labels_data = json.load(file)
            labels_data['labels'] = labels
            with open('labels.json', 'w') as file:
                json.dump(labels_data, file)
    
    