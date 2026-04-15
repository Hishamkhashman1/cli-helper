try:
    from .patterns import PYTHON_PATTERN_SEEDS
except ImportError:  # pragma: no cover - compatibility for direct file execution
    from patterns import PYTHON_PATTERN_SEEDS

def match_pattern(cleaned_output):
    for pattern in PYTHON_PATTERN_SEEDS:
        if pattern["name"] in cleaned_output:
            return pattern
    return None
