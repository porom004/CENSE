# uwsgi expects a variable called application
from api import app as application

if __name__ == '__main__':
	application.run()
