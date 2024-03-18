def check_moves(moves):
    if not moves.isalpha():
        return TypeError('Moves must have only letters')
    if not moves.isupper():
        return Exception('Moves must have only upper letters')
    if not set(moves) <= {'S', 'W', 'N', 'E'}:
        return Exception('Moves must have only S W N E letters')
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

    return x, y

