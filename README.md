# MendeleyExporter
These scripts copy the mendeley database and extract from the copy the locations and titles of the files corresponding to a query by tag. The title is written in the metadata title of the output pdf for easy re-import into Mendeley or other bibliographic software interogating the embedded metadata.

## requirements
- bash env
- python 3 with sqlite plugin

## Export pdf: -e 

if present output pdf in current directory

## Filter by tag: -t

followed by a keyword corresponding to a tag in Mendeley library

# TO DO
- Windows (no bash)
- save all title/metadata into pdf without exporting anything (make Mendeley resiliant)
