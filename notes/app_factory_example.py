from flask import Flask


def create_app(settings_env: str = "RECIPES_SETTINGS") -> Flask:
    app = Flask(__name__)
    app.config.from_envvar(settings_env, silent=True)

    from recipes import bp as recipes_bp
    from auth import bp as auth_bp

    app.register_blueprint(recipes_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app
