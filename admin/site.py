from django.contrib import admin
from django.contrib.admin import sites


class MetadataxAdminSite(admin.AdminSite):
    site_header = 'Metadatax (demo)'
    site_title = 'Metadatax (demo)'

    app_ordering = {
        "metadatax": 1,
        "meta_auth": 2,
        "auth": 2,
        "authtoken": 2
    }
    metadatax_ordering = {
        "> Map": 0,
        "Institutions": 1,
        "Projects": 2,
        "Deployments": 3,
        "Channel configurations": 4,
        "Files": 5,
        "Equipment - Recorders": 10,
        "Equipment - Hydrophones": 11,
    }

    def _build_app_dict(self, request, label=None):
        # we create manually a dict to fake a model for our view 'map'
        map_fake_model = {
            'name': '> Map',
            'admin_url': "/map/",
            'object_name': 'Map',
            'perms': {'delete': False, 'add': False, 'change': False},
            'add_url': ''
        }

        # get the app dict from the parent method
        app_dict = super()._build_app_dict(request, label)
        # check if there is value for label = admin view for specific app
        if label:
            app_dict['models'] = [m for m in app_dict['models'] if m['name'] in list(self.metadatax_ordering.keys())]
            app_dict['models'].append(map_fake_model)

        # otherwise = home admin view with all apps
        else:
            app = app_dict.get('metadatax', None)
            if app:
                app['models'] = [m for m in app['models'] if m['name'] in list(self.metadatax_ordering.keys())]
                app['models'].append(map_fake_model)
                app['models'].sort(key=lambda x: self.metadatax_ordering[x['name']])
        return app_dict

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: self.app_ordering[x['app_label']])

        return app_list



mysite = MetadataxAdminSite()
admin.site = mysite
sites.site = mysite
