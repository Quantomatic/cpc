open RG_SimpUtil

val simps = load_ruleset [
  "dir-rules/dir-hopf", "dir-rules/dir-hopf2", "dir-rules/dir-hopf3",
  "dir-rules/green-id", "dir-rules/red-id"
];

val spiders = load_ruleset [
  "dir-rules/green-sp-dir", "dir-rules/red-sp-dir",
  "dir-rules/green-sp-dir2", "dir-rules/red-sp-dir2"
];

val simproc = LOOP (REDUCE_ALL simps ++ REDUCE_ALL spiders);

register_simproc ("dir-simp", simproc);














