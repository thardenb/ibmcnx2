'''
Print ports list

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          09/19/2015

License:       Apache 2.0
'''

servers = AdminConfig.list('ServerEntry').splitlines()
for server in servers:
    scope = str(server.split('(')[1].split(
        '/')[3].split('|')[0]) + ' ' + str(server.split('(')[0])
    print ''
    print scope

    # ServerName = server.split( '(', 1 )[ 0 ]
    # print "System information: Server Name : " + ServerName

    NamedEndPoints = AdminConfig.list("NamedEndPoint", server).splitlines()
    NamedEndPoints.sort()

    ports = []

    for namedEndPoint in NamedEndPoints:
        endPointName = AdminConfig.showAttribute(namedEndPoint, "endPointName")
        endPoint = AdminConfig.showAttribute(namedEndPoint, "endPoint")
        host = AdminConfig.showAttribute(endPoint, "host")
        port = AdminConfig.showAttribute(endPoint, "port")
        ports.append(endPointName + " : " + host + " : " + port)

        # print "\t" + endPointName + " : " + host + " : " + port

    ports.sort()
    for item in range(len(ports)):
        print '\t' + ports[item]

    del ports
