all: test

test: testjs testpy testgo

testjs:
	node index.js

testgo:
	make -C shortestrep all

testpy: collect1 collect2

collect1:
	py.test

collect2:
	python -m doctest powersof2/__init__.py
