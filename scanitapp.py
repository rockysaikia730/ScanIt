#-----------Modules--------------------------
#Module for App and builder _string, screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.core.window import Window
#camera 
import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from plyer import flash

#widget
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.dialog import MDDialog
#Module for layout and scrolling
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
#Module for effects and cropping
import numpy as np
from kivymd.uix.button import MDFlatButton

#filemanager(lets is module for filemanager---Modified version of MDFilemanager)
from lets import *

from kivymd.toast import toast
import time
import os
#pdf 
import PIL
#adv
from kivmob import KivMob , TestIds
from kivymd.uix.label import MDLabel
#-----------------------



#storage== meta



#Builder string(design)

screen_helper = '''
Screen:
    NavigationLayout:
        id : navlayout
        ScreenManager:
            id: screenmanager
            
            FileScreen:
                id : file_screen
                name : 'file_screen'
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDToolbar:
                        title: 'Scan It'
                        type: 'top'
                        elevation: 10
                        left_action_items : [['menu', lambda x: nav_drawer.set_state('open')]]
                    
                    BoxLayout:
                        padding : 15
                        orientation : 'vertical'
                        canvas.before:
                            Color:
                                rgba : 0,0,0,0.1
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius : (5,5,5,5)
                            Color:
                                rgba : 1,1,1,1
                            RoundedRectangle:
                                size: self.size[0] - 12 , self.size[1]-12
                                pos: self.pos[0]+6,self.pos[1]+6
                                radius : (5,5,5,5)  
                        MDLabel:
                            text: "App Tour"
                            font_style : 'H6'
                            size_hint :(1,0.05) 
                            halign: 'center'
                            pos_hint : {'center_x':0.5,'top':1}
                        ScrollView:
                            GridLayout:
                                cols : 1
                                Image:
                                    source : 'app_ad/PIC1.jpg'
                                Image:
                                    source: 'app_ad/PIC2.jpg'
                                Image:
                                    source: 'app_ad/PIC3.jpg'
                                
                    
                    LabelButton:
                        size_hint: (1,0.1)
                        pos_hint: {'center_x':0.5,'bottom':0.1}
                        halign : 'center'
                        on_release:
                            app.advertise()
                        
                    

        
            CameraScreen:
                id: camera_screen
                name: 'camera'
                FloatLayout:
                    id : box_camera_screen
                    orientation: 'horizontal'
                    OpenCvCamera:
                        id: camerascan
                        pos : self.pos
                        size :self.size
                       
                    MDFloatingActionButton:
                        icon: 'flash'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: camera_button.pos[0]-80 , camera_button.pos[1]
                        on_press:
                            app.count()
                            app.flash()
                    MDFloatingActionButton:
                        id : camera_button
                        icon: 'camera'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos_hint : {'center_x':0.5,'center_y': 0.1}  
                        on_press:
                            camerascan.on_capture()
                            image_preview.reload()
                        on_release:
                            screenmanager.current = 'selection'
                            touch_dictionary
                    MDFloatingActionButton:
                        icon: 'home'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: camera_button.pos[0]+80 , camera_button.pos[1]
                        on_press:
                            app.returning()
                            screenmanager.current = 'file_screen'
                            app.advertise()
                            
            SelectionScreen:
                id: selection
                name:'selection'
                FloatLayout:
                    orientation: 'vertical'
                     
                    ScrollView:    
                    ImageButton:
                        id: image_preview
                        source: 'meta/resize_jst.jpg'
                        size: self.size
                        pos: self.pos
                        on_press:
                            drawing_the_dots
                            image_preview.reload()
                            image_preview.pos
                            
                    Touch_Dictionary:
                        id: touch_dictionary 
                    Draw_Dots:
                        id :drawing_the_dots
                        
                    MDFloatingActionButton:
                        icon: 'arrow-left'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: check_button.pos[0]-80 , check_button.pos[1]  
                        on_press:
                            app.returning()
                            screenmanager.current = 'camera'
                            
                    MDFloatingActionButton:
                        id : check_button
                        icon: 'check'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos_hint: {'center_x':0.5,'center_y': 0.1}
                        on_press:
                            screenmanager.current = 'editting'
                            final_image_editting.reload()
                            app.change_perspective()
                        on_release:
                            final_image_editting.reload()
                            
                            
                            
                    MDFloatingActionButton:
                        icon: 'help'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: check_button.pos[0]+80 , check_button.pos[1]
                        on_press:
                            app.help_dot_dialog()
                        
                            
                       
                       
                             
            
                                
            EdittingScreen:
                id: editting
                name:'editting'
                FloatLayout:
                    orientation: 'vertical'
                    ScrollView:
                    ImageButton:
                        id: final_image_editting
                        source: 'meta/jst1.jpg'
                        size: self.size
                        pos: self.pos
                        
                    MDFloatingActionButton:
                        icon: 'home'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: download_button.pos[0]+160 , download_button.pos[1]
                        on_release:
                            screenmanager.current = 'file_screen'
                            app.returning()
                            app.advertise()
                            
                    MDFloatingActionButton:
                        icon: 'rotate-right'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: download_button.pos[0]-80 , download_button.pos[1] 
                        on_press:
                            app.rotating_right()
                            final_image_editting.reload()
                            
                    MDFloatingActionButton:
                        id : download_button
                        icon: 'download'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos_hint: {'center_x':0.5,'center_y': 0.1}
                        on_press:
                            app.saving_the_image()
                        
                    MDFloatingActionButton:
                        icon: 'rotate-left'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: download_button.pos[0]+80 , download_button.pos[1]
                        on_press:
                            app.rotating_left()
                            final_image_editting.reload()
                        
                    MDFloatingActionButton:
                        icon: 'camera'
                        elevation:10
                        md_bg_color: 1, 1, 1, 0.5
                        pos: download_button.pos[0]-160 , download_button.pos[1]
                        on_press:
                            screenmanager.current = 'camera'
                            app.returning()
                            
                        
                    MDRectangleFlatButton:
                        text: "B&W"
                        italic : 'True'
                        text_color: 0, 0, 0, 1
                        md_bg_color: 1, 1, 1, 1
                        pos : download_button.pos[0]-100 ,  download_button.pos[1]+70
                        on_press:
                            app.BW()
                            final_image_editting.reload()
                    
                    MDRectangleFlatButton:
                        text: "ORIGINAL"
                        text_color: 0, 0, 0, 1
                        md_bg_color: 1, 1, 1, 1
                        pos : download_button.pos[0]+70 ,  download_button.pos[1]+70
                        on_press:
                            app.original()
                            final_image_editting.reload()
                        
            
                    
            PDF_Screen:
                id : pdf_screen
                name: 'pdf_screen'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Image To PDF'
                        type: 'top'
                        elevation: 10
                        left_action_items : [['menu', lambda x: nav_drawer.set_state('open')]]
                    
                    BoxLayout:
                        padding : 15
                        orientation : 'vertical'
                        canvas.before:
                            Color:
                                rgba : 0,0,0,0.1
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius : (5,5,5,5)
                            Color:
                                rgba : 1,1,1,1
                            RoundedRectangle:
                                size: self.size[0] - 12 , self.size[1]-12
                                pos: self.pos[0]+6,self.pos[1]+6
                                radius : (5,5,5,5)  
                           
                        ScrollView:
                        MDFillRoundFlatIconButton:
                            icon : 'folder'
                            text: 'Select Images'
                            pos_hint : {'center_x' : 0.5 , 'center_y':0.6}
                            on_press:
                                app.file_manager_open()
                        ScrollView:        
                        MDFillRoundFlatIconButton:
                            id: centerbutton
                            icon : 'home'
                            text: 'Process Images to PDF'
                            pos_hint : {'center_x' : 0.5 , 'center_y':0.5}
                            on_press:
                                app.imagetoPDF()
                        ScrollView:
                        MDFillRoundFlatIconButton:
                            icon : 'help'
                            text : 'HELP'
                            pos_hint : {'center_x' : 0.5 , 'center_y':0.4}
                            on_press:
                                app.show_help_dialog()
                        ScrollView:
                     
                    LabelButton:
                        size_hint: (1,0.1)
                        pos_hint: {'center_x':0.5,'bottom':0.1}
                        halign : 'center'
                        on_release:
                            app.advertise()
                       
                
                            
        
    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                padding: '10sp'
                spacing: '10sp'
                MDList:
                    OneLineIconListItem:
                        text: 'Home'
                        on_release:
                            screenmanager.current = 'file_screen'
                            app.returning()
                            nav_drawer.set_state('close')
                        IconLeftWidget: 
                            icon:'home'
                            color:(1,0,0,1)          
                MDList:
                    OneLineIconListItem:
                        text: 'Camera'
                        on_release:
                            screenmanager.current = 'camera'
                            app.returning()
                            nav_drawer.set_state('close')
                            app.hideadvertise()
                        IconLeftWidget: 
                            icon:'camera'
                            color:(1,0,0,1)
                
                            
                MDList:
                    OneLineIconListItem:
                        text: 'Image to PDF'
                        on_release:
                            screenmanager.current = 'pdf_screen'
                            nav_drawer.set_state('close')
                            app.returning()
                        IconLeftWidget: 
                            icon:'folder'
                            color:(1,0,0,1)
                MDList:
                    OneLineIconListItem:
                        text: 'Exit'
                        on_press:
                            app.returning()
                            app.stop()
                        IconLeftWidget: 
                            icon:'exit-to-app'
                            color:(1,0,0,1)
                
                            
                ScrollView:
                MDLabel:
                    text:'Scan It'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height:self.texture_size[1]
                MDLabel:
                    text:'rockysaikia730@gmail.com'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height:self.texture_size[1]             
'''
#---------Global Variables-------------
#list of all touch points, tranformed frame sizes required for transformation          
all_points = []
x_length_of_frame = []
y_length_of_frame = []

