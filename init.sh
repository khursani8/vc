cd /content/
wget http://www.udialogue.org/download/VCTK-Corpus.tar.gz
tar xvf VCTK-Corpus.tar.gz
cd -
pip3 install -r requirements.txt
apt install festival
python3 pre-train/reader/extract_features.py /content/VCTK-Corpus/ audio
python3 pre-train/reader/extract_features.py /content/VCTK-Corpus/ text
cd pre-train
bash run.sh