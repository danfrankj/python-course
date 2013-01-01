def triples_gen(xpoints, ypoints, zpoints):
  for x in xpoints:
    for y in ypoints:
      for z in zpoints:
        yield (x, y, z)



