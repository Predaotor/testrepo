from PIL import Image
import os

images_dir = "images"

for infile in os.listdir(images_dir):
    full_infile_path = os.path.join(images_dir, infile)

    if os.path.isfile(full_infile_path):
        outfile = os.path.splitext(full_infile_path)[0] + ".Thumbnail.jpg"

        if infile != outfile:
            try:
                with Image.open(full_infile_path) as im:
                    source = im.split()
                    R, G, B = 0, 1, 2
                    mask = source[R].point(lambda i: i < 100 and 255)
                    out = source[G].point(lambda i: i * 0.7)
                    source[G].paste(out, None, mask)
                    im = Image.merge(im.mode, source)
                    im.show()
                    im.save(outfile)
            except OSError:
                print(f"Cannot edit image {infile}")
