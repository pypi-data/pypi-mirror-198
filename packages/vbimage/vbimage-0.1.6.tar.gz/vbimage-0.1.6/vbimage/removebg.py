
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
@click.option(
		'-c',
		'--color',
		type=click.Tuple([int, int, int]),
		default=(255, 255, 255),
		show_default=True,
		help="Color to be removed"
		)
def removebg(inputimage, outputimage, color):
	inputimage = Image.open(inputimage)
	img = inputimage.convert("RGBA")
	datas = img.getdata()
	newData = []

	for item in datas:
		if item[0] == color[0] and item[1] == color[1] and item[2] == color[2]:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save(outputimage, "PNG")
	click.echo(f'{inputimage} is processed as {outputimage}.')





