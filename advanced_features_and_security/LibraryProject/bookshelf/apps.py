from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

class BookshelfConfig(AppConfig):
    name = 'bookshelf'

    def ready(self):
        import bookshelf.signals