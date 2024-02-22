import subprocess

# Define the command as a list
command = [
    'python', 'detect.py',
    '--source', '../input.mp4',
    '--weights', '../models/best.pt',
    '--conf', '0.2'
]

# Run the command
subprocess.run(command, check=True)
