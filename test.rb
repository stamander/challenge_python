
word = gets.chomp.split('')
word.each {|w|
  case w
  when 'A'
    print '4'
  when 'B'
    print '8'
  when 'C'
    print '［'
  when 'D'
    print 'T)'
  when 'E'
    print '3'
  else
    print w
  end
}