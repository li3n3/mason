import exifread

test_path = "photos/IMG_0679.jpg"

def grab_tags(filepath):
    """ A wee function to grab the EXIF tags of a given photo when provided with
    the path to that file. """
    # open image file for reading (in binary mode)
    f = open(filepath, 'rb')

    # grab EXIF tags
    tags = exifread.process_file(f)

    return tags

grab_tags(test_path)
