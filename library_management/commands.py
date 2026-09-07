import click
@click.command()
def welcome_msg():
    print("Hello from the custom Bench CLI!")
commands=[welcome_msg]


@click.command("hello-app")
def hello_app():
    print("Hello from custom command!")

commands = [hello_app]

    