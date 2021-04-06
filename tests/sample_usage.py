

import sys
from ffprobe import FFProbe

metadata=FFProbe('/tests/view/GMT20210115-monte.mp4')

print(metadata.streams)

for stream in metadata.streams:
    if stream.is_video():
        print('Stream contains {} frames.'.format(stream.frames()))