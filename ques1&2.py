import twitter
import preprocessor as p
import collections
import re

# For removing URLs from the tweets 
url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# for removing  extra emojis
remove_list = ["⭐", "🦉", "🇰🇷","🤣"]

res_dict = collections.defaultdict(lambda: collections.defaultdict(int))

#for removing URLs, Emojis, Smileys and Solo Numbers.
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)

#user_list = ["sundarpichai", "arealmodi","elonmusk"]
user_list = open('twitterHandler.txt','r').read().split('\n')

'''
Create Twitter Instance. All the fields can be collected from the developer site of Twitter
I also used the tweet mode as extented to get all the tweet text data in a response header.
'''
api = twitter.Api(consumer_key='D4FTu7BxLzIvWX9zZXbMsmz5P',
                consumer_secret='USEtyYLc5Cpbzz7CHL6OeUBpsdNsn260PETveTzA13z8DNp70B',
                access_token_key='1094978973245812738-jpaa6imCOodCVdZpHE2ncXn2E0VIkU',
                access_token_secret='TQhxCWR6LCcqiN3BOEdkKHJBUb6xUG5uEUGPbYFVQYc4b',
                sleep_on_rate_limit=True, tweet_mode="extended" 
                )

for user in user_list:
    statuses = api.GetUserTimeline(screen_name=user, count=200)
    texts = [ x.full_text for x in statuses ]
    text = " ".join(texts)
    ntext = re.sub(url_regex, "",  text)
    n2text = p.clean(ntext)
    n3text = n2text
    for x in remove_list:
        n3text = n3text.replace(x, "")
    # n4list = re.split(r'[;,\s()."“]', n3text) 
    # Split words by all non-alpha characters and remove unecesary spaces.
    words = re.compile(r'[^A-Z^a-z]+').split(n3text)
    # Convert to lowercase
    n5list = [word.lower() for word in words if word != '']
    res_dict[user].update(dict(collections.Counter(n5list)))


key_list = set()
for user in list(res_dict.keys()):
    key_list.update(set(res_dict[user].keys()))

key_list = list(key_list)

with open("tweetdata.txt", "w") as f:
    f.write("Username")
    for k in key_list:
        f.write(f"\t{ k }")
    f.write("\n")
    for user in user_list:
        f.write(f"{ user }")
        for k in key_list:
            f.write(f"\t{ res_dict[user][k] }")
        f.write("\n")
    
