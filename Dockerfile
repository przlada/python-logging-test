FROM python:3-onbuild
#instalation of gettext tools for language translations

# ADD . /usr/src/app
WORKDIR /usr/src/app
CMD python main.py
