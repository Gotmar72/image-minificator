import os
from PIL import Image

images_to_process_path = '.\\images_to_process'
processed_images_path = '.\\processed_images'

def get_image_names(dir_path):
    image_names = []
    dir_list = os.listdir(dir_path)
    files_only = [f for f in dir_list if os.path.isfile(dir_path + '/' + f)]

    for name in files_only:
        if name.endswith(".jpg") or name.endswith(".png") or name.endswith(".jpeg"):
            image_names.append(name)

    return image_names

def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width
    new_height = round(aspect_ratio * new_width)

    return image.resize((new_width, new_height))

def transform_image(image_name, params):
    image = Image.open(images_to_process_path + '\\' + image_name)
    new_image = resize_image(image, params['width'])
    # TODO: Add quantization.
    # new_image = image.quantize(256)
    new_image.save(processed_images_path + '\\' + image_name, optimize = True, quality = params['quality'])

def get_inputs():
    params = {}

    # TODO: Add validation and more params.
    params['quality'] = int(input('Insert a new quality (1-100): '))
    params['width'] = int(input('Insert a new width: '))

    return params

def main():
    image_names = get_image_names(images_to_process_path)

    if not image_names:
        print('No images to transform.')
        return

    params = get_inputs()

    print('Transforming images...')
    for name in image_names:
        print(name)
        transform_image(name, params)

    print('Transformation has been done!')

main()
