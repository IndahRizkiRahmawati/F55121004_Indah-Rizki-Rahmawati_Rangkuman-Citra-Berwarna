# Import library yang dibutuhkan
from PIL import Image

# Fungsi untuk mengambil nilai RGB dari sebuah pixel
def get_pixel_rgb(img, x, y):
    r, g, b = img.getpixel((x,y))
    return r, g, b

# Fungsi untuk mengubah nilai RGB dari sebuah pixel
def set_pixel_rgb(img, x, y, r, g, b):
    img.putpixel((x,y), (r,g,b))

# Buka gambar
image = Image.open("img1.jpeg")

# Dapatkan ukuran gambar
width, height = image.size

# Iterasi setiap pixel pada gambar
for x in range(width):
    for y in range(height):
        # Ambil nilai RGB dari pixel saat ini
        r, g, b = get_pixel_rgb(image, x, y)

        # Ubah nilai RGB dari pixel saat ini
        r = 255 - r
        g = 255 - g
        b = 255 - b

        # Set nilai RGB baru ke pixel saat ini
        set_pixel_rgb(image, x, y, r, g, b)

# Simpan gambar yang telah diubah
image.save("gambar_rgb.jpg")

