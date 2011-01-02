Install
---

  sudo python setup.py install

Use
---
1) Setup an SQLServer

2) Setup your target database

3) Download and import the database dump from http://www.eveonline.com/community/toolkit.asp

4) run evedb (this example assumes mysql as target database)
  evedb "mssql://<user>:<password>@<server>/<database>?PORT=51950" "mysql://<user>:<password>@<server>/<database>"

4.b) Watch the epic fail, since you are probably using an untested datasource as target ; ) - start hacking!

Description
---
I don't like sqlserver, but I still have interest in using the database backups that CCP makes available for "fansite" use.

This is a set of script which allows you to easily 'coerce' a subset of the data that is exported. Currently I am using a very limited set of fields from each table, but these can be expanded at will easily. Directly incompatible fields must have a custom type handling the conversion. And this script will probably need expansion in the future to work proparly.

The connection string is directly passed into create_engine of the sqlalchemy package, this means that the specified engine must be available on the system you are using.

In my case, I am using FreeTDS to connect to the SQLServer through unixODBC, my /etc/unixODBC/odbcinst.ini looks like this:

  [SQL Server]
  Description=v0.63 with protocol v8.0
  Driver=/usr/lib/libtdsodbc.so
  UsageCount=1

I'm also running sqlserver on a different port, which above displays how arguments can be passed directly into the odbc infrastructure (if you are into that sort of things).

License
---
Everything here is licensed under GPL v3 - except for documentation which is copyleft.
