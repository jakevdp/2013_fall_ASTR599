Introduction to Scientific Computing in Python
==============================================

- Course Number: ASTR 599, Fall 2013
- Instructor: Jake Vanderplas
- Room: PAB 356
- Credits: 1 credit, pass/fail

ASTR 599 is an introduction to the concepts of scientific computing using the
Python programming language, and the Scipy ecosystem, including NumPy, SciPy,
Matplotlib, IPython, and other related packages.  

Course Goals
------------
This course is aimed at incoming graduate students who have some experience
with computers, but who are not necessarily familiar with the Python
programming language.  We will assume that before starting the course, 
students have some experience with:

- using the terminal for simple tasks (i.e. you should be familiar with
  ``ls``, ``cd``, ``pwd``, ``mv``, and other basic shell commands)
- writing simple scripts in a modern programming language such as Python,
  IDL, MatLab, Mathematica, C, Fortran, etc. (i.e. you should be familiar
  with variables, functions, for loops, while loops, and if-else statements
  in some language, not necessarily Python)

Students who don't meet this basic background are encouraged to spend some
time preparing for the course.  A basic shell tutorial can be found
[here](http://www.freeos.com/guides/lsst/), while list of basic Python
programming tutorial for a non-programmer can be found
[here](http://learnpythonthehardway.org/book/)

By the end of the course, students will have seen experience with many more
advanced techniques which are vital to effective scientific research,
including but not limited to:

- The basic syntax and use of Python as a scientific tool, including writing
  and executing scripts to automate common tasks, using the IPython
  interpreter for interactive exploration of data and code, and using the
  IPython notebook to share and collaborate.
- Loading data from a variety of common astronomical formats.
- Manipulating data efficiently with NumPy.
- Visualizing data with Matplotlib.
- Performing more sophisticated data mining and machine learning analysis
  with Scipy and Scikit-learn.
- Tracking changes and collaborating with [Git](http://git-scm.com/).
- Emphasis on how to use documentation and online resources to learn more.

By the end of the quarter, a student with little experience in computational
research will be equipped to start working in any area of Astronomical
research, whether the emphasis is observational or theoretical.  While there
is no way a single quarter class can provide every student experience with
all the computing tools they will encounter in grad school, this course will
lay a firm foundation from which new tools and techniques can be explored.


Credit and Grading
------------------
The seminar portion of this course is available for 1 pass/fail credit.
In order to receive a pass, students must do the following:

- Attend at least six of the nine weekly class meetings.
- Turn in at least six of the nine weekly programming assignments.

### Assignments
The assignments each week will be a chance to go deeper in the subject we 
cover each week, and to highlight coding practices that are useful for 
astronomical research.  They are designed to take between one and two hours
for a typical student with the background described above, though those with
more experience will likely be able to finish much more quickly.

Course Schedule
---------------
The course will consist of a two-day intensive bootcamp before the start
of the quarter, followed by a weekly seminar during the fall term
where more advanced material will be discussed in-depth.  The boot
camp will be very hands-on and driven by short and long exercises where the
concepts will be applied to programming puzzles as well as basic research
problems.

**Note: the following is still in draft form, and will likely be extensively
modified before the course starts.**

### Boot Camp Day 1
- 9:00am - 10:00am : Intro: What is Python and why learn it?

  + Origins & features of Python.

  + Why Python?  Some motivating examples.
 
  + The built-in Python interpreter: Python as a calculator

  + Stand-alone scripts: Python to automate common tasks

  + The IPython interpreter: interactive Python development

  + The IPython notebook: sharing and collaborating on research

- 10:00am - 11:00am : Basic Training: Types, Variables, Calculations, and Flow

  + Example script: extracting data from a csv file

  + Simple types & variables: integers, floats, complex, characters.

  + Compound types and other objects: strings, lists, sets, dicts, file objects

  + functions and methods: string & list manipulation

- 11:00am - noon : Controlling the flow of a program

  + user-defined functions

  + if-else statements

  + for loops and while loops

  + try...except statements

- noon - 1pm : **Lunch Break**

- 1pm - 3pm : Introduction to version control with Git

- 3pm - 4pm : Setting up a git repository for this class.


## Boot Camp Day 2

- 9:00 am - 11:00 am : NumPy -- introduction to importing, storing and manipulating data

- 11:00 am - noon    : NumPy -- best practices for efficient computation

- noon - 1pm : **Lunch Break**

- 1:00pm - 2:30pm : matplotlib -- data visualization

  + line plots, scatter plots, contour plots, images
  + 3D plots
  + multiple axes & figures
  + animations?

- 2:30pm - 4:00pm : SciPy -- broad overview of available tools

  + special functions
  + linear algebra
  + optimization/minimization
  + integration
  + sparse matrices


## Weekly Seminar

- Mon. Sept 30, 3:00-4:00: TBA

- Mon, Oct 7, 3:00-4:00: TBA

- Mon, Oct 14, 3:00-4:00: optimization and minimization (Andy Becker)

- Mon, Oct 21, 3:00-4:00: pyfits & astronomy data formats (Oliver Frasier)

- Mon, Oct 28, 3:00-4:00: TBA

- Mon, Nov 4, 3:00-4:00: TBA

- Mon, Nov 11: **Veteran's Day (no class)**

- Mon, Nov 18, 3:00-4:00: TBA

- Mon, Nov 25, 3:00-4:00: TBA

- Mon, Dec 2, 3:00-4:00: TBA



## Notes

*Potential topics to cover... not scheduled just yet:*

- Optimization and Minimization in Scipy
- Wrapping legacy code: Python C-API & cython
- Cython for writing fast numerical code
- Linear algebra
- Scikit-learn/machine learning
- astroML/datasets and visualization ideas
- PYFITS and astro-specific tools
- Advanced python: iterators, generator expressions, decorators, context managers
- Advanced python: OO computing, classes & modules
- Debugging
- unit-testing with nose (test-driven development)
- Sparse matrix manipulation
- IPython notebook in depth (including sympy)

*Dataset ideas*

- near-earth asteroids
- automated clustering on the CMD
- Spectra PCA (svd/linear algebra)
- class implementing basic cosmology computations