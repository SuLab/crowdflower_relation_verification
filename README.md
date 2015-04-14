### Data and Code for *Exposing ambiguities in a relation-extraction gold standard with crowdsourcing*

Last updated 2015-04-14 Tong Shu Li

This repository contains the code and data used to generate *Exposing ambiguities in a relation-extraction gold standard with crowdsourcing*.

### Contents

- **crowdflower/**: this directory contains all of the instructions and markup for CrowdFlower job 710587, which was used to gather the data analyzed in the paper.
- **data/**: this directory contains the CrowdFlower output data as well as other data.
- **src/**: this directory contains all of the source code referenced by the iPython notebooks.
- **fig2_expert_crowd_confidence.ipynb**: [best viewed with nbviewer](http://nbviewer.ipython.org/github/sulab/crowdflower_relation_verification/blob/master/fig2_expert_crowd_confidence.ipynb). Contains all of the code used to generate figure 2.
- **fig3_raw_annotation_agreement.ipynb**: [best viewed with nbviewer](http://nbviewer.ipython.org/github/sulab/crowdflower_relation_verification/blob/master/fig3_raw_annotation_agreement.ipynb). Contains all of the code used to generate figure 3.
- **identify_published_drug_disease_relations.ipynb**: [best viewed with nbviewer](http://nbviewer.ipython.org/github/sulab/crowdflower_relation_verification/blob/master/identify_published_drug_disease_relationships.ipynb). Assigns unique identifiers to the published EU-ADR drug-disease relationships.
- **identify_raw_annotations.ipynb**: [best viewed with nbviewer](http://nbviewer.ipython.org/github/sulab/crowdflower_relation_verification/blob/master/identify_raw_annotations.ipynb). Assigns unique identifiers to the raw annotations in the raw EU-ADR.
- **map_euadr_pub_to_raw.ipynb**: [best viewed with nbviewer](http://nbviewer.ipython.org/github/sulab/crowdflower_relation_verification/blob/master/map_euadr_pub_to_raw.ipynb). Maps the identifiers for the published drug-disease relationships back to the identifiers for the raw annotations.
