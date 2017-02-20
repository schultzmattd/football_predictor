#Stole template from here:
#http://www.itnotes.de/docker/development/tools/2014/08/31/speed-up-your-docker-workflow-with-a-makefile/
TAG = 0.1

BASENAME = mschultz/football_predictor

.PHONY: all
all: build


build:
	docker build -f Dockerfile -t $(BASENAME):latest -t $(BASENAME):$(TAG) ./
notebook:
	docker run -v "`pwd`"/data:/opt/data/ -v "`pwd`"/notebooks:/opt/notebooks -i -t -p 8888:8888 mschultz/football_predictor:latest /bin/bash -c "/opt/conda/bin/jupyter notebook --notebook-dir=/opt/ --ip='*' --port=8888 --no-browser"
test:
	docker run --rm -it $(BASENAME):$(TAG) py.test tests/