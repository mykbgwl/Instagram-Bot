from instapy import InstaPy

#headless_browser = True
session = InstaPy(username="<instagramID>", password="<instagramPassword>")
session.login()

session.set_relationship_bounds(enabled=True, max_followers=200)

session.set_do_follow(True, percentage=100)

session.like_by_tags(["anime", "instagram"], amount=3)
session.set_dont_like(["nsfw"])

#session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60)

session.end()
