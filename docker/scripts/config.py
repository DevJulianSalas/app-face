# -*- encoding: utf-8 -*-
#Modulo que contiene toda la configuracion para flask
#---- build-in Packages----#
import os
# from datetime import timedelta
# from celery.schedules import crontab



#Variables de configuracion
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Configuracion general."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED= True
    # CELERY_TIMEZONE = 'America/Bogota'
    # CELERY_IMPORTS = ['app.send_data.views']
    # CELERY_BROKER_URL='amqp://guest@localhost',
    # # SERVER_NAME = "DEVELOP"
    # CELERY_BACKEND = "amqp"
    # CELERYBEAT_SCHEDULE = {
    # 'add-every-5-minute': {
    #     'task': 'app.send_data.views.task_periodically',
    #     'schedule': timedelta(minutes=5),
    # },
    # }
    # DATABASE_URI = "" crear este wrapper para la conexion (task)

    @staticmethod
    def init__app(app):
        """Inicializa la app para pruebas"""
        pass

class ProductionConfig(Config):
    """Configuracion para produccion"""
    # DATABASE_URI =


class DevelopmentConfig(Config):
    """Configuracion para desarrollo"""
    DEBUG = True


class TestingConfig(Config):
    """Configuracion para testing"""
    TESTING = True


#Diccionario de clases con las configuraciones

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
