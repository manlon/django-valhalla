
# if we have many dispatchers we probably
# want to dynamically import

import twitter

DISPATCHERS = {
    'twitter': twitter.TwitterDispatcher,
}


def dispatch_to(dispatcher, message):
    if dispatcher in DISPATCHERS:
        d = DISPATCHERS[dispatcher]()
        d.send(message)
    else:
        raise "no dispatcher %s found" % dispatcher

