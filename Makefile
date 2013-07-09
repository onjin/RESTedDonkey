all:
	pip install -r requirements.txt --upgrade

run:
	twistd -n web --class donkey.core.resource
