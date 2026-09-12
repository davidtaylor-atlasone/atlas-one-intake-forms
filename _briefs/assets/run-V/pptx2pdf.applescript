on run argv
  set inPath to item 1 of argv
  set outPath to item 2 of argv
  with timeout of 110 seconds
    tell application "Microsoft PowerPoint"
      open (POSIX file inPath)
      set thePres to active presentation
      save thePres in (POSIX file outPath) as save as PDF
      close thePres saving no
    end tell
  end timeout
end run
