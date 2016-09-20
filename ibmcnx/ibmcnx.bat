REM Replace JDBC_DRIVER value with the correct location of the JDBC driver
REM Update values for -username and -password 

SET JDBC_DRIVER=D:\IBM\SQLLIB\java\db2jcc4.jar

wsadmin.bat -lang jython -username wasadmin -password password -javaoption -Dcom.ibm.ws.scripting.classpath=%JDBC_DRIVER% -f ibmcnx/menu/cnxMenu.py

