class GenePatterns:
  def __init__(self):
    self.sequences = []
    self.patterns = []
    self.matches = {}

  def add_sequence(self, seq):
    if seq not in self.sequences:
      self.sequences.append(seq)
      self.update_matches()

  def add_pattern(self, pattern):
    if pattern not in self.patterns:
      self.patterns.append(pattern)
      self.update_matches()

  def update_matches(self):
    for seq in self.sequences:
      self.matches[seq] = []
      for pattern in self.patterns:
        if seq.find(pattern) != -1:
          self.matches[seq].append(pattern)

  def __getitem__(self, key):
    if key in self.sequences and key in self.matches:
      return self.matches[key]
    else:
      return []
    
  def __contains__(self, key):
    return key in self.patterns

gp = GenePatterns()
gp.add_sequence('AGACTTTCAA')
gp.add_sequence('GAAAAATCGT')
gp.add_sequence('AAAAGACTTT')
gp.add_pattern('GACT')
gp.add_pattern('AAAA')
print 'AAAA' in gp
print 'TGCC' in gp
print gp['AAAAGACTTT']


