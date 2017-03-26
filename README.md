# Artist Expander

This little tool creates a playlist of the ~5 or so most popular songs from artists in a user's Spotify library for which they have only 1 song saved. The goal is to make it easy to find more good music by artists they've already shown interest in, but haven't fully explored yet.

## Usage

For now, you can only use this by running it on your own machine.
You will need Python 2.7 and the pip package manager.
Virtualenvs will also help.

1. Clone the project.  
   ```$ git clone git@github.com:jzimbel/artist-expander.git```
2. Make a virtualenv for the project. (Optional)  
   ```$ mkvirtualenv artist-expander```
3. Go to the directory of the cloned project, and install dependencies.  
   ```$ cd artist-expander```  
   ```$ pip install -r requirements.txt```
4. Now you need to grab some info about your Spotify account.
   Open Spotify and click on your name at the top right. Click the "..." menu
   under your name in the page that loads, and select "Copy Profile Link".
   Paste this somewhere, like a message window or a text file, and copy the part
   after the last `/`. If you signed up through Facebook, this is just a number.  
   ```https://open.spotify.com/user/128300609```  
   ```____________________this part ^^^^^^^^^```
5. Run the project. In the same terminal session where you did step 3, run:  
   ```$ ./local_launch.sh```  
   Enter the user ID you copied when prompted.
6. Open your browser of choice and go to http://localhost:5000/login.
7. Spotify will check if you're okay with giving the program some permissions for your account.
   If you are, click 'Okay'.
8. You'll get redirected to Google, but if you look at your browser's URL bar,
   you'll see a huge code after '.com'. Copy the WHOLE link, as in, 'select all'+'copy',
   and paste this into the same terminal session where you did step 5.
9. You're done! Phew. The program will take 30 seconds to a minute to build your playlist.
   Wait another 2 or so minutes after it's done for the playlist to show up in Spotify.

## Options

Options will go here eventually. Maybe.

---

I made this during the HackBeanpot 2017 hackathon: https://hackbeanpot.com/
