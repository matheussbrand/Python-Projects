import qrcode  # Importa o módulo qrcode para gerar QR codes

# Cria um objeto QRCode com os seguintes parâmetros:
qr = qrcode.QRCode(
    version=1,  # Versão do QR code (no caso, 1)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro (baixo)
    box_size=20,  # Tamanho dos quadrados que compõem o QR code
    border=2,
)  # Espessura da borda do QR code

# Adiciona os dados que serão codificados no QR code
qr.add_data("https://www.linkedin.com/in/matheussbrandao/")

# Gera o QR code
qr.make(fit=True)

# Gera a imagem do QR code com as cores especificadas
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem do QR code como um arquivo PNG
img.save("link.png")
