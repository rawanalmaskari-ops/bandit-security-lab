import os
import yaml

def unsafe_command(input_str):
    os.system(input_str)  # Bandit should flag this once

with open('config.yaml', 'r') as f:
    config = yaml.full_load(f)  # Bandit may also flag yaml.full_load (depends on rules)

unsafe_command(config.get('user_input', 'echo Hello'))

