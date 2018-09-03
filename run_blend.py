"""
Run Blender with in the background with a Python script.
"""
import os
import subprocess



exe = "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe"
script = "blenditioner.py"
command = [exe, '--background', '--python', script]
blend = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = blend.stdout.decode(), blend.stderr.decode()
print("Stdout:\n\n%s\nStderr:\n%s" % (stdout, stderr))
