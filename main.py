import qrcode
import time

def gerar(texto):
    imagem = qrcode.make(f"{texto}")
    nome = f"qrcode_{time.time()}.png"
    imagem.save(f"app/static/src/{nome}")
    return nome