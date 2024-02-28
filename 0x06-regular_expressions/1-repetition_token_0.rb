#!/usr/bin/env ruby
# matchs the hbttn+ patterns
puts ARGV[0].scan(/hbt{2,5}n/).join
