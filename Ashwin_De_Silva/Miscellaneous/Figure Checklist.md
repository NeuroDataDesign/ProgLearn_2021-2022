# Figure Checklist 

The following note is based on an informative [article](https://bitsandbrains.io/2018/09/08/figures.html) by Dr. Joshua Vogelstein. It contains a comprehensive set of guidelines that would help one create impactful explanatory figures (including tables).

## Main Point 

* Most important property of a figure
* Know well about the main claim that you want to make and about the audience you are reaching.
* First step of making a figure

## Data to Ink Ratio

* Be sure to remove unnecessary, 
    * borders
    * gridlines
    * data markers
    * legends (label data directly)
    * excess dimensions

* If there's a way to reduce the cognitive effort for audience and still make the same claim, follow that way!

## Color

* clear and consistent color schemes.
    * [qualitative color scheme](https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=9) for mulitple lines
    * [diverging color scheme](https://colorbrewer2.org/#type=diverging&scheme=PRGn&n=11) for heatmaps
    * [blue](https://colorbrewer2.org/#type=sequential&scheme=Blues&n=9) or [orange](https://colorbrewer2.org/#type=sequential&scheme=Oranges&n=9) sequential color scheme for multiple lines changing a single variable

* Tip: if a given algorithm uses blue as its color in one figure, it should use blue for that algorithm in all other figures, and blue should not be used for anything else
* Use red to direct the audience to the proposed method.

## Title

* Provides context such as sample size, dimensionality, dataset/simulation name, etc.

## Axes

* Show the minimal possible number of numbers on the x- and y-axis
* Are the number of significant digits reasonable (eg, the number of significant digits cannot reasonably be larger than the sample size)?
* Axis labels should be words, not symbols, not abbreviations, so one need not read the caption to understand the figure.
* Are your axes ‘tight’?
* Is the aspect ratio correct?

## Caption

* Begin with a sentence stating what the figure is demonstrating 
* If there are panels, one sentence explains the collective take home message of all the panels.
* Define all acronyms used in the figure.
* End by pointing out particularly interesting aspects of the figure that one should note

## Lines and Markers

* If there are multiple lines/dots, is each a different line style and color?
* Are all lines sufficiently thick?
* Are the markers different?
* If errorbars make sense, are they there? If there, does the caption explain whether they are standard error?

## Aesthetics

* Use vector graphics 
* Reectify alignment issues
* If it’s a pie chart, can you replace it with a stacked barchart (or something else)?
* When you are comparing multiple approaches across multiple settings, group by the key comparison
* Is there enough whitespace?

## Multipanel Figures

* Remove redundant axes and labels
* Are the captions complete?

## Table

* Can it be converted to a figure? Put the table in appendix if there would be an information loss.
* Are the rows sorted reasonably?



