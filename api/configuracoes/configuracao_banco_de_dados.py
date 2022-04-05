def inicia_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lucas:lucas123@localhost/apirest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app