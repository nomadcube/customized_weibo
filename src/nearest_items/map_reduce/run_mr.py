#!/usr/bin/env /Users/wumengling/PycharmProjects/customized_weibo/bin/python2.7

import subprocess
from hdfs import InsecureClient

client = InsecureClient("http://127.0.0.1:50070")

cmd = ["map_reduce", "jar", "/Users/wumengling/src/pig-0.15.0/test/e2e/pig/lib/map_reduce-streaming.jar",
       "-file", "./mapper.py",
       "-mapper", "./mapper.py",
       "-file", "./reducer.py",
       "-reducer", "./reducer.py",
       "-input", "latest_posts.json",
       "-output", "best_posts"]
subprocess.call(cmd)