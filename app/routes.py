from flask import Blueprint, render_template, jsonify
from flask import request, redirect, url_for
from .models import db, Usuario, Sueno
from flask_login import login_required, current_user  
from datetime import datetime

main  = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/registro', methods=['POST'])
def registro():
    nuevo_usuario = request.json

    # Verifica si se proporcionaron los datos necesarios
    if 'username' not in nuevo_usuario or 'password' not in nuevo_usuario:
        return jsonify({'success': False, 'error': 'Se requiere nombre de usuario y contraseña'})

    username = nuevo_usuario['username']
    password = nuevo_usuario['password']

    # Verifica si el nombre de usuario ya existe
    if Usuario.query.filter_by(nombre_usuario=username).first():
        return jsonify({'success': False, 'error': 'El nombre de usuario ya está en uso'})

    # Utiliza bcrypt u otra función de hash para almacenar la contraseña de manera segura
    nuevo_usuario_db = Usuario(nombre_usuario=username, contraseña=password)
    db.session.add(nuevo_usuario_db)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Usuario registrado exitosamente'})



@main.route('/menu_principal')
@login_required  # Protege esta ruta para que solo los usuarios autenticados puedan acceder
def menu_principal():
    return render_template('menu_principal.html')

@main.route('/escribir_sueno', methods=['GET', 'POST'])
@login_required
def escribir_sueno():
    if request.method == 'POST':
        # Procesa y guarda el sueño en la base de datos
        texto_sueno = request.form.get('texto_sueno')

        # Verifica que el texto del sueño no esté vacío antes de guardarlo
        if texto_sueno:
            # Crea una instancia del modelo con el sueño y la información actual
            nuevo_sueno = Sueno(texto_sueno=texto_sueno, fecha_hora=datetime.utcnow(), usuario=current_user)

            # Agrega y guarda el nuevo sueño en la base de datos
            db.session.add(nuevo_sueno)
            db.session.commit()

            # Redirige a una página de éxito o a donde desees después de guardar
            return redirect(url_for('main.pagina_exito'))

    return render_template('escribir_sueno.html')

@main.route('/registrar_horas_sueno', methods=['GET', 'POST'])
@login_required
def registrar_horas_sueno():
    if request.method == 'POST':
        # Procesa y guarda las horas de sueño en la base de datos
        horas_sueno = request.form.get('horas_sueno')
        

    return render_template('registrar_horas_sueno.html')

@main.route('/evaluacion_calidad_sueno')
@login_required
def evaluacion_calidad_sueno():
    
    return render_template('evaluacion_calidad_sueno.html')
