


docker build -t amazonlinux-py3.8 .

docker run -it --name lambdalayer amazonlinux-py3.8 bash

-> in docker shell:

pip install -r requirements.txt -t ./python
zip -r python.zip ./python/

exit

docker cp lambdalayer:/var/task/python.zip ./lambda-layer.zip

# (manually upload lambda-layer.zip as a lambda layer and update terraform to reference the lambda layer arn)



cd ~/josh-text-summary-service && \
rm -rf terraform/bundle.zip && \
cd src && \
zip -r ../terraform/bundle.zip * && \
cd ../terraform && \
AWS_PROFILE=skunkjweir terraform apply -auto-approve && \
cd ..



# transformers (not yet finished / working):

git clone https://github.com/huggingface/transformers
cd transformers
pip install -e .
cd examples/seq2seq
wget https://s3.amazonaws.com/datasets.huggingface.co/summarization/cnn_dm_v2.tgz
tar -xzvf cnn_dm_v2.tgz  # empty lines removed
mv cnn_cln cnn_dm
export CNN_DIR=${PWD}/cnn_dm

export DATA_DIR=cnn_dm
python run_eval.py sshleifer/distilbart-cnn-12-6 $DATA_DIR/val.source dbart_val_generations.txt \
    --reference_path $DATA_DIR/val.target \
    --score_path cnn_rouge.json \
    --task summarization \
    --n_obs 100 \
    --max_source_length 1024 \
    --max_target_length 56 \
    --fp16 \
    --bs 32

# i removed:
#     --device cuda \


# OLD WAY (inefficient dont use - instead use lambda layer above)


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


