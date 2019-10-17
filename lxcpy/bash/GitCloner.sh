##
# $1 repo url
# $2 repo branch
# $3 ComponentName
##

cd $COMPONENTSPATH;
git clone $1 $3;
cd $3;
pwd;
git checkout $2;
