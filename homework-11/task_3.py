def check_moves(moves):
    if not moves.isalpha():
        return TypeError('Moves must have only letters')
    if not moves.isupper():
        return Exception('Moves must have only upper letters')
    if not set(moves) <= {'S', 'W', 'N', 'E'}:
        return Exception('Moves must have only S W N E letters')
    return False


def check_coordinates(x, y, start_coordinates):
    if x not in range(100) or y not in range(100):
        return Exception(f'You can move in range 0-100. Start coordinates: {start_coordinates}')
    return False


def moving(moves: str, start_coordinates: tuple) -> tuple or Exception:
    if check_moves(moves):
        return check_moves(moves)

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

        if check_coordinates(x, y, start_coordinates):
            return check_coordinates(x, y, start_coordinates)

    return x, y





