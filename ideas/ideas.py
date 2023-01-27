import random

ideas = ['hike','picnic','board games','trip','zoo','museum','baking/cooking','brewery/winery','laser tag/airsoft/paintball','restaurants']
number = random.randint(1,len(ideas)+1)

print(ideas[number-1])