#! /usr/bin/env python
import copy

import nmrglue as ng
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
from pathlib import Path
from collections import defaultdict
from itertools import combinations

from nmrtoolbox.peak import PeakTable, PeakTablePipeRec, PeakTablePipeInj
from nmrtoolbox.util import ParsePeakTableError, calc_rms, check_file_existence
from nmrtoolbox.roc import RocData


class screening_study_strip_plots:
    """
    A class for generating strip plots using the ROC classification of true / false peaks
    """

    def __init__(
            self,
            recSpectrum,
            recTable,
            injSpectrum=None,
            injTable=None,
            empSpectrum=None,
            empTable=None,
            roc_obj=None,
            peak_count=20,
            pairs_strips_per_plot=10,
            num_displayed_contours=8,
            force_delete=True,
            output_dir=Path.cwd(),
            max_strip_plot=None,
    ):

        # Parse inputs and perform error checking
        if empSpectrum is not None:
            self.empSpectrum = empSpectrum

            if empTable is not None:
                if isinstance(empTable, PeakTable):
                    self.empTable = empTable
                else:
                    self.empTable = PeakTablePipeRec(empTable)
            else:
                raise ValueError('If an empirical spectrum is provided, a corresponding peak table of peaks'
                                 'must be provided in order to create the appropriate strip plots.')

        # TODO: Consider additional scenarios of accidental single entry lists provided, etc ...
        if isinstance(recSpectrum, list) and isinstance(recTable, list):
            if len(recSpectrum) != len(recTable):
                raise ValueError('The number of recovered spectrum must match that of the number of recovered peak tables.')

        if max_strip_plot is not None:
            self.peak_count = min(peak_count, max_strip_plot * pairs_strips_per_plot)

        if isinstance(recSpectrum, list) and len(recSpectrum) > 1:
            self.recTable = []
            for rec_table in recTable:
                if isinstance(rec_table, PeakTable):
                    pass
                else:
                    self.recTable.append(PeakTablePipeRec(rec_table))
            self.recSpectrum = recSpectrum

            for rec_1, rec_2 in list(combinations(range(len(self.recSpectrum)), 2)):
                strip_plot(
                    reference_spectrum=self.recSpectrum[rec_2],
                    candidate_spectrum=self.recSpectrum[rec_1],
                    candidate_peak_table=self.recTable[rec_1],
                    output_dir=output_dir,
                    peak_count=self.peak_count,
                    pairs_strips_per_plot=pairs_strips_per_plot,
                    num_displayed_contours=num_displayed_contours,
                    force_delete=force_delete,
                    plot_filename=f'qualitative_comparison_recon{rec_1}_and_recon{rec_2}'
                )

                strip_plot(
                    reference_spectrum=self.recSpectrum[rec_1],
                    candidate_spectrum=self.recSpectrum[rec_2],
                    candidate_peak_table=self.recTable[rec_2],
                    output_dir=output_dir,
                    peak_count=self.peak_count,
                    pairs_strips_per_plot=pairs_strips_per_plot,
                    num_displayed_contours=num_displayed_contours,
                    force_delete=force_delete,
                    plot_filename=f'qualitative_comparison_recon{rec_2}_and_recon{rec_1}'
                )

            if empSpectrum is not None:
                for idx_rec, rec_spec in enumerate(self.recSpectrum):
                    strip_plot(
                        reference_spectrum=self.empSpectrum,
                        candidate_spectrum=self.recSpectrum[idx_rec],
                        candidate_peak_table=self.recTable[idx_rec],
                        output_dir=output_dir,
                        peak_count=self.peak_count,
                        pairs_strips_per_plot=pairs_strips_per_plot,
                        num_displayed_contours=num_displayed_contours,
                        force_delete=force_delete,
                        plot_filename=f'qualitative_comparison_recon{idx_rec}_and_empirical'
                    )

                    strip_plot(
                        reference_spectrum=self.recSpectrum[idx_rec],
                        candidate_spectrum=self.empSpectrum,
                        candidate_peak_table=self.empTable,
                        output_dir=output_dir,
                        peak_count=self.peak_count,
                        pairs_strips_per_plot=pairs_strips_per_plot,
                        num_displayed_contours=num_displayed_contours,
                        force_delete=force_delete,
                        plot_filename=f'qualitative_comparison_empirical_and_recon{idx_rec}'
                    )

            print('All combinations of reconstruction in provided list and if, provided empirical spectrum their '
                  'combinations as well, have been generated. If strip plots utilizing ROC data for true positive '
                  'and false negative peak categorization is desired, then provide a single reconstructed spectrum with'
                  'its peak table and ROC python object.')
            sys.exit(0)

        if recSpectrum is not None:
            self.recSpectrum = recSpectrum
        else:
            raise ValueError('A spectrum passed in as the recovery spectrum must be provided.')

        if roc_obj is not None:
            self.roc = roc_obj
            self.injTable = self.roc.injected_peaks
            self.recTable = self.roc.recovered_peaks
        else:
            if recTable and injTable is not None:
                if isinstance(recTable, PeakTable):
                    self.recTable = recTable
                else:
                    self.recTable = PeakTablePipeRec(recTable)

                if isinstance(injTable, PeakTable):
                    self.injTable = injTable
                else:
                    self.injTable = PeakTablePipeInj(file=injTable, carrier_frequency=self.recTable.axis)
            else:
                raise ValueError('Both an injected and recovered peak table is required.')

        if recSpectrum and injSpectrum is not None:
            self.recSpectrum = recSpectrum
            self.injSpectrum = injSpectrum
        else:
            raise ValueError('Both an injected and recovered spectrum is required.')

        if hasattr(self, 'roc'):
            index_true_recovery_peaks = [p.recovered_peak.get_par('INDEX') for p in self.roc.roc_points
                                             if p.category == RocData.Category.true]
            false_negative_indices = list(
                set([peak.get_par('INDEX') for peak in self.roc.injected_peaks.peaks]).difference(
                    set([p.injected_peak.get_par('INDEX') for p in self.roc.roc_points if p.injected_peak is not None])))
            false_negative_injected_peaks = [p for p in self.roc.injected_peaks.peaks
                                             if p.get_par('INDEX') in false_negative_indices]

            # false_negative_reference_peak_table = copy.deepcopy(self.recTable)
            false_negative_reference_peak_table = copy.deepcopy(self.injTable)
            false_negative_reference_peak_table.peaks = false_negative_injected_peaks
            _false_negative_reference_peak_count = len(false_negative_reference_peak_table.peaks)
            fn_ref_peak_count = min(_false_negative_reference_peak_count, max_strip_plot * pairs_strips_per_plot)

            _precision_peak_count = self._determine_roc_plateau() + 1
            precision_peak_count = min(_precision_peak_count, max_strip_plot * pairs_strips_per_plot)

            strip_plot(
                    reference_spectrum=self.injSpectrum,
                    candidate_spectrum=self.recSpectrum,
                    candidate_peak_table=self.recTable,
                    output_dir=output_dir,
                    recovery_indices=index_true_recovery_peaks,
                    peak_count=precision_peak_count,
                    pairs_strips_per_plot=pairs_strips_per_plot,
                    num_displayed_contours=num_displayed_contours,
                    force_delete=force_delete,
                    plot_filename='precision_plot'
                )

            # If there are no false negative peaks, then do not call strip plotter.
            if len(false_negative_reference_peak_table.peaks) > 0:
                strip_plot(
                    reference_spectrum=self.recSpectrum,
                    candidate_spectrum=self.injSpectrum,
                    candidate_peak_table=false_negative_reference_peak_table,
                    output_dir=output_dir,
                    peak_count=fn_ref_peak_count,
                    pairs_strips_per_plot=pairs_strips_per_plot,
                    num_displayed_contours=num_displayed_contours,
                    force_delete=force_delete,
                    plot_filename='false_negative_plot'
                )
        else:
            strip_plot(
                reference_spectrum=self.injSpectrum,
                candidate_spectrum=self.recSpectrum,
                candidate_peak_table=self.recTable,
                output_dir=output_dir,
                peak_count=self.peak_count,
                pairs_strips_per_plot=pairs_strips_per_plot,
                num_displayed_contours=num_displayed_contours,
                force_delete=force_delete,
                plot_filename=f'qualitative_comparison_recon_and_injected'
            )
            strip_plot(
                reference_spectrum=self.recSpectrum,
                candidate_spectrum=self.injSpectrum,
                candidate_peak_table=self.injTable,
                output_dir=output_dir,
                peak_count=self.peak_count,
                pairs_strips_per_plot=pairs_strips_per_plot,
                num_displayed_contours=num_displayed_contours,
                force_delete=force_delete,
                plot_filename=f'qualitative_comparison_injected_and_recon'
            )

        if hasattr(self, 'empSpectrum'):
            strip_plot(
                reference_spectrum=self.recSpectrum,
                candidate_spectrum=self.empSpectrum,
                candidate_peak_table=self.empTable,
                output_dir=output_dir,
                peak_count=self.peak_count,
                pairs_strips_per_plot=pairs_strips_per_plot,
                num_displayed_contours=num_displayed_contours,
                force_delete=force_delete,
                plot_filename=f'reconstruction_artifacts'
            )


    def _determine_roc_plateau(self):
        rr = [p.RR for p in self.roc.roc_points]
        return rr.index(max(rr))


