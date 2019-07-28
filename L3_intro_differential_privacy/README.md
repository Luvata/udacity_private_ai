# Differential Privacy


## Introducing:
Rising problem: Improve quality of models and accessible data, but also **keep data safe** from both 
intentional & accidential leakage

Most datasets are [siloed](https://dictionary.cambridge.org/dictionary/english/siloed) within large enterprises because of:
- Legal risks when sharing their datasets outside
- Competitive advantage of large datasets from customers
    
Research's data is constrained, scientists do not have access to the proper training data -> Challenging to 
solve real-world problems like diseases, societal trends, ...

The more personal to data & uses of data -> The more restricted it is from scientists

**Privacy preserving AI** to the rescue: Machine learning that **protects privacy**


## What is Differential privacy ?
The general goal of differential privacy is to ensure that different kinds of **statistical analysis** 
don't compromise privacy

Old definitions about privacy:
> "**Anything** that can be learned about a participant from the statistical database can be learned without access to 
the database" 

It's **insufficient** because even **information pertaining to the general classification** (which was learned from a 
private dataset) will be considered **violated the definition**
    
In truth, we're not really trying to protect information, **we're trying to protect people**

Modern definitions by Cynthia Dwork:

"Differential Privacy" describes a **promise**, made by a data holder, or curator, **to a data subject**, and the 
promise is like this
> "You will not be affected, adversely or otherwise, by allowing your data to be used in any study or analysis, no 
matter what other studies, data sets, or information sources are available"

## Can we just anonymize data?
> "... no matter what other studies, data sets, or information sources, are available"

Good old-fashioned data anonymization simply isn't strong enough. If someone else releases a related anonymized private 
dataset, often it can be possible to [divulge](https://dictionary.cambridge.org/dictionary/english/divulge) the private 
aspects of the information you're trying to hide by studying these two separate dataset releases
- Netflix Prize was [de-anonymize](https://www.cs.utexas.edu/~shmat/shmat_oak08netflix.pdf) by using statistical 
technique: They scraped the IMDB movie review & use statistical analysis to find individuals who were rating on both 
IMDB and on Netflix
- [Harvard Professor Re-Identifies Anonymous Volunteers In DNA Study
](https://www.forbes.com/sites/adamtanner/2013/04/25/harvard-professor-re-identifies-anonymous-volunteers-in-dna-study)
by cross-referencing them with other publicly available datasets

## Introducing the canonical database
> "If we remove a person from the database, and the query does not change, then that person's privacy would be fully 
protected"

In other words, if the query (actually the result of the query) doesn't change even if we remove someone from the 
database, then that person wasn't leaking any statistical information into the output of the query

[Parallel database notebook](https://github.com/Luvata/udacity_private_ai/blob/master/L3_intro_differential_privacy/Generate%20Parallel%20Databases.ipynb)