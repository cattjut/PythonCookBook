p = (4, 5)
x, y = p

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

name, shares, price, (year, mon, day) = data

s = 'Hello'
a, b, c, d, e = s

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data # _ is a throwaway variable name

def drop_first_last(grades): # grades is any iterable object (tuples, lists, strings, files, iterators, and generators)
first, *middle, last = grades
return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)

records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
   if tag == 'foo':
      do_foo(*args)
   elif tag == 'bar':
      do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
           yield line, previous_lines
        previous_lines.append(line)
# Example use on a file
if __name__ == '__main__':
   with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
               print(pline, end='')
        print(line, end='')
        print('-'*20)
