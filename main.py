from app.bootstrap import Bootstrap
from app.application import AngryBirdApplication
from ui.main_window import MainWindow


def main():

    bootstrap = Bootstrap()

    if bootstrap.start():

        application = AngryBirdApplication()

        window = MainWindow()

        application.run(window)


if __name__ == "__main__":
    main()