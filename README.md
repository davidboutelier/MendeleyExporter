# MendeleyExporter
These scripts copy the mendeley database and extract from the copy the locations and titles of the files corresponding to a query by tag. The title is written in the metadata title of the output pdf for easy re-import into Mendeley or other bibliographic software interogating the embedded metadata.

## Requirements
- bash env
- python 3 with sqlite plugin

## Filter by tag: -t

followed by a keyword corresponding to a tag in Mendeley library

# Example

./MendeleyExporter.bash -t keyword

# TO DO
- Windows (no bash)
- save all title/metadata into pdf without exporting anything (make Mendeley resiliant)
