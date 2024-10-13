from mcrcon import MCRcon

# Connect to the Minecraft server using RCON
with MCRcon("162.19.159.205", "12and12", port=21511) as mcr:
    # Coordinates for the structure
    x, y, z = 1065, 94, 1106  # Starting position
    width, height, length = 1, 32, 32
    block_type = "minecraft:mycelium"
    fill_command = f"/fill {x} {y} {z} {x + width - 1} {y + height - 1} {z + length - 1} {block_type}"
    response = mcr.command(fill_command)
    print(response)  # Prints the response from the server
    