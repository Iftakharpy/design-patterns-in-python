"""
Here we have a naive builder that builds HTML markup.
This is error prone and not very easy.
This example is not very good, but it shows the basic idea 
of when builder pattern can be useful.
"""

text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))


# now, imagine you want to build a list with 50 items
words = ['hello', 'world'] * 25
parts = ['<ul>']
for w in words:
	parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))
