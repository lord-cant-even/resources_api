from os.path import join

from flask import send_from_directory, current_app

from app.views import bp


@bp.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(join(current_app.root_path, 'static'), 'favicon.ico')
