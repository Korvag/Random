import random

ideas = ['hike','picnic','board games','trip','zoo','museum','baking/cooking','brewery/winery','laser tag/airsoft/paintball','restaurants']
print(ideas)
while True:
    number = random.randint(1,len(ideas)+1)
    print(number, number-1)
    ideas = ideas.pop(number-1)
    print(ideas)

    print(ideas[number-1])