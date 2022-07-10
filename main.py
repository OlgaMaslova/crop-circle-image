import numpy as np
from PIL import Image, ImageDraw

def crop_circle(zoom, offset_x, offset_y):
    # Open the input image as numpy array, convert to RGB
    img = Image.open("moana.jpeg").convert("RGB")
    w, h = img.size
    # on the site image is fitted in container of width 400px
    # so we take the scale of the transformation due to site representation
    scale_on_site = w / 400
    diameter = 400 * scale_on_site
    start_x = offset_x * scale_on_site
    start_y = offset_y * scale_on_site
    # crop the square of interest chosen by the user (coordinates transformed to sizes of the real image, undo zoom)
    cropped = img.crop((start_x / zoom, start_y / zoom,
                        (start_x + diameter / zoom), (start_y + diameter / zoom)))
    # save to visualize
    cropped.save("cropped_image.jpg")
    npImage = np.array(cropped)
    # Create same size alpha layer with circle
    alpha = Image.new('L', cropped.size, 0)
    draw = ImageDraw.Draw(alpha)

    # draw a pie (complete circle in our case) in the chosen square
    draw.pieslice(((0, 0), (diameter / zoom, diameter / zoom)), 0, 360, fill=255)

    # Convert alpha Image to numpy array
    npAlpha = np.array(alpha)

    # Add alpha layer to RGB
    npImage = np.dstack((npImage, npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('result.png')


if __name__ == '__main__':
    crop_circle(zoom=2.01, offset_x=159, offset_y=30)

