# https://flatdict.readthedocs.io
# https://github.com/gmr/flatdict

import pprint
import flatdict

values = {'foo': {'bar': {'baz': 0,
                          'qux': 1,
                          'corge': 2},
                  'grault': {'baz': 3,
                             'qux': 4,
                             'corge': 5}},
          'garply': {'foo': 0, 'bar': 1, 'baz': 2, 'qux': {'corge': 3}}}

flat = flatdict.FlatDict(values)
print(flat['foo:bar:baz'])

flat['test:value:key'] = 10
del flat['test']
for key in flat:
    print(key)

for value in flat.itervalues():
    print(value)

pprint.pprint(flat.as_dict())
pprint.pprint(dict(flat))
print(flat == flat.as_dict())