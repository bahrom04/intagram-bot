# imports
from instapy import InstaPy
from instapy import smart_run
from dotenv import load_dotenv
import os


load_dotenv()

# login credentials
insta_username = os.getenv("USERNAME")
insta_password = os.getenv("PASSWORD")


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=False,
    browser_executable_path=r"C:\Program Files\Mozilla Firefox\firefox.exe",
)

with smart_run(session):
    """Activity flow"""
    # general settings

    # activity
    session.like_by_tags(["bahrom"], amount=10)

    session.set_do_follow(True, percentage=100)
