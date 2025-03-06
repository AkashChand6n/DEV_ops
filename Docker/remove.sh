echo "removing Gnome Desktop"
echo "----------------------"
sudo apt-get remove --auto-remove ubuntu-gnome-desktop
# echo "purge Gnome Desktop"
# echo "----------------------"
# sudo apt-get purge --auto-remove ubuntu-gnome-desktop
sudo apt-get autoremove 
sudo dpkg-reconfigure gdm
sudo apt-get remove gdm  
apt list --installed | grep gnome
