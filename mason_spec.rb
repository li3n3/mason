# starting to stab away at some things

describe Mason do
	it 'should print out latitude and longitude in hours/minutes/seconds'
		p = Mason.new
		p.


# do I have an object that represents a photo?
# do I have some data, and then it spits out lat/lon?

# put this kinda stuff in photo_spec.rb
# p = Photo.new("/tmp/photo.jpg")
# p.latitude
# => "0.22.33"
# p = Photo.new("/tmp/photo.jpg")
# p.parse_exif_data
# => Exif(:latitude => 1, :long => 2)


# write myself a Gemfile that has the dependencies I have in it (so I can require just the libraries I want)
# Gemfile hides other gem dependencies from interfering (isolates dependencies)
# put whichever libraries/gems I want in the Gemfile
# "should be able to create a Photo with a path to it"
# make a Fixtures directory -- put a photo with known attributes in there
# Success: when you make a new photo and call latitude on it, and it works
# Fixtures directory: stuff that's the same every time (fake data for testing)
# write specs off a photo in the Fixtures file