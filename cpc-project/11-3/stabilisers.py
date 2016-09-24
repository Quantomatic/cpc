from quanto.util.Scripting import *

enc = load_graph('11-3/encoder')

rules = map(load_rule, [
  'pushers/gg', 'pushers/rr',
  'pushers/rgd', 'pushers/grd',
  'pushers/ggd', 'pushers/rrd',
  'pushers/ggu', 'pushers/rru'])

zinputs = ['b0', 'b3', 'b6', 'b7']
xinputs = ['b1', 'b5', 'b8', 'b9']

x = load_graph('pushers/X')
z = load_graph('pushers/Z')
for inp in zinputs:
  g = plug(enc, z, inp, 'b1')
  d = derivation(g)
  d.normalise(rules)
  d.save('11-3/stab/stab-Z-' + inp)
for inp in xinputs:
  g = plug(enc, x, inp, 'b1')
  d = derivation(g)
  d.normalise(rules)
  d.save('11-3/stab/stab-X-' + inp)
