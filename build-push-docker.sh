docker build -t amazonlinux-py3.8 .

docker run -v $(pwd):/my_project -ti amazonlinux-py3.8 bash

-> in docker shell:

pip install -r /my_project/requirements.txt -t /my_project

exit


cd ~/josh-text-summary-service && \
rm -rf terraform/bundle.zip && \
zip -r terraform/bundle.zip * -x terraform/**\* && \
cd terraform && \
AWS_PROFILE=skunkjweir terraform apply -auto-approve && \
cd ..


