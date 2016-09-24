open RG_SimpUtil


val simps = load_ruleset [
  "pushers/gg", "pushers/rr",
  "pushers/rgd", "pushers/grd",
  "pushers/ggd", "pushers/rrd",
  "pushers/ggu", "pushers/rru"
];

val simproc = REDUCE_ALL simps;

register_simproc ("push", simproc);





