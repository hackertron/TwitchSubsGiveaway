# download twitch channel subscription list and select random sub from the list
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator
import random

client_id = ""
client_secret = ""
username = ""

target_scope = [AuthScope.CHANNEL_READ_SUBSCRIPTIONS]

twitch = Twitch(client_id, client_secret)


auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()

print("token : ", token)
print("refresh_token : ", refresh_token)
# add User authentication
twitch.set_user_authentication(token, target_scope, refresh_token)


# get ID of user
user_info = twitch.get_users(logins=[username])
print(user_info)
user_id = user_info['data'][0]['id']
print(user_id)

subs = twitch.get_broadcaster_subscriptions(user_id, user_id)

subs_list = subs['data']

# random sub
random_sub = random.choice(subs_list)
print("Giveaway Winner :", random_sub)
