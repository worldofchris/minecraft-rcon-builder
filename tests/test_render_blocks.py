import pytest

from minecraft import render_string

def test_map_char_to_block():
    chars = ['*', '#', ' ']

    block_map = {
        '*': '',
        '#': '',
        ' ': ''
    }

    expected = [
        ''
    ]

block_map = {
    '*': 'minecraft:stone',
    '#': 'minecraft:granite',
    ' ': 'minecraft:air'
}

origin = 1065, 94, 1106

mixed_block_string = "*############*"
single_char_block_string = "*"
empty_block_string = ""

@pytest.mark.parametrize("block_string,expected", 
                         [(mixed_block_string, 
                           [
                            f"/fill {origin[0]} {origin[1]} {origin[2]} {origin[0]} {origin[1]} {origin[2]} {block_map['*']}",
                            f"/fill {origin[0] + 1} {origin[1]} {origin[2]} {origin[0] + (len(mixed_block_string)-2)} {origin[1]} {origin[2]} {block_map['#']}",
                            f"/fill {origin[0] + len(mixed_block_string) - 1} {origin[1]} {origin[2]} {origin[0] + len(mixed_block_string) - 1} {origin[1]} {origin[2]} {block_map['*']}"
                           ]
                          ), 
                          (single_char_block_string,
                           [
                            f"/fill {origin[0]} {origin[1]} {origin[2]} {origin[0]} {origin[1]} {origin[2]} {block_map['*']}"
                           ]
                          ), 
                          (empty_block_string, 
                           []
                          )
                         ]
)
def test_map_string_to_blocks(block_string, expected):
    """
    Test map utf-8 character string of blocks to minecraft command string
    """
    actual = render_string(block_string, block_map, origin)
    assert actual == expected