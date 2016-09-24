open RG_SimpUtil


val simps = load_ruleset [
  "dir-rules/green-sp-dir", "dir-rules/red-sp-dir"
];

val simproc = REDUCE_ALL simps;

register_simproc ("join", simproc);










