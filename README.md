# Video Search Application for Case Studies
This is a basic application to perform video search tasks in our case studies. 

## Requirements
* Python 2.7
* A single computer with additional screen
* A Linux distro with `canberra-gtk-play` utility (e.g. Ubuntu)
* [Sample case study videos](https://github.com/ozymaxx/soccercasestudy_videos)
* [VLC Player](http://www.videolan.org/vlc/index.tr.html)
* [VLC Python wrapper](https://wiki.videolan.org/python_bindings)

## How to Use
* Download the repository
* Download the case study videos to your computer and extract them into a directory
* Get IP address of your computer by typing `ifconfig` on terminal
* Open `shuffle.py`. At line 38, change `videosroot` variable to the path to the case study videos
 * Starting from line 23, comment out the lines whose event type you don't want to present to participant (in our studies, first 7 or last 7)
* Type `python shuffle.py <ipaddr>` on terminal where `<ipaddr>` is your IP address
* Type `python client.py <ipaddr>` on terminal where `<ipaddr>` is your IP address
* Now you'll see two windows. Extend the desktop to the additional screen, then drag the window in black to the additional screen
* Now you're ready to use!
 * Press "SOR" button to pick a random video of the next category
 * For experimenters: Once the participant described the video, click on numeric buttons to take a look at the videos. If you think you found the correct video, click on "SOR BAKALIM BU MU?" button to display it on the participant's side.
 
## Credits
Ozan Can Altıok (oaltiok15 at ku dot edu dot tr) - [Koç University Intelligent User Interfaces Laboratory](http://iui.ku.edu.tr)