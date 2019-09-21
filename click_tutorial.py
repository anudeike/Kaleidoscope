import click

# must call it a group so you can nest it
@click.group()
def cli():
    pass

@click.command()
def init_database():
    click.echo("Created Database: ")

@click.command()
def destroy_database():
    click.echo("Destroyed Database: ")

# adding parameters
@click.command() # create a command
@click.option("--count", default=1, help='number of greetings') # click
@click.argument('name')
def hello(count, name):
    for _ in range(count):
        click.echo('Hello %s' % name)

# nesting the commands in the cli command
cli.add_command(init_database)
cli.add_command(destroy_database)
cli.add_command(hello)

if __name__ == '__main__':
    cli()