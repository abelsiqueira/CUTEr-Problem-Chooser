C     ******************************************************************
C     ******************************************************************
C
C     This program filters the problems of CUTEr collection. For 
C     achieving this objective YOU MUST MODIFY it according to the type 
C     of problems you want to select. See below where your modifications
C     must be inserted. The program returns a text file called my_problems 
C     containing the names of filtered problems. 
C
C     See http://www.cuter.rl.ac.uk/Problems/classification.shtml for 
C     a complete explanation of the CUTE classification scheme.
C
C     For use this routine you must have a text file called CUTEr_problems
C     with the names of all problems (line by line), and other text file
C     called CUTEr_classification with the classifications of all problems
C     (line by line). You can get this information on the website 
C     http://www.cuter.rl.ac.uk/Problems/mastsif.shtml
C     A simple way is to copy all the table with name, files available
C     and CUTEr classification, paste into a xlsx file and extract the 
C     required information by copying and pasting the first and third
C     columns.
C
C     Author: Leandro Prudente
C     e-mail: lfprudente@gmail.com
C     Date:   12/03/2012 
C
C     If you find any error, please contact me by e-mail.
C

      program CUTEr_classification
      
      implicit none
      
      character(1) objective, constraint, smooth, origin, 
     +             eivariable
      character(8) problem, numvariable, numconstraint
      character(30) classification
      integer derivative, hifen, nvariable, nconstraint, nproblem,
     +        end_file
      logical fixnumvar, fixnumconst
      
C     Variables of the program:
C
C     The possible values of the variables follow the CUTE classification
C     scheme.
C     
C     objective    character, contains the type of the problem objective
C                  function. Possible values are:
C                  N no objective function is defined,
C                  C the objective function is constant,
C                  L the objective function is linear,
C                  Q the objective function is quadratic,
C                  S the objective function is a sum of squares, and
C                  O the objective function is none of the above. 
C
C     constraint   character, contains the type of constraints of the 
C                  problem. Possible values are:
C                  U the problem is unconstrained,
C                  X the problem's only constraints are fixed variables,
C                  B the problem's only constraints are bounds on the 
C                    variables,
C                  N the problem's constraints represent the adjacency 
C                    matrix of a (linear) network,
C                  L the problem's constraints are linear,
C                  Q the problem's constraints are quadratic, and
C                  O the problem's constraints are more general than any
C                    of the above alone.
C
C     smooth       character, indicates the smoothness of the problem. 
C                  There are two choices:
C                  R the problem is regular, that is its first and second
C                    derivatives exist and are continuous everywhere, or
C                  I the problem is irregular.
C
C     derivative,  integer, indicates the degree of the highest derivatives
C                  provided analytically within the problem description.
C                  It is restricted to be 0, 1 or 2.
C
C     origin,      character,  indicates the primary origin and/or interest
C                  of the problem. Possible values are:
C                  A the problem is academic, that is, has been constructed
C                    specifically by researchers to test one or more 
C                    algorithms,
C                  M the problem is part of a modelling exercise where the
C                    actual value of the solution is not used in a genuine
C                    practical application, and
C                  R the problem's solution is (or has been) actually used
C                    in a real application for purposes other than testing
C                    algorithms.
C
C     eivariable,  character, ndicates whether or not the problem 
C                  description contains explicit internal variables. 
C                  There are two possible values, namely
C                  Y the problem description contains explicit internal 
C                    variables, or
C                  N the problem description does not contain any explicit
C                    internal variables. 
C
C     nvariable,   integer, see below.
C
C     nconstraint, integer, see below.
C
C     fixnumvar,   logical, 
C                  true the number of variables in the problem is fixed
C                        and is available in nvariable,
C                  false the number of variables in the problem can be 
C                         chosen by the user.
C
C     fixnumconst, logical,
C                  true  the number of constraints in the problem is fixed
C                        and is available in nconstraint.
C                  false the number of constraints in the problem can be 
C                        chosen by the user
C
      
      open(10,file='CUTEr_problems')
      open(20,file='CUTEr_classification')
      open(30,file='my_problems')
      
      nproblem = 0

 100  continue
      
          read(10,'(A8)', iostat = end_file) problem
          
          if ( end_file .ne. 0 ) stop
          
          nproblem = nproblem + 1
          
          read(20,'(A30)')classification
          
          objective  = classification(1:1)
          constraint = classification(2:2)
          smooth     = classification(3:3)
          read(classification(4:4),*) derivative
          origin     = classification(6:6)
          eivariable = classification(7:7)
          
          hifen = scan(classification,'-',back = .true.)
          
          numvariable   = classification(9:hifen-1)
          numconstraint = classification(hifen+1:30)
          
          if ( scan(numvariable,'V') .eq. 0 ) then 
              fixnumvar = .true.
              read(numvariable,*) nvariable
          else
              fixnumvar = .false.
          end if
          
          if ( scan(numconstraint,'V') .eq. 0 ) then 
              fixnumconst = .true.
              read(numconstraint,*) nconstraint
          else
              fixnumconst = .false.
          end if
          
C     ******************************************************************
C     FROM HERE ON YOU MUST MODIFY THE PROGRAM TO SELECT THE PROBLEMS 
C     ACCORDING TO YOUR DESIRE.
C     ******************************************************************

C     In this exemple we will select the problems with linear or quadratic
C     objective function and constraints and with at least ten variables 
C     (or the problems for wich we can choose the number of variables).

      if ( ( scan(objective,'LQ') .ne. 0 ) .and.  
     +     ( scan(constraint,'LQ') .ne. 0 ) ) then
          if ( .not. fixnumvar ) then
              write(30,'(A8)') problem
          else if ( nvariable .ge. 10 ) then
              write(30,'(A8)') problem
          end if            
      end if
          
C     ******************************************************************
C     STOP HERE YOUR MODIFICATIONS.
C     ******************************************************************          
      
      go to 100
    
      end program
