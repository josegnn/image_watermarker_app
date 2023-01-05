# For handling the image customization, PIL package is going to be used.
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Watermark class takes the filename (including the path) and returns a Watermark object, from which it is possible to
# access the PIL Image.
class Watermark:
    def __init__(self, filename):
        self.filename = filename.split('.')[0].split('/')[-1]
        self.image = Image.open(filename).convert('RGBA')
    # The simple function bellow add the logo to the image right-bottom corner. It considers the transparency set by the
    # user (alpha).
    def add_logo(self, logo_image, alpha=255):
        self.logo = Image.open(logo_image).convert("RGBA")
        self.logo.putalpha(alpha)
        width, height = self.image.size
        if int(width / 5) < int(height / 5):
            logo = self.logo.resize((int(width / 5), int(width / 5)))
        else:
            logo = self.logo.resize((int(height / 5), int(height / 5)))
        logo_width, logo_height = logo.size
        self.image.paste(logo, (width - logo_width, height - logo_height), logo)

    # This function, in time, is accountable for adding the custom text to the image.
    def add_text(self, font='arial', fontsize=50, position=None, text="Hello, World!", color=(255, 255, 255), angle=0):
        if not position:
            # If user does not set a position, text will be placed at the image center.
            position = (self.image.size[0] / 2, self.image.size[1] / 2)
        # The variable bellow is a intermediate image, completely transparent, that is receiving the text.
        txt = Image.new("RGBA", self.image.size, (255, 255, 255, 0))
        img_font = ImageFont.truetype(f'{font}.ttf', fontsize)
        draw = ImageDraw.Draw(txt)
        draw.text(xy=position, text=text, font=img_font, fill=color, align="center", anchor="mm")
        txt = txt.rotate(angle=angle, expand=False)
        # In the line bellow, the intermediate image referred above will be merged with the user image.
        self.image = Image.alpha_composite(self.image, txt)

    # As its name says, the function bellow saves the image in the selected directory.
    def save_image(self, directory, file_format='.jpg', logo=False, written=False):
        # The logo and written variables come from "written_bool" and "logo_bool", in submit_click() function, in
        # main.py. When any of them is True, it means that logo or text was added to the image, so the filename is
        # edited in order to make it easy for user identifying his/her images.
        if logo:
            self.filename += '-lg'
        if written:
            self.filename += '-txt'
        self.image.save(f'{directory}/{self.filename}{file_format}')
    # The function bellow make the PIL image TkInter friendly.
    def pil_to_tk(self, image):
        return ImageTk.PhotoImage(image.image.resize((200, 200)))
