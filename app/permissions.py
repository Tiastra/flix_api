from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permissions_codename(
            request.method, view
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)  # nome_app.action_model. Para testar a permissão

    def __get_model_permissions_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
