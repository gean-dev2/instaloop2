#!/usr/bin/env python3
"""
Ponto de entrada para a aplicação Flask na Vercel.
Este arquivo atua como um wrapper para o app.py principal.
"""

import os
import sys
from pathlib import Path

# Adicionar o diretório backend ao path Python
backend_dir = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_dir))

# Importar e criar a aplicação
from app import create_app

# Criar instância da aplicação para ambiente serverless
app = create_app('production')

# Forçar ambiente de produção
import os
os.environ['FLASK_ENV'] = 'production'
os.environ['VERCEL'] = '1'

print("🚀 API INDEX - Forcing production environment")
print(f"🔧 ENV - FLASK_ENV: {os.environ.get('FLASK_ENV')}")
print(f"🔧 ENV - VERCEL: {os.environ.get('VERCEL')}")
print(f"🔧 ENV - DATABASE_URL: {os.environ.get('DATABASE_URL', 'NOT_SET')[:50]}...")

# Exportar para Vercel
# Vercel espera uma variável 'app' ou 'handler' no módulo principal
__all__ = ['app']
