from django.apps import AppConfig


class DetailsScrapperAppConfig(AppConfig):
    name = 'details_scrapper_app'

    # TO IMPLICITLY START EXECUTION WHEN THE APP LOADS INTO MEMORY
    def ready(self):
        from .views import start
        start()
