"""
Render rcon command strings
"""

from logging import INFO, getLogger, basicConfig
from mcrcon import MCRcon

logger = getLogger(__name__)
basicConfig(level=INFO)

def _split_on_change(string):
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
    """
    Render a set of minecraft server commands from a sting representation of a row of blocks
    """
    command_list = []
    block_parts = _split_on_change(block_string)
    offset = 0
    for part in block_parts:
        command = f"/fill {origin[0] + offset} {origin[1]} {origin[2]} {origin[0] + offset + len(part) -1} {origin[1]} {origin[2]} {block_map[part[0]]}"
        command_list.append(command)
        offset += len(part)

    return command_list


def render_rectangle(block_string: str, block_map: dict, origin: tuple) -> list:
    """
    Render a set of minecraft server commands from a \n separated string representation of a row of blocks
    """
    command_list = []
    block_strings = block_string.split('\n')
    for block_string in block_strings:
        command_list.append(render_string(block_string, block_map, origin))
        origin = origin[0],origin[1]+1,origin[2]
    return command_list


def render_cuboid(block_string: str, block_map: dict, origin: tuple):
    """
    Render a set of minecraft server commands from a --- separated 
    set of \n separated strings representing a cuboid of blocks
    """
    command_list = []
    rectangles = block_string.split('---')
    for rectangle in rectangles:
        command_list.append(render_rectangle(rectangle, block_map, origin))

    return command_list


def send_command(command, server_address, server_password):
    # Connect to the Minecraft server using RCON
    with MCRcon(server_address, server_password, port=21511) as mcr:
        response = mcr.command(command)
        return response
    