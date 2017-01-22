#!/usr/bin/env python
import asyncio,threading,time
'''
@asyncio.coroutine
def hello():
    print("hello world")
    r = yield from asyncio.sleep(1)
    print('Hello again!')

loop = asyncio.get_event_loop()

loop.run_until_complete(hello())
loop.close()
'''

@asyncio.coroutine
def hello():
    print('hello world ! ===> %s' % threading.current_thread())
    yield from asyncio.sleep(4)
    print('Hello two %s ' % threading.current_thread())
start_time=time.time()
loop = asyncio.get_event_loop()
tasks = [hello(),hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end_time=time.time()
times=end_time - start_time
print(times)