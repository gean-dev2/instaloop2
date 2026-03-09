#!/usr/bin/env python3
"""
Script para configurar InstaLoop com Supabase
"""

import os
import sys
from sqlalchemy import create_engine, text

def setup_supabase():
    """Configura o banco de dados Supabase para o InstaLoop."""
    
    print("🚀 Configurando InstaLoop com Supabase...")
    
    # Verificar DATABASE_URL
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ ERRO: DATABASE_URL não encontrado!")
        print("Configure a variável de ambiente DATABASE_URL:")
        print("export DATABASE_URL='postgresql://postgres:[PASSWORD]@[PROJECT_ID].supabase.co:5432/postgres'")
        return False
    
    print(f"✅ DATABASE_URL encontrado: {database_url.split('@')[1]}")
    
    try:
        # Conectar ao Supabase
        engine = create_engine(database_url)
        
        # Ler schema SQL
        schema_file = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
        if not os.path.exists(schema_file):
            print("❌ ERRO: Arquivo schema.sql não encontrado!")
            return False
        
        with open(schema_file, 'r') as f:
            schema_sql = f.read()
        
        # Executar schema
        with engine.connect() as conn:
            print("📝 Criando tabelas no Supabase...")
            conn.execute(text(schema_sql))
            conn.commit()
        
        print("✅ Tabelas criadas com sucesso!")
        
        # Verificar tabelas
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = 'public' 
                ORDER BY table_name
            """))
            tables = [row[0] for row in result]
            
            print(f"📊 Tabelas criadas: {', '.join(tables)}")
        
        print("🎉 Supabase configurado com sucesso!")
        print("\n📝 Próximos passos:")
        print("1. Adicione DATABASE_URL ao Environment Variables da Vercel")
        print("2. Faça deploy novamente")
        print("3. O InstaLoop usará Supabase como banco persistente")
        
        return True
        
    except Exception as e:
        print(f"❌ ERRO ao configurar Supabase: {e}")
        return False

if __name__ == "__main__":
    success = setup_supabase()
    sys.exit(0 if success else 1)
