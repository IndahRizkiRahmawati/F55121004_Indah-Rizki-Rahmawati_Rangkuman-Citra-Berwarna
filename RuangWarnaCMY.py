# Import library yang dibutuhkan
from PIL import Image

# Fungsi untuk mengambil nilai CMY dari sebuah pixel
def get_pixel_cmy(img, x, y):
    r, g, b = img.getpixel((x,y))
    c = 255 - r
    m = 255 - g
    y = 255 - b
    return c, m, y

# Fungsi untuk mengubah nilai CMY dari sebuah pixel
def set_pixel_cmy(img, x, c, m, y):
    r = 255 - c
    g = 255 - m
    b = 255 - y
    img.putpixel((x,y), (r,g,b))

# Buka gambar
image = Image.open("img1.jpeg")

# Dapatkan ukuran gambar
width, height = image.size

# Iterasi setiap pixel pada gambar
for x in range(width):
    for y in range(height):
        # Ambil nilai CMY dari pixel saat ini
        c, m, y = get_pixel_cmy(image, x, y)

        # Ubah nilai CMY dari pixel saat ini
        c = 255 - c
        m = 255 - m
        y = 255 - y

        # Set nilai CMY baru ke pixel saat ini
        set_pixel_cmy(image, x, c, m, y)

# Simpan gambar yang telah diubah
image.save("gambar_cmy.jpg")

