from rest_framework import permissions


# Não vai mais ser usado. Vai ficar como exemplo para permissions local e não global
class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):

        # Exemplo de uma permission
        # return Assinatura.objects.filter(user=request.user).exists()
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')  # nome_app.action_model. Para testar a permissão

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')

        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        return False
