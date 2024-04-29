from io import BytesIO
import cairosvg
from PIL import Image


def make_icon(base_color, icon_file, key_image):
    # ベース画像の生成
    base_image = Image.new("RGBA", (300, 300), color=base_color + "FF")

    # アイコン画像の読み込み
    # icon_image = Image.open(icon_file).convert("RGBA")
    png_image = cairosvg.svg2png(url=icon_file, )
    with BytesIO(png_image) as f:
        icon_image = Image.open(f).convert("RGBA")
        # icon_image.putalpha(128)

    # キー画像の読み込み
    key_image = Image.open(key_image).convert("RGBA")

    # アイコン画像のリサイズ
    icon_image = icon_image.resize((200, 200))
    

    # キー画像のリサイズ
    key_image = key_image.resize((100, 100))

    # ベース画像にアイコン画像を貼り付け
    base_image.paste(icon_image, (100, 100), icon_image)

    # ベース画像にキー画像を貼り付け
    base_image.paste(key_image, (150, 150), key_image)
    # # base_image.save("base_image_with_key.png")

    return base_image


if __name__ == "__main__":
    base_color = "#0000ff"
    # icon_file = "../data/icon.png"
    icon_file = "../data/paintbrush-solid.svg"
    key_image = "../data/key-image.png"

    # with open("../data/icon_file.png", "wb") as f:
    #     f.write(make_icon(base_color, icon_file, key_image))
    icon_file = make_icon(base_color, icon_file, key_image)
    icon_file.show()
    # icon_file.save("../data/icon_file.png")
