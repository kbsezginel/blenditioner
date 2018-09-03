"""
Add transitions.
"""
import bpy
import os


bpm = 77
fps = 29.97
time_signature = (4, 4)
measures = 57
beats = [4, 8, 12, 24, 32, 36, 48, 54]
beat_strength = [0.2, 0.5, 0.8, 0.8, 1.0, 0.6, 1.0, 0.8]
frames = []

audio_file = "C:\\Users\\kutay\\Dropbox\\Recordings\\no-slip-aug27.wav"
video_file = "C:\\Users\\kutay\\Documents\\Videos\\feribot-yanak.MOV"


for b, bs in zip(beats, beat_strength):
    d = b * time_signature[0] / bpm * 60
    f = fps * d
    frames.append(f)


scene = bpy.context.scene
scene.sequence_editor_create()

duration = measures * time_signature[0] / bpm * 60 * fps # Duration in frames
beat_frames = duration / measures

# Add audio
scene.sequence_editor.sequences.new_sound(name="song1", channel=1, frame_start=1, filepath=audio_file)

# Add movie
scene.sequence_editor.sequences.new_movie(name="mov1", channel=2, frame_start=1, filepath=video_file)
# scene.sequence_editor.sequences_all["aa"].frame_start = 20

for f in frames:
    trans = scene.sequence_editor.sequences.new_effect(name='background',
                                                       frame_start=f,
                                                       frame_end=int(f + beat_frames / 2),
                                                       channel=3,
                                                       type='COLOR')
    trans.color = (0.0, 0.0, 0.0)

scene.render.fps = fps
scene.render.resolution_x, scene.render.resolution_y = 1920, 1080
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'FFMPEG'
# scene.audio_codec = 'AAC'
# scene.audio_bitrate = 384
scene.frame_end = duration

bpy.ops.wm.save_as_mainfile(filepath="test.blend")

# Render
# scene.render.filepath = settings['vid_file']
# bpy.ops.render.render(animation=True)
