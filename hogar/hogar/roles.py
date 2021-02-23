from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'hogar.add_user': True,
        'hogar.change_user': True,
        'hogar.delet_user': True,
        'hogar.view_user': True,
    }

class Usuario(AbstractUserRole):
    available_permissions = {
        }