class strip_plot:
    """
    A class for creating strip plots, comparing reference and contestant reconstructions
    """

    def __init__(
            self,
            reference_spectrum,
            candidate_spectrum,
            candidate_peak_table,
            output_dir,
            spectral_window=None,
            plot_filename='strip_plot_',
            recovery_indices=None,
            peak_count=20,
            pairs_strips_per_plot=10,
            num_displayed_contours=8,
            force_delete=True,
    ):

        self.outdir = Path(output_dir)
        self.filename = plot_filename
        self.force_delete = force_delete
        self.pspp = pairs_strips_per_plot

        # Peak count is used to define reduce the size of peak table as well as
        # to capture the last of the peaks to plot and save the figure.
        self.peak_count = peak_count

        # TODO:
        #  this looks like a copy of the input handling logic used in roc module
        #  we should consider making this a method in the peak class
        if isinstance(candidate_peak_table, PeakTable):
            self.candidate_peak_table = candidate_peak_table
        else:
            try:
                self.candidate_peak_table = PeakTablePipeRec(
                    file=candidate_peak_table,
                )
            except FileNotFoundError as e:
                raise FileNotFoundError(e)
            except ParsePeakTableError as e:
                raise ParsePeakTableError(e)

        self.recovery_indices = recovery_indices

        if spectral_window is not None:
            self.upfield = spectral_window[::2]
            self.downfield = spectral_window[1::2]
        else:
            self.upfield = [axis.max for axis in candidate_peak_table.axis.get_field('range')]
            self.downfield = [axis.min for axis in candidate_peak_table.axis.get_field('range')]

        # Note: When nmrglue reads in a spectrum, internally it does the following to the axes (X, Y, Z) --> (Z, Y, X)
        self.candidate_dic, self.candidate_data = ng.pipe.read_lowmem(candidate_spectrum)
        self.reference_dic, self.reference_data = ng.pipe.read_lowmem(reference_spectrum)

        # Create a dictionary of unit conversions.
        # This will be later used in plotting the two spectra at the same peak location
        self.ref_uc = {x: ng.pipe.make_uc(self.reference_dic,
                                          self.reference_data,
                                          x)
                       for x in range(len(self.candidate_peak_table.axis.dimensions()))}

        self.cand_uc = {x: ng.pipe.make_uc(self.candidate_dic,
                                           self.candidate_data,
                                           x)
                        for x in range(len(self.candidate_peak_table.axis.dimensions()))}

        # Determine the axes mapping between spectral data and peak tables
        self.axis_order = self._determine_axis_ordering()

        self._determine_contour(num_displayed_contours)
        self.candidate_peak_table.reduce(number=self.peak_count)

        self.create_strips()


    def _determine_axis_ordering(self):
        dct = defaultdict(lambda: defaultdict(int))
        for i, (pts, ppm_bounds) in enumerate(
                zip(self.candidate_peak_table.axis.get_field('num_pts'),
                    self.candidate_peak_table.axis.get_field('range'))):
            ii = [cand_key for cand_key, cand_val in self.cand_uc.items() if pts == cand_val._size]
            jj = [cand_key for cand_key, cand_val in self.cand_uc.items() if
                  abs(ppm_bounds.min - cand_val._first) / cand_val._first < 0.001]
            unique_axis_idx = list(set(ii) & set(jj))[0]
            dct['cand'][i] = unique_axis_idx

        inverted_cand_dct = {v: k for k, v in dct['cand'].items()}
        for ref_key, ref_val in self.ref_uc.items():
            ii = [cand_key for cand_key, cand_val in self.cand_uc.items() if (ref_val._car == cand_val._car and ref_val._first == ref_val._first)]
            dct['ref'][inverted_cand_dct[ii[0]]] = ref_key
        return dct


    def _determine_contour(self, contour_count):
        # TODO: Determine contour on a per peak basis
        self.ref_noise = calc_rms(self.reference_data[1][-1][-1])
        self.cand_noise = calc_rms(self.candidate_data[1][-1][-1])

        ref_contour_stop = np.nanmax(self.reference_data[:, :, :])
        cand_contour_stop = np.nanmax(self.candidate_data[:, :, :])

        # TODO:
        #  Adjust range of peak intensity displayed by users input of counter count
        self.cand_contour_levels = np.logspace(start=np.log(self.cand_noise),
                                               stop=np.log(cand_contour_stop),
                                               num=contour_count+3, endpoint=True, base=np.e)[1:-1]
        self.ref_contour_levels = np.logspace(start=np.log(self.ref_noise),
                                              stop=np.log(ref_contour_stop),
                                              num=contour_count+3, endpoint=True, base=np.e)[1:-1]


    def create_strips(self):
        plot_number = 1
        # TODO: Choose colorblind color palette
        fig = plt.figure()

        # TODO: Adjust width of pairs of strip plots based on number of pairs to be displayed.
        #  E.g., for FN plotting when there is only a few pairs of strips to be plotted.
        for idx, peak in enumerate(self.candidate_peak_table.peaks):
            # Recall transposed axes in nmrglue, i.e., (Z, Y, X)
            # TODO: error handling to catch uses of x_width for peaks
            #       whose extended boundary would be outside the spectral window
            if 'XW' in peak.prop:
                x_width = abs(
                    3.0 * (peak.get_par('XW') * self.cand_uc[self.axis_order['ref'][0]]._delta))
            else:
                x_width = abs(
                    1.0 * ((peak.get_par('X1') - peak.get_par('X3')) * self.cand_uc[self.axis_order['ref'][0]]._delta))

            print(idx)
            if idx == 45:
                print('mismatch longitduinally')
            # if idx == 305:
            #     print('edge case')

            ### Reference spectrum ###
            idx_ref_a1 = self.ref_uc[self.axis_order['ref'][1]](peak.get_par('Y_PPM'), "ppm")
            min_ref_a0 = self.ref_uc[self.axis_order['ref'][0]](peak.get_par('X_PPM') + x_width, "ppm")
            max_ref_a0 = self.ref_uc[self.axis_order['ref'][0]](peak.get_par('X_PPM') - x_width, "ppm")
            min_ref_a2 = min(self.ref_uc[self.axis_order['ref'][2]](self.upfield[2], "ppm"),
                          self.ref_uc[self.axis_order['ref'][2]](self.downfield[2], "ppm"))
            max_ref_a2 = max(self.ref_uc[self.axis_order['ref'][2]](self.upfield[2], "ppm"),
                             self.ref_uc[self.axis_order['ref'][2]](self.downfield[2], "ppm"))

            # Ensures width of strip plot does not exceed spectral bounds
            # TODO: Discussion with Mike; require understanding of how data was acquired (STATES, TPPI, STATE-TPPI)
            #  in order to determine folding pattern
            if min_ref_a0 < self.ref_uc[self.axis_order['ref'][0]](self.downfield[0], "ppm"):
                min_ref_a0 = self.ref_uc[self.axis_order['ref'][0]](self.downfield[0], "ppm")

            if max_ref_a0 > self.ref_uc[self.axis_order['ref'][0]](self.upfield[0], "ppm"):
                max_ref_a0 = self.ref_uc[self.axis_order['ref'][0]](self.upfield[0], "ppm")

            # extract strip
            # TODO: Option to sum across planes above and below
            ref_order = (self.axis_order['ref'][2], self.axis_order['ref'][1], self.axis_order['ref'][0])
            strip_ref = self.reference_data.transpose(ref_order)[min_ref_a2:max_ref_a2 + 1,
                        idx_ref_a1, min_ref_a0:max_ref_a0 + 1]

            # determine ppm limits of contour plot; x, y - axes of generated figure
            # TODO: Verify the following ... x-axis -> direct dim (0-th index); y-axis -> 2nd-indirect dimension (n-th index)
            strip_ppm_x = self.ref_uc[self.axis_order['ref'][0]].ppm_scale()[min_ref_a0:max_ref_a0 + 1]
            strip_ppm_y = self.ref_uc[self.axis_order['ref'][2]].ppm_scale()[min_ref_a2:max_ref_a2 + 1]
            strip_x, strip_y = np.meshgrid(strip_ppm_x, strip_ppm_y)

            # add contour plot of strip to figure
            ax1 = fig.add_subplot(1, 2 * self.pspp + 1, 2 * idx + 1 - (plot_number - 1) * (2 * self.pspp))
            # print(idx)
            ax1.contour(strip_x,
                        strip_y,
                        strip_ref,
                        self.ref_contour_levels,
                        colors='black',
                        linewidths=0.5)

            if 'ZW' in peak.prop:
                peak_width_a2_upfield = peak.get_par('Z_PPM') - 1.0 * abs(
                    (peak.get_par('ZW') * self.ref_uc[self.axis_order['ref'][2]]._delta))
                peak_width_a2_downfield = peak.get_par('Z_PPM') + 1.0 * abs(
                    (peak.get_par('ZW') * self.ref_uc[self.axis_order['ref'][2]]._delta))
            else:
                peak_width_a2_upfield = peak.get_par('Z_PPM') - 1.0 * abs(
                    ((peak.get_par('Z1') - peak.get_par('Z3')) * self.ref_uc[self.axis_order['ref'][2]]._delta))
                peak_width_a2_downfield = peak.get_par('Z_PPM') + 1.0 * abs(
                    ((peak.get_par('Z1') - peak.get_par('Z3')) * self.ref_uc[self.axis_order['ref'][2]]._delta))

            # This could be of use to identify artifacts with spectral widths exceeding that of the spectral window
            if peak_width_a2_upfield < self.upfield[2]:
                peak_width_a2_upfield = self.upfield[2]

            if peak_width_a2_downfield > self.downfield[2]:
                peak_width_a2_downfield = self.downfield[2]

            ax1.fill_between(np.linspace(peak.get_par('X_PPM') - x_width,
                                         peak.get_par('X_PPM') + x_width,
                                         10),
                             peak_width_a2_upfield,
                             peak_width_a2_downfield,
                             facecolor='silver')
            ax1.invert_yaxis()
            ax1.invert_xaxis()

            # turn off ticks and labels, add labels
            ax1.tick_params(axis='both', labelbottom=False, bottom=False, top=False,
                            labelleft=False, left=False, right=False)
            ax1.text(0.5, 1.01, f'{peak.get_par("Y_PPM"):.1f}', size=6, transform=ax1.transAxes)
            ax1.text(0.65, -0.025, f'{peak.get_par("X_PPM"):.1f}', size=6, transform=ax1.transAxes)

            # label and put ticks on first strip plot
            if idx % self.pspp == 0:
                ax1.set_ylabel(f"{self.candidate_peak_table.axis.keys()[2]} [PPM]")
                ax1.tick_params(axis='y', labelleft=True, left=True, direction='out', labelsize=6)

            ### Candidate spectrum ###
            idx_cand_a1 = self.cand_uc[self.axis_order['cand'][1]](peak.get_par('Y_PPM'), "ppm")
            min_cand_a0 = self.cand_uc[self.axis_order['cand'][0]](peak.get_par('X_PPM') + x_width, "ppm")
            max_cand_a0 = self.cand_uc[self.axis_order['cand'][0]](peak.get_par('X_PPM') - x_width, "ppm")
            min_cand_a2 = min(self.cand_uc[self.axis_order['cand'][2]](self.upfield[2], "ppm"),
                              self.cand_uc[self.axis_order['cand'][2]](self.downfield[2], "ppm"))
            max_cand_a2 = max(self.cand_uc[self.axis_order['cand'][2]](self.upfield[2], "ppm"),
                              self.cand_uc[self.axis_order['cand'][2]](self.downfield[2], "ppm"))

            # Ensures width of strip plot does not exceed spectral bounds
            # TODO: Discuss with Mike of how to handle this case wih wrapped spectral windows in mind
            if min_cand_a0 < self.cand_uc[self.axis_order['cand'][0]](self.downfield[0], "ppm"):
                min_cand_a0 = self.cand_uc[self.axis_order['cand'][0]](self.downfield[0], "ppm")

            if max_cand_a0 > self.cand_uc[self.axis_order['cand'][0]](self.upfield[0], "ppm"):
                max_cand_a0 = self.cand_uc[self.axis_order['cand'][0]](self.upfield[0], "ppm")

            cand_order = (self.axis_order['cand'][2], self.axis_order['cand'][1],  self.axis_order['cand'][0])
            strip_cand = self.candidate_data.transpose(cand_order)[min_cand_a2:max_cand_a2 + 1,
                         idx_cand_a1, min_cand_a0:max_cand_a0 + 1]

            # determine ppm limits of contour plot; x, y - axes of generated figure
            # x-axis -> direct dim (0-th index); y-axis -> 2nd-indirect dimension (n-th index)
            strip_ppm_x = self.cand_uc[self.axis_order['cand'][0]].ppm_scale()[min_cand_a0:max_cand_a0 + 1]
            strip_ppm_y = self.cand_uc[self.axis_order['cand'][2]].ppm_scale()[min_cand_a2:max_cand_a2 + 1]
            strip_x, strip_y = np.meshgrid(strip_ppm_x, strip_ppm_y)

            # add contour plot of strip to figure
            ax2 = fig.add_subplot(1, 2 * self.pspp + 1, 2 * idx + 2 - (plot_number - 1) * (2 * self.pspp))
            ax2.contour(strip_x,
                        strip_y,
                        strip_cand,
                        self.cand_contour_levels,
                        colors='blue',
                        linewidths=0.5)

            if 'ZW' in peak.prop:
                peak_width_a2_upfield = peak.get_par('Z_PPM') - 1.0 * abs(
                    (peak.get_par('ZW') * self.cand_uc[self.axis_order['cand'][2]]._delta))
                peak_width_a2_downfield = peak.get_par('Z_PPM') + 1.0 * abs(
                    (peak.get_par('ZW') * self.cand_uc[self.axis_order['cand'][2]]._delta))
            else:
                peak_width_a2_upfield = peak.get_par('Z_PPM') - 1.0 * abs(
                    ((peak.get_par('Z1') - peak.get_par('Z3')) * self.cand_uc[self.axis_order['cand'][2]]._delta))
                peak_width_a2_downfield = peak.get_par('Z_PPM') + 1.0 * abs(
                    ((peak.get_par('Z1') - peak.get_par('Z3')) * self.cand_uc[self.axis_order['cand'][2]]._delta))

            # This could be of use to identify artifacts with spectral widths exceeding that of the spectral window
            if peak_width_a2_upfield < self.upfield[2]:
                peak_width_a2_upfield = self.upfield[2]

            if peak_width_a2_downfield > self.downfield[2]:
                peak_width_a2_downfield = self.downfield[2]

            # If provided with indices of candidate's peaktable that correspond to successfully recovered
            # peaks from the reference spectrum, assign the appropriate color shading
            if self.recovery_indices is not None:
                if peak.get_par('INDEX') in self.recovery_indices:
                    facecolor = 'orange'
                else:
                    facecolor = 'red'
            else:
                facecolor = 'silver'

            ax2.fill_between(np.linspace(peak.get_par('X_PPM') - x_width,
                                         peak.get_par('X_PPM') + x_width,
                                         10),
                             peak_width_a2_upfield,
                             peak_width_a2_downfield,
                             facecolor=facecolor)
            ax2.invert_yaxis()
            ax2.invert_xaxis()

            # turn off ticks and labels, add labels and assignment
            ax2.tick_params(axis='both', labelbottom=False, bottom=False, top=False,
                            labelleft=False, left=False, right=False)

            if (idx + 1) % self.pspp == 0 or idx == self.peak_count - 1:
                fig.text(0.45, 0.05, f"{self.candidate_peak_table.axis.keys()[0]} [PPM]")

                if check_file_existence(f"{self.outdir}/{self.filename}_{plot_number}.eps"):
                    if self.force_delete:
                        Path(f"{self.outdir}/{self.filename}_{plot_number}.eps").unlink()
                        fig.set_size_inches(25.6, 12.4)
                        fig.savefig(f"{self.outdir}/{self.filename}_{plot_number}.eps", format='eps',
                                    dpi=1200)
                    else:
                        print(f'No figure was saved because there is an existing figure saved as '
                              f'{self.outdir}/{self.filename}_{plot_number}.eps '
                              f'and f{self.force_delete} is set to False.')
                else:
                    fig.set_size_inches(25.6, 12.4)
                    fig.savefig(f"{self.outdir}/{self.filename}_{plot_number}.eps", format='eps',
                                dpi=1200)
                fig = plt.figure()
                plot_number += 1


def parse_args():
    # TODO: you are missing parameters here
    parser = argparse.ArgumentParser(description='You can add a description here')
    parser.add_argument('--reference_spectrum', required=True)
    parser.add_argument('--candidate_spectrum', required=True)
    parser.add_argument('--candidate_peak_table', required=True)
    parser.add_argument('--spectral_window', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--true_recovery_indices', required=False)
    return parser.parse_args()


def main():
    # parse the arguments from command line input and execute
    args = parse_args()

    try:
        my_strip_plot = strip_plot(
            reference_spectrum=args.reference_spectrum,
            candidate_spectrum=args.candidate_spectrum,
            candidate_peak_table=args.candidate_peak_table,
            spectral_window=args.spectral_window,
            output_dir=args.output_dir,
        )
    except (SystemExit, EnvironmentError, OSError) as e:
        print(e)
        sys.exit()
