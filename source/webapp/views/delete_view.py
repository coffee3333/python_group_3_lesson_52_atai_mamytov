from django.db.models.deletion import ProtectedError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View


class DeleteView(View):
    template_name = None
    confirm_deletion = True
    model = None
    key_kwarg = 'pk'
    context_key = 'object'
    redirect_url = ''

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.confirm_deletion:
            return render(request, self.template_name, self.get_context_data())
        else:
            try:
                self.perform_delete()
                return redirect(self.get_redirect_url())
            except ProtectedError:
                return HttpResponse("<h2>This object is protected</h2>")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.perform_delete()
            return redirect(self.get_redirect_url())
        except ProtectedError:
            return HttpResponse("<h2>This object is protected</h2>")

    def perform_delete(self):
        self.object.delete()

    def get_context_data(self, **kwargs):
        return {self.context_key: self.object}

    def get_object(self):
        pk = self.kwargs.get(self.key_kwarg)
        return get_object_or_404(self.model, pk=pk)

    def get_redirect_url(self):
        return self.redirect_url