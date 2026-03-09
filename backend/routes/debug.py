from flask import Blueprint, jsonify
import os

debug_bp = Blueprint('debug', __name__, url_prefix='/api/debug')

@debug_bp.route('/env', methods=['GET'])
def get_env():
    """Debug endpoint para verificar variáveis de ambiente."""
    return jsonify({
        'VERCEL': os.environ.get('VERCEL'),
        'DATABASE_URL': os.environ.get('DATABASE_URL', 'NOT_SET')[:50] + '...' if os.environ.get('DATABASE_URL') else 'NOT_SET',
        'FLASK_ENV': os.environ.get('FLASK_ENV'),
        'SQLALCHEMY_DATABASE_URI': os.environ.get('SQLALCHEMY_DATABASE_URI')
    })
