import click


#from .resize import resize
#from .info import info
from .removebg import removebg


CONTEXT_SETTINGS = dict(
        help_option_names = [
            '-h',
            '--help'
        ]
)

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass



main.add_command(removebg)
#main.add_command(resize)
#main.add_command(info)