#image loactions for pdf transformation
global pdf_images
pdf_images =[]

global count
count = 0
#------------------------
class LabelButton(ButtonBehavior,MDLabel):
    pass
#a hybrid class of image and button used in builder string for drawing dots
class ImageButton(ButtonBehavior,Image):
    pass

#class for drawing dots on string
class Draw_Dots(Widget):
    try:
        def on_touch_down(self,touch):
            global frame_width,frame_height
            x_window =Window.size[0]     #X- Window size
            y_window = Window.size[1]    #Y- Window size
            x_image = frame_width        #X- camera frame(captured image size)
            y_image = frame_height       #Y- camera frame(captured image size)
            
            #condition to check if frame size is greater than window size
            #if yes then then size of frame reduces by 40%
            if x_image >= x_window or y_image >= y_window:
                x_image = int(x_image * 0.6)
                y_image = int(y_image * 0.6)
                
            #reads the captured image
            img = cv2.imread("meta/resize_jst.jpg")
            
            #setting the origin of the image so that we can crop from
            #the original image to keep the aspect ratio
            x_origin_image = (x_window-x_image)/2     #X-origin
            y_origin_image = (y_window-y_image)/2     #Y-origin 
            
            #x-coordinate of touch point
            x_coord = int(touch.x - x_origin_image)
            #y-coordinate of touch point
            y_coord = int(touch.y - y_origin_image)
            
            #drawing the circle on the touched point
            modified_img = cv2.circle(img,(x_coord-1,int(y_image)-y_coord-2),5,(85,255,52),3)
            #saves the image in the storage for displaying in the app
            cv2.imwrite("meta/resize_jst.jpg",modified_img)
    except:
        print('Draw_Dots')
        
        
        
