"""
auth.py
Decoradores de autenticacion y autorizacion.
"""

from functools import wraps
from flask import session, redirect, url_for, flash


def login_requerido(f):
    """
    Decorador que exige una sesion activa (sin importar el rol).
    """
    @wraps(f)
    def decorada(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Debes iniciar sesion para acceder a esa pagina.", "danger")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorada


def rol_requerido(rol):
    """
    Fabrica de decoradores: retorna un decorador que exige un rol
    especifico. Se usa asi: @rol_requerido("admin")
    """
    def decorador(f):
        @wraps(f)
        def decorada(*args, **kwargs):
            if "usuario_id" not in session:
                flash("Debes iniciar sesion para acceder a esa pagina.", "danger")
                return redirect(url_for("login"))
            if session.get("usuario_rol") != rol:
                flash("No tienes permisos para acceder a esa pagina.", "danger")
                return redirect(url_for("inicio"))
            return f(*args, **kwargs)
        return decorada
    return decorador
