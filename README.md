# atlas-analysisbase-dask-environment
Example of how to create an ATLAS AnalysisBase Docker image that can install dask and other tools

Based off of https://gitlab.cern.ch/recast-atlas/examples/analysis-base-container-python-venv

## AnalysisBase images

Lists of all AnalysisBase releases are provided on the ATLAS Twikis:

* [Release 24.2.X series](https://twiki.cern.ch/twiki/bin/view/AtlasProtected/AnalysisBaseReleaseNotes24pt2)
* [Release 21.2.X series](https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/AnalysisBaseReleaseNotes21_2)

More easily though, you can just use [`crane`](https://github.com/google/go-containerregistry/blob/v0.14.0/cmd/crane/) to get a listing of all images from the command line

```
crane ls gitlab-registry.cern.ch/atlas/athena/analysisbase
```
