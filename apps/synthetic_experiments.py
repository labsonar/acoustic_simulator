"""
Simple classifier over iemanja dataset
"""
import os
import argparse

import torch
import lps_ml.core as ml_core
import lps_ml.core.cv as ml_cv
import lps_ml.datasets as ml_db
import lps_ml.datasets.selection as ml_sel
import lps_ml.utils.general as ml_utils
import lps_sp.acoustical.analysis as lps_analysis
import lps_ml.audio_processors as ml_procs
import lps_ml.core.processor as ml_proc

import acoustic_simulator.synthetic_experiments as syn_exp

def _main():
    """Main function for the dataset info tables."""

    parser = argparse.ArgumentParser(description="Train an MLP classifier on iara.")
    parser.add_argument("--output-dir", default="./results/synthectic_experiments",
        help="Output Directory (default: ./results/synthectic_experiments)"
    )
    lps_analysis.SpectralAnalysis.add_args(parser)
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    torch.set_float32_matmul_precision('medium')
    ml_utils.set_seed()


    analysis, params = lps_analysis.SpectralAnalysis.build_from_args(args)

    audio_pipelines : list[ml_proc.AudioPipeline] = [ml_procs.ToFloatConverter()]
    sample_pipelines: list[ml_core.SamplePipeline] = []

    audio_pipelines.append(ml_procs.SpectralProcessor(analysis=analysis, params=params))

    n_samples=2**17
    overlap=2**16

    n_samples=int(n_samples / params.n_spectral_pts / 2)
    overlap=int(overlap / params.n_spectral_pts / 2)

    file_processor = ml_procs.SampleProcessor(
        n_samples=n_samples,
        overlap=overlap,
        audio_pipelines=audio_pipelines,
        sample_pipelines=sample_pipelines
    )

    for exp in syn_exp.SyntheticExperiment:

        dynamic_selection = exp.get_dynamic_selection()
        channel_selection = exp.get_channel_selection()

        for exp_name, filt in exp.get_filters().items():

            print(ml_utils.format_header(60, str(exp)))
            print(ml_utils.format_header(40, exp_name))

            selection = ml_sel.Selector(
                    target = ml_sel.ColumnTarget(column="CLASS", map_values=True),
                    filters = [filt]
                )

            dm = ml_db.Iemanja(
                file_processor = file_processor,
                selection = selection,
                cv = ml_cv.FiveByTwo(),
                dynamic_selection = dynamic_selection,
                channel_selection = channel_selection,
            )

            print(dm.to_compile_df())
            print(dm.to_df().to_csv(os.path.join(output_dir, f"{exp.name.lower()}_{exp_name}.csv"), index=False))

if __name__ == "__main__":
    _main()
