# Virtual envaroment preparation

Last week, we learn how to set up a virtual machine in gcp with all important tools for this course
as continuation of week 1, know is time to work with data orchestation procces.

Data orchestration refers to the process of managing and coordinating multiple sources of data to ensure that they are available, reliable, well-structured, and accessible for analysis.

Data orchestration is important in data science because it helps teams effectively integrate, transform, and combine data from different sources. This, in turn, enables data scientists to gain valuable insights and generate ideas that can be used for informed decision-making and to improve business processes.

In summary, data orchestration is the process of coordinating and managing data from diverse sources to ensure that they can be effectively used in data science, which is critical for generating useful insights and improving decision-making.

Last week we create a set-up in a gcp virtual machine, this basic set up contains anaconda navegator, so we will initialize this week creating a new anaconda enviroment .

## Create anaconda enviroment 
clone git repo from this week:
git clone https://github.com/discdiver/prefect-zoomcamp.git

create enviroment

    conda create -n zoomcamp python=3.9

Enviroment activation

    conda activate zoomcamp

Set up enviroment

    pip install -r requirements.txt


## Bibliography

PREFECT: https://docs.prefect.io/concepts/overview/