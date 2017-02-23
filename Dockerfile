FROM continuumio/anaconda3

#RUN apt-get update
#RUN apt-get install -y r-base
RUN /opt/conda/bin/conda install -y jupyter rpy2
RUN conda install -y -c r r-essentials
RUN mkdir /opt/notebooks
ADD * /python_modules/football_predictor/