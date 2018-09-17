#!/usr/bin/env python3.5
import vk_api


login =
passw =

def vk_auth(login, passw):
    vk_session = vk_api.VkApi(login, passw)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk

vk = vk_auth(login, passw)

num_of_posts = vk.wall.get()["items"][0]["id"]

for i in range(num_of_posts+1):
    try:
        vk.wall.delete(post_id=i)
    except:
        pass
