# blenditioner
Automated video transitions using Blender video sequence editor.

## Usage

### Add video

```python
scene.sequence_editor.sequences.new_movie(name="mov1", channel=1, frame_start=1, filepath="")
scene.sequence_editor.sequences_all["mov1"].frame_start = 20
scene.sequence_editor.sequences_all["mov1"].blend_alpha = 0.5 # Opacity
scene.sequence_editor.sequences_all["mov1"].color_saturation = 0.5 # Opacity
scene.sequence_editor.sequences_all["mov1"].use_flip_x = True # flip x
scene.sequence_editor.sequences_all["mov1"].use_flip_y = True # flip y
scene.sequence_editor.sequences_all["mov1"].animation_offset_start = 200 # Video start frame
```

### Add audio

```python
scene.sequence_editor.sequences.new_sound(name="song1", channel=3, frame_start=1, filepath="")
scene.sequence_editor.sequences_all["song1"].frame_final_duration # Length of audio

```

### Additional Resources
- [Sequences API](https://docs.blender.org/api/blender_python_api_2_77_0/bpy.types.Sequences.html)
