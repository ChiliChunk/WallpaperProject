from PIL import Image
import os
if __name__== '__main__':
    print('Wallpaper_HotnSpicy, app for gnome and Unity desktop to set two different wallpaper')
    print('Path of the left image')
    pathImg1=raw_input()
    try:
        im1 = Image.open(pathImg1 , 'r')
    except IOError :
        print ('Error : Are you sure that '+pathImg1+' is a correct path to an image?\n Exemple:/home/Tux/Images/MyAwesomeWallpaper.jpg')
        exit()
    
    
    print('Path of the right image')
    pathImg2=raw_input()
    try:
        im2 = Image.open(pathImg2 , 'r')
    except IOError :
        print ('Error : Are you sure that '+pathImg1+' is a correct path to an image?\n Exemple:/home/Tux/Images/MyAwesomeWallpaper.jpg')
        exit()
        
    w1,h1=im1.size
    box1 = (0, 0, w1, h1)
    
    w2,h2=im2.size
    box2 = (0, 0, w2, h2)
    
    src1 = im1.crop(box1)
    src2 = im2.crop(box2)
    if h1>h2:
        htotal = h1
    else :
        htotal = h2
        
    out = Image.new(mode='RGB' ,size = (w1+w2,htotal))
    out.paste(src1,(0,0,w1,h1))
    out.paste(src2,(w1,0,2*w1,h2))
    
    username = os.getlogin()
    if not os.path.exists('/home/'+username+'/Images/WallpaperHotnSpicy/'):
        os.system('mkdir /home/'+username+'/Images/WallpaperHotnSpicy')
        
    out.save('/home/'+username+'/Images/WallpaperHotnSpicy/wallpaperHotnSpicy.png')
    os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/'+username+'/Images/WallpaperHotnSpicy/wallpaperHotnSpicy.png')
    
    print ('Done! Wallpaper saved in your Images/WallpaperHotnSpicy/ \n If your wallpaper seams to be cut, go in the gnome tweak tools > Desktop and change your wallpaper mode (Recommanded: Spanned)')