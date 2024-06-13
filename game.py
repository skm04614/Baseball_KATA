def baseball_game(solution: str,
                  guess: str) -> tuple[bool, int, int]:
    try:
        int(solution)
        int(guess)
    except ValueError:
        raise ValueError("Only numerical arguments are allowed.")

    if len(solution) != 3 or len(guess) != 3:
        raise ValueError("Arguments must be 3 characters long each.")

    if solution == guess:
        return True, 0, 3

    strikes = 0
    unmatched_sol = [0] * 10
    unmatched_guess = [0] * 10
    for s, g in zip(solution, guess):
        if s == g:
            strikes += 1
            continue
        unmatched_sol[int(s)] += 1
        unmatched_guess[int(g)] += 1

    balls = sum(map(lambda pair: min(*pair), zip(unmatched_sol, unmatched_guess)))
    return False, balls, strikes
