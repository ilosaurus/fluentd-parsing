import datetime, sys, time, random, string

def randomString(stringLength=10):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

while True:
    time.sleep(30)
    print('{"order_time":"'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'","order_id":"ORDER-'+randomString(14)+'","order_amount":"'+str(random.randrange(10,99,1)*1000)+'"}', flush=True)
