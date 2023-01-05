# For this program, I decided to create 2 classes: the first one, ProgramInterface, is accountable for setting the
# app interface as well as managing the parameters set by the user for custom his/her images and inherits the features
# of Tk class, from TkInter library, while the second one, Watermark, is the class accountable for actually applying the
# custom features to the user's images. The two classes are interconnected in the current file (main.py).
from interface import ProgramInterface
from add_watermark import Watermark

# The edit_image() function, once the parameters and the image to be edited are provided, is responsible for triggering
# the Watermark functions that custom the provided image, besides handling errors that might occur. The logo_bool and
# written_bool variables indicate the kind of watermarking the images received (it is going to be useful when we are
# setting the file name for saving it).
def edit_image(params, image_to_be_edited):
    global logo_bool, written_bool
    if 'logo' in params.keys():
        image_to_be_edited.add_logo(**params['logo'])
        logo_bool = True
    if 'written' in params.keys():
        try:
            image_to_be_edited.add_text(**params['written'])
        except OSError:
            app.app_error()
            return None
        written_bool = True
    return image_to_be_edited

# The function bellow is the one triggered when user clicks on submit button. It gets the parameters set by the user
# through ProgramInterface's get_parameters() function. This get_parameters() function returns False if the user did not
# provide an essential info, as a image file.
def submit_click():
    global logo_bool, written_bool
    parameters = app.get_parameters()
    if not parameters:
        return
    logo_bool = False
    written_bool = False
    for file in parameters['filesnames']:
        # Setting the Watermark object. It is the image to be edited.
        wtmk_image = Watermark(file)
        if edit_image(params=parameters, image_to_be_edited=wtmk_image):
            edit_image(params=parameters, image_to_be_edited=wtmk_image).\
            save_image(directory=app.askdirectory_(), file_format=".png", logo=logo_bool, written=written_bool)

# Similar to submit() function, this one in time is triggered when user clicks on Preview button. The difference is that
# this one does not save anything, just show the first edited image on GUI so that the user can see if it is the final
# result he/she is looking for.
def preview_click():
    parameters = app.get_parameters()
    if not parameters:
        return
    # Setting the Watermark object. It is the image to be edited.
    wtmk_image = Watermark(parameters['filesnames'][0])
    if edit_image(params=parameters, image_to_be_edited=wtmk_image):
        image_tk = wtmk_image.pil_to_tk(edit_image(params=parameters, image_to_be_edited=wtmk_image))
        app.preview(image=wtmk_image.image, image_tk=image_tk)

# Setting the ProgramInterface object, called by me of "app". Also, assigning the functions to "Submit" and "Preview"
# buttons.
app = ProgramInterface()
app.submit_button.config(command=submit_click)
app.preview_button.config(command=preview_click)
app.mainloop()
