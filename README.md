# Video Search Application for Multi-Modal Data Collection Studies
This is a basic application to perform video search tasks in our case studies. 

## Requirements
* Python 2.7
* A single computer with additional screen
* A Linux distro with `canberra-gtk-play` utility (e.g. Ubuntu)
* [Sample case study videos](https://github.com/ozymaxx/soccercasestudy_videos), together with transition videos ("Video is about to play!", "Again", and a blank video to clear the screen)
* [VLC Player](http://www.videolan.org/vlc/index.tr.html)
* [VLC Python wrapper](https://wiki.videolan.org/python_bindings)

## How to Use
* Download the repository
* Download the case study videos to your computer and extract them into a directory
* Get IP address of your computer by typing `ifconfig` on terminal
* Open `shuffle.py`. At line 38, change `videosroot` variable to the path to the case study videos
 * At lines between 23 to 36, comment out the lines whose event type you don't want to present to participant (in our studies, first 7 or last 7)
* Open `SinglePanel.py`. At lines 15,16 and 17, you'll see paths of transition videos. Change them to the path to the directory where you have extracted the case study videos.
* Type `python shuffle.py <ipaddr>` on terminal where `<ipaddr>` is your IP address
* Type `python client.py <ipaddr>` on terminal where `<ipaddr>` is your IP address
* Now you'll see two windows. Extend the desktop to the additional screen, then drag the window in black to the additional screen
* Now it's ready to use!
 * Press "SOR" button to pick a random video of the next category. Note that you'll hear a sound when you clicked on this button. This sound means the participant has started watching the video.
 * For experimenters: Once the participant described the video, click on numeric buttons to take a look at the videos. If you think you found the correct video, click on "SOR BAKALIM BU MU?" button to display it on the participant's side.
 
## Credits
Ozan Can Altıok (oaltiok15 at ku dot edu dot tr) - [Koç University Intelligent User Interfaces Laboratory](http://iui.ku.edu.tr)

## Citation
If you'd like to use this work in your research, please cite [this article](https://iui.ku.edu.tr/sezgin_publications/2017/SezginAltiok-IUI-2017.pdf). Here's the BibTeX code for citing in LaTeX templates:

```
@inproceedings{altiok2017characterizing, title={Characterizing user behavior for speech and sketch-based video retrieval interfaces}, author={Alt{\i}ok, Ozan Can and Sezgin, Tevfik Metin}, booktitle={Proceedings of the Symposium on Non-Photorealistic Animation and Rendering}, pages={10}, year={2017}, organization={ACM} }
```
