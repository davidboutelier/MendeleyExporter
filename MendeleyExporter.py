#!/usr/local/opt/python/libexec/bin/python

import sys
import os
import sqlite3
import numpy as np
import shutil
import urllib.request

from PyPDF2 import PdfFileWriter, PdfFileReader

# tag to extract
Target=sys.argv[1]

# connect to the copy of the mendeley database
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# get the documentId which have been tagged with target tag
sql = "SELECT documentId FROM DocumentTags WHERE tag=?"
cursor.execute(sql,(Target,))
IdSearch = cursor.fetchall()
IdSearch = np.asarray(IdSearch)
IdSearch = IdSearch[:,0]

for i in range(0,len(IdSearch)):
    SingleId = IdSearch[i]
    SingleId = str(SingleId)

    # get title of the document
    sql = "SELECT title FROM Documents WHERE id=?"
    cursor.execute(sql, (SingleId,))
    titleDocument = cursor.fetchall()
    titleDocument = np.asarray(titleDocument)
    titleDocument = titleDocument[0,0]
    titleDocument = str(titleDocument)

    # get the hash of the document
    sql = "SELECT hash FROM DocumentFiles WHERE documentId=?"
    cursor.execute(sql, (SingleId,))
    ResultHash = cursor.fetchall()
    ResultHash = np.asarray(ResultHash)
    ResultHash = ResultHash[:,0]
    ResultHash = ResultHash[0]
    ResultHash = str(ResultHash)

    # find local url of document from ResultHash
    sql = "SELECT localUrl FROM Files WHERE hash=?"
    cursor.execute(sql, (ResultHash,))
    ResultSinglelocalURL=cursor.fetchall()
    ResultSinglelocalURL=np.asarray(ResultSinglelocalURL)
    ResultSinglelocalURL =ResultSinglelocalURL[0,0]
    ResultSinglelocalURL = str(ResultSinglelocalURL)

    # trim the resuly
    ResultSinglelocalURL=ResultSinglelocalURL[7:]

    # convert to file path
    ResultSinglelocalURL = urllib.request.unquote(ResultSinglelocalURL)

    # get name of file
    base=os.path.basename(ResultSinglelocalURL)

    # rewrite the pdf to be able to change the title field in metadata
    output = PdfFileWriter()
    input = PdfFileReader(open(ResultSinglelocalURL, "rb"))
    npage = input.getNumPages()
    for j in range(0,npage):
        output.addPage(input.getPage(j))

    # change the title metadata so that mendeley can get it later on re-import
    output.addMetadata({'/Title': titleDocument})
    outputStream = open(base, "wb")
    output.write(outputStream)
