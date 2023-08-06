# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plannerbenchmark',
 'plannerbenchmark.exec',
 'plannerbenchmark.generic',
 'plannerbenchmark.planner',
 'plannerbenchmark.planner.acadosMpc',
 'plannerbenchmark.planner.acadosMpc.models',
 'plannerbenchmark.planner.forcesProMpc',
 'plannerbenchmark.postProcessing',
 'plannerbenchmark.ros',
 'plannerbenchmark.tests']

package_data = \
{'': ['*'],
 'plannerbenchmark': ['assets/*',
                      'assets/meshes/collision/*',
                      'assets/meshes/visual/*'],
 'plannerbenchmark.planner.forcesProMpc': ['solverCollection/.gitignore'],
 'plannerbenchmark.postProcessing': ['plottingAlbert/*',
                                     'plottingGroundRobot/*',
                                     'plottingPanda/*',
                                     'plottingPanda/results/fabric_20220223_102405/plots/*',
                                     'plottingPlanarArm/*',
                                     'plottingPointMass/*',
                                     'plottingPointMassUrdf/*',
                                     'plottingSeries/*'],
 'plannerbenchmark.tests': ['cases/pdplanner_pointMass/default_result/*',
                            'cases/pdplanner_pointMass/setup/*',
                            'cases/pdplanner_pointMass_2/default_result/*',
                            'cases/pdplanner_pointMass_2/default_result/plots/*',
                            'cases/pdplanner_pointMass_2/setup/*',
                            'local_cases/fabric_panda/default_result/*',
                            'local_cases/fabric_panda/setup/*',
                            'local_cases/fabric_panda_dynamic/default_result/*',
                            'local_cases/fabric_panda_dynamic/setup/*',
                            'local_cases/fabric_planarArm/default_result/*',
                            'local_cases/fabric_planarArm/setup/*',
                            'local_cases/fabric_pointMass/default_result/*',
                            'local_cases/fabric_pointMass/setup/*',
                            'local_cases/mpc_panda/default_result/*',
                            'local_cases/mpc_panda/setup/*',
                            'local_cases/mpc_planarArm/default_result/*',
                            'local_cases/mpc_planarArm/setup/*',
                            'local_cases/mpc_pointMass/default_result/*',
                            'local_cases/mpc_pointMass/setup/*']}

install_requires = \
['forwardkinematics>=1.1.1,<2.0.0', 'urdfenvs>=0.7.1,<0.8.0']

extras_require = \
{'fabric': ['fabrics>=0.6.2,<0.7.0'], 'mpc': ['robotmpcs>=0.2.1,<0.3.0']}

entry_points = \
{'console_scripts': ['post_process = plannerbenchmark.exec.post_processor:main',
                     'runner = plannerbenchmark.exec.runner:main']}

