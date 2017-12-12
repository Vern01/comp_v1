MAKEFLAGS += --silent

all:
	chmod +x computerV1.py
	echo "Example => ./computerV1.py \"42 + 42X - 42X^2 = 21\""

clean:
	rm -rf __pycache__
	rm -rf *.pyc

fclean: clean

re: fclean all
