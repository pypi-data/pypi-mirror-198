import click

from .split import split
from .overlay import overlay
#from .compress import compress



CONTEXT_SETTINGS = dict(
        help_option_names = [
            '-h',
            '--help'
        ]
)

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass




main.add_command(split)
main.add_command(overlay)
#main.add_command(compress)
