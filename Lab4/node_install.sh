file='node-v10.15.1-linux-x64.tar.xz'
if [ ! -f $file ]; then
        wget https://nodejs.org/dist/v10.15.1/node-v10.15.1-linux-x64.tar.xz
fi
tar -xvf $file
dir='node-v10.15.1-linux-x64/'
mv $dir $HOME/.node
echo 'export PATH=$HOME/.node/bin/:$PATH' >> $HOME/.bashrc
rm -rf $file
source $HOME/.bashrc
