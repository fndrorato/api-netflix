# Importando as permissions do Rest Framework
from rest_framework import permissions

# Criando uma classe de permissão nossa 
# que tem que herdar de permissions

class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Lógica da permissão
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            # nome da app .  metodo _ nome do model 
            # nesse exemplo, genres.view_genre
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False