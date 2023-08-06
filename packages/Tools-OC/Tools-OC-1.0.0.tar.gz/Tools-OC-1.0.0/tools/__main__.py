# coding=utf8
"""Main

Used mainly to test that the module works as expected
"""

# Import everything
from . import clone, combine, eval, get_client_ip, keys_to_ints, merge

print('clone')
o = clone({
	'1': 'one',
	'2': 'two',
	'3': 'three'
})

print('combine')
o = combine(o, {'4': 'four'})

print('merge')
merge(o, {'5': 'five'})

print('keys_to_ints')
print(keys_to_ints(o))

print('eval')
try:
	eval(o, [6, 7])
except ValueError as e:
	print(e.args)

get_client_ip({})

# If we got here, everything seems fine
print('I work')