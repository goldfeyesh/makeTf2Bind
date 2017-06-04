# WHO:   Alice Li (goldfeyesh)
# WHEN:  5.20.2016 (created)
#        8.25.2016 (last updated)
# WHAT:  makeTf2Bind.py
#        generate rolling and random bind .cfg files from .txt files

# NOTE: call the function writeBindFile to generate your bind config file.
#       if you want to divide your file int <= 127 character lines by hand,
#       feel free to do that. my code will not mess with your partitioning.
#
#       see example input files:       cuiltheory.txt   and   cuiltheorycut.txt
#       and resulting output files:    cuiltheory1.txt  and   cuiltheory2.txt
#       example function calls are at bottom of file
#
#       please add goldfeyesh with questions: steamcommunity.com/id/goldfeyesh/

MAX_CHAR = 127       # max number of characters per line of text for tf2 chat
MAX_CMD = 14         # can't have more than 30 commands per alias. 2*14 + 1 = 29
                     # (say command + wait command) * (14 times) + (next alias)

# helper function to read lines from file and prepares them to be processed
# params:   filename: the name of the file to be read
# returns:  array of lines, each <= 127 characters long
def linesFromFile(filename):
    inputFile = open(filename, "r")
    strippedLines = [line.strip() for line in inputFile.readlines()]

    fixedLines = []
    for line in strippedLines:
        if len(line) > 127:                # if length of text line is too long
            fixedLines += fixLine(line)    # fix it, then add to array to return
        else:                              # else, simply add to array
            fixedLines.append(line)

    inputFile.close()
    return fixedLines

# helper function to break up overly long lines into chunks and keep whole words
# params:  longstr: long string to break into pieces
# returns: array of strings, all 127 characters or less
def fixLine(longstr):
    fixedLines = []        # array of strings <= 127 chars long to return
    mindex = 0
    maxindex = len(longstr)

    while mindex < maxindex:
        maxdex = (mindex + MAX_CHAR) if (mindex + MAX_CHAR) < maxindex else maxindex
        cutstr = longstr[mindex : maxdex]      # get a substring of 127 characters

        # when last character of the cut substring is a space or
        # the substring reaches end of string, just add to the fixedLines array
        if longstr[maxdex - 1] == ' ' or maxdex == maxindex:
            fixedLines.append(cutstr)
            mindex += MAX_CHAR                # increase substring's start index
        else:
            lastspace = 0                     # find last space in substring by
            control = len(cutstr) - 1         # searching from end of substring
            while control > 0:
                if cutstr[control] == ' ':
                    lastspace = control
                    break                     # exit loop soon as space is found
                control -= 1
            fixedLines.append(cutstr[0 : lastspace])
            mindex += lastspace + 1
    return fixedLines

# writes a cfg file for the rolling bind
# params:  cfgFileName: name of the file you want to create and write into
#          txtFileName: text file to read from
#          msbetw:      number of milliseconds between each message
#          deskey:      preferred key to bind: for recognized key names, see
#                                             wiki.teamfortress.com/wiki/Scripting
# returns: nothing
def writeBindFile(cfgFileName, txtFileName, msbetw, deskey):

    bindtxt = linesFromFile(txtFileName)

    outFile = open(cfgFileName + ".cfg", "w")

    outFile.write(deskey, cfgFileName[0:2] + '0')
    counter = 0                       # keeps count of what line number to write
    aliaslist = []                    # list to populate full of alias## strings

    # forloop writes all strings in bindtxt to file:
    for phrase in bindtxt:
        aliastxt = cfgFileName[0] + str(counter)
        outFile.write('alias "' + aliastxt + '" "say ' + phrase + '"\n')
        aliaslist.append(aliastxt)
        counter += 1

    # create string to join aliases together with
    waitstr = '; wait ' + str(msbetw) + '; '

    if counter > MAX_CMD:       # if there are more than 14 lines of text in the
                                # bind, must alias every 30 commands together
        countxtras = 0              # tracks which number of extra alias to add
        mindex = 0                  # begin creating chunks from the first alias
        lastdex = counter           # store maximum index position

        for i in range(int(counter/MAX_CMD) + 1):          # create sets of text

            # find what the maximum index to look through partial array
            maxdex = (mindex + MAX_CMD) if (lastdex > mindex + MAX_CMD) else lastdex

            # join text in partial array of aliases with wait commands
            joina = waitstr.join(aliaslist[mindex:maxdex])
            xastr = 'alias "' + cfgFileName[0 : 2] + str(countxtras) + '" "' + joina

            countxtras += 1           # keep track how many alias chunks created

            # add the next extra alias OR nothing to the end
            end = (waitstr + cfgFileName[0 : 2] + str(countxtras)) if countxtras < len(aliaslist)/MAX_CMD else ''
            xastr += end + '" \n'
            outFile.write(xastr)
            mindex += MAX_CMD              # increase the minimum index position

        # no problems on valve servers, but sourcemod might block rollbinds.
        outFile.write('echo "------------------- WARNING: bind may be blocked on'
                      + ' non-valve servers for flooding. -------------------"\n')
    else:  # if there are less than or equal to 14 lines of text to bind, simply
           # join them together with the wait command.
        joina = waitstr.join(aliaslist)
        outFile.write('alias "' + cfgFileName[0 : 2] + '0" "' + joina + '"\n')

    outFile.write('echo "' + "---------------------------------- " + cfgFileName
                  + ' on key ' + deskey + ' loaded ----------------------------------"\n')
    outFile.write('echo "--------------- bind generator written by goldfeyesh. '
                  + 'she hopes you have a nice time B) ---------------"\n')
    outFile.close()


