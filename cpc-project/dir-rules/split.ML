open RG_SimpUtil


val simps = load_ruleset [
  "dir-rules/mk-cnot-strict1", "dir-rules/mk-cnot-strict2",
  "dir-rules/green-id", "dir-rules/red-id"
];

val simproc = REDUCE_ALL simps;

register_simproc ("split", simproc);










