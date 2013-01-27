require 'exifr'

puts 'Path, please'
photo_path       = gets.chomp
# where it lives = that sans newline

puts 'Thanks! Here\'s that file again.'
puts photo_path

print 'Here\'s the latitude: '

puts EXIFR::JPEG.new(photo_path).gps_latitude.to_s

print 'And here\'s the longitude: '

puts EXIFR::JPEG.new(photo_path).gps_longitude.to_s