def moving(moves: str, start_coordinates: tuple) -> tuple or Exception:
    x, y = start_coordinates
    for move in moves:
        match move:
            case 'S':
                y -= 1
            case 'N':
                y += 1
            case 'W':
                x -= 1
            case 'E':
                x += 1

    return x, y

