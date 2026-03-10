#!/usr/bin/env python3
"""
Ponto de entrada para a aplicação Flask na Vercel.
Este arquivo atua como um wrapper para o app.py principal.
"""

import os
import sys
from pathlib import Path

# FORÇAR VARIÁVEIS DE AMBIENTE ANTES DE QUALQUER COISA
os.environ['VERCEL'] = '1'
os.environ['FLASK_ENV'] = 'production'
os.environ['DATABASE_URL'] = 'postgresql://postgres.ynotajlmnxdrvelzxdyq:Darson2017%40%40@aws-1-us-east-1.pooler.supabase.com:6543/postgres'
os.environ['JWT_SECRET_KEY'] = '967e561a954b541927ff56b1ca03237f9ca1abede1bf0d1d80b3d952054d181'
os.environ['ADMIN_ROUTE_SECRET'] = 'Nj4SzW3JoQQ'
os.environ['SECRET_KEY'] = '24ffbcb16d218148b229935b9019606ee345d8070bec2a6fa552046981520edf'

print("🚀 API INDEX - FORCING ALL ENVIRONMENT VARIABLES")
print(f"🔧 FORCED VERCEL: {os.environ.get('VERCEL')}")
print(f"🔧 FORCED DATABASE_URL: {os.environ.get('DATABASE_URL')[:50]}...")

# Adicionar o diretório backend ao path Python
backend_dir = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_dir))

# Importar e criar a aplicação
from app import create_app

print("🔍 DEBUG: Importing blueprints...")
try:
    from routes.auth import auth_bp
    print(f"✅ auth_bp imported with {len(auth_bp.deferred_functions) if hasattr(auth_bp, 'deferred_functions') else 'unknown'} routes")
except Exception as e:
    print(f"❌ Error importing auth_bp: {e}")

# Criar instância da aplicação para ambiente serverless
app = create_app('production')

print("✅ APP CREATED SUCCESSFULLY")
print(f"🔧 APP DATABASE_URI: {app.config.get('SQLALCHEMY_DATABASE_URI', 'NOT_FOUND')[:50]}...")

# Debug: mostrar rotas registradas
print("\n=== ROTAS REGISTRADAS ===")
for rule in app.url_map.iter_rules():
    print(f"  {rule.rule} -> {rule.endpoint} [{', '.join(rule.methods)}]")
print("========================\n")

# Exportar para Vercel
# Vercel espera uma variável 'app' ou 'handler' no módulo principal
__all__ = ['app']
