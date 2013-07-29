Astronomy 599: Introduction to Scientific Computing in Python
=============================================================

**Jake Vanderplas**

**University of Washington**

**Fall, 2013**

This repository will contain all the curriculum and materials for the Astronomy 599 seminar, Fall 2013.

Instructor
----------
[Jake Vanderplas](http://www.astro.washington.edu/vanderplas) is an NSF post-doctoral fellow at UW working
jointly between the Computer Science department's [Database Research Group](http://db.cs.washington.edu/) and
the Astronomy department's [Survey Science Group](http://ssg.astro.washington.edu/).  He received his PhD in
Astronomy from the University of Washington in 2012.  He is active in the open-source Scientific Python
community, and actively contributes to and helps maintain several of the core packages in the SciPy ecosystem.

Class Location
---------------
[PAB](http://uw.edu/maps/?pab) 356 / 356A

Meeting times
-------------
- Two-day “Boot Camp”: September 19-20 / 23-24 9:00am-4:00pm (dates TBD)
- Weekly meetings: Mondays, 3:00-4:00pm throughout Fall quarter

Broad Description
-----------------
This graduate seminar course will offer a comprehensive introduction to scientific computing in Python, geared 
toward students and researchers in Astronomy.  The course is aimed at those who already have some familiarity 
with computational tools and programming languages -- i.e. who know what a terminal is and how to use it, and 
are familiar with basic programming concepts such as for loops and if-else statements -- though it will assume 
no familiarity with the Python programming language.

The two-day boot camp in the days before the start of the quarter will begin with a broad introduction to the 
basic syntax of Python: data types and operations, loops and conditionals, input and output of data, and basic 
object-oriented programming.  From that base, we will move on to a broad overview of the main computing tools 
of scientific computing in Python: IPython for an interactive computing environment, NumPy for handling of 
array-based data, Matplotlib for visualization of this data, and Scipy for common tasks such as integration, 
interpolation, optimization, and linear algebra.  In addition to this, we will introduce the use of Git, a 
distributed version control system, which we will be using throughout the quarter to keep track of code and 
assignments.

The hour-long seminar slots each week during the quarter will build upon the knowledge-base covered in the 
boot camp, and introduce more advanced Python tools such as Scikit-learn for machine learning and data mining, 
Scikit-image for pixel-level data processing, SymPy for symbolic mathematics, IPython for parallel processing, 
Cython for writing fast algorithms, and much more.  Each week will include a short 1-2 hour take-home assignment 
aimed at reinforcing the concepts covered during class.  The assignments will focus on tasks that will be useful 
in the day-to-day work of astronomical research.

While the course is designed for graduate students who are in their first year or two of research, it is also
open to any faculty, researchers or others who would like to brush-up on their Python skills.  Upper-level
undergraduates and students from other departments will also be considered on a case-by-case basis.  For
more information, please email jakevdp@cs.washington.edu


Prerequisites: Setting up your Computer
---------------------------------------
This will be a hands-on course, so it's vital that you come with a computer
set up to use Python.

### System Setup
The instructions below assume you have access to a bash/csh shell.  If you're
on Mac or Linux, this is easy: just open a terminal and you have it.  If
you're on windows, this is much harder.  Windows has a shell available, but
it's not nearly as powerful as the bash/csh shell on Linux and Mac.  Working
with most scientific software is a pain on Windows: the best option is
probably to install a dual-boot Linux system or a linux virtual machine.
This is not reflective of any anti-windows bias on my own part: it's simply
a reflection of the fact that in general, the scientific tools you'll use
in your research career will be very difficult to use on Windows.

Another option is to sign-up for the free web-based [wakari](http://wakari.io/)
service.  It's a browser-based scientific computing environment that lets
you run all the things you'll need on a cloud-based computer.  It's not quite
as nice as having everything running locally, but it's a good option.

### Make Sure Git is installed
When you have your terminal up and running, make sure you have installed the
[git](http://git-scm.com/) version management system.  You can check if it's
already installed on your system by typing at the command-line
```
$ git --version
```
Version 1.6 or better should be sufficient.

### Clone this repository
When you have git installed, please clone this repository.  You can do this
by navigating to the directory you'd like to use, and typing
```
$ git clone https://github.com/jakevdp/2013_fall_ASTR599.git
```
for HTTP, or for SSH
```
$ git clone git@github.com:jakevdp/2013_fall_ASTR599.git
```
This will create a directory ``2013_fall_ASTR599``.

### Check your Python install
For your Python installation, I recommend using
[Anaconda](https://store.continuum.io/], a free all-in-one Python installer
for Windows, Mac, and Linux.  It contains up-to-date versions of all the
packages we will use in this course.  Even if you have a local Python
installation on your laptop, installing Anaconda can make your life easier.

Note that after installing Anaconda, you should type
```
$ which python
```
and make sure it points to the anaconda version of the Python program.  If
not, you'll have to adjust your ``$PATH`` variable to point to this version.

Once you have Python installed, you can use the script provided
in this repository to check the versions of the various packages.
In the ``scripts`` subdirectory of ``2013_fall_ASTR599``, there is a script
called ``check_installation.py``.  This will check the versions of various
Python packages you have installed on your system.  At the command line, type
```
$ cd 2013_fall_ASTR599/scripts
$ python check_installation.py
```
If you get any warnings, you should either upgrade those packages yourself, or
switch to an Anaconda build.

### Check IPython notebook
We'll be making use of IPython notebook, a browser-based Interactive
Development Environment (IDE) for Python.  To make sure it's set up, type
```
$ ipython notebook
```
A browser window should open to your IPython dashboard.  If it doesn't, I'd
recommend installing Anaconda Python; this comes equipped with everything
you need for IPython notebook.

### Text Editor
The last thing you'll need is a good text editor.  This should not be a word
processor, but a program that lets you write simple text files.  Preferably
it should also have syntax highlighting for code.  Something simple like
``gedit`` or ``textmate`` is fine.  Many people like ``emacs``, ``vim``, and
other more powerful options.  Find one that works for you and make sure you
can create, edit, and save text files.