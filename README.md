# new-terminal-group-screening

### extension of https://github.com/daico007/TRUE-nanotribology.git,
### https://github.com/summeraz/monolayer_screening,
### https://github.com/summeraz/terminal_group_screening, and
### https://github.com/summeraz/terminal_groups_mixed

This signac project involves the molecular simulation of two functionalized monolayers shearing against one another at different normal loads (5, 15, and 25 nN), an amorphous silica surface, and different random seeds like the original study (__J.Chem.TheoryComput.2020, 16, 1779−1793__). A chain length of 17 carbons is used.

However, this project is an extension of the previous perojects in that is uses the following new terminal groups:
* amide
* biphenyl
* cyclohexyl
* dihydroxyphenyl
* formyl
* nitroso
* pentafluorophenyl
* sulfhydryl
* triazole
* benzoic acid
* isopropylbenzene

This workspace is meant to provide simulation data for these groups not screened previously, and not fed to the machine learning model. (https://github.com/daico007/tribology-machine-learning) Using this data, along with RDKit to determine the molecular descriptors, this will allow for the generalization ability of the random forest and neural networks to new data.

In this project, the 2422 monolayer systems being studied include:
* 11 single-terminal group monolayer systems, each using one of the new terminal groups.
* 110 two-terminal group systens with a new terminal group on monolayer A and a different new terminal group on monolayer B.
* 209 two-terminal group systems, each with monolayer A functionalized with one of the 11 new terminal groups and monolayer B funcionalized with one of the 19 old terminal groups.
* 2090 combinations of terminal group 1 on monolayer A as one of the new terminal groups, terminal group 2 on monolayer A as one of the old terminal groups, and one of the 10 following groups as terminal group 3 on monolayer B: carboxyl, fluorophenyl, hydroxyl, isopropyl, methyl,  nitro, perfluoromethyl, cyano, nitroso, and amide.
* The 2 combinations of nitro and amino groups on one monolayer with amino groups on the other monolayer, with nitro as terminal group 1 and amino as terminal group 2, and vice versa, to investigate whether these reult in different tribological properties (COF & intercept). According to grand-descriptors.csv, they are different, but they should be the same. 

Each monolayer system will be simulated at 3 normal loads, and each normal load will be simulated with 5 random seeds, for a total of 36,330 simulations! The coefficient of friction and adhesive force for each normal load will be calculated by averaging the values from each random seed, and linear regression is used to determine the COF and F0 for each system.