setup_kwargs = {
    'name': 'plannerbenchmark',
    'version': '1.1.0',
    'description': 'Benchmark suite for local planner in dynamic environments. Multiple planners can be compared on different kinematic chains in different environment. The suite is highly extendable for new planners, robots and environments.',
    'long_description': 'Local Motion Planning Benchmark Suite\n=====================================\n\nThis repository is meant to allow quick comparison between different\nlocal motion planning algorithms. Running and postprocessing is\navailable and we aim to offer a nice interface to implement a wrapper to\nyour own motion planner.\n\nScreenshots\n-----------\n\n<table>\n <tr>\n  <td> Trajectory planar arm</td>\n  <td> Trajectory point robot</td>\n  <td> Simulation panda arm</td>\n </tr>\n <tr>\n  <td> <img src="docs/source/img/trajectory_planar_arm.png" width="250"/> </td>\n  <td> <img src="docs/source/img/trajectory_point_robot.png" width="250"/> </td>  \n  <td> <img src="docs/source/img/trajectory_panda.gif" width="250"/> </td>  \n </tr>\n</table>\n<table>\n <tr>\n  <td> Evaluation of series</td>\n </tr>\n <tr>\n  <td> <img src="docs/source/img/results_comparison.png" width="500"/> </td>\n </tr>\n</table>\n\nGetting started\n===============\n\nThis is the guide to quickly get going with the local motion planning\nbenchmark suite.\n\nPre-requisites\n--------------\n\n-   Linux Ubuntu LTS &gt;= 18.04\n-   Python &gt;3.6, &lt; 3.10\n-   pip3\n-   gnuplot (`sudo apt install gnuplot`)\n-   \\[Optional\\] [poetry](https://python-poetry.org/docs/)\n-   \\[Optional\\] [embotech forces\n    pro](https://www.embotech.com/products/forcespro/overview/) for mpc\n-   \\[Optional\\] [acados_template](https://github.com/acados/acados/tree/master/interfaces/acados_template) for mpc\n\nInstallation\n------------\n\nYou first have to download the repository\n\n``` {.sourceCode .bash}\ngit clone git@github.com:maxspahn/localPlannerBench.git\n```\n\nThen, you can install the package using pip as:\n\n``` {.sourceCode .bash}\npip3 install .\n```\n\nOptional: Installation with poetry\n----------------------------------\n\nIf you want to use [poetry](https://python-poetry.org/docs/), you have\nto install it first. See their webpage for instructions\n[docs](https://python-poetry.org/docs/). Once poetry is installed, you\ncan install the virtual environment with the following commands. Note\nthat during the first installation `poetry update` takes up to 300 secs.\n\n``` {.sourceCode .bash}\npoetry update\npoetry install\n```\n\nThe virtual environment is entered by\n\n``` {.sourceCode .bash}\npoetry shell\n```\n\nTutorial\n--------\n\n### Simple\n\nThe following is a very simple example case containing a point mass robot and a PD planner.\n\nRun an experiments:\n\nExperiments should be added in separate folder in `examples`. One\nvery simple example can be found in this folder. Note that you need to\nactive your poetry shell if you have installed the package using poetry\nby\n\n``` {.sourceCode .bash}\npoetry shell\n```\n\n> Or alternatively active your virtual python environment\n\nThen you navigate there by\n\n``` {.sourceCode .bash}\ncd examples/point_robot\n```\n\nThen the experiment is run with the command line interface\n\n``` {.sourceCode .bash}\nrunner -c setup/exp.yaml -p setup/pdplanner.yaml --render\n```\n\nPostprocessing:\n\nThe experiments can be postprocessed using the provide executable. Again make sure you are in the virtual environment, when\nusing poetry run: \n(`poetry shell`)\n\n``` {.sourceCode .bash}\ncd examples/point_robot\n```\n\nThe you can run the post processor with arguments as\n\n``` {.sourceCode .bash}\npost_process --exp path/to/experiment -k time2Goal pathLength --plot\n```\n\n![Example trajectory](docs/source/img/trajectory_point_robot.png)\n\n### Advanced\n\nTo showcase the power of localPlannerBench we would also like to show you a more complex example, containing the 7-DoF frankaemika panda robot arm and a custom opensource [acados](https://github.com/acados/acados) based MPC planner.\n\nAgain make sure you are in your virtual python environment.\n``` {.sourceCode .bash}\npoetry shell\n```\n\nInstall [acados_template](https://github.com/acados/acados/tree/master/interfaces/acados_template) inside of the virtual environment if you haven\'t already.\n\nThen you navigate to \n\n``` {.sourceCode .bash}\ncd examples/panda_arm\n```\n\nThen the experiment is run with the command line interface\n\n``` {.sourceCode .bash}\nrunner -c setup/exp.yaml -p setup/acados_mpc.yaml --render\n```\n\n<img src="docs/source/img/panda_arm_acados_mpc.gif" width="70%"/>\n\nThe you can run the post processor with arguments as\n\n``` {.sourceCode .bash}\npost_process --exp results --latest -k time2Goal pathLength --plot\n```\n\n![Example trajectory](docs/source/img/trajectory_panda_acados_mpc.png)\n\n\n',
    'author': 'Max Spahn',
    'author_email': 'm.spahn@tudelft.nl',
    'maintainer': 'Max Spahn',
    'maintainer_email': 'm.spahn@tudelft.nl',
    'url': 'https://maxspahn.github.io/localPlannerBench/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
