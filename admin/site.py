from django.contrib import admin
from django.contrib.admin import sites


class MetadataxAdminSite(admin.AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_ordering = {
            "metadatax": 1,
            "meta_auth": 2,
            "auth": 2,
            "authtoken": 2
        }
        metadatax_ordering = {
            "Institutions": 1,
            "Projects": 2,
            "Deployments": 3,
            "Channel configurations": 4,
            "Files": 5,
            "Equipment - Recorders": 10,
            "Equipment - Hydrophones": 11,
        }
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: app_ordering[x['app_label']])

        final_apps = []
        for app in app_list:
            print(app)
            if app['app_label'] == 'metadatax':
                app['models'] = [m for m in app['models'] if m['name'] in list(metadatax_ordering.keys())]
                app['models'].sort(key=lambda x: metadatax_ordering[x['name']])
            final_apps.append(app)

        return final_apps


mysite = MetadataxAdminSite()
admin.site = mysite
sites.site = mysite
