from django.shortcuts import redirect

class Metadatax(object):
    def metadatax(self):
        return redirect('/admin/login/?next=/admin/')
