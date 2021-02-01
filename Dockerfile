FROM dva-registry.internal.salesforce.com/dva/sfdc_centos7_python3.7:11

RUN mkdir certs
COPY certs/ certs/

RUN mkdir pylibs
WORKDIR /pylibs

RUN mkdir pyhive
COPY pyhive/ /pylibs/pyhive
COPY setup.py /pylibs
COPY README.rst /pylibs
COPY MANIFEST.in /pylibs
COPY TCLIService/ /pylibs/TCLIService
RUN pip install requests
RUN python3 setup.py install


WORKDIR /
RUN mkdir app
COPY bdmpresto_test.py app/


CMD [ "python3 /app/bdmpresto_test.py" ]