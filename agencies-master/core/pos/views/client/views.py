import datetime

from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.pos.forms import ClientForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.pos.models import Client
from core.user.models import User


class ClientListView(ValidatePermissionRequiredMixin, ListView):
    model = Client
    template_name = 'client/list.html'
    permission_required = 'view_client'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                today = datetime.datetime.today().strftime('%A')[:3].lower()
                query = Client.objects.select_related().filter(is_active=True)

                if today == 'mon':
                    data = [i.toLIST() for i in query.filter(Q(frequent=True) | Q(mon=True))]
                if today == 'tue':
                    data = [i.toLIST() for i in query.filter(Q(frequent=True) | Q(tue=True))]
                if today == 'wed':
                    data = [i.toLIST() for i in query.filter(Q(frequent=True) | Q(wed=True))]
                if today == 'thu':
                    data = [i.toLIST() for i in query.filter(Q(frequent=True) | Q(thu=True))]
                if today == 'fri':
                    data = [i.toLIST() for i in query.filter(Q(frequent=True) | Q(fri=True))]
                if today == 'sat':
                    data = [i.toLIST() for i in query.filter(Q(frequent=True) | Q(sat=True))]
                else:
                    data = [i.toLIST() for i in query.filter(frequent=True)]
            elif action == 'search_client':
                data = []
                query = Client.objects.select_related()
                term = request.POST['term']
                clients = query.filter(
                    Q(names__icontains=term) | Q(dni__icontains=term))[0:10]

                for i in clients:
                    item = i.toJSON()
                    item['text'] = f'{i.get_full_name()} - {i.dni}'
                    data.append(item)
            elif action == 'search_client_id':
                query = Client.objects.get(id=request.POST['id'])
                data = [query.toLIST()]
            elif action == 'search_client_all':
                data = [i.toLIST() for i in Client.objects.select_related()]
            elif action == 'delete':
                cli = Client.objects.get(id=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error con el action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('client_create')
        context['list_url'] = reverse_lazy('client_list')
        context['entity'] = 'Clientes'
        context['frmClient'] = Client.objects.select_related()
        return context


class ClientCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('client_list')
    url_redirect = success_url
    permission_required = 'add_client'

    def get_form(self, form_class=None):
        id = self.request.user.id
        form = ClientForm(initial={'user': User.objects.get(id=id)})
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    form = ClientForm(request.POST)
                    form.save()
                    data = form.save()
            else:
                data['error'] = 'Error del action'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ClientUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('client_list')
    url_redirect = success_url
    permission_required = 'change_client'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ocurrio un error en el action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
