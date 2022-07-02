import asyncio
import aiohttp
from config import Config
import time
import random

config = Config()
print(config()['requests'][0]['method'])


async def execute(req, session):
    body = req['body']
    return await session.request(req['method'], req['url'], headers=req['headers'], data=body)


async def send_request(req):
    req_txt = req['url']
    for stage in config.stages:
        for rep in range(int(stage['repeats'])):
            req_num = 0
            success = 0
            errors = 0
            start = time.time()
            duration = stage['duration']
            full_t = start + duration

            rps_from, rps_to = stage['rps_from'], stage['rps_to']
            if rps_from > rps_to:
                rps_from, rps_to = stage['rps_to'], stage['rps_from']
            while time.time() < full_t:
                c_rate = random.randint(rps_from, rps_to)
                req_num += c_rate
                async with aiohttp.ClientSession(loop=loop) as session:
                    futures = [execute(req, session) for _ in range(c_rate)]
                    responses = await asyncio.gather(*futures)
                    for r in responses:
                        if 200 <= r.status <= 299:
                            success += 1
                        else:
                            errors += 1
                if (full_t - time.time()) > 0:
                    delay = random.randint(0, (full_t - time.time()) // 2)
                    duration -= delay
                    await asyncio.sleep(delay)

        print(
                {req_num} + '''of requests''' + 
              str({success / req_num * 100}) +
              '''% of success requests (200-299 status code)''' +
            str({errors / req_num * 100}) + '''% of errors (other status codes), 
            average query duration is'''+ str( {duration / req_num}) + """seconds.""")
        await asyncio.sleep(stage['timeout'])


async def tasks():
    start = time.time()
    tasks = []
    for i in config.requests:
        tasks.append(asyncio.ensure_future(send_request(i)))

    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


loop = asyncio.get_event_loop()
result = loop.run_until_complete(tasks())
loop.close()
