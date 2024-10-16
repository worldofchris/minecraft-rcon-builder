"""
Render rcon command strings
"""

from logging import INFO, getLogger, basicConfig

logger = getLogger(__name__)
basicConfig(level=INFO)

def split_on_change(string):
    if not string:
        return []

    splits = []
    current_split = string[0]

    for char in string[1:]:
        if char != current_split[-1]:
            splits.append(current_split)
            current_split = char
        else:
            current_split += char

    splits.append(current_split)
    return splits

def render_string(block_string: str, block_map: dict, origin: tuple) -> list: 
    command_list = []
    block_parts = split_on_change(block_string)
    offset = 0
    for part in block_parts:
        command = f"/fill {origin[0] + offset} {origin[1]} {origin[2]} {origin[0] + offset + len(part) -1} {origin[1]} {origin[2]} {block_map[part[0]]}"
        command_list.append(command)
        offset += len(part)

    return command_list