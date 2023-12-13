from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
    
    # Configuración adicional para evitar advertencias de seguimiento de la base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importar modelos después de inicializar la base de datos
    from app import models

    with app.app_context():
        try:
            # Crear tablas en la base de datos (si no existen)
            db.create_all()
        except Exception as e:
            print("Error al crear tablas en la base de datos:", e)

    # Importar rutas después de inicializar la base de datos
    from .routes import main
    app.register_blueprint(main)

    return app
