from instapy import InstaPy



#LIKEING
#session = InstaPy(username="viralism1", password="Viral@786")
session = InstaPy(username="travelling.lad", password="Japan@786")
#session = InstaPy(username="mayankshivhare", password="Shivhare@786")
session.login()


##### Settting s###########
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=10,
                              peak_likes_daily=170,
                               peak_comments_hourly=4,
                               peak_comments_daily=12,
                                peak_follows_hourly=3,
                                peak_follows_daily=20,
                                 peak_unfollows_hourly=5,
                                 peak_unfollows_daily=ArithmeticError,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)

session.set_relationship_bounds(enabled=True,
				 potency_ratio=1.25,
				  delimit_by_numbers=True,
				   max_followers=5000,
				    max_following=None,
				     min_followers=500,
				      min_following=None,
				       min_posts=50,
                                        max_posts=1000)

session.set_relationship_bounds(min_posts=50,
                                max_posts=1000)

session.set_skip_users(skip_private=True,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)
session.set_simulation(enabled=True, percentage=37)

session.set_action_delays(enabled=True,
                           like=10,
                           comment=50,
                           follow=4.17,
                           unfollow=28,
                           story=10,
                            randomize=True, random_range_from=70, random_range_to=140)

session.set_user_interact(amount=7, randomize=True, percentage=100, media='Photo')
session.set_skip_users(skip_bio_keyword = ['free shipping',' Order', 'visa', 'paypal'])


#### LIKE ####
#hashtags = session.target_list("C:\\Users\\Sony\\InstaPy\\hashtags.txt")
session.like_by_tags(['foodgasm'], amount=20)
session.set_delimit_liking(enabled=True, max_likes=100, min_likes=10)
session.like_by_feed(amount=50, randomize=True, unfollow=True, interact=True)

### COMMENT ###
session.set_do_comment(enabled=True, percentage=10)
session.set_comments(['It is Yummy', 'Wow! seems Tasty', 'Mouthwatering', 'This look so delicious','This look good', 'Absolutely love this', 'Love the presentation'])
session.set_delimit_commenting(enabled=True, max_comments=32, min_comments=1)


### FOLLOW ###
session.follow_by_tags(['FoodBlogger', 'TravelBlogger'], amount=20, randomize=True, interact=True)



### UNFOLLOW ###
session.set_dont_unfollow_active_users(enabled=True, posts=5)
session.unfollow_users(amount=40, allFollowing=True, style="RANDOM", unfollow_after=3*60*60, sleep_delay=600)


### Stories ###
session.set_do_story(enabled = True, percentage = 70, simulate = False)

### Pods ###
