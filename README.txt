README

  in makeTf2Bind.py call writeBindFile to generate a bind config file.

  for more information on the parameters of writeBindFile, see comments
  above the function.

  see example input files:       cuiltheory.txt   and   cuiltheorycut.txt
  and resulting output files:    cuiltheory1.cfg  and   cuiltheory2.cfg

------------- cuiltheory1.cfg was generated from cuiltheory.txt ----------------
  cuiltheory.txt is raw copypaste text of the cuil theory reddit comment
  (https://reddit.com/r/worldnews/comments/7da5i/police_raids_reveal_baby_farms/c06cqxb)

------------- cuiltheory2.cfg was generated from cuiltheorycut.txt -------------
  cuiltheorycut.txt is a file i spaced into line phrases that roughly make sense
  and are less than 127 characters long per line.
  if you want to divide your file int <= 127 character lines by hand,
  feel free to do that. my code will not mess with your partitioning.

  example function calls are at bottom of makeTf2Bind.py

  please contact goldfeyesh with questions: steamcommunity.com/id/goldfeyesh/
