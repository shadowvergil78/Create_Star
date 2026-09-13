import imageio.v3 as iio
from PIL import Image

filenames = ['red_star.png', 'yellow_star.png']
images = []
frame_size = None

for filename in filenames:
  image = Image.open(filename).convert('RGBA')
  if frame_size is None:
    frame_size = image.size
  images.append(image.resize(frame_size))

iio.imwrite('stars.gif', images, duration=500, loop=0)