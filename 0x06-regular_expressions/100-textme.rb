#!/usr/bin/env ruby
# extracts [sender] [receiver] [flags] from a log file
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
