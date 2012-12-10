"""
Copyright (C) 2012 Raniere Silva <ra092767@ime.unicamp.br>

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import sys

def get_info():
    """
    Get Information from the site.
    """
    from subprocess import call
    call("./get_files.sh", shell=True)

def _w2f():
    """
    Write To File

    This function wait the user input the name of the wanted file for output.
    """
    print("Choose the name of the file where the output will be write.")
    tmp = input("Default is stdout:")
    return tmp
    
def _tof():
    """
    Type of problem Objective Function

    This function wait the uset input the wanted type of objective
    function.
    """
    print("Choose the type of the problem objective function.\n")
    print("\tN - no objective function is defined,")
    print("\tC - the objective function is constant,")
    print("\tL - the objective function is linear,")
    print("\tQ - the objective function is quadratic,")
    print("\tS - the objective function is a sum of squares,")
    print("\tO - the objective function is none of the above.\n")
    tmp = input("Default 'NCLQSO':")
    if not tmp:
        tmp = 'NCLQSO'
    return tmp

def _tc():
    """
    Type of Constraints of the problem

    This function wait the uset input the wanted type of constraints of the
    problem.
    """
    print("Choose the type of constraints of the problem.\n")
    print("\tU - the problem is unconstrained,")
    print("\tX - the problem's only constraints are fixed variables,")
    print("\tB - the problem's only constraints are bounds on the variables,")
    print("\tN - the problem's constraints represent the adjacency matrix of a (linear) network,")
    print("\tL - the problem's constraints are linear,")
    print("\tQ - the problem's constraints are quadratic,")
    print("\tO - the problem's constraints are more general than any of the above alone.\n")
    tmp = input("Default 'UXBNLQO':")
    if not tmp:
        tmp = 'NCLQSO'
    return tmp

def _ts():
    """
    Type of the Smoothness of the problem.

    This function wait the user input the wanted type of smoothness.
    """
    print("Choose the smoothness of the problem.\n")
    print("\tR - the problem is regular, that is its first and second "
    "derivatives exist and are continuous everywhere, or")
    print("\tI - the problem is irregular.\n")
    tmp = input("Default 'RI':")
    if not tmp:
        tmp = 'RI'
    return tmp

def _dhd():
    """
    Degree of the Highest Derivatives

    This function wait the user input the degree of the highest
    derivatives provided analytically.
    """
    print("Choose the degree of the highest derivatives provided "
    "analytically within the problem description. It is restricted to being "
    "0, 1 or 2.\n")
    tmp = input("Default '012':")
    if not tmp:
        tmp = '012'
    return tmp

def _torigin():
    """
    Type of Origin of the problem

    This function wait the user input the wanted type of origin of the problem.
    """
    print("Choose the primary origin and/or interest of the problem.\n")
    print("\tA - the problem is academic, that is, has been constructed "
    "specifically by researchers to test one or more algorithms,")
    print("\tM - the problem is part of a modelling exercise where the actual "
    "value of the solution is not used in a genuine practical "
    "application,")
    print("\tR the problem's solution is (or has been) actually used in a real "
    "application for purposes other than testing algorithms.\n")
    tmp = input("Default 'AMR':")
    if not tmp:
        tmp = 'ARM'
    return tmp

def _eiv():
    """
    Explicit Internal Variable

    This function wait the user input the wanted the configuration for the
    explicit internal variables.
    """
    print("Choose if the problem description contains explicit internal "
    "variables or not.\n")
    print("\tY - the problem description contains explicit internal "
    "variables,")
    print("\tN - the problem description does not contain any explicit internal "
    "variables.")
    tmp = input("Default 'YN':")
    if not tmp:
        tmp = 'YN'
    return tmp
 
def interact():
    print("Py-CUTEr-Problem-Chooser Copyright (C) 2012 Raniere Silva")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions; type `show c' for details.\n")

    w2f = _w2f()
    tof = _tof()
    tc = _tc()
    ts = _ts()
    dhd = _dhd()
    torigin = _torigin()
    eiv = _eiv()

    classification(tof, tc, ts, dhd, torigin, eiv)

def classification(tof='NCLQSO', tc='UXBNLQO', ts='RI', dhd='012',
        torigin='ARM', eiv='YN', w2f=''):
    # get_info()
    f_name = open('CUTEr_problems')
    f_clas = open('CUTEr_classification')
    if w2f:
        f_out = open(w2f, 'w')

    for p in f_name:
        choosed = True
        p_clas = f_clas.readline()
        p_clas = p_clas.split('-')
        if p_clas[0][0] not in tof:
            choosed = False
        elif p_clas[0][1] not in tc:
            choosed = False
        elif p_clas[0][2] not in ts:
            choosed = False
        elif p_clas[0][3] not in dhd:
            choosed = False
        elif p_clas[1][0] not in torigin:
            choosed = False
        elif p_clas[1][1] not in eiv:
            choosed = False
        if choosed:
            if w2f:
                f_out.write('{0}\n'.format(p.rstrip()))
            else:
                print('{0}'.format(p.rstrip()))

    f_name.close()
    f_clas.close()
    if w2f:
        f_out.close()

if __name__ == "__main__":
    """Call the classification from the command line interpreter. ::

        $ python classification.py --help
    """
    import argparse
    from argparse import RawTextHelpFormatter

    if sys.version_info[0] < 3:
        raise Exception('It require Python 3.0 or later.')

    # Parse of flags.
    parser = argparse.ArgumentParser(description='Choose problems from CUTer.',
            formatter_class=RawTextHelpFormatter)
    parser.add_argument('-i', action='store_true',
            help='start interact mode.')
    parser.add_argument('-f', type=str, default='',
            help='Specify the file where the output will be write.')
    parser.add_argument('-tof', type=str, default='NCLQSO',
            help="Select type of objective function. Default is 'NCLQSO'.\n"
            "N - no objective function is defined,\n"
            "C - the objective function is constant,\n"
            "L - the objective function is linear,\n"
            "Q - the objective function is quadratic,\n"
            "S - the objective function is a sum of squares,\n"
            "O - the objective function is none of the above.\n")
    parser.add_argument('-tc', type=str, default='UXBLQO',
            help="Select the type of constraints of the problem. Default is 'UXBLQO'.\n"
            "U - the problem is unconstrained,\n"
            "X - the problem's only constraints are fixed variables,\n"
            "B - the problem's only constraints are bounds on the variables,\n"
            "N - the problem's constraints represent the adjacency matrix of a (linear) network,\n"
            "L - the problem's constraints are linear,\n"
            "Q - the problem's constraints are quadratic,\n"
            "O - the problem's constraints are more general than any of the above alone.\n")
    parser.add_argument('-ts', type=str, default='RI',
            help="Select the smoothness of the problem. Default is 'RI'\n"
            "R - the problem is regular, that is its first and second "
            "derivatives exist and are continuous everywhere, or\n"
            "I - the problem is irregular.\n")
    parser.add_argument('-dhd', type=str, default='012',
            help="Select the degree of the highest derivatives provided "
    "analytically within the problem description. It is restricted to being "
    "0, 1 or 2.\n")
    parser.add_argument('-to', type=str, default='AMR',
            help="Select the primary origin and/or interest of the problem.\n"
            "A - the problem is academic, that is, has been constructed "
            "specifically by researchers to test one or more algorithms,\n"
            "M - the problem is part of a modelling exercise where the actual "
            "value of the solution is not used in a genuine practical "
            "application,\n"
            "R the problem's solution is (or has been) actually used in a real "
            "application for purposes other than testing algorithms.\n")
    parser.add_argument('-eiv', type=str, default='YN',
            help="Select if the problem description contains explicit internal "
            "variables or not.\n"
            "Y - the problem description contains explicit internal "
            "variables,\n"
            "N - the problem description does not contain any explicit internal "
            "variables.")

    args = parser.parse_args()

    if args.i:
        interact()
    else:
        classification(args.tof, args.tc, args.ts, args.dhd, args.to,
                args.eiv, args.f)
