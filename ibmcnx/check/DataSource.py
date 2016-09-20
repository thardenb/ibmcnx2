'''
  Description:   Show the status of all data sources. Updated for 5.5 to correct and add data source names

  Author:        Christoph Stoettner
  Mail:          christoph.stoettner@stoeps.de
  Documentation: http://scripting101.stoeps.de
  
  Updated by:    Ted Hardenburgh
  Mail:          thardenb@gmail.com

  Version:       5.5
  Date:          09/20/2016

  License:       Apache 2.0

'''

runDB = []
errorDB = []
notInstDB = []

dbs = ['FNOSDS', 'FNGCDDS', 'IBM_FORMS_DATA_SOURCE', 'activities', 'blogs', 'communities', 'dogear', 'files', 'forums',
       'homepage', 'metrics', 'mobile', 'news', 'oauth provider', 'profiles', 'pushnotification', 'search', 'urlpreview', 'widgetcontainer', 'wikis']    # List of all databases to check

for db in dbs:    # loop through databases
    ds = AdminConfig.getid('/DataSource:' + db + '/')
    try:
        checkDS = AdminControl.testConnection(ds)
        if checkDS == "WASX7217I: Connection to provided datasource was successful.":
            # print 'Connect to %s was successful' % db
            runDB.append(db)
        else:
            errorDB.append(db)
            # print 'Error: %s is not available' % db
    except:
        if notInstDB != "All DB checked ":
            notInstDB.append(db)


runDB.sort()
errorDB.sort()
notInstDB.sort()

print ''
print '\tConnection to DataSource successful: \n'
try:
    for db in runDB:
        print '\t\t' + db
except:
    print '\t\tNo running DB'

if notInstDB:
    print ''
    print '\tDB not installed: \n'
    try:
        for db in notInstDB:
            print'\t\t' + db
    except:
        print '\t\tAll DB checked'

if errorDB:
    print ''
    print '\tERROR connecting to: \n'
    try:
        for db in errorDB:
            print '\t\t' + db
    except:
        print '\t\tAll DB running\n'
    print ''
