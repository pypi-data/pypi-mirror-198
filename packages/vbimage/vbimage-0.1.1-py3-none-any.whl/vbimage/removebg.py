
import click
import os
from PIL import Image



@click.command(
        help="Adds background to any transparent image"
        )
@click.option(
        '-i', 
        '--inputimage', 
        type=click.Path(),
        default="./main.png",
        show_default=True,
        help="Front Image"
        )
@click.option(
        '-o', 
        '--outputimage', 
        type=click.Path(),
        default="./main_removedbg.png",
        show_default=True,
        help="Resized output image"
        )
def removebg(inputimage, outputimage):
    inputimage = Image.open(inputimage)
	img = inputimage.convert("RGBA")
	datas = img.getdata()
	newData = []

	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save(outputimage, "PNG")

    click.echo(f'{inputimage} is processed as {outputimage}.')





