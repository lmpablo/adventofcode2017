def captcha_part2(seq):
  original_length = len(seq)
  halfway = original_length // 2
  total = 0
  
  for index, el in enumerate(seq):
    next_index = int((index + halfway) % original_length)
    if el == seq[next_index]:
      total += int(el)
  
  return total
