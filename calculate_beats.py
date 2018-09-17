"""
Calculate times for beats in song.
"""
import math


title = 'no-slip'
bpm = 77
fps = 29.97
time_signature = (4, 4)
measures = 57
beats = [4, 8, 12, 24, 32, 36, 48, 54]
beat_strength = [0.2, 0.5, 0.8, 0.8, 1.0, 0.6, 1.0, 0.8]



def sec_to_min_sec(seconds):
    return (math.floor(seconds / 60), seconds % 60)

print('|' + '-' * 14 + title + '-' * 15 + '|')
print('| BPM: %i  |  FPS: %.2f  |  TS: %i/%i |' % (bpm, fps, *time_signature))
print('|' + '-' * 36 + '|')
duration = measures * time_signature[0] / bpm * 60
print('| Duration: %i : %i  |  %5i frames  |' % (*sec_to_min_sec(duration), fps * duration))
beat_dur = duration / measures
print('|' + '-' * 36 + '|')
print('| Beat length: %.2f frames %.2f s   |' % (beat_dur * fps, beat_dur))
print('|' + '-' * 36 + '|')
print('| Beat | Frame |   Time   | Strength |')
for b, bs in zip(beats, beat_strength):
    d = b * time_signature[0] / bpm * 60
    t = sec_to_min_sec(d)
    f = fps * d
    print('| %3i  |%6i | %2i : %2i  |%7.1f   |' % (b, f, t[0], t[1], bs))
print('|' + '-' * 36 + '|')
