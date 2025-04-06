# mango_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.http import Http404
from .data import mango_items, get_item_by_id, get_pests, get_diseases

class HomeView(TemplateView):
    template_name = 'mango_app/home.html'

class ProjectListView(TemplateView):
    template_name = 'mango_app/projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get filter type from request or default to 'all'
        filter_type = self.request.GET.get('filter', 'all')
        
        # Apply filter if needed
        if filter_type == 'all':
            context['mango_items'] = mango_items
        elif filter_type == 'pest':
            context['mango_items'] = [item for item in mango_items if item.item_type == 'pest']
        elif filter_type == 'disease':
            context['mango_items'] = [item for item in mango_items if item.item_type == 'disease']
        else:
            context['mango_items'] = mango_items
            
        # Pass the current filter to the template
        context['current_filter'] = filter_type
        return context
        
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        # Check if this is an HTMX request
        if request.headers.get('HX-Request'):
            # For HTMX requests, only return the filtered items partial
            return render(request, 'mango_app/partials/item_grid.html', context)
        
        # For normal requests, return the full page
        return render(request, self.template_name, context)

class MangoItemDetailView(View):
    template_name = 'mango_app/detail.html'
    
    def get(self, request, item_id):
        # Convert to integer
        try:
            item_id = int(item_id)
        except ValueError:
            raise Http404("Invalid item ID")
        
        # Get the item
        item = get_item_by_id(item_id)
        if not item:
            raise Http404("Item not found")
        
        # Return the context
        return render(request, self.template_name, {'item': item})

# class PestsView(TemplateView):
#     template_name = 'mango_app/pests.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pests'] = get_pests()
#         return context

# class DiseasesView(TemplateView):
#     template_name = 'mango_app/diseases.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['diseases'] = get_diseases()
#         return context

class SurveillanceView(TemplateView):
    template_name = 'mango_app/surveillance.html'

class AboutView(TemplateView):
    template_name = 'mango_app/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = [
            {'name': 'Arpan Nepal', 'student_id': '371945'},
            {'name': 'Samir Bajgain', 'student_id': '369784'},
            {'name': 'Abdullah AL mahmud Didar', 'student_id': '386212'},
            {'name': 'Abishek Kandel', 'student_id': '387576'},
        ]
        return context