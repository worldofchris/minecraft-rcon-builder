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

def test_map_string_to_blocks():
    block_string = "*############*"

    block_map = {
        '*': 'minecraft:stone',
        '#': 'minecraft:granite',
        ' ': 'minecraft:air'
    }

    origin = 1065, 94, 1106
    expected = [
        f"/fill {origin[0]} {origin[1]} {origin[2]} {block_map['*']}",
        f"/fill {origin[0] + 1} {origin[1]} {origin[2]} {block_map['#']}",
        f"/fill {origin[0] + len(block_string) - 1} {origin[1]} {origin[2]} {block_map['*']}"
    ]

    actual = render_string(block_string, block_map)

    assert actual == expected