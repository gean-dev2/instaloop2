#!/usr/bin/env python3
"""
Ponto de entrada para a aplicação Flask na Vercel.
Este arquivo atua como um wrapper para o app.py principal.
"""

import os
import sys
from pathlib import Path

print("🚀 API INDEX - STARTING")

# FORÇAR VARIÁVEIS DE AMBIENTE ANTES DE QUALQUER COISA
os.environ['VERCEL'] = '1'
os.environ['FLASK_ENV'] = 'production'
os.environ['DATABASE_URL'] = 'postgresql://postgres.ynotajlmnxdrvelzxdyq:Darson2017%40%40@aws-1-us-east-1.pooler.supabase.com:6543/postgres'
os.environ['JWT_SECRET_KEY'] = '967e561a954b541927ff56b1ca03237f9ca1abede1bf0d1d80b3d952054d181'
os.environ['ADMIN_ROUTE_SECRET'] = 'Nj4SzW3JoQQ'
os.environ['SECRET_KEY'] = '24ffbcb16d218148b229935b9019606ee345d8070bec2a6fa552046981520edf'

print("� ENVIRONMENT VARIABLES SET")

# Adicionar o diretório backend ao path Python
backend_dir = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_dir))
print(f"🔧 BACKEND DIR ADDED TO PATH: {backend_dir}")

# Importar e criar a aplicação
try:
    from app import create_app
    print("✅ APP MODULE IMPORTED")
except Exception as e:
    print(f"❌ ERROR IMPORTING APP: {e}")
    raise

# Criar instância da aplicação para ambiente serverless
try:
    app = create_app('production')
    print("✅ APP CREATED SUCCESSFULLY")
except Exception as e:
    print(f"❌ ERROR CREATING APP: {e}")
    raise

# Debug: mostrar rotas registradas
print("\n=== ROTAS REGISTRADAS ===")
for rule in app.url_map.iter_rules():
    print(f"  {rule.rule} -> {rule.endpoint} [{', '.join(rule.methods)}]")
print("========================\n")

# Exportar para Vercel
# Vercel espera uma variável 'app' ou 'handler' no módulo principal
__all__ = ['app']

print("🎯 API INDEX - READY")
