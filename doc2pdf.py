from docx2pdf import convert
import os

# Create folders if they don't exist
os.makedirs('scraping', exist_ok=True)
os.makedirs('statci', exist_ok=True)

# Convert all DOCX files using absolute paths
for file in os.listdir('scraping'):
    if file.endswith('.docx'):
        input_path = os.path.abspath(f'scraping/{file}')
        output_path = os.path.abspath(f'static/{file.replace(".docx", ".pdf")}')
        
        try:
            convert(input_path, output_path)
            print(f'✓ Converted: {file}')
        except Exception as e:
            print(f'✗ Failed: {file} - {e}')