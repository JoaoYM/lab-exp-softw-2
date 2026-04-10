import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def convert_md_to_pdf():
    # Definição de caminhos
    base_dir = Path(__file__).resolve().parent.parent.parent
    reports_dir = base_dir / "reports"
    md_file = reports_dir / "relatorio.md"
    pdf_file = reports_dir / "relatorio.pdf"
    
    if not md_file.exists():
        print(f"❌ Arquivo não encontrado: {md_file}")
        return

    print("📖 Lendo o arquivo Markdown...")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Converte MD para HTML (suportando tabelas e blocos de código)
    print("⚙️  Convertendo para HTML...")
    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Monta o HTML com uma estrutura básica
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Relatório Laboratório 02</title>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # CSS Moderno focado em impressão (WeasyPrint)
    css_content = """
    @page {
        size: A4;
        margin: 2.5cm 3cm 2.5cm 3cm; /* Padrão aproximado ABNT */
        @bottom-right {
            content: counter(page);
            font-family: "Times New Roman", serif;
            font-size: 10pt;
        }
    }
    
    body { 
        font-family: "Times New Roman", serif; 
        font-size: 12pt;
        line-height: 1.5; 
        text-align: justify;
        color: #000;
    }
    
    h1, h2, h3 { 
        font-family: "Arial", sans-serif;
        color: #333;
        page-break-after: avoid; /* Evita que o título fique isolado no final da página */
    }
    
    h1 { font-size: 16pt; text-align: center; margin-bottom: 24pt; }
    h2 { font-size: 14pt; margin-top: 18pt; }
    
    img { 
        max-width: 100%; 
        height: auto; 
        display: block;
        margin: 20px auto;
        page-break-inside: avoid; /* Evita cortar imagens no meio */
    }
    
    table { 
        border-collapse: collapse; 
        width: 100%; 
        margin: 20px 0; 
        page-break-inside: avoid;
    }
    
    th, td { 
        border: 1px solid #000; 
        padding: 8px; 
        text-align: center; 
    }
    
    th { background-color: #f2f2f2; font-weight: bold; }
    
    blockquote {
        margin: 15px 40px;
        font-style: italic;
        color: #555;
    }
    """

    print("🚀 Gerando o PDF com WeasyPrint...")
    try:
        # Usa o formato URI seguro (file:///) apontando diretamente para a pasta reports
        base_uri = reports_dir.resolve().as_uri() + "/"
        
        HTML(string=html_content, base_url=base_uri).write_pdf(
            target=str(pdf_file),
            stylesheets=[CSS(string=css_content)]
        )
        print(f"✅ Sucesso! PDF gerado e salvo em: {pdf_file}")
    except Exception as e:
        print(f"❌ Erro ao gerar o PDF: {e}")

if __name__ == "__main__":
    convert_md_to_pdf()