# this function will write a randomized bind file
# params:  cfgFileName: name of the file you want to create and write into
#          txtFileName: text file to read from
#          deskey:      preferred key to bind: for recognized key names, see
#                                             wiki.teamfortress.com/wiki/Scripting
# returns: nothing, creates cfg file
def writeRandomBindFile(cfgFileName, txtFileName, deskey):
    bindtxt = linesFromFile(txtFileName)

    outFile = open(cfgFileName + ".cfg", "w")

    counter = 0                          # keeps count of what line number to write
    aliaslist = []                       # list to populate full of alias# strings
    alet = cfgFileName[0]                # alias letter string

    cyclestr = alet + '_cycle '          # a_cycle string
    resultstr = alet + '_result '        # a_result string
    dicestr = alet + '_diceroll_'        # a_diceroll_ string

    # forloop writes all strings in bindtxt to file:
    for phrase in bindtxt:
        aliascounter = cfgFileName[0] + str(counter)
        outFile.write('alias "' + aliascounter + '" "say ' + phrase + '"\n')
        aliaslist.append(aliascounter)
        counter += 1

    # for loop writes diceroll aliases and cycle aliases
    for num in range(0, counter - 1):
        diceroll = 'alias "' + dicestr + str(num) + '" '
        result = '"alias ' + resultstr + aliaslist[num] + '; '
        cyclediceroll = 'alias ' + cyclestr + ' ' + dicestr + str(num + 1) + '"\n'
        outFile.write(diceroll + result + cyclediceroll)

    outFile.write('alias "' + dicestr + str(counter - 1) + '" "alias ' + resultstr +
                  aliaslist[-1] + '; alias ' + cyclestr + ' ' + dicestr + '0"\n')

    outFile.write('alias ' + cyclestr + ' ' + dicestr + '0\n')

    outFile.write('bind ' + deskey + ' "' + resultstr + '; ' + cyclestr + '"\n')

    # randomize the binds with wasd
    outFile.write(bind('w', '+forward; ' + cyclestr))
    outFile.write(bind('a', '+moveleft; ' + cyclestr))
    outFile.write(bind('s', '+back; ' + cyclestr))
    outFile.write(bind('d', '+moveright; ' + cyclestr))

    outFile.write('echo "' + "---------------------------------- " + cfgFileName
                  + ' on key ' + deskey + ' loaded ----------------------------------"\n')
    outFile.write('echo "--------------- bind generator written by goldfeyesh. '
                  + 'she hopes you have a nice time B) ---------------"\n')
    outFile.close()

# helper function for creating the bind command string
# params:  target: preferred key to bind: for recognized key names, see
#          tobind: command(s) to bind to the target key
# returns: string to bind whatever command tobind to target
def bind(target, tobind):
    return 'bind ' + target + ' "' + tobind + '"\n'

# ------------------------------------------------------------------------------
# example function calls to writeBindFile and writeRandomBindFile
# uncomment to generate files, add your own calls below.
# writeBindFile('cuiltheory1', 'cuiltheory.txt', 266, 'KP_ENTER')
# writeBindFile('cuiltheory2', 'cuiltheorycut.txt', 266, 'KP_PLUS')
# writeRandomBindFile('birdsrights', 'birdsrights.txt', 'END')
# writeBindFile('cuiltheory1', 'cuiltheory.txt', 266, 'KP_ENTER')
# writeBindFile('cuiltheory2', 'cuiltheorycut.txt', 266, 'KP_PLUS')
# writeRandomBindFile('guyfieri', 'guyfieriquotes.txt', 'END')
# ------------------------------------------------------------------------------
