import click
@click.command()
def welcome_msg():
    print("Hello from the custom Bench CLI!")
commands=[welcome_msg]