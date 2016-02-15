---
layout: post
subtitle: null
date: "2016-02-15"
published: false
title: "Review of Hadley Wickham's R Master Developer Course"
---

## Review of Hadley Wickham's R Master Developer Course

I had the privilege of attending Hadley's [Master R developer course](http://www.eventbrite.com/e/master-r-developer-workshop-san-francisco-tickets-13388329855) a few weeks ago. It was two days packed full of great knowledge that is a great stepping stone that will give a beginner/intermediate R programmer to the tools they need to go to the next level. I learned R back in my undergrad days in Berkeley through a course called [Stat 133](http://www.stat.berkeley.edu/~s133/). Professionally though I haven't used R extensively until I started working at [Payoff](https://www.payoff.com/). 

## Day 1
Day 1 was mostly about functions, functional programming and R's object-oriented 
programming interface. Hadley's rule of thumb is if you find yourself copy-pasting 3 or more times, you should write a function. Functions should be do one thing and do that one thing well. One somewhat mind-blowing learning was you can write functions that return a function aka "function factories." 
![Screen Shot 2016-02-15 at 3.07.28 PM.png]({{site.baseurl}}/img/Screen Shot 2016-02-15 at 3.07.28 PM.png)

## Day 2
Day 2 was all about package development. Like many of the things that Hadley has touched, he has streamlined and made life much easier for the would-be future R developer. His packages devtools and roxygen2 hide many of the pain points and difficulties that normally come with navigating package development.  He broke down the package development process in a few steps:
1. R\
  - Use devtools::create("PACKAGE_NAME") as a first step - automates many things for you
  - Use a style guide - http://r-pkgs.had.co.nz/r.html#style  
  - Do not intermingle side-effects and computation. Common functions that have side effects are anything related to plotting or printing and also source() and library().
2. DESCRIPTION
  - R description file. See an example [here](https://github.com/hadley/dplyr/blob/master/DESCRIPTION). What actually gets rendered on a packages' index.html page on CRAN, e.g. https://cran.r-project.org/web/packages/dplyr/index.html
  - License
  - Imports - need these packages to run
  - Suggests - packages that are nice to have but not critical for this package to run
  - Depends - deprecated, don't use
3. MAN - Hadley went through using his roxygen2 package that takes special R comments and turns them into Rd files which then get rendered as HTML. See his book for more info on this topic: http://r-pkgs.had.co.nz/man.html
4. Vignettes - Basically longform documentation. Helps would-be users of your package understand WHY they would use it. 
5. Tests - Automated tests that are run to check for errors. One key tip: when you fix a bug, write a unit test so that you can be sure this bug never returns. Hadley went over his testthat package. More here: http://r-pkgs.had.co.nz/tests.html
6. NAMESPACE - controls which files are available internally (for use within the package) or externally (for use by others).
7. Release - He went over the joys of going through submitting your package to CRAN which involves passing R CMD check without any errors. http://r-pkgs.had.co.nz/check.html


The above slides are from Hadley Wickham, see [copyright](http://creativecommons.org/licenses/by-nc/3.0/us/)
