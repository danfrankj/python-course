sequences = ['AGACTTTCAA', 'GAAAAATCGT', 'AAAAGACTTT']
patterns = ['GACT', 'AAAA']

matches = {'AGACTTTCAA': ['GACT'], 'GAAAAATCGT': ['AAAA'],
           'AAAAGACTTT': ['GACT', 'AAAA']}

def add_sequence(seq):
    sequences.append(seq)

def add_pattern(pattern):
    patterns.append(pattern)

def contains_pattern(pattern):
    return pattern in patterns

def update_matches(pattern):
  # make sure that matched dictionary is up to date
  # Implement this
  return
