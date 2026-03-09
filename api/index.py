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

# Exportar para Vercel
# Vercel espera uma variável 'app' ou 'handler' no módulo principal
__all__ = ['app']
