# builds the final human-readable output.

# take matched result

# build final output cause, possible fix, Recommended , w:here to run recommendation

# from matcher import matched_pattern



def format_hint(command, exit_code, matched_pattern):
    if matched_pattern:
        return (
            matched_pattern["cause"],
            matched_pattern["solution"],
            matched_pattern["recommended_command"],
            matched_pattern["context"]
        )
    else:
        return None
