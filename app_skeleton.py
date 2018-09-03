import os
from os.path import join, dirname
from dotenv import load_dotenv

# Beware: .env variables are only loaded from here. Modules imported before don't have those variables in
# the code executed directly in the root of the files (executed too early)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def _main() -> None:
    access_token = os.environ.get("ACCESS_TOKEN")
    verify_token = os.getenv('VERIFY_TOKEN')


if __name__ == "__main__":
    _main()
