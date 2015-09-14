import exifread

test_path = "photos/IMG_0679.jpg"

class GPScoordinates(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def grab_tags(filepath):
    """ A wee function to grab the EXIF tags of a given photo when provided with
    the path to that file. """
    # open image file for reading (in binary mode)
    f = open(filepath, 'rb')

    # grab EXIF tags
    tags = exifread.process_file(f)

    return tags


def starts_with(given_string, substring):
    """ Returns boolean to indicate if the given_string starts with the substring. """
    if substring == given_string[:len(substring)]:
        return True
    else:
        return False


def get_gps_tags(filepath = test_path):
    """ Takes output from grab_tags, returning only the GPS tags. """
    gps_tags = []
    for tag in grab_tags(filepath).keys():
        if starts_with(tag, 'GPS'):
            gps_tags.append(tag)
    return gps_tags


print grab_tags(test_path)
