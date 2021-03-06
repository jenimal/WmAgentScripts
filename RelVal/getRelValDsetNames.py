#!/usr/bin/env python

import urllib2,urllib, httplib, sys, re, os, phedexSubscription
import json
from xml.dom.minidom import getDOMImplementation
sys.path.append("..")
import dbsTest



def main():
    args=sys.argv[1:]
    if not len(args)==1:
        print "usage: python getRelValDsetNames.py <inputFile_containing_a_list_of_workflows>"
        sys.exit(0)
    inputFile=args[0]
    f = open(inputFile, 'r')

    url='cmsweb.cern.ch'
    for line in f:
        workflow = line.rstrip('\n')
        outputDataSets=phedexSubscription.outputdatasetsWorkflow(url, workflow)
    #    print "These are the output datasets:"
    #    print outputDataSets
        #inputEvents=getInputEvents(url, workflow)
        #print inputEvents
        for dataset in outputDataSets:
            outputEvents=dbsTest.getEventCountDataSet("https://cmsweb.cern.ch",dataset)
    #        print dataset+" match: "+str(outputEvents/float(inputEvents)*100) +"%"
            print dataset+"\t\t"+str(outputEvents)

    f.close
    sys.exit(0);

if __name__ == "__main__":
    main()

