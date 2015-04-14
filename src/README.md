### Code

Last updated 2015-04-14 Tong Shu Li

This directory contains all of the source code imported and used by the iPython notebooks.

### File Contents

- **aggregate_votes.py**: takes all the votes for a single CrowdFlower work unit and aggregates the results to determine how many people voted on each choice.
- **broad_reltype_performance.py**: ranks the choices made for each CrowdFlower work unit by the crowd and calculates confidence scores and agreement percentages for all work units.
- **check_settings.py**: checks that the settings used for processing the CrowdFlower data are correct.
- **file_util.py**: a file containing helper functions for processing text files.
- **filter_data.py**: filters and subsets the complete CrowdFlower output data down to the relevant portions.
- **get_pubmed_abstract.py**: queries PubMed for an abstract. Unicode characters are converted to ASCII.
- **true_relation_type.py**: determines the EU-ADR answer for each CrowdFlower work unit.
- **unicode_to_ascii.py**: converts Unicode text to an ASCII representation.
