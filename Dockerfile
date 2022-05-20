FROM continuumio/miniconda3


COPY deploy/conda/linux_cpu_py39.yml env.yml

RUN conda env create -n housing -f env.yml

RUN git clone https://github.com/LogeshwaranV/mle-training.git

RUN cd mle-training \
    && conda run -n housing python3 setup.py install\
    && cd src/housing\
    && conda run -n housing python3 ingest_data.py
    
RUN cd mle-training/src/housing\
    &&conda run -n housing python3 train.py \
    && conda run -n housing python3 score.py

CMD ["/bin/bash"] 

COPY entrypoint.sh .
ENTRYPOINT [ "./entrypoint.sh" ]

