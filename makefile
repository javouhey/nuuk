all: test

test: testjs testpy testgo testjava

testjs:
	node index.js

testgo:
	make -C shortestrep all

testjava:
	make -C filesize all

testpy: collect1 collect2

collect1:
	py.test

collect2:
	python -m doctest powersof2/__init__.py
