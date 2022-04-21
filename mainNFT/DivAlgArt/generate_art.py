import random
from PIL import Image, ImageDraw

def generate_art():
    print("Generating Art!")
    image_size_px = 128
    image_bg_color = (255, 255, 255)
    image = Image.new(
        size=(image_size_px, image_size_px), 
        mode="RGB", 
        color= (image_bg_color),
        )

    # Draw some lines  
    draw = ImageDraw.Draw(image)
    line_xy = ((0, 0 ), (image_size_px, image_size_px))    
    line_color = (0, 0, 0)
    draw.line(line_xy, fill=line_color)

    for _ in range(10):
        random_points_1 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px)
            )
        random_points_2 = (
            random.randint(0, image_size_px),
            random.randint(0, image_size_px)
        )
        line_xy = (random_points_1, random_points_2)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill=line_color)

    image.show()
    image.save("test_art.png")


if __name__ == "__main__":
    generate_art()