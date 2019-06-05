## app.py Functionality

### What Does it Do?
When this script is run it initially does two things: turns the 'ready' LED on and starts the server, subsequently if the server is ever exited, the ready LED is turned off. Other than that app.py contains many important function definitions including:
* Updating the settings and statistics dictionaries
* Global Flask server render template
* LED declarations and updating functions
* Camera setting altering functions
* The server shutdown function
* Flask routing functions for:
    * Shutting the server down
    * Altering a camera setting
    * Refreshing the Pi Statistics
    * Starting the video feed
* Main video feed loop (generator function)

The names and briefly the ways in which each of these functions work are explained below:

### Functions Breakdown

#### update_settings_cache
Updates the dictionary entry for the corresponding attribute and updates the whole json settings file with the correct formatting

#### update_system_stats
Updates the statistics cache with the new cpu usage, cpu temperature and ram usage, as well accounts for errors temperature reading. This uses the module: psutil

#### index
(Flask routing function)Performs an initial statistics update and defines the global Flask server render template (being: index.html). Note: this is a routing function and is called the moment the web page is opened

#### all_led_off
Turns all LEDs off by writing 0 (positive logic)

#### alter_light_level
Updates the physical voltage applied to the LEDs based on a maximum duty cycle at a refresh rate of 750Hz or turns the LEDs off if the light level value is 0. For both these cases the settings cache is updated (call to function)

#### alter_cam_setting
updates the settings cache (call to function) based on the attribute being changed, e.g. if it was the light level then the alter_light_level function also needs to be called

#### shutdown_server
Shuts down the Flask server, raises a runtime error if not able to do so

#### shut_server
(Flask routing function) Turns all LEDs off when server needs to be shutdown and calls the shutdown_server function

#### alter_config
(Flask routing function) Requests the attribute and value that needs to be changed and calls alter_cam_setting using these values

#### refresh_stats
(Flask routing function) Makes a call to update_system_stats when this was requested on server side

#### gen(camera)
Defines the main generator loop that grabs processed frames from the other script. Makes a call to get_frame from camera_piopencv.py and yields it in the correct format for HTML

#### video_feed
(Flask routing function) Gets called when the user turns the camera on in the UI. Initialises the camera class from camera_piopencv.py with the current setting cache and using it makes a call to the gen(camera) function

## camera_piopencv.py Functionality

### What Does it Do?
This script does not run anything when called, as it only contains three classes all used to obtain and process frames from the camera. 

The first of these classes is essentially a general purpose event class that wait for events, set events adn clear events. This class is used so that app.py is essentially only ever attempting to get new processed images as fast as they are being returned so that the raspberry pi isn't working any harder than it should

The second of these classes simply defines how the MJPEG output bytes stream of the camera when recording should split and store each frame

The third and most important class in this script defines and calculates camera values, describes how camera settings are updated from the settings cache, runs a thread that searches for new frames and sets an event, and sets up the raspberry pi camera to grab frames, process them and send them to the Flask server in the correct format.

The names and briefly the ways in which each of the functions within these classes work are described below:

### Functions Breakdown

#### CameraEvent Class
##### init
* Sets up the events dictionary
##### wait
* Waits for an event to be set before moving on
##### set
* Sets an event (called by the _thread function)
##### clear
* Clears any set events

#### StreamOutput Class
##### init
* Sets up frame and stream variables (Note that stream will be a bytes class, and frame will be a string class)
##### write
* Defines how the MJPEG stream is written the stream variable. Each time it is written this function checks if the stream starts with the hexadecimal value of FFD8, which indicates the start of a new frame. If this happens the reference point is set to the start of the stream, frame is set to the string value of the stream, the stream is truncated and the reference point is reset.
#### Camera Class
##### init
* sets up the camera settings as the current setting cache, sets up the crop and roi sizes using the crop_size function, and starts the camera thread (_thread)
##### crop_size
* Calculates the 4 pixel locations of the crop and roi sizes then appends them to a list and returns the list
##### update_settings
* updates the roi and contrast settings of the camera if they have changed in the settings cache
##### get_frame
* This is function called by app.py in its main video feed generator loop. It simply calls wait and clear to make sure a new frame is ready the returns the new frame
##### _thread
* This sets up the frames function as a generator loop and and calls the set function whenever a new frame is ready. The thread will break if the camera is turned off on the server side.
##### frames
* The main function that obtains the initial image. The raspberry pi camera is initialised and depending on what type of image capture technique the user has selected, the function will either:
    * Start a MJPEG recording and write to the StreamOutput Class, the frame variable in that class is converted to an array, then to an image, passed to the image_processing function and encoded back to bytes
    * Or start a YUV continuous image capture, write to a vector array variable, reshape the vector to an image array, pass it to the image_processing function and encode it back to bytes
##### image_processing
* This function takes in an image and does the following things in this order:
    * Crops the input image depending on crop values set in init
    * Creates a copy of the cropped image (final image)
    * If ROI is selected in UI (and subsequently in the settings cache):
        * Creates a new array that is the region of interest crop (If roi is selected)
        * Creates a histogram_equalisation
        * If the colour setting is applied:
            * Converts the roi image to LAB
            * Splits up the channels into L, A and B
            * Applies the histogram equalisation to the L channel
            * Merges the Channels together
        * If the colour setting is not applied:
            * Applies histogram to the roi image
        * Sets the roi portion of the final image (copy) to the applied histogram equalisation