class Touch_Dictionary(Widget):
    try:
        #method called when  start button is pressed
        def on_touch_down(self,touch):
            #creates a list of the touch point
            points = [touch.x , touch.y]
            
            x_window =Window.size[0]      #X-window size
            y_window = Window.size[1]     #Y window size
            x_image = frame_width         # x size of the captured image
            y_image = frame_height        #y size of the captured image
            global x_length_of_frame,y_length_of_frame
            #origin of the image
            x_origin_image = (x_window-x_image)/2
            y_origin_image = (y_window-y_image)/2
            #coordinates of touch point
            x_coord = int(touch.x - x_origin_image)   #X-coordinates
            y_coord = int(touch.y - y_origin_image)   #Y-coordinates
            points = [x_coord-1, int(y_image)-y_coord-2]   #list of touch point
                
            x_length_of_frame.append(x_coord)
            y_length_of_frame.append(y_coord)
            
            #if the frame size is greater than window size
            if x_image >= x_window or y_image >= y_window:
                x_origin_image = (x_window-(x_image*0.6))/2
                y_origin_image = (y_window-(y_image*0.6))/2
        
                x_apparent_coord = int(touch.x - x_origin_image)
                y_apparent_coord = int(touch.y - y_origin_image)
                x_coord = x_apparent_coord/0.6
                y_coord = y_apparent_coord/0.6
                points = [x_coord-1,int(y_image)-y_coord-2]
                
                x_length_of_frame.append(x_coord)
                y_length_of_frame.append(y_coord)
            #prints the touch point
            print(points)
            print(type(points))
            #calls the global variable ar_point list to store all touch
            global all_points
            
            #adds all the points to ar points list using append(both x and y coordinates)
            all_points.append(points)
            #prints the list of all the points
            print(all_points)
            
        #the medthod to keep the the function itirating 
        def on_touch_move(self,touch):
            pass
    except:
        print("Touch Dictionary")
        
