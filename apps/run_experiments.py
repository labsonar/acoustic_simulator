"""
Run Synthetic Experiments and save the dataset info tables to CSV files.
"""
import os
import argparse

import torch
import lps_ml.utils.general as ml_utils
import lps_sp.acoustical.analysis as lps_analysis

import acoustic_simulator.synthetic_experiments as as_exp
import acoustic_simulator.trainer as as_trn

def _main():
    """Main function for the dataset info tables."""

    parser = argparse.ArgumentParser(description="Train an MLP classifier on iara.")
    as_trn.Trainer.add_args(parser, default_output_dir="./results/synthectic_experiments")
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    torch.set_float32_matmul_precision('medium')
    ml_utils.set_seed()

    for exp in as_exp.SyntheticExperiment:

        exp_dir = os.path.join(output_dir, exp.as_str())

        for exp_name, dm in exp.build_datamodules().items():

            exp_sub_dir = os.path.join(exp_dir, exp_name)

            print(ml_utils.format_header(60, str(exp)))
            print(ml_utils.format_header(40, exp_name))

            print(dm.to_compile_df())

            as_trn.Trainer(args, exp_sub_dir).train(dm)
            break






if __name__ == "__main__":
    _main()
