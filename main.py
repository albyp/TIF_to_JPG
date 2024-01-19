import os
from PIL import Image, UnidentifiedImageError

# SETTINGS
# enter the root folder to search
path = 'X:\\01-ARCHIVED EOW-IPF-PB-DATA FROM K DRIVE\\EOW'
# location to save outputs
output_path = 'Outputs'
# maximum x, y resolution of output
resolution = 8000
# quality of output (0-100)
img_quality = 80

extension = '.tif'

# disable limit for resolution
Image.MAX_IMAGE_PIXELS = None

# check if the output folder exists, if not, create it
if not os.path.exists(output_path):
    os.mkdir(output_path)

# check existing files in the output folder
existing_files = set(os.listdir(output_path))

# iterate through path
for root, dirs, files in os.walk(path):
    for name in files:
        # check if the file has the specified extension, does not contain "tiles" or "dem" in its name
        if extension in name and "tiles" not in name.lower() and "dem" not in name.lower():
            # check if the file is not already in the output folder
            if name not in existing_files:
                print("Processing file: ", name)
                infile = os.path.join(root, name)
                
                # change the extension to '.jpg' in the outfile variable
                outfile = os.path.join(output_path, name[:-3] + 'jpg')

                try:
                    im = Image.open(infile)
                    im.thumbnail((resolution, resolution))
                    out = im.convert('RGB')
                    out.save(outfile, 'JPEG', quality=img_quality)
                    print("File saved as:", outfile)
                except UnidentifiedImageError:
                    print("Skipping file (UnidentifiedImageError): ", name)
            else:
                print("File already exists in the output folder: ", name)
        else:
            print("Skipping file (contains 'tiles' or 'dem'): ", name)