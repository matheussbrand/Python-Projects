# Importa as bibliotecas necessárias para criar e salvar o QR code em formato SVG
import qrcode  # Biblioteca para criar QR codes
import qrcode.image.svg  # Módulo específico para criar QR codes em formato SVG

# Define a fábrica de imagem como SvgPathImage, que é a classe específica para criar imagens SVG
factory = qrcode.image.svg.SvgPathImage

# Cria o QR code com o conteúdo "Hi, Stranger!" e especifica a fábrica de imagem como SvgPathImage
svg_img = qrcode.make("Hi, Stranger!", image_factory=factory)

# Salva o QR code gerado no arquivo "qrcode.svg"
svg_img.save("qrcode.svg")
