# In this module, we are dealing with the Program interface. To do so, we are going to need many resources from
# tkinter library. These resources are need to many goals, from setting the screen where the program will be displayed
# to providing a better user experience (e.g. to open dialog boxes to notify some problem or make the files selection
# easier. The matplotlib library is also being used, but just for listing some fonts to be chosen by the user, just for
# practical purpose.
from tkinter import *
from tkinter.filedialog import askopenfilenames, askopenfilename, askdirectory
import tkinter.messagebox
from matplotlib import font_manager

# The ProgramInterface class inherits features from Tk class.
class ProgramInterface(Tk):
    # Throughout this init function, the program interface is being set.
    def __init__(self):
        super().__init__()
        # Some basic settings.
        self.config(padx=20, pady=20)
        self.title("Image Watermarker")
        # Here the user can choose the watermark type he/she wants.
        self.text_1 = Label(text="WaterMark Type:")
        self.text_1.grid(column=1, row=0, stick="w")
        self.written_wm = tkinter.BooleanVar()
        self.logo_wm = tkinter.BooleanVar()
        self.written = Checkbutton(self, text="Written", onvalue=True, offvalue=False, variable=self.written_wm)
        self.logo = Checkbutton(self, text="Logo", onvalue=True, offvalue=False, variable=self.logo_wm)
        self.written.grid(column=2, row=0, stick="w"), self.logo.grid(column=3, row=0, stick="w")
        # In this part there are 2 buttons. One for choosing the images the user wants to customize and another for
        # choosing the logo user wants to add to his/her images.
        self.files_label = Label(text="Select the Images:")
        self.files_button = Button(text="Click to Select", command=self.select_images)
        self.logo_label = Label(text="Select the Logo:")
        self.logo_button = Button(text="Click to Select", command=self.select_logo)
        self.files_button.grid(column=2, row=1, stick="w"), self.logo_button.grid(column=2, row=2, stick="w")
        self.files_label.grid(column=1, row=1, stick="w"), self.logo_label.grid(column=1, row=2, stick="w")
        # If user wants, he/she can set some transparency to the logo image.
        self.transparency_label = Label(text="Add Transparency:")
        self.transparency_select = Spinbox(from_=0, to=255, width=10)
        self.transparency_select.delete(0, "end")
        self.transparency_label.grid(column=1, row=3, stick="w")
        self.transparency_select.grid(column=2, row=3, stick="w")
        # If user has chosen a text watermark, the field bellow allows to set the text to be added to the image.
        self.text_label = Label(text="Text to Be Added:")
        self.text_entry = Entry()
        self.text_label.grid(column=1, row=4, stick="w"), self.text_entry.grid(column=2, row=4, stick="w")
        # The users also can set a font to the text. The fonts displayed are imported from matplotlib. Some of them
        # do not work so, in order to improve the User Experience, the ones that does not work are added to a .txt file,
        # so that they are removed from the list and are not being loaded again in the future.
        self.font_label = Label(text="Choose the Font:")
        available_fonts = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
        available_fonts = sorted([item.split('.')[-2].split('\\')[-1].title() for item in available_fonts])
        try:
            with open('unavailable-fonts.txt', "r") as unavailable_fonts:
                to_be_excluded = unavailable_fonts.read().splitlines()
            available_fonts = [item for item in available_fonts if item not in to_be_excluded]
        except:
            with open('unavailable-fonts.txt', "w") as unavailable_fonts:
                pass
        self.font_variable = StringVar(self)
        self.font_list = OptionMenu(self, self.font_variable, *available_fonts)
        self.font_list.config(width=10)
        self.font_label.grid(column=1, row=5, stick="w"), self.font_list.grid(column=2, row=5, stick="w")
        # Setting the font size.
        self.fontsize_label = Label(text="Set the Fontsize:")
        self.fontsize_select = Spinbox(from_=0, to=100, width=10)
        self.fontsize_select.delete(0, "end")
        self.fontsize_label.grid(column=1, row=6, stick="w"), self.fontsize_select.grid(column=2, row=6, stick="w")
        # User can also add some transparency to the text.
        self.text_transparency_label = Label(text="Add Text Transparency:")
        self.text_transparency_select = Spinbox(from_=0, to=255, width=10)
        self.text_transparency_select.delete(0, "end")
        self.text_transparency_label.grid(column=1, row=7, stick="w"), self.text_transparency_select.grid(column=2, row=7, stick="w")
        # Here there are 3 Spinbox for getting an RGB color, so that user can customize a bit more his/her text.
        self.color_label = Label(text="Set Text Color:")
        self.red_label = Label(text="Set Red:")
        self.blue_label = Label(text="Set Blue:")
        self.green_label = Label(text="Set Green:")
        self.red_select = Spinbox(from_=0, to=255, width=10)
        self.green_select = Spinbox(from_=0, to=255, width=10)
        self.blue_select = Spinbox(from_=0, to=255, width=10)
        self.color_label.grid(column=1, row=8, stick="w")
        self.red_select.delete(0, "end")
        self.green_select.delete(0, "end")
        self.blue_select.delete(0, "end")
        self.red_label.grid(column=2, row=8, stick="w"), self.red_select.grid(column=3, row=8, stick="w")
        self.green_label.grid(column=2, row=9, stick="w"), self.green_select.grid(column=3, row=9, stick="w")
        self.blue_label.grid(column=2, row=10, stick="w"), self.blue_select.grid(column=3, row=10, stick="w")
        # Setting the text position.
        self.text_position_label = Label(text="Set Text Position:")
        self.text_x_label = Label(text="X:")
        self.text_y_label = Label(text="Y:")
        self.text_x_select = Spinbox(from_=0, to=2550, width=10)
        self.text_y_select = Spinbox(from_=0, to=2550, width=10)
        self.text_y_select.delete(0, "end")
        self.text_x_select.delete(0, "end")
        self.text_position_label.grid(column=1, row=11, stick="w")
        self.text_x_label.grid(column=2, row=11, stick="w"), self.text_x_select.grid(column=3, row=11, stick="w")
        self.text_y_label.grid(column=2, row=12, stick="w"), self.text_y_select.grid(column=3, row=12, stick="w")
        # If he/she like, user can set a rotation to his/her text.
        self.text_rotate_label = Label(text="Set the Text Rotation")
        self.text_rotate_select = Spinbox(from_=0, to=360, width=10)
        self.text_rotate_select.delete(0, "end")
        self.text_rotate_label.grid(column=1, row=13, stick="w"), self.text_rotate_select.grid(column=2, row=13, stick="w")
        # The button for applying the features set above.
        self.submit_button = Button(text="Submit")
        self.submit_button.grid(column=2, row=20)
        # Preview button, so that user can foresee the final result before saving anything.
        self.preview_button = Button(text="Preview")
        self.preview_button.grid(column=3, row=20)
    # The function bellow opens a dialog box where user can select his/her logo image. It also returns the number of
    # files selected (green check if there is a file selected).
    def select_logo(self):
        global filename
        filename = askopenfilename(filetypes=[('Images', '.jpeg .jpg .png')])
        if filename:
            n = "✔ 1"
        else:
            n = "❌ 0"
        self.logo_button.config(text=f'{n} file selected.')

    # The function bellow opens a dialog box where user can select his/her images to be customized. It also returns the number of
    # files selected (green check if there is a file selected).
    def select_images(self):
        global filesnames
        filesnames = askopenfilenames(filetypes=[('Images', '.jpeg .jpg .png')])
        if len(filesnames) > 0:
            self.files_button.config(text=f'✔ {len(filesnames)} file(s) selected.')
        else:
            self.files_button.config(text=f'❌ {len(filesnames)} file(s) selected.')

    # The function bellow is accountable for showing the result preview. The difference between "image" and "image_tk"
    # is that the second one is supported by TkInter, so it can be shown on the GUI (check preview_click() in main.py).
    def preview(self, image, image_tk):
        preview_label = Label(text="Take a Look:")
        preview_label.grid(column=5, row=0)
        preview_img = Label(image=image_tk)
        preview_img.image = image_tk
        preview_img.grid(column=5, row=1, rowspan=20, padx=20)
        preview_dimensions = Label(text=f'({image.size[0]} x {image.size[1]})')
        preview_dimensions.grid(column=5, row=13)
    # In the function bellow all the parameters set by the user are got together in a dictionary. This dictionary will
    # be used to both logo and text (if the user likes so).
    def get_parameters(self):
        kwargs = {}
        try:
            kwargs['filesnames'] = filesnames
        except:
            tkinter.messagebox.showerror("No File Selected", "Please, select at least one image file.")
            return False

        if self.logo_wm.get():
            kwargs['logo'] = {}
            try:
                kwargs['logo']['logo_image'] = filename
            except:
                tkinter.messagebox.showerror("No File Selected", "Please, select your logo image.")
                return False
            if not self.transparency_select.get():
                kwargs['logo']['alpha'] = 255
            else:
                kwargs['logo']['alpha'] = int(self.transparency_select.get())

        if self.written_wm.get():
            kwargs['written'] = {}
            if self.fontsize_select.get() and int(self.fontsize_select.get()) > 0:
                kwargs['written']['fontsize'] = int(self.fontsize_select.get())
            if self.font_variable.get():
                kwargs['written']['font'] = self.font_variable.get().lower()
            if self.red_select.get() or self.green_select.get() or self.blue_select.get() or self.text_transparency_select.get():
                color = []
                for item in [self.red_select.get(), self.blue_select.get(), self.green_select.get(),
                             self.text_transparency_select.get()]:
                    if item:
                        color += [int(item)]
                    else:
                        if item == self.text_transparency_select.get():
                            pass
                        else:
                            color += [0]
                color = tuple(color)
                kwargs['written']['color'] = color
            if self.text_x_select.get() or self.text_y_select.get():
                position = []
                for coordinate in [self.text_x_select.get(), self.text_y_select.get()]:
                    if coordinate:
                        position += [int(coordinate)]
                    else:
                        position += [0]
                position = tuple(position)
                kwargs['written']['position'] = position
            if self.text_entry.get():
                kwargs['written']['text'] = self.text_entry.get()

            if self.text_rotate_select.get():
                kwargs['written']['angle'] = int(self.text_rotate_select.get())

        return kwargs
    # The app_error() function is triggered when the font can not be loaded. When it occurs, besides user being notified,
    # so that he/she can choose another font, the troublesome font name is added to unavailable-fonts.txt and deleted
    # from the font_list, so that user can not choose it again.
    def app_error(self):
        with open("unavailable-fonts.txt", "a") as unavailable_fonts_2:
            unavailable_fonts_2.write(f'{self.font_variable.get()}\n')
            self.font_list['menu'].delete(self.font_list['menu'].index(self.font_variable.get()))

        tkinter.messagebox.showerror(title='Font Unavailable', message="This font is not available."
                                                                   "\nPlease, choose another one.")
    # The function bellow is triggered when used has submitted the work. It is a frindly way for user choosing the file
    # he/she wants to save the images in.
    def askdirectory_(self):
        return askdirectory()

