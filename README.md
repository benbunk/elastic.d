Elastic.D
===

Deamon (True Daemon):
 
Backend Locator (Python Scheduler):
	Runs on Plugins:	
        	Azure
		AWS
		Softlayer

Server Listener (main entry point for all incoming request--including backend locator):
	Python API
	Flask
	Swagger

Registrar (daemon):
	Data Store (Plugins)
		In memory
	 	SQL Lite

	 Frontend Driver (Runs on Scheduler):
		Plugins:
			Nginx
			Apache
			HaProxy
			Varnish
				always given current active backends
				wipe and rebuild basically

