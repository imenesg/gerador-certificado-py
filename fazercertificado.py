from PIL import Image, ImageFont, ImageDraw

with open(r'nomes alunos.txt', 'r') as f:
    nomes = f.read()
    for nome in nomes.split('\n'):
        if nome != "":
            cord_aluno = (1000,707)
            nome_pessoa = nome.strip()
            certificado = Image.open(r'certificadomodelo\certificadomodelo.png')
            caminho_fonte = r"fonte\Montserrat\Montserrat-VariableFont_wght.ttf"
            fonte_aluno = ImageFont.truetype (caminho_fonte, 115)
            cor_azul= (27,160,238)
            desenho = ImageDraw.Draw(certificado)
            desenho.text(cord_aluno, nome_pessoa, anchor="ms", font=fonte_aluno, fill=cor_azul)
            certificado.save(f'certificados alunos\{nome_pessoa}.png')

print("\033[92mPrograma Finalizado")
