README

  i made this to satisfy all my bind meme needs.

  in makeTf2Bind.py
    call writeBindFile to generate a rolling bind config file.
    or writeRandomBindFile to generate a random bind config file.

  for more information on parameters for writeBindFile and writeRandomBindFile,
  see comments above the function.

  example input files:       cuiltheory.txt,  cuiltheorycut.txt, birdsrights.txt
  resulting output files:    cuiltheory1.cfg, cuiltheory2.cfg,   birdsrights.cfg

------------- cuiltheory1.cfg was generated from cuiltheory.txt ----------------
  cuiltheory.txt is raw copypaste text of the cuil theory reddit comment
  (https://reddit.com/r/worldnews/comments/7da5i/police_raids_reveal_baby_farms/c06cqxb)

------------- cuiltheory2.cfg was generated from cuiltheorycut.txt -------------
  cuiltheorycut.txt is the first 4 cuils of cuil theory text i spaced into line
  phrases that roughly make sense and are <= 127 characters long per line.
  if you want to divide your file int <= 127 character lines by hand,
  feel free to do it. my code will not mess with your partitioning.

------------- birdsrights.cfg was generated from birdsrights.txt -------------
  birdsrights.txt has a tweet from birdsrightsactivist on each line.
  if you execute birdsrights.cfg, run around with wasd, push the bound key,
  it will say a random tweet from this text file in chat.
  (https://twitter.com/ProBirdRights)

  example function calls are at bottom of makeTf2Bind.py

  some binds i've generated can be found here: http://pastebin.com/u/goldfeyesh

  please contact goldfeyesh with questions: steamcommunity.com/id/goldfeyesh/
