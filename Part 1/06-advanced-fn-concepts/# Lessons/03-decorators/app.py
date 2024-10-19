# decorators -> add functionality to another function

def luigi_move(func):
    # convention of decorators -> wrapper
    def wrapper():
        print('Luigi is preparing a move...')
        func()
        print('Move complete!')

    return wrapper


# decorator example -> similar to luigi_move(stealth_attack)
@luigi_move
def stealth_attack():
    print("Performing a stealth attack!")


def main():
    stealth_attack()


if __name__ == "__main__":
    main()


# real-world uses of decorators
# --> @require_auth (check user auth before func conditionally runs)
# --> @validate_input (check & validate func arguments before func runs)
# --> @preprocess (modify func arguments to be in a specific format)
