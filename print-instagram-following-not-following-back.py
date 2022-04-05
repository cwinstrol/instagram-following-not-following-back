from instapy import InstaPy
from instapy import smart_run

session = InstaPy(#username='',
                  #password='',
                  headless_browser=True)

with smart_run(session):
    followers= session.grab_followers(#username="",
                                      amount="full", live_match=True, store_locally=True)
    following= session.grab_following(#username="",
                                      amount="full", live_match=True, store_locally=True)
    for account in following:
        if account not in followers:
            print(account)
