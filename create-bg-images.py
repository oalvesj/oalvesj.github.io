import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
import numpy as np

# Criar diretório para salvar as imagens
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Função para criar um fundo tech gradiente
def create_tech_gradient_bg(width, height, filename, colors=None):
    if colors is None:
        colors = [(25, 25, 40), (60, 60, 100)]
    
    img = Image.new('RGB', (width, height), color=colors[0])
    draw = ImageDraw.Draw(img)
    
    # Criar gradiente
    for y in range(height):
        r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * y / height)
        g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * y / height)
        b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Adicionar elementos tech
    for _ in range(50):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(50, 200)
        y2 = y1 + random.randint(1, 3)
        
        # Cor com um toque de laranja (tema do site)
        line_color = (255, 122, 48, random.randint(30, 100))
        draw.line([(x1, y1), (x2, y2)], fill=line_color, width=1)
    
    # Adicionar pontos brilhantes
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(1, 3)
        alpha = random.randint(30, 150)
        draw.ellipse((x-r, y-r, x+r, y+r), fill=(255, 255, 255, alpha))
    
    # Aplicar um leve desfoque
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    # Salvar a imagem
    img.save(os.path.join(output_dir, filename))
    print(f"Imagem salva: {filename}")
    return img

# Função para criar um fundo com grid tech
def create_tech_grid_bg(width, height, filename):
    # Criar uma imagem com fundo escuro
    img = Image.new('RGB', (width, height), color=(15, 15, 25))
    draw = ImageDraw.Draw(img)
    
    # Desenhar linhas de grid
    grid_spacing = 50
    grid_color = (40, 40, 60, 100)
    
    # Linhas horizontais
    for y in range(0, height, grid_spacing):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
    
    # Linhas verticais
    for x in range(0, width, grid_spacing):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    
    # Adicionar pontos de destaque nas interseções
    for x in range(0, width, grid_spacing):
        for y in range(0, height, grid_spacing):
            if random.random() > 0.7:  # Apenas algumas interseções
                r = random.randint(1, 3)
                # Usar a cor primária do site (laranja)
                draw.ellipse((x-r, y-r, x+r, y+r), fill=(255, 122, 48, random.randint(100, 200)))
    
    # Adicionar alguns elementos hexagonais (representando tecnologia)
    for _ in range(15):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(20, 60)
        
        # Desenhar hexágono
        hex_points = []
        for i in range(6):
            angle = i * 60 * 3.14159 / 180
            px = x + size * np.cos(angle)
            py = y + size * np.sin(angle)
            hex_points.append((px, py))
        
        # Cor com um toque de laranja (tema do site)
        hex_color = (255, 122, 48, random.randint(10, 40))
        draw.polygon(hex_points, outline=hex_color, fill=None)
    
    # Salvar a imagem
    img.save(os.path.join(output_dir, filename))
    print(f"Imagem salva: {filename}")
    return img

# Função para criar um fundo com partículas tech
def create_particles_bg(width, height, filename):
    # Criar uma imagem com gradiente
    colors = [(10, 10, 20), (30, 30, 50)]
    img = Image.new('RGB', (width, height), color=colors[0])
    draw = ImageDraw.Draw(img)
    
    # Criar gradiente
    for y in range(height):
        r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * y / height)
        g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * y / height)
        b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Adicionar partículas
    for _ in range(300):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(1, 4)
        
        # Algumas partículas na cor primária (laranja)
        if random.random() > 0.7:
            particle_color = (255, 122, 48, random.randint(50, 150))
        else:
            brightness = random.randint(100, 200)
            particle_color = (brightness, brightness, brightness, random.randint(30, 100))
        
        draw.ellipse((x-r, y-r, x+r, y+r), fill=particle_color)
    
    # Adicionar algumas linhas conectando partículas
    for _ in range(50):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(-200, 200)
        y2 = y1 + random.randint(-200, 200)
        
        line_color = (255, 255, 255, random.randint(10, 30))
        draw.line([(x1, y1), (x2, y2)], fill=line_color, width=1)
    
    # Salvar a imagem
    img.save(os.path.join(output_dir, filename))
    print(f"Imagem salva: {filename}")
    return img

# Criar imagens de fundo
create_tech_gradient_bg(1920, 1080, 'hero-bg.jpg', colors=[(15, 15, 25), (40, 40, 70)])
create_tech_grid_bg(1920, 1080, 'about-bg.jpg')
create_particles_bg(1920, 1080, 'skills-bg.jpg')
create_tech_gradient_bg(1920, 1080, 'contact-bg.jpg', colors=[(40, 40, 70), (15, 15, 25)])

print("Todas as imagens de fundo foram criadas com sucesso!")
