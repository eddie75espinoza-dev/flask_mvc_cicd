 # Archivo de inicialización y configuración de la aplicación Flask.

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Otras configuraciones de la aplicación
    # TEMPLATE_FOLDER = 'views/templates/'
    # STATIC_FOLDER = 'views/static/'