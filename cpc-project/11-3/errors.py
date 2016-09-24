from quanto.util.Scripting import *

dec = load_graph('11-3/decoder')

rules = map(load_rule, [
  'pushers/gg', 'pushers/rr',
  'pushers/rgd', 'pushers/grd',
  'pushers/ggd', 'pushers/rrd',
  'pushers/ggu', 'pushers/rru'])

inputs = ['b' + str(i) for i in range(11)]

for error in ['X', 'Z']:
  p = load_graph('pushers/' + error)
  for inp in inputs:
    g = plug(dec, p, inp, 'b1')
    d = derivation(g)
    d.normalise(rules)
    d.save('11-3/stab/error-' + error + '-' + inp)