#class for camera 
class OpenCvCamera(Image):
    try:
        #initialises camera and updating the frames
        def __init__(self, **kwargs):
            super(OpenCvCamera, self).__init__(**kwargs)
            self.capture = cv2.VideoCapture(0)
            Clock.schedule_interval(self.update, 1.0 / 30)
        #updating the frame  and creating the texture
        def update(self, dt):
            ret, self.frame = self.capture.read()
            global frame_width,frame_height
            frame_width = self.capture.get(3)
            frame_height = self.capture.get(4)
            
            
            if ret:
                # convert it to texture
                
                buf1 = cv2.flip(self.frame, 0)
                buf = buf1.tostring()
                image_texture = Texture.create(
                    size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                # display image from the texture
                self.texture = image_texture
                
        #method called when camera button is pressed         
        def on_capture(self):
            #captures the frame and saves in folder
            cv2.imwrite("meta/original_jst.jpg", self.frame)
            #the dimensions of captured image and window
            x_window =Window.size[0]
            y_window = Window.size[1]
            x_image = frame_width
            y_image = frame_height
            
            #transformation made in captured image when frame is smaller
            if x_image >= x_window or y_image >= y_window:
                x_image = int(x_image * 0.6)
                y_image = int(y_image * 0.6)
                
            #resized depending on condition
            #May or may not resize depending on frame size and windoe
            resized_frame = cv2.resize(self.frame,(int(x_image),int(y_image)))
            #storing the resized image
            cv2.imwrite("meta/resize_jst.jpg", resized_frame)
    except:
        print('camera')
    finally:
        #switches off camera when the cmera is not in used
        cv2.VideoCapture(1).release()
        



#Camera screen when camera is started
class CameraScreen(Screen):
    pass
    
#screen for cropping making selection
class SelectionScreen(Screen):
    pass
#screen for editting  
class EdittingScreen(Screen):
    pass
#Home Screen    
class FileScreen(Screen):
    pass
#pdf screen     
class PDF_Screen(Screen):
    pass
    
    
#Main Class:App 

class ScanIt(MDApp):
    def build(self):
        
        try:
            self.icon = 'app_ad\\logo.jpg'
            self.ads = KivMob("ca-app-pub-7526428266463384~7719002568")
            self.ads.new_banner("ca-app-pub-7526428266463384/7151794843", top_pos = False)
            self.ads.request_banner()
            self.ads.show_banner()
            self.toggled = False
            #Screen----All Screens managed by screen manager
            self.all_screen = ScreenManager()
            #Builder file loaded
            camerascreen    = Builder.load_string(screen_helper) 
            self.all_screen.add_widget(camerascreen)
            
            #screen manager returning all screen----Beginning of app
            
            return self.all_screen
        except:
            toast('Unable to open')
            print('APP')
        
            
    def advertise(self):
        if not self.toggled:
            self.ads.show_banner()
        
    def hideadvertise(self):
        self.ads.hide_banner()
        
    def on_pause(self):
        return True
    def on_resume(self):
        return True
        
        
    try:
        #starting the file manager from lets module 
        def __init__(self, **kwargs):
                super().__init__(**kwargs)
                #for window button in mobile
                Window.bind(on_keyboard=self.events)
                self.manager_open = False
                self.file_manager = MDFileManager(exit_manager=self.exit_manager,  #funtions for exitting manager 
                                                  select_path=self.select_path,    #function for selecting the path 
                                                  previous=True,                   #function for showing the images in icon view
                                                  )
        #displaying the file manager 
        def file_manager_open(self):
            self.file_manager.show('/')
            self.manager_open =True
        #selecting the path and displaying it    
        def select_path(self, path):
                '''It will be called when you click on the file name '''
                #path is the path to folder
                toast("Added  "+path)
                #seq is used to store the location of images 
                seq=str()
                #we have to exclude the scanit part in path so that PIL can access it
                if path.find('ScanIt') != -1:
                    r = path.split('/ScanIt\\')
                    for i in range(len(r)):
                        if r[i] == '/ScanIt\\':
                            continue
                        else:
                            seq += r[i]
                else:
                    seq = path
                #takes all the path to be used by PIL    
                pdf_images.append(seq)
        #exitting the manager
        def exit_manager(self, *args):
            
    
            self.manager_open = False
            self.file_manager.close()
            
        #additional feature
        def events(self, instance, keyboard, keycode, text, modifiers):
            '''Called when buttons are pressed on the mobile device.'''
    
            if keyboard in (1001, 27):
                if self.manager_open:
                    self.file_manager.back()
            return True
    except:
        toast('Unexpected Error')
        print('filemanger')
    
    #changing the perspectiive i.e. cropping and perspective        
    def change_perspective(self):
        try:
            #creates the output image of the largest frame to be displayed
            global all_points,x_length_of_frame,y_length_of_frame
            x_length_of_frame.sort()
            y_length_of_frame.sort()
            
            width = x_length_of_frame[-1]-x_length_of_frame[0]
            height = y_length_of_frame[-1]-y_length_of_frame[0]
            #read the image
            img = cv2.imread('meta/original_jst.jpg')
            #all the points
            detected_points = np.float32((all_points))    #the touch points
            transformed_points = np.float32([[0,0],[width,0],[width,height],[0,height]])  #the transformed points
            
            #transformation matrix
            matrix = cv2.getPerspectiveTransform(detected_points , transformed_points)
            #image is warped
            output = cv2.warpPerspective(img ,matrix,(int(width),int(height)))
            
            #conditions for displaying the image
            #two image required jst1 and jst2 so thatcolour transformation can be made
            if width >= Window.size[0] or height >= Window.size[1]:
                cv2.imwrite('meta/jst1.jpg',output)
                cv2.imwrite('meta/jst2.jpg',output)
            elif width < Window.size[0] or height < Window.size[1]:
                if width>height:
                    scale_ratio = Window.size[0]/width
                    modified_img = cv2.resize(output,(int(width*scale_ratio),int(height*scale_ratio)))
                elif width<height:
                    scale_ratio = Window.size[1]/height
                    modified_img = cv2.resize(output,(int(width*scale_ratio),int(height*scale_ratio))) 
                  
                cv2.imwrite('meta/jst1.jpg',modified_img)
                cv2.imwrite('meta/jst2.jpg',modified_img)
        except:
            print('perspective')
    #called when saving the image        
    def saving_the_image(self):
        try:
            file_name = time.strftime('%Y%m%d%S',time.localtime())
            meta_img = cv2.imread('meta/jst1.jpg')
            cv2.imwrite('storage/{}.jpg'.format(file_name),meta_img)
            toast('Image saved in storage')
        except:
            toast('Unexpected Error: Image not saved')
            print('saving')
    #erasing all the global lists so that they can be reused
    def returning(self):
        try:
            global all_points,x_length_of_frame,y_length_of_frame
            x_length_of_frame.clear()
            y_length_of_frame.clear()
            pdf_images.clear()
            if len(all_points)>=0:
                all_points.clear()
        except:
            print('returning')
    #-----Rotating Image-------------
    try:  
        #rotaing left or right by accesing and then saving 
        def rotating_left(self):
            initial_img = cv2.imread('meta/jst1.jpg')
            rotated_img = cv2.rotate(initial_img,cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite('meta/jst1.jpg',rotated_img)
            cv2.imwrite('meta/jst2.jpg',rotated_img)
            
        def rotating_right(self):
            initial_img = cv2.imread('meta/jst1.jpg')
            rotated_img = cv2.rotate(initial_img,cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite('meta/jst1.jpg',rotated_img)
            cv2.imwrite('meta/jst2.jpg',rotated_img)
    except:
       print('rotation')
    #------------Colour effects----------
    try:
        #Black and white transformation
        def BW(self):
            orig_img = cv2.imread("meta/jst2.jpg")
            gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("meta/jst1.jpg",gray)
        #coloured image    
        def original(self):
            orig_img = cv2.imread("meta/jst2.jpg")
            cv2.imwrite("meta/jst1.jpg" ,orig_img)
    except:
        print('colour trnasformation')

    #called to convert into pdf
    def imagetoPDF(self):
        try:
            #in case pdf image list has no item
            if len(pdf_images) == 0:
                toast("No file selected")
            else:
                #imagelist to store all the RGB image
                imagelist = []
                for i in pdf_images:
                    #PIL opening the image
                    imageread = PIL.Image.open(r'{}'.format(i))
                    #conversion to RGB format from RGBA(if any)
                    imageconversion = imageread.convert('RGB')
                    #imagelist stores all the converted mage
                    imagelist.append(imageconversion)
                #at the end of loop    
                else:
                    file_name = time.strftime('%Y%m%d%S',time.localtime())
                    #all the other images are appended with the first image
                    imagelist[0].save(r'storage/{}.pdf'.format(file_name),save_all=True, append_images=imagelist[1:])
                    toast('Saved in storage')  
        except:
            print('imageto PDF')
        finally:
            #clearing the list to be reused
            pdf_images.clear()
            
                
        
    #accessing flash using plyer
    def flash(self):
        try:
            global count
            
            if count%2 !=0 :
                flash.on()
            else:
                flash.off()
            print('2',count)
        except:
            toast("Flash not accessible")
        finally:
            flash.release()
            count = 0 
    #for flash
    def count(self):
        global count
        count += 1
        
     
    try:
        #opens up dialog for help in pdf
        def show_help_dialog(self):
            global dialog
            dialog = MDDialog(title = "How To?",
                              text = 'Select all the images in "order" and click Process',
                              size_hint =(0.7,1),
                              buttons =[MDFlatButton(text= "OK",
                                                    on_release= self.close_dialog)])
            dialog.open()
        #dialog for drawing dots    
        def help_dot_dialog(self):
            global dialog
            dialog = MDDialog(title = "How To?",
                              text = "Select the 4 corners of your document in a 'sequence'",
                              size_hint=(0.7,1),
                              buttons = [MDFlatButton(text = 'OK',
                                                      on_release = self.close_dialog)])
            dialog.open()
        #closing dialog    
        def close_dialog(self,obj):
            dialog.dismiss()
    except:
        print('dialog')

#Execution
if __name__ ==  '__main__':        
    ScanIt().run()
