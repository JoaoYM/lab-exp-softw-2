import os
import subprocess
import shutil
import csv
from pathlib import Path

class MetricsCollector:
    def __init__(self, ck_jar_path: str = "ck.jar"):
        self.base_path = Path(__file__).resolve().parent.parent.parent
        self.data_dir = self.base_path / "data"
        self.temp_clone_dir = self.base_path / "temp_repos"
        self.ck_jar_path = self.base_path / ck_jar_path
        
    def process_single_repository(self, repo_url: str, repo_name: str):
        """Clona o repositório, roda o CK e limpa a pasta"""
        repo_path = self.temp_clone_dir / repo_name.replace("/", "_")
        
        # 1. Clone do repositório
        print(f"\n📥 Clonando {repo_name}...")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, str(repo_path)], check=True)
        
        # 2. Execução da ferramenta CK
        print(f"⚙️ Analisando métricas com CK em {repo_name}...")
        # O CK gera os arquivos CSV (class, method, etc) no diretório de saída especificado
        output_dir = self.data_dir / "ck_results" / repo_name.replace("/", "_")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            subprocess.run([
                "java", "-jar", str(self.ck_jar_path),
                str(repo_path), "true", "0", "False", str(output_dir)
            ], check=True)
            print(f"✅ Análise concluída. Resultados salvos em {output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao rodar CK: {e}")
            
        # 3. Limpeza (Deleta o repositório clonado para não encher o HD)
        print("🧹 Removendo arquivos clonados...")
        shutil.rmtree(repo_path, ignore_errors=True)

    def run_first_repository(self):
        """Para o Lab02S01, analisa apenas 1 repositório do arquivo coletado"""
        csv_file = self.data_dir / 'repos.csv'
        if not csv_file.exists():
            print("❌ Arquivo repos.csv não encontrado. Rode a coleta primeiro.")
            return

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            first_repo = next(reader)
            
        self.process_single_repository(first_repo['url'], first_repo['name'])