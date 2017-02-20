FROM tensorflow/magenta:0.1.9

# IPython
EXPOSE 8888

ADD container /workshop/

# /workshop/shared should be mapped to the host on startup.
RUN chmod +x /workshop/scripts/* && mkdir /workshop/shared # && mv /workshop/jupyter_notebook_config.py /root/.jupyter 

WORKDIR /workshop/scripts
CMD ["/bin/bash"]