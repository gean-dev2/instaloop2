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

@debug_bp.route('/db-test', methods=['GET'])
def test_db_connection():
    """Testa conexão com banco de dados."""
    try:
        from extensions import db
        from sqlalchemy import text
        
        # Testa conexão
        with db.engine.connect() as conn:
            result = conn.execute(text("SELECT 1 as test"))
            row = result.fetchone()
            
        return jsonify({
            'status': 'success',
            'database_type': 'postgresql' if 'postgresql' in str(db.engine.url) else 'sqlite',
            'database_url': str(db.engine.url).replace(str(db.engine.url.password or ''), '***') if db.engine.url.password else str(db.engine.url),
            'test_result': row[0] if row else None
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': type(e).__name__
        })
