from rembg import remove

from PIL import Image

input_path=r"C:download (3).jpg"
output_path=r"output.png"
input=Image.open(input_path)
output=remove(input)
output.save(output_path)