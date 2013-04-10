id_dept_pairs = [(8283, 'Aero/Astro'),
                 (3456, 'CS'),
                 (7888, 'Math')]

# Sort by id number
print sorted(id_dept_pairs,
             key=lambda pair: pair[0])
# [(3456, 'CS'), (7888, 'Math'),
#  (8283, 'Aero/Astro')]

# Sort by department alphabetically
print sorted(id_dept_pairs,
             key=lambda pair: pair[1])
# [(8283, 'Aero/Astro'), (3456, 'CS'),
#  (7888, 'Math')]
