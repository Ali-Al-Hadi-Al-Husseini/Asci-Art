import PIL.Image

CHARS= ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.' ]

def resize(image , new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int( new_width * ratio)
    resized = image.resize((new_width, new_height))

    return resized


def convert_to_grey(image):
    gray_img = image.convert('L')
    return gray_img

def convert_pixels_to_asci(image):
    pixels = image.getdata()
    chars = ''.join([CHARS[pixel//25] for pixel in pixels ])
    return chars

def main(new_width=100):

    image_path = input("Enter image path:")
    try:
        image = PIL.Image.open(image_path)

    except Exception:
        print(image_path,"is invalid.")

    new_img = convert_pixels_to_asci( convert_to_grey( resize(image)))

    pixel_count = len(new_img)
    ascii_img = '\n'.join( new_img[i:(i + new_width)] for i in range(0, pixel_count, new_width ))

    print(ascii_img)

    with open('asci_image.txt', 'w') as pic:
        pic.write(ascii_img)
        
if __name__ == '__main__':
    main()
