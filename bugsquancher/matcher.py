# pure logic that returns the best matching pattern

# compares it against known patterns

# load patterns

from patterns import patterns
# compare normalized text against keywords or regex

# return matched pattern or None

def match_pattern(cleaned_output):
    for pattern in patterns:
        if pattern.matches(cleaned_output):
            return pattern
    return None
