

import sys

sys.path.append("/Users/hcruz/development/coding/ffprobe-python/ffprobe")

from ffprobe import FFProbe

metadata=FFProbe('/Users/hcruz/Downloads/20230711_215927000_iOS.mov')
#metadata=FFProbe('/Users/hcruz/Downloads/v_20240101_000645.mov')


#print(metadata.streams)
print(metadata)


for stream in metadata.streams:
    if stream.is_video():
        print('Stream contains {} frames.'.format(stream.frames()))