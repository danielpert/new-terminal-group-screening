#!/usr/bin/env python
"""Initialize the project's data space.

Iterates over all defined state points and initializes
the associated job workspace directories."""
import argparse
import logging
import datetime
from copy import deepcopy
from hashlib import sha1

import signac

logging.basicConfig(filename='init.log', filemode='w', level=logging.INFO)

chainlength = 17 # only study this chainlength

'''
-----------------------------
New terminal groups (11)
-----------------------------
'''
terminal_groups_new = \
    ['amide', 'biphenyl', 'cyclohexyl', 'dihydroxyphenyl',
     'formyl', 'nitroso', 'pentafluorophenyl', 'sulfhydryl',
     'triazole', 'benzoicacid', 'isopropylbenzene']
'''
-----------------------------
Old terminal groups (19)
-----------------------------
'''
terminal_groups_old = \
    ['acetyl', 'amino', 'carboxyl', 'cyano', 'cyclopropyl',
     'difluoromethyl', 'ethylene', 'fluorophenyl', 'hydroxyl',
     'isopropyl', 'methoxy', 'methyl', 'nitro', 'nitrophenyl',
     'perfluoromethyl', 'phenol', 'phenyl', 'pyrrole', 'toluene']

    
# Initialize the project
def main(args, random_seed):
    project = signac.init_project("NewTerminalGroupScreening")
    logging.info("Init begin: {}".format(datetime.datetime.today()))
    logging.info("Initialized project name")
    statepoints = list()
    
    for replication_index in range(args.num_replicas):
        
        for tg_a in terminal_groups_new:
            for tg_b in terminal_groups_new:
                the_statepoint = dict(
                  # Carbon backbone length
                    chainlength = chainlength,
                  # Backbone chemistry
                    backbone = 'Alkylsilane',
                  # Terminal groups
                    terminal_group_1 = tg_a,
                    terminal_group_2 = tg_a,
                    terminal_group_3 = tg_b,
                  # Number of monolayer chains
                    n = 100,
                  # monolayer pattern type
                    pattern_type = 'random',
                  # Random seed
                    seed = random_seed*(replication_index + 1))
                project.open_job(statepoint=the_statepoint).init()
                statepoints.append(the_statepoint)
                logging.info(msg="At the statepoint: {}".format(the_statepoint))
            
        for tg_a in terminal_groups_new:
            for tg_b in terminal_groups_old:
                the_statepoint = dict(
                  # Carbon backbone length
                    chainlength = chainlength,
                  # Backbone chemistry
                    backbone = 'Alkylsilane',
                  # Terminal groups
                    terminal_group_1 = tg_a,
                    terminal_group_2 = tg_a,
                    terminal_group_3 = tg_b,
                  # Number of monolayer chains
                    n = 100,
                  # monolayer pattern type
                    pattern_type = 'random',
                  # Random seed
                    seed = random_seed*(replication_index + 1))
            project.open_job(statepoint=the_statepoint).init()
            statepoints.append(the_statepoint)
            logging.info(msg="At the statepoint: {}".format(the_statepoint))
        
        for tg_1 in terminal_groups_new:
            for tg_2 in terminal_groups_old:
                for tg_3 in ['carboxyl', 'fluorophenyl', 'hydroxyl',
                             'isopropyl', 'methyl', 'nitro', 'perfluoromethyl',
                             'cyano', 'nitroso', 'amide']:
                    the_statepoint = dict(
                      # Carbon backbone length
                        chainlength = chainlength,
                      # Backbone chemistry
                        backbone = 'Alkylsilane',
                      # Terminal groups
                        terminal_group_1 = tg_1,
                        terminal_group_2 = tg_2,
                        terminal_group_3 = tg_3,
                      # Number of monolayer chains
                        n = 100,
                      # monolayer pattern type
                        pattern_type = 'random',
                      # Random seed
                        seed = random_seed*(replication_index + 1))
                    project.open_job(statepoint=the_statepoint).init()
                    statepoints.append(the_statepoint)
                    logging.info(msg="At the statepoint: {}".format(the_statepoint))
        
        for nitro_amino_comb in [['nitro', 'amino'], ['amino', 'nitro']]:
            the_statepoint = dict(
                      # Carbon backbone length
                        chainlength = chainlength,
                      # Backbone chemistry
                        backbone = 'Alkylsilane',
                      # Terminal groups
                        terminal_group_1 = nitro_amino_comb[0],
                        terminal_group_2 = nitro_amino_comb[1],
                        terminal_group_3 = 'amino',
                      # Number of monolayer chains
                        n = 100,
                      # monolayer pattern type
                        pattern_type = 'random',
                      # Random seed
                        seed = random_seed*(replication_index + 1))
            project.open_job(statepoint=the_statepoint).init()
            statepoints.append(the_statepoint)
            logging.info(msg="At the statepoint: {}".format(the_statepoint))
    # write statepoints to signac statepoint file
    project.write_statepoints(statepoints=statepoints)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Initialize the data space.")
    parser.add_argument(
        '-s','--seed',
        type=str,
        help="A string to generate a random seed.")
    parser.add_argument(
        '-n', '--num-replicas',
        type=int,
        default=1,
        help="Initialize multiple replications.")
    args = parser.parse_args()

    # Generate an integer from the random str.
    try:
        random_seed = int(args.seed)
    except ValueError:
        random_seed = int(sha1(args.random.encode()).hexdigest(), 16) % (10 ** 8)

    logging.info("Params:\
                random: {}\
                num-replicas: {}".format(
                                    random_seed,
                                    args.num_replicas,
                                    ))

    main(args, random_seed)
