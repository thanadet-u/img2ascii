# img2ascii

Generating a ascii art from an image.

Basic generation: We are using a 8x8 pixel character (by specifying the font) to generate an ascii art from an image, but since an pixel is 1x1 pixels we will have to downscale the image by 8. This is done to keep the ratio and "size" of the image

Now we will use the brightness/luminace of an image to determine the characters to map it to. We take the value of the brightness and bucketing it into 8 bucket and then mapping it to a ascii character.

[" ", ".", ":", "c", "o", "P", "O", "?", "@", "█"]