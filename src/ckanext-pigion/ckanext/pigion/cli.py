import click


@click.group(short_help="pigion CLI.")
def pigion():
    """pigion CLI.
    """
    pass


@pigion.command()
@click.argument("name", default="pigion")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [pigion]
