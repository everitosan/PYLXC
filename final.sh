## Rxpose frontend via django

cd $COMPONENTSPATH;

mkdir Backend/front;
cp -r Frontend/build/* Backend/front;

cd Backend;
python3 manage.py migrate;
python3 manage.py loaddata TShirtColors TShirtSizes TShirtStyles
python3 manage.py registerstaff

vim .envs/.local/.django
cd ..
