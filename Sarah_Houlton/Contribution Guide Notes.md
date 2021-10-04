[Contribution Guide Notes](https://proglearn.neurodata.io/contributing.html)

# Bug report
* verify it's not covered by another issue
* follow basic github guidelines
# Good bug report
* short, reproducible code snippet
  * < 50 lines
* specific about classes, fns involved and the shape of the data
* provide traceback
* include os and version number, as well as python and proglearn versions
* format well
# Contributing code
* fork the project repo
* clone your fork
* create a feature branch
  * use feature branch forked from staging
* develop feature on this branch, git add and git commit
* push to your github account
# Pull request checklist
* follow coding guidelines
* give pull request a title that summarizes what it does
  * sometimes fix #issue is enough, sometimes not
* public methods need informative docstrings w/ sample usage
* at least a paragraph of narrative docs, w/ links to literature and the example
* all fn/classes must have unit tests
  * at least type checking and ensuring correct computation/outputs
* pytest to check that all tests are passing locally
* run black autoformatter
* pr into staging
  * link relevant issues
  * summarize pr
  * use format in guide to comment on pr
# Coding guidelines
* closely follows [PEP8](https://www.python.org/dev/peps/pep-0008/)
# Docstring guidelines
* reuired for documentation by Sphinx
* follow this [guide](https://numpydoc.readthedocs.io/en/latest/format.html#overview)
# Tutorial guidelines
* add notebook name to docs/tutorials.rst
* organize local fns into separate file and put in docs/tutorials/functions
* make tutorial self-contained
  * should not need input or produce output
* format first line with # at front and make it the one and only informative title
* format subtitles w/ ## at front
* minimize cell outputs
*  avoid unnecessary prints
*  remove all empty cells
*  check the netlify deployment preview  
