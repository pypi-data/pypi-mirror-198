# nmrtoolbox

## Introduction
This is a simple utility that provides modules for working with NMRPipe peak tables and performing a receiver operator characteristic (ROC) analysis to quantify the quality of the "recovered" peaks relative to a control set of "injected" peaks.  The modules in this package are as follows:
- `nmrtoolbox.peak`: classes for reading in peak tables (currently supports both synthetically generated and recovered peak tables from NMRPipe)
- `nmrtoolbox.roc`: perform receiver operator characteristic (ROC) analysis of a recovered peak table relative to an injected peak table
- `nmrtoolbox.mask`: define regions of a spectrum that contain signal or are empty
- `nmrtoolbox.util`: various supporting utilities used by other modules
- `nmrtoolbox.strip_plot`: generate color coded strip plots that correspond to the true positive and false positive peaks classified by an ROC analysis

## Applications

### Example #1 - Formal Workflow
The tools in this package are utilized by the [NUScon](https://nuscon.org/home) software package.  You can access NUScon on the NMRbox platform (free for academic, government, and non-profit users).  Running `nuscon -h` will provide instructions on how to run the NUScon evaluation workflow, which directly utilizes the tools presented here in the `nmrtoolbox` package.

### Example #2 - Kick the Tires

```commandline
from nmrtoolbox.roc import roc

# perform ROC analysis and specify filtering criteria for 
# cluster_type and chi2prob
my_roc = roc(
    recovered_table=<file-recovered.tab>,
    injected_table=<file-injected.tab>,
    cluster_type=1,
    chi2prob=.75,
)

# show and plot results
my_roc.print_stats()
my_roc.plot_roc()
my_roc.plot_peaks()
my_roc.plot_outliers()
```

The roc function supports the following filter criteria:
- `number`
- `height` 
- `abs_height` 
- `roi_list` 
- `index`
- `cluster_type`
- `mask_file`
- `chi2prob`
- `outlier`
- `vol_height_mismatch`
- `maxLW_percent_SW`


Note: Filtering by `mask` requires the external use of NMRPipe to generate a mask file indicating where the spectrum is empty.  This binary data is converted by [Connjur Spectrum Translator](https://nmrbox.nmrhub.org/software/spectrum-translator) into a "tabular" format file (i.e. plain text) which is then read in by `nmrtoolbox.mask`.


## Changelog

v10
- major change: ROC now sorts peaks by absolute value of intensity (previously used intensity from largest positive down to largest negative)
- new module added for generating strip plots
- add more options for peak table filtering

v9
- change in internal data model for storing metadata in Peak, PeakTable, Mask, ROC, and ROI classes
- allow roc class to accept Mask object (not just mask file)
- approximate maximum LW for injected peaks from X1/X3, etc. parameters in the injected peak table
- function to write NMRPipe peak table to file

v8
- change to MIT license
- box_radius for mask filtering is multidimensional
- improved input options for setting carrier frequency
- axis labels used to verify compatibility of Peak, Mask, ROI, and ROC objects

v7
- addition of `roc` module
- addition of `mask` module

v6
- rename package as `nmrtoolbox`
- use subclasses to handle NMRPipe peak tables coming from genSimTab or from the peak picker

v5
- new Axis class for containing metadata from peak table header
