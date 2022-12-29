from itertools import product


def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    # list of coordinates
    lands = []

    # list of islands (list of land coordinates)
    islands = []

    # get coordinates from lands
    all_coordinates = list(product(list(range(len(grid))), repeat=2))
    for x, y in all_coordinates:
        if grid[x][y]:
            lands.append((x, y))

    # get a land not yet checked
    while len(lands) > 0:
        checked_land = lands.pop()
        touching_islands = []

        # get island being touched by the land
        for island in islands:
            for land in island:
                distance = abs(land[0] - checked_land[0]) + abs(land[1] - checked_land[1])
                if distance < 2 and island not in touching_islands:
                    touching_islands.append(island)

        # touches nothing => new island
        if len(touching_islands) == 0:
            islands.append([checked_land])
            print('New island', checked_land)

        # touches 1 => new land to one island
        elif len(touching_islands) == 1:
            print('Existing island', checked_land, touching_islands[0])
            touching_islands[0].append(checked_land)

        # touches > 1 => island merged by land
        else:
            print('Island merge', checked_land, touching_islands)

            for touching_island in touching_islands[1:]:
                touching_islands[0] += touching_island
                islands.remove(touching_island)

            # add land to merged island
            touching_islands[0].append(checked_land)

    return len(islands)
