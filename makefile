all: test

test: testjs testpy

testjs:
	node index.js

testpy: collect1 collect2

collect1:
	py.test

collect2:
	python -m doctest powersof2/__init__.py
