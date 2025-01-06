info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
sections = info.split(":")
recombine = "+".join(sections)
#new_string = info.replace(":", "+") 