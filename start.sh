#Install dependencies
echo "Install pip3 pkg dependencies"
pip3 install -r requirements.txt
echo "Executing the script"
python3 mongo_app.py 
